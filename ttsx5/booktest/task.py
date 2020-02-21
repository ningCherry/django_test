import time
from celery import task

@task
def sayhello():
    print('hello1')
    time.sleep(5)
    print('hello2')