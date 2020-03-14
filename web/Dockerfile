FROM ubuntu:18.04
MAINTAINER oToToT

RUN git clone https://github.com/oToToT/YTPoop /YTPoop

WORKDIR /YTPoop

RUN npm install

COPY songs.json /YTPoop/models/songs.json

CMD ["npm", "start"]
