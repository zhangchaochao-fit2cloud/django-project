from django.contrib import admin

# Register your models here.

# 必须加点 否则启动项目会报错
from .models import Question

admin.site.register(Question)
