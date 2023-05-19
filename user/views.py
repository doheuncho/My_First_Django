from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from argon2 import PasswordHasher
from bobjoying.settings import MEDIA_ROOT
from uuid import uuid4
import os


class Login(APIView):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        user_id = request.data.get('user_id', None)
        password = request.data.get('password', None)

        user = User.objects.filter(user_id=user_id).first()

        if user is None:
            return Response(status=400, data=dict(message='입력정보가 잘못되었습니다.'))

        if PasswordHasher().verify(user.password, password) is False:
            return Response(status=400, data=dict(message='입력정보가 잘못되었습니다.'))
        
        request.session['user_id'] = user.user_id

        return Response(status=200)


class LogOut(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, "user/login.html")


class UploadProfile(APIView):
    def post(self, request):

        file = request.FILES['file']
        user_id = request.data.get('user_id')

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        profile_image = uuid_name

        user = User.objects.filter(user_id=user_id).first()

        user.thumbnail = profile_image
        user.save()

        return Response(status=200)
                  