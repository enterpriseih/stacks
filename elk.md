# elk

## install

```bash
# in production env
sudo sysctl -w vm.max_map_count=262144

# elasticsearch data volumes permission
chmod 777 /data/elasticsearch/data/

# setup password
curl -XPUT -u elastic 'my_ip:9200/_xpack/security/user/elastic/_password'  -H "Content-Type: application/json" -d '{"password" : "my_password"}'
```

## elasticsearch

```bash

```

## service

```bash
# elasticsearch
docker service create \
  --network isa \
  --replicas 1 \
  --name elasticsearch \
  -p 9200:9200 \
  -p 9300:9300 \
  --env LS_JAVA_OPTS="-Xmx256m -Xms256m" \
  --env discovery.type=zen \
  --env discovery.zen.ping.unicast.hosts=elasticsearch \
  --env xpack.security.enabled=false \
  --constraint node.hostname==<my_host> \
  --mount type=bind,source=/data/elasticsearch/data,destination=/usr/share/elasticsearch/data \
  docker.elastic.co/elasticsearch/elasticsearch:6.4.2

# logstash
docker service create \
  --network isa \
  --replicas 1 \
  --name logstash \
  -p 5000:5000 \
  -p 9600:9600 \
  --env LS_JAVA_OPTS="-Xmx256m -Xms256m" \
  --env elasticsearch.url=http://elasticsearch:9200 \
  --constraint node.hostname==<my_host> \
  docker.elastic.co/logstash/logstash:6.4.2

docker service update \
  --mount-add type=bind,source=/data/logstash/logstash.conf,destination=/usr/share/logstash/pipeline/logstash.conf \
  logstash

# kibana
docker service create \
  --network isa \
  --replicas 1 \
  --name kibana \
  -p 5601:5601 \
  --env elasticsearch.url=http://elasticsearch:9200 \
  --constraint node.hostname==<my_host> \
  docker.elastic.co/kibana/kibana:6.4.2

# logspout
docker service create \
  --network isa \
  --mode global \
  --restart-condition "on-failure" \
  --restart-delay 30s \
  --name logspout \
  --mount type=bind,source=/var/run/docker.sock,destination=/var/run/docker.sock \
  --env-add RAW_FORMAT="{{ toJSON .Data }}\n" \
  gliderlabs/logspout:latest \
  multiline+raw://<kibana_host>:5000
```
