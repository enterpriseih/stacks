# aws

## basic

```bash
# add ~/.aws/config
[profile my_profile_1]
region = cn-north-1
output = json
[profile my_profile_2]
region = cn-north-1
output = json

# add ~/.aws/credentials
[my_profile_1]
aws_access_key_id= my_key_1
aws_secret_access_key= my_secret_1
[my_profile_2]
aws_access_key_id= my_key_2
aws_secret_access_key= my_secret_2

# install
pip3 install awscli
pip3 install aws-shell

# use
aws-shell --profile=my_profile_1
```

## file
```bash
# list
s3 ls s3://my_bucket/my_path --recursive --human-readable

# copy
s3 cp s3://my_bucket/my_path local_path --recursive
```
