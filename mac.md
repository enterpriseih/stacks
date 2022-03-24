# mac

## basic

```bash
# show wireless ip address
ipconfig getifaddr en1

# show ethernet ip address
ipconfig getifaddr en0

# show top 5 process
ps aux -O pcpu | head -5

# create custom domain/ip mapping
sudo vi /etc/hosts
# add [real-ip] [custom-domain] in file

# can't open
sudo xattr -rd com.apple.quarantine /Applications/<APP>.app
sudo xattr -rd com.apple.quarantine "/Applications/wpsoffice.app"

sudo spctl --master-disable

# convert caj to pdf
pip install PyPDF2
brew install mupdf
./caj2pdf show <source.pdf>
./caj2pdf convert <source.pdf> -o <target.pdf>

# zip with maxsize
zip -r -s 1g 20190516_bak.zip ./

# maximun compression
zip -9 ...

# unzip error: Unzipping large file: bad zipfile offset (local header sig)
zip -FF original.zip --out fixed.zip
unzip fixed.zip

# stop creating .DS_Store files
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE

# delete .DS_Store file
find . -name '.DS_Store' -type f -delete

# upon start
sudo launchctl list
sudo launchctl unload /Library/LaunchDaemons/com.symantec.manufacturer.agent.plist
sudo launchctl unload /Library/LaunchDaemons/com.mcafee.ssm.Eupdate.plist
sudo launchctl unload /Library/LaunchDaemons/com.mcafee.ssm.ScanFactory.plist
sudo launchctl unload /Library/LaunchDaemons/com.mcafee.ssm.ScanManager.plist
sudo launchctl unload /Library/LaunchDaemons/com.mcafee.virusscan.fmpd.plist
sudo launchctl unload /Library/LaunchDaemons/com.mcafee.aac.plist
sudo launchctl unload "/Library/Manufacturer/Endpoint Agent/CUI.plist"
sudo launchctl unload /Library/LaunchDaemons/com.vmware.hub.installer.daemon.plist
sudo launchctl unload /Library/LaunchDaemons/com.airwatch.airwatchd.plist
sudo launchctl unload /Library/LaunchDaemons/com.airwatch.awcmd.plist
sudo launchctl unload /Library/LaunchDaemons/com.airwatch.AWRemoteManagementDaemon.plist
sudo launchctl unload /Library/LaunchDaemons/com.airwatch.AWRemoteTunnelAgent.plist

# restart audio
sudo killall coreaudioud

# delete .DS
cd /my/dir
find . -name '.DS_Store' -type f -delete

# batch download
# 1. save url in a txt
# 2. use wget
wget -E -H -k -p -i /path/to/url/txt

# open url in chromw
/usr/bin/open -a "/Applications/Google Chrome.app"  'http://google.com'

# change brew source
git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git

echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles' >> ~/.bash_profile
source ~/.bash_profile

# mov to gif
ffmpeg -i in.mov -s 600x300 -pix_fmt rgb24 -r 30 -f gif - | gifsicle --optimize=3 --delay=3 > out.gif

# show port
sudo lsof -iTCP -sTCP:LISTEN -n -P
```

## sdk

```bash
curl -s "https://get.sdkman.io" | bash
```
