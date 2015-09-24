from fabric.api import *

def hello():
    print('Hello world!')
    
def info():
    run('date')
    run('cat /proc/cpuinfo | grep "model name"')
    run('cat /etc/hostname')
    run('hostname -I')
    run('who am i')
    run('pwd')
    
