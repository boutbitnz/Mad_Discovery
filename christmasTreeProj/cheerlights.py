# CheerLights interface for lightcontroller
# Reads Cheerlights hex color from thingspeak, sends to lightcontroller 
# see http://cheerlights.com/cheerlights-api/
# Davi Post, 2015-11


#I've implemented a CheerLights interface. This polls a server every 10 seconds, changes the lights to the last color anyone has tweeted @cheerlights. Revised lightcontroller.py to handle hex color string.

#Tested (on Python 2.7), but not with Arduino yet.



import time

import urllib.request as urllibrary     # Python 3
# import urllib2 as urllibrary           # Python 2

import lightcontroller


POLLING_INTERVAL = 10       # seconds between requests to CheerLights server

url = 'http://api.thingspeak.com/channels/1417/field/2/last.txt'


def run(interval):
    """ Poll server at interval seconds, change lights color to hex value received """
    controller = lightcontroller.Controller()
    while True:
        stream = urllibrary.urlopen(url)
        hexcolor = stream.read()
        stream.close()

        controller.sendhexcolor(hexcolor)
        time.sleep(interval)


if __name__ == '__main__':
    run(POLLING_INTERVAL)

