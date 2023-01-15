# A hacker-News client using Algolia Search's API for Hacker News

Utilizes API which built on top of Algolia Search's API for Hacker News,
HN Search(Algolia Search's API) provides real-time full-text search for the Hacker News 
community site, its search backend is implemented using Algolia instant search engine.

## Explanation

The client has visually clear containerized posts, useful when we want to remain updated
about latest news, even tho hacker news is not a proper news site, but still it's better
platform to remain updated about tech updates. 

### Redis

It utilizes Redis cache, so it won't burden the server for normal actions,
and increase response time, Redis cache expires in around 1 minutes, till
newer posts get updated, cache applies when getting latest posts.

### Containerization

The applications are containerized in individual docker containers,
for Django and Nginx (Dockerfile), and official Redis image, handled
together by docker compose, where nginx is connected to frontend 
network (docker networking), while Django and Redis are connected to 
backend network, nginx is serving simple reverse proxy, Django server 
serves it on port "8000".

### Key points

1. Can view posts in a bit of visual UI.
2. Mostly focused on latest posts, to remain updated.
3. Redis cache is utilized to cache posts for certain time interval, 
- Approximately till new posts get updated.
- It reduces number of server requests.
- Makes response time faster.
4. Utilized nginx as simple reverse proxy server to hide direct access.
5. Containerization of Django, nginx and Redis to handle complex dependencies.

## Explanatory diagram

![Diagram.svg](./Diagram.svg)

## Instructions 

### Python
---

**Python 3.8**

(for linux)
```
sudo apt install python3-pip
```
```
sudo apt install python3.8-venv
```

**Venv**

creating-
```
python3 -m venv env
```
activating-
```
source env/bin/activate
```
### Docker
---

**To install docker**

(Using curl)

install curl-
```
sudo apt install curl
```
get convineint script using curl-
```
curl -fsSL https://get.docker.com -o get-docker.sh
```
execute the script-
```
sudo sh get-docker.sh
```
### Docker Compose standalone
---

**Installing Docker Compose standalone**

(Using curl)
```
sudo curl -SL https://github.com/docker/compose/releases/download/v2.15.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
```
give the sudo permission to get it.

**Apply Executable permissons**
```
sudo chmod +x /user/local/bin/docker-compose
```
Compose standalone uses the -compose syntax instead of 
the current standard syntax compose.

**Test and Execute compose commands using docker-compose**

for example-
```
docker-compose --version
```

**To individually  install requirements**
```
 pip3 install -r requirements.txt
```
### Using only dockerfile
---

**Create docker image using single dockerfile**
```
sudo docker build -t image_name .
```
**Run it**
```
sudo docker run -p 8000:8000 image_name
```

### Gunicorn server
---

**Running gunicorn server**
```
gunicorn projectname.wsgi:application --bind 0.0.0.0:8000 
```

### Docker Compose
---

(which can handle everything, once defined)

**To build images via docker compose**
```
sudo docker compose build
```
**To run docker images**
```
sudo docker compose up
```

## Normal Installation

(of dependencies)

**For installing django**
```
pip install django
```
**Install request library**
```
pip install requests
```
**Installing redis library**
```
pip install redis
```
**Install gunicorn**
```
pip install gunicorn
```
**Django runserver**
```
python manage.py runserver
```

## Known issues

1. It's been hard to parse paragraph tags coming from API, I have used Django 
template filters and other things to make it parse, but I don't know yet
what more can be done.

2. UI is still not perfect since I didn't use much of frontend technologies,
and my lack of knowledge in this portion.

3. Redis cache only helps in latest posts, we have to still have to
request server in case of getting particular post.