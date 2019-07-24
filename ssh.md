# ssh

## ~/.ssh/config

    Host *
      ServerAliveInterval 5
      UseKeychain yes
      IdentityFile ~/.ssh/github
      IdentityFile ~/.ssh/id_rsa
      StrictHostKeyChecking no

## ~/sync.sh

```bash
#!/bin/bash

echo `date`
printf "\n"

filenames=$(ls -d */*/.git)

for name in $filenames
do
    folder=~/${name::${#name} - 4}
    echo $folder
    cd $folder
    git pull --all && git submodule update
    printf "\n"
done
```

## /Users/zhiyang.wang/Library/LaunchAgents/sync.git.plist

```bash
# check validity
plutil /Users/zhiyang.wang/Library/LaunchAgents/sync.git.plist

# load
launchctl load /Users/zhiyang.wang/Library/LaunchAgents/sync.git.plist

# unload
launchctl unload /Users/zhiyang.wang/Library/LaunchAgents/sync.git.plist

# start
launchctl start sync.git
```

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>Label</key>
<string>sync.git</string>
<key>Program</key>
<string>/Users/zhiyang.wang/sync.sh</string>
<key> StartCalendarInterval</key>
<dict>
<key>Hour</key>
<integer>10</integer>
<key>Minute</key>
<integer>40</integer>
</dict>
</dict>
</plist>
```
