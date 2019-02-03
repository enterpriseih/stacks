# airflow

```bash
# install
pip install cryptography

# generate frenet key
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```
