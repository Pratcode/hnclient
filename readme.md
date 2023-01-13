# A hacker-News client from Algolia Search's API for Hacker News

Utilises API which built on top of Algolia Search's API for Hacker News,
HN Search provides real-time full-text search for the HackerNews community site,
The search backend is implemented using Algolia instant search engine.

1. can view posts in bit better UI.
2. mostly focused on latest posts, to remain updated.
3. redis cache is utilised to cache posts for certain time interval 
- approximatly till new posts get updated.
- it reduces amount of server requests.
- makes response time faster.
4. utilized nginx as simple reverse proxy server to hide direct access.
5. containerition of django, nginx and redis to handle complex dependencies.

## Explainatory diagram

## Instructions 

**to indivisually  install requirements**- 
```
 pip3 install -r requirements.txt
```
**django runserver**-
```
python manage.py runserver
```
**create docker image using single dockerfile**-
```
sudo docker build -t image_name .
```
**run it**-
```
sudo docker run -p 8000:8000 image_name
```
**running gunicorn server**-
```
gunicorn projectname.wsgi:application --bind 0.0.0.0:8000 
```
**to build images via docker compose**-
```
sudo docker compose build
```
**to run docker images**-
```
sudo docker compose up
```

## Known issues-
1. Its been hard to parse paragraf tags comming from api, i have used django 
template filters and other things to make it parse, but i don't know yet
what more can be done.

2. UI is still not perfect since i didn't used much of frontend technologies,
and my lack of knowledge this portion.

3. Redis cache only helps in lastest posts, we have to still have to
request server to get perticular post.