from database import Database
from model.post_model import Post


Database.initialize()

post = Post(blog_id="123", title="first", content="sample", author="zirong")

post.save_to_mongo()