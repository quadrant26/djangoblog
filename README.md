### 创建一个虚拟环境
    
    ```git
        mkdir djangoblog
        cd djangoblog
        
        // 创建虚拟环境
        python3 -m venv myvenv
        
        // 运行虚拟环境
        .\myvenv\Scripts\activate
        
        // 安装 django
        pip install django
        // 提示pip需要升级
        python -m pip install --upgrade pip
    
    ```

### 初始化项目
    ```python
        // 初始化
        django-admin startproject mysite .

        // 设置时区 mysite/settings.py
        TIME_ZONE = 'Asia/Shanghai'

        // 静态文件的路径
        STATIC_URL = '/static/'
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')

        // 创建数据库
        python manage.py migrate
        // 启动服务器
        python manage.py runserver [port]

        // 模型创建数据表
        python manage.py makemigrations blog
        python manage.py migrate blog

        // 创建用户
        python manage.py createsuperuser

        // 设置 ALLOWED_HOSTS mysite/settings.py
        ALLOWED_HOSTS = ['yourusername.pythonanywhere.com', '127.0.0.1']
        
    ```

### 上传到git
    
    ```git
        git init
        git add --all .
        git commit -m "content"
        git remote add origin gitpath
        git push -u origin master
    ```

### 上传到 PythonAnywher
    
    ```git
        // cong git 上拉取本代码
        git clone project_gitpath
        cd project_gitpath

        // 创建一个 虚拟环境
        // python 版本需要和本机版本一样 
        // 指定python -p /usr/bin/python3.6
        virtualenv -p /user/bin/python3.6 myvenv

        // 使用虚拟环境
        source myvenv/bin/activate

        // 为虚拟环境安装 django
        pip install django

        // 收集静态文件
        // 多次输入
        python manage.py collectstatic

        // 创建数据库
        python manage.py migrate
        python manage.py createsuperuser
    ```

### 发布网络应用程序
    
+ web ->  Add a new web app

    ```
    PythonAnywhere -> Add a new web app ->  Manual configuration -> Python 3.6(与虚拟环境的版本一致)
    ```
+ 配置 Virtualenv
  
    ```python
        # 配置 Virtualenv
  
        /home/username/djangoblog/myvenv
    ```
+ WSGI configuration
  
    ```python
        # WSGI configuration file
        import os
        import sys
        
        path = '/home/<your-username>/my-first-blog'  # use your own username here
        if path not in sys.path:
            sys.path.append(path)
        
        os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
        
        from django.core.wsgi import get_wsgi_application
        
        application = get_wsgi_application()
    
    ```

+ static 文件
    
    ``` 
        这是静态文件路径
        # URL
        /static/
        # Directory
        /home/<your-username>/my-first-blog/static/
    ```

### 添加页面
  
  ```python
    # mysite/urls
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('blog.urls')),
    ]

    # blog/urls
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', views.post_list, name='post_list')
    ]

    # blog/views.py
    def post_list(request):
        return render(request, 'blog/post_list.html', {})
  ```

## Django ORM 和 QuerySets（查询集）
### Django shell
  
  开启 shell
  ```python manage.py shell```

  ```python
    # 导入 Post
    from blog.models import Post
    # 打印全部数据
    Post.objects.all()
    # 导入 User
    from blog.contrib.auth.models import User
    # 打印全部用户
    User.object.all()
    # 设置me
    me = User.objects.get(username='admin')
    # 向表中插入一条数据
    Post.objects.create(author=me, title='sample title', text='Text')
    # 查看内容
    Post.objects.all()
    
  ```

### 筛选对象
  
  ```python
    Post.objects.filter(author=me)
    # 在 title 与 contains 之间有两个下划线字符 ( _ )。 Django 的 ORM 使用此语法来分隔字段名称 （"title"） 和操作或筛选器 （"contains"）
    Post.objects.filter(title__contains="title")
    # 已经发布的文章
    from django.utils import timezone
    Post.objects.filter(published_date__lte=timezone.now())
  ```

### 排序
  
  ```python
    Post.objects.order_by('created_date')
  ```

### 链式 QuerySets
  
  ```python
    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  ```

### 退出shell
  
  ```python
    exit()
  ```


### 表单
  
  添加表单时报错， 强制解决
  ```python
    # mysite/setting.oy
    # 注释 MIDDLEWARE -> 'django.middleware.csrf.CsrfViewMiddleware',
    
    MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

  ```
  