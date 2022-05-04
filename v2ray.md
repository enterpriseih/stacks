# v2ray

## server

```bash
# tutorial at
# https://github.com/233boy/v2ray/wiki/V2Ray%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E8%84%9A%E6%9C%AC

# install
bash <(curl -s -L https://git.io/v2ray-setup.sh)

# 1. use script
# file at /etc/v2ray/
v2ray

# 2. use as systemd

# check config
ls /etc/systemd/system/v2ray.service.d
cat /etc/systemd/system/v2ray.service.d/10-donot_touch_single_conf.conf

# enable as systemd
sudo systemctl enable v2ray
sudo systemctl disable v2ray

# start
sudo systemctl start v2ray
sudo systemctl stop v2ray
sudo systemctl restart v2ray

# check status
systemctl status v2ray

# check log
ll /var/log/v2ray/
tail /var/log/v2ray/error.log

# firewall
systemctl stop firewalld
systemctl disable firewalld

# update ECS security rule to allow port

```

## client

```bash
# download clashX for mac
https://github.com/yichengchen/clashX/releases

# download new yaml file and add to config folder
https://v2raytech.com/clash_template2.yaml

# modify vmess config
# don't change v2ray name in yaml
- name: "v2ray"
  type: vmess
  server: 1.2.3.4
  port: xxxx
  uuid: xxx
  alterId: 0
  cipher: auto
```
