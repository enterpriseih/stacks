# spark

## start master & slave

```bash
# download
wget http://mirror.bit.edu.cn/apache/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz
wget http://mirrors.tuna.tsinghua.edu.cn/apache/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz

# unzip
tar xf spark-2.4.0-bin-hadoop2.7.tgz
cd spark-2.4.0-bin-hadoop2.7

# start master
./sbin/start-master.sh

# start slave
./sbin/start-slave.sh spark://my_ip:7077

# path
export PATH=/data/spark/bin:$PATH
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
# show current version
brew info apache-spark
# switch to 2.3.1
brew switch apache-spark 2.3.1
# list all available version
brew list apache-spark --versions

# install specific version via formula
# find commit
cd "$(brew --repo homebrew/core)"
git log Formula/apache-spark.rb
# 2.3.2 0f3992a1e6d036dab8b420903d856231e7701ba1
# or use github history
# then download formula rb https://github.com/Homebrew/homebrew-core/blob/0f3992a1e6d036dab8b420903d856231e7701ba1/Formula/apache-spark.rb
# modify line4 to a correct url "http://archive.apache.org/dist/spark/spark-2.3.2/spark-2.3.2-bin-hadoop2.7.tgz"
# save rb to local and install via it
brew install ./apache-spark.rb
```

## spark-shell

```bash
# open shell
spark-shell
spark-shell --executor-memory 9g --total-executor-cores 9 --num-executors 9 --driver-memory 9g
spark-shell --executor-memory 4g --total-executor-cores 8 --num-executors 8 --driver-memory 4g

# local
spark-shell --master local[*]

# yarn
spark-shell --master yarn-client

# open shell with es
# use wan.only to turn off auto lookup
spark-shell --jars /Users/zhiyang.wang/.ivy2/cache/org.elasticsearch/elasticsearch-hadoop/jars/elasticsearch-hadoop-6.5.4.jar --conf spark.es.nodes="my_elasticsearch_ip" --conf spark.es.port=9200 --conf spark.es.nodes.wan.only=true

# open shell with cassandra
spark-shell \
--jars /Users/zhiyang.wang/.ivy2/cache/com.datastax.spark/spark-cassandra-connector_2.11/jars/spark-cassandra-connector_2.11-2.3.2.jar,/Users/zhiyang.wang/.ivy2/cache/com.twitter/jsr166e/jars/jsr166e-1.1.0.jar \
--conf spark.cassandra.connection.host=<my_ip1>,<my_ip2>

# open shell with jdbc
spark-shell --jars /Users/zhiyang.wang/.ivy2/cache/mysql/mysql-connector-java/jars/mysql-connector-java-5.1.24.jar

# open shell with application.conf
spark-shell --jars /Users/zhiyang.wang/.ivy2/cache/com.typesafe/config/bundles/config-1.4.0.jar --files 'application.conf'

# multiple line mode
:paste
```

```scala
// read conf
import com.typesafe.config.ConfigFactory
import java.io.File
import org.apache.spark.SparkFiles

val config = ConfigFactory.parseFile(new File(SparkFiles.get("application.conf")))
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
HADOOP_USER_NAME=root spark-submit --master local[4] --num-executors 4 --conf spark.es.nodes="my_elasticsearch_ip" --conf spark.es.port=9200 --conf spark.es.nodes.wan.only=true --class my_main_class path_to_my_jar my_param_1 my_param_2

# submit job in python to cluster
spark-submit --master spark://my_cluster_ip:7077 --executor-memory 2G --total-executor-cores 8 --num-executors 50 my_job.py

# submit job in python to local
spark-submit --master local[4] my_job.py
spark-submit \
  --master local[4] \
  --driver-memory 4G --executor-memory 4G  \
  --num-executors 4 --total-executor-cores 8 \
  --conf spark.driver.maxResultSize=2G \
  my_job.py
```

## spark-shell

### fs

```scala
import org.apache.hadoop.fs.{FileSystem,Path}
import org.apache.commons.io.FileUtils

val statuses = FileSystem.get( sc.hadoopConfiguration ).listStatus(new Path("/user"))

for (status <- statuses) {
    println(status.toString())
    println(FileUtils.byteCountToDisplaySize(status.getLen()))
}
```

### read

```java
// scala
// input
spark.read.parquet("path/to/file").printSchema()
spark.read.option("header", "true").csv("/path/to/csv.csv")
val path = "s3a://my_bucket/my_path/201907{10,11,12,13,14,15,16,17,18}"
spark.read.option("basePath",base_path).parquet(base_path + "day=20181030")
```

### write

```scala
// output parquet
df.coalesce(1)
.write
.mode("overwrite")
.parquet(OUTPUT_PATH)

// output csv
df.coalesce(1)
.write
.format("csv")
.option("header","true")
.mode("overwrite")
.save("/tmp/")
```

### view

```scala
trueUserOrderData.createOrReplaceTempView("order_data")
```

### select

```scala
// select
df.select(List($"column1", $"column2.column2sub".getItem(0).getField("field1")):_*)
df.select($"*", posexplode($"parent_field.nested_fields").as("nested_fields_index" :: "nested_fields_list" :: Nil))
df.select(
  List(
    $"column1",
    to_timestamp(extract_first($"time"), "yyyyMMddHHmmssSSS").as("timestamp")
    when($"nested_fields_index".isNull, typedLit(null))
      .otherwise(callUDF("extract_first", $"nested_fields_index"))
      .as("nested_fields_index")
  )
  ++ List.range(0,42).map( i => $"nested_fields_list".getItem(i).as(s"nested_fields_list_$i").cast(DoubleType))
)
df.first
df.take(10)
df.filter($"column1".isNotNull && $"column2" === "value2" && $"column3" =!= "value3")
df.filter($"column1".isin("column1", "column2"))
df.orderBy($"column1")
df.sort($"column1".desc)
df.foreach(println)
df.cache()
```

### withColumn

```scala
df.withColumn("hour",hour(col("sample_ts")))
df.withColumn("column1", typedLit(null))
df.withColumnRenamed("column1", "new_column1")

// output jdbc
val OUTPUT_URL: String = "jdbc:mysql://ip:port/db?characterEncoding=UTF-8&useSSL=false&useUnicode=true"
val OUTPUT_TABLE: String = "my_table"
val OUTPUT_PROP = new java.util.Properties()
OUTPUT_PROP.put("user", "user")
OUTPUT_PROP.put("password", "pwd")
OUTPUT_PROP.put("driver", "com.mysql.jdbc.Driver")
OUTPUT_PROP.put("batchsize", "5000")
OUTPUT_PROP.put("numPartitions", "8")
OUTPUT_PROP.put("truncate", "true")
df.repartition(8)
  .write.mode("overwrite")
  .jdbc(OUTPUT_URL, OUTPUT_TABLE, OUTPUT_PROP)
```

### udf

```scala
def getHours(start:java.sql.Timestamp,end:java.sql.Timestamp): List[Int] = {
  if(start != null && end != null) {
    val result = ListBuffer[Int]()
    while(start.before(end)) {
      val hour = start.getHours()
      result += hour
      val timestamp = start.getTime() + 3600000
      start.setTime(timestamp)
    }
    result.toList
  } else {
    List()
  }
}

def extract_first = udf((key:String) => key.split("#")(0))

def secondsBetween(c1: Column, c2: Column) = c2.cast("timestamp").cast("bigint") - c1.cast("timestamp").cast("bigint")

def previousHalf(pre: Column, cur: Column) = (cur.cast("timestamp").cast("bigint") - pre.cast("timestamp").cast("bigint")) / 2.0

def bothHalf(pre: Column, cur: Column, next: Column) = {
  (cur.cast("timestamp").cast("bigint") - pre.cast("timestamp").cast("bigint")) / 2.0 +
  (next.cast("timestamp").cast("bigint") - cur.cast("timestamp").cast("bigint")) / 2.0
}

def nextHalf(cur: Column, next: Column) = (next.cast("timestamp").cast("bigint") - cur.cast("timestamp").cast("bigint")) / 2.0

def avg_list: Row => Double = (row) => {
  row.getAs[Seq[Short]]("list_field")
  .map(_.doubleValue)
  .foldLeft((0.0, 1))((acc, i) =>((acc._1 + (i - acc._1) / acc._2), acc._2 + 1))
  ._1
  .asInstanceOf[Double]
}

spark.udf.register("avg_list", avg_list)
```

### udaf

```scala
// merge rows by use any non-null value
class MergeSingleWithNulls (field : String, data_type: DataType) extends UserDefinedAggregateFunction {
   override def inputSchema: StructType = StructType(StructField(field, data_type) :: Nil)
   override def bufferSchema: StructType = StructType(StructField(field, data_type) :: Nil)
   override def dataType: DataType = data_type
   override def deterministic: Boolean = true
   override def initialize(buffer: MutableAggregationBuffer): Unit = {
     buffer.update(0, null)
   }
   override def update(buffer: MutableAggregationBuffer, input: Row): Unit = {
     if(buffer(0) == null && input(0) != null){
       buffer.update(0, input(0))
     }
   }
   override def merge(buffer1: MutableAggregationBuffer, buffer2: Row): Unit = {
     if(buffer1(0) == null && buffer2(0) != null){
       buffer1.update(0, buffer2(0))
     }
   }
   override def evaluate(buffer: Row): Any = {
     buffer(0)
   }
}
// merge seq[double] lists by element-wise sum
class MergeListSum (field : String) extends UserDefinedAggregateFunction {
   override def inputSchema: StructType = StructType(StructField(field,  ArrayType(DoubleType)) :: Nil)
   override def bufferSchema: StructType = StructType(StructField(field,  ArrayType(DoubleType)) :: Nil)
   override def dataType: DataType =  ArrayType(DoubleType)
   override def deterministic: Boolean = true
   override def initialize(buffer: MutableAggregationBuffer): Unit = {
     buffer(0) = Array.fill[Double](42)(0.0).toSeq
   }
   override def update(buffer: MutableAggregationBuffer, input: Row): Unit = {
     val b1 = buffer.getAs[Seq[Double]](0)
     val b2 = input.getAs[Seq[Double]](0)
     buffer.update(0, b1.zip(b2).map { case(x,y) => x+y})
   }
   override def merge(buffer1: MutableAggregationBuffer, buffer2: Row): Unit = update(buffer1, buffer2)
   override def evaluate(buffer: Row): Any = {
     buffer(0)
   }
}
// concat all string
class ConcatString (field : String) extends UserDefinedAggregateFunction {
   override def inputSchema: StructType = StructType(StructField(field, StringType) :: Nil)
   override def bufferSchema: StructType = StructType(StructField(field,  StringType) :: Nil)
   override def dataType: DataType =  StringType
   override def deterministic: Boolean = true
   override def initialize(buffer: MutableAggregationBuffer): Unit = {
     buffer(0) = ""
   }
   override def update(buffer: MutableAggregationBuffer, input: Row): Unit = {
     val b1 = buffer.getAs[String](0)
     val b2 = input.getAs[String](0)
     if(b1 == ""){
       buffer.update(0,b2)
     }else{
       if(b2 != ""){
         buffer.update(0, b1+"#"+b2)
       }
     }
   }
   override def merge(buffer1: MutableAggregationBuffer, buffer2: Row): Unit = update(buffer1, buffer2)
   override def evaluate(buffer: Row): Any = {
     buffer(0)
   }
}

spark.udf.register("field1", new MergeSingleWithNulls("field1", TimestampType))
spark.udf.register("list_field1", new MergeListSum("list_field1"))
df.groupBy($"field1", $"field2")
  .agg(
    callUDF("field1", $"field1").as("field1"),
    callUDF("list_field1", $"list_field1").as("list_field1"),
  )
```

### window

```scala
// using temp to merge (start_timestamp - end_timestamp) < 10min rows
val window = Window.partitionBy($"id").orderBy($"start_timestamp")
val window2 = Window.partitionBy($"id").orderBy($"start_timestamp".desc)
df.withColumn("merge_start", when(
    row_number.over(window) === 1 ||
    secondsBetween(lag($"end_timestamp", 1).over(window), $"start_timestamp") > 600, $"start_timestamp"))
  .withColumn("merge_end", when(
    row_number.over(window2) === 1 ||
    secondsBetween($"end_timestamp", lead($"start_timestamp", 1).over(window)) > 600, $"end_timestamp"))
  .withColumn("start", last($"merge_start", ignoreNulls = true).over(window.rowsBetween(Window.unboundedPreceding,0)))
  .withColumn("end", first($"merge_end", ignoreNulls = true).over(window.rowsBetween(0,Window.unboundedFollowing)))
  .withColumn("merged_id", concat(
    $"start".cast(StringType),
    typedLit("#"),
    $"end".cast(StringType)))
```

### join

```scala
df1.join(df2, Seq("key column"), "left_outer")
```

## util

### time

```scala
spark.time(
// code
)
```

### size

```scala
import org.apache.spark.util.SizeEstimator
SizeEstimator.estimate(df)
```

### explain physical plan

```scala
spark.sql("select * from db.table").explain
```

## docker-compose.yml

```yml
version: '2'
services:
  spark-worker-1:
    image: bde2020/spark-worker:2.3.2-hadoop2.7
    environment:
      SPARK_MASTER: spark://spark-master:7077
    ports:
    - 8081:8081/tcp
    labels:
      io.rancher.scheduler.affinity:host_label: spark-worker=true
  spark-master:
    image: bde2020/spark-master:2.3.2-hadoop2.7
    environment:
      INIT_DAEMON_STEP: setup_spark
    ports:
    - 8080:8080/tcp
    - 7077:7077/tcp

```

## rancher-compose.yml

```yml
version: '2'
services:
  spark-worker-1:
    scale: 1
    start_on_create: true
  spark-master:
    scale: 1
    start_on_create: true
```
