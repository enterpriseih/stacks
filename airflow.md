# airflow

```bash
# install
pip install cryptography

# generate frenet key
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

# create Admin
airflow create_user -r Admin -u <user_name> -e <email> -f <first_name> -l <last_name> -p <password>
```
