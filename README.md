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

```

### 注意事项

#### 自动重新加载服务
```text
自动重新加载服务 runserver
用于开发的服务器会在对每次访问的时候重新加载一次代码，不需要为了修改代码重新启动服务器，而新添加的文件需要重启服务
```







