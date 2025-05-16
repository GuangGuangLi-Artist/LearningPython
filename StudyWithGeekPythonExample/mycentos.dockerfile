FROM centos
MAINTAINER lglg<lala163@163.com>
ENV MYPATH /usr/local
WORKDIR $MYPATH

RUN yum -y install vim
RUN yum -y install net-tools

EXPOSE 80

CMD echo $MYPATH
CMD echo "success----------------ok"
CMD /bin/bash