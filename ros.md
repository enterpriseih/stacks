# ros

## docker
```bash
# pull image
docker pull ros:foxy

# run docker name=foxy
docker container run --name foxy -it ros:latest

# enter docker
docker exec -it foxy /bin/bash

# source setup
source ./ros_entrypoint.sh

# backup container
docker commit -p <container_id> <image_name>

# run backup
docker container run --name foxy -it <image_name>:latest
```
