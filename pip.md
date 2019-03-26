# pip

```bash
# update outdated packages
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

# install from requirements.txt
pip install -r requirements.txt
```
