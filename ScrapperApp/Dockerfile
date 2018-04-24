FROM openshift/base-centos7

RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm

RUN yum -y install python36u

RUN yum -y install python36u-pip

RUN pip3.6 install setuptools

#ARG TEMP_LOCATION=which firefox

#ENV WEBDRIVER_LOCATION=TEMP_LOCATION

RUN mkdir /tmp/predictor-repo

RUN git clone https://github.com/jaycondon/predictor.git /tmp/predictor-repo -v

EXPOSE 8000

WORKDIR /tmp/predictor-repo/ScrapperApp

RUN python3.6 setup.py install

CMD ["python3.6","manage.py","runserver"]