from database import Database
from model.post_model import Post


Database.initialize()

post = Post()
post2 = Post()

print(post.content)
print(post2.content)

