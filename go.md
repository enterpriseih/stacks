# go

## env

```go
// list env
go env

// set env
go env -w GOPATH=$HOME/go
export PATH=$PATH:$(go env GOPATH)/bin
export GOPATH=$(go env GOPATH)

// 无法安装依赖时
go env -w GOPROXY=https://goproxy.io,direct
go env -w GOSUMDB="sum.golang.google.cn"
```

## basic

```go
// init go.sum
go mod init my-repo

// list selected module versions
go list -m all

// install module
go get -u github.com/gin-gonic/gin
```
