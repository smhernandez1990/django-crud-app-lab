from django.contrib import admin
from .models import Artist, Release

# Register your models here.
admin.site.register(Artist)
admin.site.register(Release)