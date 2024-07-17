from my_jsonplaceholder_api import JSONPlaceHolderAPI

# 해당 클래스 초기화 (Class Instantiation)
api = JSONPlaceHolderAPI()

user_posts = api.get_posts_by_user(1)
for comment in user_posts:
    print(comment['title'])

post_comments = api.get_comments_by_post(1)
for comment in post_comments:
    print(comment['email'])