import requests

class Post:
    def __init__(self):
        blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
        response = requests.get(url=blog_url)
        self.info = response.json()

        
    def get_post(self, num:int):
        for blog_post in self.info:
            if blog_post["id"] == num:
                return blog_post["title"], blog_post["subtitle"], blog_post["body"]
        

