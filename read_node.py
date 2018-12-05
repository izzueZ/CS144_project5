import sys, random
from locust import HttpLocust, TaskSet

def readNode(locust):
    postid = random.randint(1, 500)
    url_prefix = '/blog/cs144/'
    locust.client.get(url_prefix + str(postid), name='/blog/cs144')

class MyTaskSet(TaskSet):
    tasks = [readNode]

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000