import sys, random
from locust import HttpLocust, TaskSet

def writeNode(locust):
    postid = random.randint(1, 500)
    url_prefix = '/api/cs144/'
    locust.client.put(url_prefix + str(postid), data={"title":"Loading Test", "body":"***Hello World!***"}, name='/api/cs144')

class MyTaskSet(TaskSet):
    tasks = [writeNode]
    def on_start(locust):
        response = locust.client.post("/login?redirect=/", data={"username":"cs144", "password": "password"}, name='/login')

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000