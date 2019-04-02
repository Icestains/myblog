from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "you git repository"

env.user = 'icestains'
env.password = 'm@5QU3R@D3@ESC'

# 填写你自己的主机对应的域名
env.hosts = ['47.103.5.67']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


def deploy():
    source_folder = '/home/icestains/sites/demo/blog'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-demo.zmrenwu.com')
    sudo('service nginx reload')