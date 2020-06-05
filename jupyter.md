# jupyter

## basic

```bash
source activate my_env

# if jupyter not recognize my_env
conda install jupyter
conda install nb_conda_kernels

# activate notebook
jupyter notebook

# install extension
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

## lab

```python
# show module
help()

# show device
from tensorflow.python.client import device_lib
device_lib.list_local_devices()

# show system
import platform
platform.uname()
```

```bash
# create new kernel
conda create -n tf2
conda activate tf2
pip install ipykernel
python -m ipykernel install --user --name tf2 --display-name "Python (tf2)"

# show kernels
jupyter kernelspec list

# remove kernel
jupyter kernelspec uninstall <old_kernel>
```
