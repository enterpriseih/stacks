# tensorflow

## install

```bash
# create env
conda create -n tensorflow python=3.6

# activate
source activate tensorflow

# install dep
pip install --ignore-installed --upgrade tensorflow
conda install -c anaconda protobuf
pip install pillow
pip install lxml
pip install Cython
pip install jupyter
pip install matplotlib
pip install pandas
pip install opencv-python
conda install libgcc

# in mac
# use pythonw instead of python
conda install python.app

# export
export PYTHONPATH=$PYTHONPATH:my_models/:my_slim/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/anaconda3/envs/tensorflow/lib/:/root/anaconda3/lib/:/data/anaconda3/lib/
```

## tensorboard

```bash
tensorboard --logdir=/path/to/train/dir
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
