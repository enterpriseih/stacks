# scala

## sbt

```bash
# ~/.sbt/repositories
[repositories]
  local
  aliyun nexus: http://maven.aliyun.com/nexus/content/groups/public/
  type safe-ivy-releases: http://repo.typesafe.com/typesafe/ivy-releases/, [organization]/[module]/[revision]/[type]s/[artifact](-[classifier]).[ext]
  maven-central
  sonatype-snapshots: https://oss.sonatype.org/content/repositories/snapshots

# install
brew install sbt@1

# update
brew upgrade sbt

# check version
sbt sbtVersion

# open terminal
sbt
sbt -Dsbt.override.build.repos=true

# show class path
sbt 'export fullClasspath'
```

## terminal

```bash
# clean
clean

# run
run

# continuous compile
~ compile

# build jar
package

# run with params运行带参数
run <param1> <param2>

# check plugins
plugins

# show subprojects of multiple projects
projects

# select subproject
project <project-id>

# generate docs in target/scala-2.11/api
doc

# check dependencies
evicted

# use sbt-assembly to build all subprojects
assembly

# build subproject fat jar only
<subproject>/assembly
```

## jar

```bash
# show content
jar tf <path_to_my_jar>
```
