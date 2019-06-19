  w34r mad

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
```
