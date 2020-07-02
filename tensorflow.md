# tensorflow

## install

```bash
# create env
conda create -n tensorflow python=3.6

# activate
source activate tensorflow

# install dep
pip install --ignore-installed --upgrade tensorflow
conda install -c anaconda protobuf libgcc
pip install pillow lxml Cython jupyter matplotlib pandas opencv-python
conda install gxx_linux-64
pip install packaging fastparquet

# install with tsinghua
pip install --ignore-installed --upgrade tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple

# install 1.14
pip install tensorflow-gpu==1.14 -i https://pypi.tuna.tsinghua.edu.cn/simple
# in mac
# use pythonw instead of python
conda install python.app

# export
export PYTHONPATH=$PYTHONPATH:my_models/:my_slim/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/anaconda3/envs/tensorflow/lib/:/root/anaconda3/lib/:/data/anaconda3/lib/
```

## tensorboard

```bash
nohup tensorboard --logdir=/path/to/train/dir --host=0.0.0.0 >/dev/null 2>&1&
```

## saved model

```bash
# inspect
saved_model_cli show --dir /path/to/model/dir
saved_model_cli show --dir /path/to/model/dir --tag_set serve --signature_def serving_default

# when error
# __new__() got an unexpected keyword argument 'serialized_options'
pip install -U protobuf
```

## serving

```bash
# deploy
docker pull tensorflow/serving
docker run -t --rm -p [port]:8501 -v "/path/to/model/with/version/subfolder:/models/[my_model_name]" -e MODEL_NAME=[my_model_name] tensorflow/serving -n [my_model_name]

# rest api
# metadata
curl -X GET http://[ip]:[port]/v1/models/my_model_name/metadata

# predict
curl -X POST \
  http://[ip]:[port]/v1/models/my_model_name/versions/[version]:predict \
  -H 'Content-Type: application/json' \
  -d '{
	"instances":[[0.5026455,0.48942696,0.67499523,0.3115942,...]]
}'
```

## jupyter

```python
# show device
from tensorflow.python.client import device_lib
device_lib.list_local_devices()
# or
import tensorflow as tf
tf.config.experimental.list_physical_devices()
# or
import tensorflow as tf
tf.test.is_gpu_available()

# error
# FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
pip install "numpy<1.17"

# check gpu

```

## cuda

```bash
# version
nvcc --version

# check status
nvidia-smi

# when gpu is not listed, check env
export PATH=/usr/local/cuda-10.0:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:$LD_LIBRARY_PATH
```
