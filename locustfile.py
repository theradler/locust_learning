from locust import HttpLocust, TaskSet,task,  Locust
import json
import redis 







class redisConnector:
    r = redis.StrictRedis(host='localhost',port=6379,db=0)
    r.set('foo','bar')
    value = r.get('foo')
    print(value)


class UserBehavior(TaskSet):
    @task
    def get_users(self):
        self.client.get("posts")
    
    @task
    def post_photo(self):
        response = self.client.post("posts",{"postId":"1"})
        self.client.get("users")
        print(response.json())



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    on_start = redisConnector() 
