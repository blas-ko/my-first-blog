from django.contrib import admin
#add Post model that we created
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
