from blog.database import mongo
from datetime import datetime

def get_all_posts(published: bool = True):
    posts = mongo.db.posts.find({"published": published})
    return posts.sort("date")
    
def get_post_by_slug(slug: str) -> dict:
    post = mongo.db.posts.find_one({"slug": slug})
    return post
    
def update_post_by_slug(slug: str, data: dict) -> dict:
    return  mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": data})

def new_post(title: str, content: str, published: bool = True) -> dict:
    slug = title.replace(" ", "-").replace("_", "-").lower()
    post = {
        "title": title,
        "content": content,
        "published": published,
        "slug": slug,
        "date": datetime.now()
    }
    mongo.db.posts.insert_one(post)
    return slug