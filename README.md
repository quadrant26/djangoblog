### 创建一个虚拟环境
    
    ```git
        mkdir djangoblog
        cd djangoblog
        
        // 创建虚拟环境
        python3 -m venv mydjango
        
        // 运行虚拟环境
        .\mydjango\Scripts\activate
        
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
        virtualenv python=python3.6 myvenv
        
        // 安装 django
        pip install django

        // 使用虚拟环境
        source myvenv

        // 为虚拟环境安装 django
        pip install django
    ```