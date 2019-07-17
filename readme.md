# 个人博客仓库
[博客链接](http://47.103.5.67/)


## run
> 虚拟环境
```shell
python manage.py runserver 8000
```


## 部署
> ！！！部署前先检查settings里的debug是不是False！！！

> 使用了fabric来部署到远程服务器，通过github托管代码，将代码同步到服务器上。
参考博客[使用 Fabric3 自动化部署](https://blog.csdn.net/qq_41854273/article/details/83344255)

```python
from fabric.api import env, run

from fabric.operations import sudo

GIT_REPO = "https://github.com/Icestains/myblog.git"

env.user = 'icestains'
env.password = '**********'

# 填写你自己的主机对应的域名
env.hosts = ['47.103.5.67']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


# 由于一些奇怪的bug 这里的shell命令会出现一些奇怪的问题，于是就直接在这里进入了虚拟环境
# 从github仓库同步代码
# 更新依赖，收集静态文件，更新 最后退出虚拟环境环境
def deploy():
    source_folder = '/home/icestains/sites/icestains/myblog'
    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        source env/bin/activate &&
        pip3 install -r requirements.txt &&
        python3 manage.py collectstatic --noinput &&
        python3 manage.py migrate &&
        deactivate
        """.format(source_folder))
    sudo('systemctl restart lcblog.service')
    sudo('service nginx reload')

```

> 在febfile的目录下执行
```shell
fab deploy
```




参考：https://www.zmrenwu.com