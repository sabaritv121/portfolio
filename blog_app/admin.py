from django.contrib import admin

# Register your models here.
from blog_app import models

admin.site.register(models.Test)