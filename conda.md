# Conda

```bash
# install
yum install -y bzip2

# install anaconda
wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
bash Anaconda3-5.0.1-Linux-x86_64.sh
export PATH=/data/anaconda3/bin:$PATH

# create new environment aws with python 3.6
conda create -n aws python=3.6

# show environment list
conda env list

# use aws
source activate aws

# show installed packages inside
conda list

# exit aws env
source deactivate

# remove env
conda env remove --name aws
```
