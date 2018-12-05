import sys, random
from locust import HttpLocust, TaskSet

def writeTomcat(locust):
    postid = random.randint(1, 500)
    url_prefix = '/editor/post?action=save&username=cs144&postid='
    url_request = url_prefix + str(postid) + '&title=Loading%20Test&body=***Hello%20World!***'
    locust.client.post(url_request, name='/editor/post?action=save')

class MyTaskSet(TaskSet):
    tasks = [writeTomcat]

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000