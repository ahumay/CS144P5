# In python, '#' is used to indicate a comment line.
"""
The string within triple-quote is also considered as a comment.
And the triple-quote can be used for multiline comments.
DISCLAIMER: This sample doesn't care about whether the use of API is correct.
"""

import sys, random
from locust import HttpLocust, TaskSet

def write_tomcat(locust):
    """ define a function in python whose name is previewPage and the argument is locust """
    postid = random.randint(1, 500) # generate a random number from 1 to 100 (include 1 and 100)
    name = "/editor/post?action=save"
    url_prefix = '/editor/post?action=save&username=cs144&postid=';
    locust.client.post(url_prefix + str(postid) + "&title=Loading%20Test&body=***Hello%20World!***", name=name)

class MyTaskSet(TaskSet):
    """ the class MyTaskSet inherits from the class TaskSet, defining the behavior of the user """
    tasks = [write_tomcat]
    def on_start(locust):
        """ on_start is called when a Locust start before any task is scheduled """

class MyLocust(HttpLocust):
    """ the class MyLocust inherits from the class HttpLocust, representing an HTTP user """
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000