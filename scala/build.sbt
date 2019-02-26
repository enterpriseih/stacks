//  THISBUILD
ThisBuild / name := "my-projects"
ThisBuild / organization := "com.example"
ThisBuild / scalaVersion := "2.11.12"

// PROJECTS

lazy val root = (project in file("."))

lazy val MyProjectA = (project in file("MyProjectA"))
.settings(
  settings,
  name := "MyProjectA",
  version := "0.1.1",
  assembly / mainClass := Some("com.example.MyProjectA"),
  libraryDependencies ++= Seq(
    "org.apache.spark" %% "spark-core" % "2.3.2" % "provided",
    "org.apache.spark" %% "spark-sql" % "2.3.2" % "provided",
    "org.apache.hadoop" % "hadoop-aws" % "2.8.5" % "provided",
  )
)

// SETTINGS

lazy val settings = Seq(
  assembly / test := {},

  assembly / assemblyMergeStrategy := {
    case PathList("META-INF", xs @ _*) => MergeStrategy.discard
    case x => MergeStrategy.first
  },

  assembly / assemblyOption := (assembly / assemblyOption).value
    .copy(includeScala = false),
  )
)
