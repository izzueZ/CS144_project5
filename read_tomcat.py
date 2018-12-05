import sys, random
from locust import HttpLocust, TaskSet

def readTomcat(locust):
    postid = random.randint(1, 500)
    url_prefix = '/editor/post?action=open&username=cs144&postid='
    locust.client.get(url_prefix + str(postid), name='/editor/post?action=open')

class MyTaskSet(TaskSet):
    tasks = [readTomcat]

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000