from django.contrib import admin
from .models import blog
from .models import User
from .models import Tag

# Register your models here.
admin.site.register(blog)
admin.site.register(User)
admin.site.register(Tag)