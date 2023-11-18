from datetime import date
from django.shortcuts import render
all_posts = [
    {
        "slug":"picture_1",
        "image":"picture_1.jpg",
        "author":"Abdur",
        "date":date(2023,11,18),
        "title":"title_picture_1",
        "excerpt":"....Anything you want",
        "content":".....content"
    },
    {
        "slug":"picture_2",
        "image":"picture_2.jpg",
        "author":"Abdur",
        "date":date(2023,11,18),
        "title":"title_picture_2",
        "excerpt":"....Anything you want",
        "content":".....content"
    },
    {
        "slug":"picture_3",
        "image":"picture_3.jpg",
        "author":"Abdur",
        "date":date(2023,11,18),
        "title":"title_picture_3",
        "excerpt":"....Anything you want",
        "content":".....content"
    },
    {
        "slug":"picture_4",
        "image":"picture_4.jpg",
        "author":"Abdur",
        "date":date(2023,11,18),
        "title":"title_picture_4",
        "excerpt":"....Anything you want",
        "content":".....content"
    }
    
]
def get_date(post):
    return post['date']
# Create your views here.

def starting_page(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(
        request,
        "blog/index.html",
        {
            "posts":latest_posts
        }
        )

def posts(request):
    return render(
        request,
        "blog/all-posts.html",
        {
            "all_posts":all_posts
        }
    )

def post_detail(request,slug):
    identified_post = next(post for post in all_posts if post["slug"]==slug)
    return render(request,"blog/post-detail.html",
                  {"post":identified_post}
                  )