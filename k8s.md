# k8s

## install

```bash
# install kubectl on mac
brew install kubectl

# check version
kubectl version --client

# install minikube on mac
brew install minikube

```

## minikube

```bash
# start
minikube start --driver=docker

# show info
kubectl get po -A

# dashboard
# need to remove /usr/local/bin/k9s
minikube dashboard

```
