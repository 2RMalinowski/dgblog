from django.contrib import admin
from .models import Post, Comment, MyItem

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(MyItem)
