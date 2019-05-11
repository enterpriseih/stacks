FROM centos:centos7
MAINTAINER Zhiyang Wang "zhiyang.wang@nio.com"

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install python36; yum clean all
RUN yum -y install python-pip; yum clean all

COPY . /app

WORKDIR /app

RUN cd /app; pip install -r requirements.txt

ENTRYPOINT ["python"]

EXPOSE 8080

CMD ["app.py"]
