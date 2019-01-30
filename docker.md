# Docker

## Basic

```bash
# install on centos
# https://docs.docker.com/install/linux/docker-ce/centos/#install-docker-ce

sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce-18.03.0.ce

# modifier image dir
touch /etc/docker/daemon.json

# add following lines assuming /data is sufficient
{
    "data-root": "/data/docker"
}

# move images
mv /var/lib/docker/* /data/docker/ -f

# start
sudo systemctl start docker

# stop
sudo systemctl stop docker

# restart
sudo systemctl daemon-reload
sudo systemctl restart docker

# login
docker login <registry> -u <username> -p <password>

# pull image
docker pull <image>

# remove container
docker container stop <container_name> && docker container rm <container_name>

# run image
docker run -d --name <container_name> --restart=always -v <server_dir>:<container_dir>  -p <server_port>:<container_port> <image>

# check port
docker port <container_name>
```

## build.sh

```bash
#!/bin/bash
PUSH_REGISTRY=docker-registry.com
PULL_REGISTRY=docker.com
GIT_COMMIT_ID=`git rev-parse HEAD`
PROJECT=my-project
IMAGE_TAG=${PUSH_REGISTRY}/${PROJECT}:${GIT_COMMIT_ID}

docker build -t ${IMAGE_TAG} .
docker push ${IMAGE_TAG}
```

## Dockerfile

### node

```Dockerfile
FROM node:8.10

RUN mkdir -p /my-group/my-project

COPY . /my-group/my-project

WORKDIR /my-group/my-project

RUN npm install --registry=https://registry.npm.taobao.org

EXPOSE 3000

CMD [ "npm", "start" ]
```
