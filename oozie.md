# oozie

## basic

```bash
# check version
oozie version

# start/stop
sudo stop oozie
sudo start oozie

# restart
sudo restart oozie

# update sharelib
sudo -u oozie oozie admin -sharelibupdate
# list sharelib
oozie admin -oozie http://$(hostname -f):11000/oozie -shareliblist
```
