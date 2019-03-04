package com.example

import java.net.URI
import org.slf4j.{ LoggerFactory, Logger }

import org.apache.hadoop.fs.Path
import org.apache.hadoop.fs.s3a.S3AFileSystem
import org.apache.spark.sql.SparkSession

object MyProjectA {
  def main(args: Array[String]) {
    val LOGGER: Logger = LoggerFactory.getLogger("MyProjectA")
    LOGGER.info("START")

    val spark = SparkSession
      .builder
      .appName("MyProjectA")
      .getOrCreate()

    fs.close()
    spark.stop()
    LOGGER.info("DONE")
  }
}
