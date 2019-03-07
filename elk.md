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
