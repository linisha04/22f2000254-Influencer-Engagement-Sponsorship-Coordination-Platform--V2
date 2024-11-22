# from celery import Celery, Task
from celery import shared_task


import time

@shared_task
def hello():
    print("hello")
    time.sleep(10)
    print("Hi")
    return "Hello"
