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

**to get latest posts** -

Sorted by date, more recent first
```
GET http://hn.algolia.com/api/v1/search_by_date?query=...
```

 **to get perticular user** -

Users
```
GET http://hn.algolia.com/api/v1/users/:username
```
**and to get items by id** -

Items
```
GET http://hn.algolia.com/api/v1/items/:id
```
