# spark shell

## install
```bash
# check java version
java -version

# install java 8 on mac
brew tap caskroom/versions
brew cask install java8

# install scala
brew install scala

# install apache
brew install apache-spark
# to upgrade to 2.4.0
brew upgrade apache-spark
```

## shell
```bash
# open shell
spark-shell

# open shell with es
# use wan.only to turn off auto lookup
spark-shell --jars /Users/zhiyang.wang/.ivy2/cache/org.elasticsearch/elasticsearch-hadoop/jars/elasticsearch-hadoop-6.5.4.jar --conf spark.es.nodes="my_elasticsearch_ip" --conf spark.es.port=9200 --conf spark.es.nodes.wan.only=true
```

## submit
```bash
# check spark version
spark-submit --version

# submit job to local
spark-submit --class my_main_class --master local[4] path_to_my_jar my_param_1 my_param_2

# submit job to cluster
spark-submit --master spark://my_cluster_ip:7077 --executor-memory 2G --total-executor-cores 8 --num-executors 4 --class my_main_class path_to_my_jar my_param_1 my_param_2

# submit job with hdfs & es
HADOOP_USER_NAME=root spark-submit ---master local[4] --num-executors 4 --conf spark.es.nodes="my_elasticsearch_ip" --conf spark.es.port=9200 --conf spark.es.nodes.wan.only=true --class my_main_class path_to_my_jar my_param_1 my_param_2
```

## config
```scala
spark.sparkContext.hadoopConfiguration.set("fs.s3.impl","org.apache.hadoop.fs.s3native.NativeS3FileSystem")
spark.sparkContext.hadoopConfiguration.set("fs.s3.awsAccessKeyId", "my_key")
spark.sparkContext.hadoopConfiguration.set("fs.s3.awsSecretAccessKey", "my_secret")
spark.sparkContext.hadoopConfiguration.set("fs.s3.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
spark.sparkContext.hadoopConfiguration.set("fs.s3a.access.key", "my_key")
spark.sparkContext.hadoopConfiguration.set("fs.s3a.secret.key", "my_secret")
```
