from django.shortcuts import render, redirect
import requests
import redis
import json
from datetime import timedelta
from django.contrib import messages

redis_data = redis.Redis.from_url('rediss://red-ces58ckgqg4dp7osntrg:IoErEp3b89kSifhHQZuRrZ7sKloq0r9M@oregon-redis.render.com:6379')

# Create your views here.
def home(request):
    if redis_data.get('hits') is None:
        url = "http://hn.algolia.com/api/v1/search_by_date?"
        params = {
            "tags": "story"
        }  
        response = requests.get(url, params=params).json()
        List_hits = response['hits']
        redis_data.set('hits', json.dumps(List_hits))
        redis_data.expire('hits', timedelta(seconds=30))
        messages.info(request, 'Could not find cache, fetched newer posts from HN server and stored cache as well, to reduce number of server requests and make response times faster.')
    else:
        List_hits = json.loads(redis_data.get('hits'))
        messages.info(request, 'Loaded from stored cache, you can refresh page after 60 seconds, ususally new posts are updated in around 1 minute.')
    return render(request, 'home.html', {'List_hits': List_hits})


def view_post(request):
    objectID = request.POST['objectID']
    url = "http://hn.algolia.com/api/v1/items/"

    response = requests.get(url + objectID).json()
    title = response['title']
    text = response['text']
    author = response['author']
    children = response['children']
    try:
        url = response['url']
    except KeyError:
        url = ''
    
    return render(request, 'view_post.html', {'title': title, 'url': url,
     'text':text, 'author': author, 'children': children})


def user(request):
    username = request.POST['username']
    url = "http://hn.algolia.com/api/v1/users/"
    user_data = requests.get(url + username).json()
    username = user_data['username']
    about = user_data['about']
    karma = user_data['karma']
    return render(request, 'user_page.html', {'username': username, 
    'about': about, 'karma': karma})
    

