from fabric.api import *

def myapp_curl():
	run('curl localhost:3000')

def myapp_install():
	run('mkdir myapp')
	put('myapp/*', 'myapp')
	sudo('cd myapp && npm install')

def nodejs_install():
	sudo('apt-get update')
	sudo('curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -')
	sudo('apt-get install -y nodejs')