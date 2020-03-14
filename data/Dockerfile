FROM ubuntu:18.04
MAINTAINER oToToT

RUN mkdir /ytp
WORKDIR /ytp

# build elastic search
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.6.0-linux-x86_64.tar.gz\
	&& tar xf elasticsearch-7.6.0-linux-x86_64.tar.gz\
	&& elasticsearch-7.6.0/bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v6.3.0/elasticsearch-analysis-ik-6.3.0.zip

COPY songs.json /ytp/songs.json
COPY upload_data.py /ytp/upload_data.py
COPY run.sh /ytp/run.sh
CMD /ytp/run.sh
