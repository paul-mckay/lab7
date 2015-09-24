from fabric.api import *
from fabric.contrib.files import upload_template

env.user = 'ubuntu'
env.hosts = [
	'1.1.1.1'
]

def nginx_curl():
	run('curl localhost')
		
def nginx_install():
	sudo('add-apt-repository ppa:nginx/stable')
	sudo('apt-get update')
	sudo('apt-get install -y nginx')

def nginx_proxy():
	sudo('rm -f /etc/nginx/sites-enabled/*')
	put('proxy', '/etc/nginx/sites-available/proxy', use_sudo=True)
	sudo('ln -s /etc/nginx/sites-available/proxy /etc/nginx/sites-enabled/')
	sudo('/etc/init.d/nginx reload')