# spark

## start master & slave

```bash
# download
wget http://mirror.bit.edu.cn/apache/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz

# unzip
tar xf spark-2.4.0-bin-hadoop2.7.tgz
cd spark-2.4.0-bin-hadoop2.7

# start master
./sbin/start-master.sh

# start slave
./sbin/start-slave.sh spark://my_ip:7077
```

## install on mac

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

## spark-shell

```bash
# open shell
spark-shell

# local
spark-shell --master local[*]

# yarn
spark-shell --master yarn-client

# open shell with es
# use wan.only to turn off auto lookup
spark-shell --jars /Users/zhiyang.wang/.ivy2/cache/org.elasticsearch/elasticsearch-hadoop/jars/elasticsearch-hadoop-6.5.4.jar --conf spark.es.nodes="my_elasticsearch_ip" --conf spark.es.port=9200 --conf spark.es.nodes.wan.only=true
```

## spark-submit

```bash
# check spark version
spark-submit --version

# submit job to local
spark-submit --class my_main_class --master local[4] path_to_my_jar my_param_1 my_param_2

# submit job to cluster
spark-submit --master spark://my_cluster_ip:7077 --executor-memory 2G --total-executor-cores 8 --num-executors 4 --class my_main_class path_to_my_jar my_param_1 my_param_2

# submit job with hdfs & es
HADOOP_USER_NAME=root spark-submit ---master local[4] --num-executors 4 --conf spark.es.nodes="my_elasticsearch_ip" --conf spark.es.port=9200 --conf spark.es.nodes.wan.only=true --class my_main_class path_to_my_jar my_param_1 my_param_2

# submit job in python to cluster
spark-submit --master spark://my_cluster_ip:7077 --executor-memory 2G --total-executor-cores 8 --num-executors 50 my_job.py

# submit job in python to local
spark-submit --master local[4] my_job.py
```

## spark-shell

```scala
spark.read.parquet("path/to/file").printSchema()

df.select(List($"column1", $"column2.column2sub".getItem(0).getField("field1")):_*).show(100, false)

df.filter($"column1".isNotNull && $"column2" === "value2" && $"column3" =!= "value3")
df.filter($"column1".isin("column1", "column2"))

df.orderBy($"column1")
df.sort($"column1".desc)

df.groupBy($"column1", $"column2").agg(sum($"column2").as("column3"))

df.withColumn("hour",hour(col("sample_ts")))

// multiple line mode
:paste
```

## pyspark

```bash
# open pyspark
pyspark
```

```python
# config
conf = SparkConf()
"""
conf.set('fs.defaultFS', 'hdfs://hdfs')
conf.set('dfs.nameservices', 'hdfs')
conf.set('dfs.ha.namenodes.hdfs', 'name-0-node,name-1-node')
conf.set('dfs.namenode.http-address.hdfs.name-0-node', 'ip:9002')
conf.set('dfs.namenode.http-address.hdfs.name-1-node', 'ip:9002')
conf.set('dfs.client.failover.proxy.provider.hdfs', 'org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider')
"""
spark = SparkSession.builder.appName('my_app').config(conf=conf).getOrCreate()

# read hdfs file
df = spark.read.csv('hdfs://ip:9001/my_file.csv', inferSchema=True, header=True)

# create RDD
lines = sc.parallelize(["pandas", "i like pandas"])
lines = sc.textFile("/path/to/README.md")
rdd = sc.textFile("s3://...")
sc.wholeTextFiles("hdfs://...")

# read
df = spark.read.parquet("*.parquet")
df = spark.read.csv("*.csv")

# write
df.saveAsTextFile()
df.saveAsSequenceFile()
df.write.option("header", True).csv('/temp/')
df.write.mode('append').parquet('/temp/')
df.write.format("parquet").save('/temp/')

# dataframe API
# transformation (returns a new RDD)
# filter
df.filter(df.column1=="value1")
df.filter("column1=='value1'")
df.filter(df.column1.isNotNull())
lines.filter(lambda line: "Python" in line)

#
df.withColumn('column1',psf.explode('column1.list_field'))

# distinct
df.select($"my_field").distinct.show()

# dedup
df.dropDuplicates(['name', 'height'])

# map
squared = nums.map(lambda x: x * x).collect()
words = rdd.flatMap(lambda x: x.split(" "))

# flatMap
words = lines.flatMap(lambda line: line.split(" "))

# set
df1.union(df2)
.intersection()
.substract()
.cartesian()

# aggregate in pair RDD
df.reduceByKey()
df.foldByKey()
df.combineByKey()

# partition
df.partitionBy()

# actions (return a result of other data type to the driver program)
df.count()
df.countByValue()

# retrieve
lines.first()
df.take(10)
df.collect()
df.top()

#
df.reduce()
df.combine()
df.fold(zero,func)
df.foreach()

#
df.countByKey()
df.collectAsMap()
df.lookup(key)

# sort
df.sortByKey()

# persist in memory
df.cache()
df.storageLevel
df.cache().storageLevel
df2.persist(StorageLevel.DISK_ONLY_2).storageLevel
df.unpersist
```
