# v2ray

## server

```bash
# https://github.com/233boy/v2ray/wiki/V2Ray%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E8%84%9A%E6%9C%AC

# install
bash <(curl -s -L https://git.io/v2ray-setup.sh)

# config example
#  地址 (Address) = 1.2.3.4.
#  端口 (Port) = 8888
#  用户 ID (User ID / UUID) = xxx
#  额外 ID (Alter Id) = 0
#  传输协议 (Network) = tcp
#  伪装类型 (header type) = none

# enable as systemd
sudo systemctl enable v2ray
sudo systemctl disable v2ray

# start
sudo systemctl start v2ray
sudo systemctl stop v2ray
sudo systemctl restart v2ray

# check status
systemctl status v2ray

# check config
ls /etc/systemd/system/v2ray.service.d

# check log
ll /var/log/v2ray/
tail /var/log/v2ray/error.log

# firewall
systemctl stop firewalld
systemctl disable firewalld

```

## client

```bash
# download clashX for mac
https://github.com/yichengchen/clashX/releases

# download new yaml file and add to config folder
https://v2raytech.com/clash_template2.yaml

# modify vmess config
- name: "v2ray"
  type: vmess
  server: 1.2.3.4
  port: 8888
  uuid: xxx
  alterId: 0
  cipher: auto

```
