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