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

![Diagram.svg](./Diagram.svg)

## Instructions 

**Python 3.8**
```
sudo apt install python3-pip

sudo apt install python3.8-venv
```
**Venv**

creating --
```
python3 -m venv env
```
activating --
```
source env/bin/activate
```

**To install docker**

install curl-
```
sudo apt install curl
```
convineint script-
```
curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh
```

**Installing Docker Compose standalone**
```
sudo curl -SL https://github.com/docker/compose/releases/download/v2.15.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
```
and give the su permission.

**Apply executable permissons**
```
sudo chmod +x /user/local/bin/docker-compose
```
Compose standalone uses the -compose syntax instead of the current standard syntax compose.

**Test and execute compose commands using docker-compose**

for example -
```
docker-compose --version
```

**To indivisually  install requirements**
```
 pip3 install -r requirements.txt
```

**Create docker image using single dockerfile**
```
sudo docker build -t image_name .
```
**Run it**
```
sudo docker run -p 8000:8000 image_name
```
**Running gunicorn server**
```
gunicorn projectname.wsgi:application --bind 0.0.0.0:8000 
```
**To build images via docker compose**
```
sudo docker compose build
```
**To run docker images**
```
sudo docker compose up
```

# Normal installation

**For installing djnago**
```
pip install django
```
**Install request library**
```
pip install requests = library
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
1. Its been hard to parse paragraf tags comming from api, i have used django 
template filters and other things to make it parse, but i don't know yet
what more can be done.

2. UI is still not perfect since i didn't used much of frontend technologies,
and my lack of knowledge this portion.

3. Redis cache only helps in lastest posts, we have to still have to
request server in case of getting perticular post.