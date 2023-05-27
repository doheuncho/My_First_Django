from uuid import uuid4
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed, Reply, Bookmark
from user.models import User
from bobjoying.settings import MEDIA_ROOT
import os


# Create your views here.
class Main(APIView):
    def get(self, request):
        user_id = request.session.get('user_id', None)

        if user_id is None:
            return render(request, "user/login.html")
        
        user = User.objects.filter(user_id=user_id).first()

        if user is None:
            return render(request, "user/login.html")
        
        feed_object_list = Feed.objects.all().order_by('-id') # select * from Feed;
        feed_list = []

        for feed in feed_object_list:
            feed_user = User.objects.filter(user_id=feed.user_id).first()
            reply_object_list = Reply.objects.filter(feed_id=feed.id)
            reply_list = []

            for reply in reply_object_list:
                reply_user = User.objects.filter(user_id=reply.user_id).first()
                reply_list.append(dict(reply_content=reply.reply_content, user_id=reply_user.user_id))
            # get bookmark info
            is_marked=Bookmark.objects.filter(feed_id=feed.id, user_id=user_id, is_marked=True).exists()
            feed_list.append(dict(id=feed.id,
                                    image=feed.image,
                                    content=feed.content,
                                    profile_image=feed_user.thumbnail,
                                    user_id=feed_user.user_id,
                                    reply_list=reply_list,
                                    is_marked=is_marked
                                    ))

        return render(request, "bobjoying/main.html", context=dict(feed_list=feed_list, user=user))
    

class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES["file"]
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        
        with open(save_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        content = request.data.get("content")
        user_id = request.session.get("user_id")

        Feed.objects.create(image=image, content=content, user_id=user_id)

        return Response(status=200)


class UpdateFeed(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        feed = Feed.objects.get(id=feed_id)
        
        old_image_path = os.path.join(MEDIA_ROOT, feed.image)

        if "file" in request.FILES:
            file = request.FILES["file"]
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = uuid4().hex
            save_path = os.path.join(MEDIA_ROOT, new_image)
            feed.image = new_image
            
            with open(save_path, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                    
        
        content = request.data.get("content")
        feed.content = content
        feed.save()
        
        return Response(status=200)
    

class DeleteFeed(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        feed = Feed.objects.get(id=feed_id)

        if feed:
            feed_image_path = os.path.join(MEDIA_ROOT, feed.image)
            if os.path.exists(feed_image_path):
                os.remove(feed_image_path)
            feed.delete()
        
        return Response(status=200)
    

class Profile(APIView):
    def get(self, request):
        user_id = request.session.get('user_id', None)

        if user_id is None:
            return render(request, "user/login.html")

        user = User.objects.filter(user_id=user_id).first()

        if user is None:
            return render(request, "user/login.html")

        feed_list = Feed.objects.filter(user_id=user_id)
        bookmark_list = list(Bookmark.objects.filter(user_id=user_id, is_marked=True).values_list('feed_id', flat=True))
        bookmark_feed_list = Feed.objects.filter(id__in=bookmark_list)
        return render(request, 'content/profile.html', context=dict(feed_list=feed_list,
                                                                    bookmark_feed_list=bookmark_feed_list,
                                                                    user=user))


class UploadReply(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        reply_content = request.data.get('reply_content', None)
        user_id = request.session.get('user_id', None)

        Reply.objects.create(feed_id=feed_id, reply_content=reply_content, user_id=user_id)

        return Response(status=200)


class ToggleBookmark(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        bookmark_text = request.data.get('bookmark_text', True)
        print(bookmark_text)
        if bookmark_text == 'bookmark_border':
            is_marked = True
        else:
            is_marked = False
        user_id = request.session.get('user_id', None)

        bookmark = Bookmark.objects.filter(feed_id=feed_id, user_id=user_id).first()

        if bookmark:
            bookmark.is_marked = is_marked
            bookmark.save()
        else:
            Bookmark.objects.create(feed_id=feed_id, is_marked=is_marked, user_id=user_id)

        return Response(status=200)
    