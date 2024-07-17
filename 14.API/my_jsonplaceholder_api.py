
# API = Application Programming Interface

# url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
# url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"

import requests

class JSONPlaceHolderAPI:
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com'

    def get_posts_by_user(self, user_id):
        url = f'{self.base_url}/posts?userId={user_id}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def get_comments_by_post(self, post_id):
        url = f'{self.base_url}/posts/{post_id}/comments'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def create_post(self, user_id, title, body):
        pass

    def update_post(self, post_id, title, body):
        pass

    def delete_post(self, post_id):
        pass