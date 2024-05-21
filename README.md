## MachineLearningProject1
1. [Github Account](https://github.com/pramodkhavare/MachineLearningProject1.git)

# Used Command in cmd

```
python -m venv env
conda create -p venv python==3.7 -y
```
```
venv\Scripts\activate.bat 
venv/Scripts/Activate.ps1 
```
```
code . (open vs code using cmd)
```
```
python setup.py install
```
```
pip install -r requirements.txt
```
```
pip install -e.
```

# git command 
```
git clone link
```
```
git add .
```
```
git push origin main
```
```
git --version
```
```
git pull
```
```
git status
```
```
git restore <file> /git remove <file>.
```
```
git commit -m "first commit"
```
```
git branch -M main
```
```
git push -u origin main
```
```
git remote -v (to check url/github link)
```

# AWS used services:-
```
1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
```

# For Heroku account
```
gmail = pramodkhavare200@gmail.com
api_key = <>
app_name = machinelearning-app
```

# Docker file command to create Docker Images
```
docker status
docker build -t<image_name>:<tagname> .
docker build -t ml_project:latest .
```
> Note : Image name for docker must lowercase

To list docker image
```
docker images
```
Run Docker Image
```
docker run -p 5000:5000 -e PORT=5000 <Image_id>
```
To check running docker container
```
docker ps
```
To stop docker container
```
docker stop <container_id>
```