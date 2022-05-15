# django-project

django框架学习

### 官方文档

> https://docs.djangoproject.com/zh-hans/4.0/

#### python和django版本对应

> https://docs.djangoproject.com/zh-hans/4.0/faq/install/#faq-python-version-support

### 官方配置

> django-admin 和 manage.py
> 
> https://docs.djangoproject.com/zh-hans/4.0/ref/django-admin/
> 
> 数据库配置
> 
> https://docs.djangoproject.com/zh-hans/4.0/ref/settings/#std:setting-DATABASES
> 
> settings配置
> 
> https://docs.djangoproject.com/zh-hans/4.0/ref/settings/
> 
> URL调度器
> 
> https://docs.djangoproject.com/zh-hans/4.0/topics/http/urls/
> 
> Django查询语法
> 
> https://docs.djangoproject.com/zh-hans/4.0/intro/tutorial02/
> 
> template语法
> 
> https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#anatomy_of_an_html_document
> 
> https://docs.djangoproject.com/zh-hans/4.0/topics/templates/
> 
> 请求和响应
> 
> https://docs.djangoproject.com/zh-hans/4.0/ref/request-response/
> 
> 通用视图
> 
> https://docs.djangoproject.com/zh-hans/4.0/topics/class-based-views/
> 
> 测试
> 
> https://docs.djangoproject.com/zh-hans/4.0/intro/tutorial05/#
> 
> 静态文件
> 
> https://docs.djangoproject.com/zh-hans/4.0/ref/contrib/staticfiles/
> 
> https://docs.djangoproject.com/zh-hans/4.0/howto/static-files/
> 
> https://docs.djangoproject.com/zh-hans/4.0/howto/static-files/deployment/
> 
> 
> pip公共仓库
> 
> https://pypi.org/
> 
> 发布应用到公共仓库
> 
> https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives
> 
> venv 隔离 python 虚拟环境
> 
> https://docs.python.org/3/tutorial/venv.html
> 
> 打包
> 
> https://docs.djangoproject.com/zh-hans/4.0/intro/reusable-apps/
> 
> django文档
> 
> https://docs.djangoproject.com/zh-hans/4.0/intro/whatsnext/


### 查看版本

```python
import django
print(django.get_version())
```

```shell
python -m django --version
```


### 基本语法

```shell
# 安装最新Django
pip install django

# 指定版本安装
pip install django==2.0.7

# makemigrations 命令查找所有可用的模型，为任意一个在数据库中不存在对应数据表的模型创建迁移脚本文件。
python manage.py makemigrations

# migrate 命令则运行这些迁移来自动创建数据库表。还提供可选的 更丰富的控制模式。
# 只会为 INSTALLED_APPS 里面的应用做数据迁移
python manage.py migrate

# 创建项目 会在当前目录创建mysite目录，并初始化项目
django-admin startproject mysite

# 导出项目所安装的包 注意：requirements.txt的内容是项目所安装的包
pip freeze > requirements.txt

# 快速安装Django项目所需要的包
pip install -U pip
pip install -r requirements/requirements.txt

# 为项目添加 python 虚拟环境 （会将依赖都下载到这个目录下）
python3 -m venv /opt/py3
# 载入虚拟环境
source /opt/py3/bin/activate

# 启动服务
python manage.py runserver
# 指定服务端口
python manage.py runserver 8080
# 指定监听IP 0 是 0.0.0.0 的简写
python manage.py runserver 0:8000

# 初始化应用
python manage.py startapp polls
# 生成应用迁移文件
python manage.py makemigrations polls
# 查看迁移文件（0001）也就是sql文件（会解析文件成sql）
python manage.py sqlmigrate polls 0001
# 检查项目中的问题
python manage.py check
# 使用应用迁移文件
python manage.py migrate


# 运行测试
python manage.py test polls

# 查看django的源文件
python -c "import django; print(django.__path__)"


```

### 数据库语法
```text

# 导入模板对象
from polls.models import Choice, Question

# 查询全部
Question.objects.all()

# 过滤
Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')

# 获取当前发布时间的集合
from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)

# 如果 ID 不存在抛异常
Question.objects.get(id=2)

# 根据 ID 查询
Question.objects.get(pk=1)

# 调用自定义的方法
q = Question.objects.get(pk=1)
q.was_published_recently()
True

q = Question.objects.get(pk=1)
# 外键关联对象
q.choice_set.all()

# 创建外键关联对象
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)
c.question

# 获取外键关联对象数量
q.choice_set.all()
q.choice_set.count()

# 查询
Choice.objects.filter(question__pub_date__year=current_year)

# 删除
c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()
```

### 注意事项

#### 自动重新加载服务
```text
自动重新加载服务 runserver
用于开发的服务器会在对每次访问的时候重新加载一次代码，不需要为了修改代码重新启动服务器，而新添加的文件需要重启服务
```

#### model调用不提示objects
```python
import datetime

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # 解决model调用没有objects问题
    objects = models.Manager()


    def __str__(self):
        return self.question_text
```







