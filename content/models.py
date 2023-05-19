from django.db import models

# Create your models here.
class Feed(models.Model):
    content = models.TextField() # 내용
    image = models.TextField() # 메뉴 이미지
    user_id = models.TextField() # 작성자 id


class Reply(models.Model):
    feed_id = models.IntegerField(default=0)
    user_id = models.TextField(default='') # 사용자 id
    reply_content = models.TextField()


class Bookmark(models.Model):
    feed_id = models.IntegerField(default=0)
    user_id = models.TextField(default='') # 사용자 id
    is_marked = models.BooleanField(default=True) # 북마크 여부
