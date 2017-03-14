FROM resin/raspberrypi3-alpine

WORKDIR /usr/src/app
ENV INITSYSTEM on

CMD while true; do echo "Idling..."; sleep 15; done
