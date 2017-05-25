from django.contrib import admin
#add Post model that we created
from .models import Post

admin.site.register(Post)
