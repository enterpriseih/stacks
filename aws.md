# aws

## basic

```bash
# add ~/.aws/config
[default]
region = cn-north-1
output = json
[profile my_profile_1]
region = cn-north-1
output = json
[profile my_profile_2]
region = cn-north-1
output = json

# add ~/.aws/credentials
[default]
aws_access_key_id= my_key
aws_secret_access_key= my_secret
[my_profile_1]
aws_access_key_id= my_key_1
aws_secret_access_key= my_secret_1
[my_profile_2]
aws_access_key_id= my_key_2
aws_secret_access_key= my_secret_2

# install
pip3 install awscli
pip3 install aws-shell
```

## aws-shell

```bash
# use
aws-shell --profile=my_profile_1

# list
s3 ls s3://my_bucket/my_path --recursive --human-readable

# copy
s3 cp s3://my_bucket/my_path local_path --recursive
```

## aws cli

```bash
# show credentials
aws configure list
aws configure list --profile=my_profile_1

# list
aws s3 ls s3://my_bucket/my_path --profile=my_profile_1

# copy source to target
aws s3 cp s3://my_bucket/my_path local_path --recursive

# remove
aws s3 rm s3://my_bucket/my_path --recursive
```
