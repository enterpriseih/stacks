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
