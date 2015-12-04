# lightcontroller module
# for Build Madison 2015
# Davi Post, 2015-11-21


import colorsys

# from PySerial
import serial
import serial.tools.list_ports


def rgb_from_hsv(h, s, v):
    """ Return RGB tuple (0 to 255) from HSV values (0.0 to 1.0) """
    rgb = colorsys.hsv_to_rgb(h, s, v)
    return [int(x * 255) for x in rgb]


colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),             # off
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'yellow': (255, 180, 0),
    'orange': rgb_from_hsv(0.033, 1, 1),
}


def find_port():
    """ Find serial devices available;
        return string portname of first device found,
        or '' if none available.
    """
    ports = []
    for port in serial.tools.list_ports.comports():
        name, desc, id = map(str, port)     # some info may be None
        if 'usb' in name or 'COM' in name:
            ports.append(port)
    if len(ports) == 0:
        return ''
    port = ports[0]
    if len(ports) == 1:
        print('Using serial port %s (%s, %s)' % tuple(port))
    else:
        print('Multiple serial devices, using %s (%s, %s)' % tuple(port))
        portlist = ['            %s (%s, %s)' % tuple(p) for p in ports[1:]]
        print('  Others are:\n' + '\n'.join(portlist))
    return port[0]    # name


class Controller(object):
    """ Light controller: receives text commands, sends control commands to Arduino """
    
    def __init__(self):
        """ Create controller, open com port """
        self.portname = find_port()
        if self.portname:
            self.comport = serial.Serial(port=self.portname, baudrate=9600)
        else:
            print('No serial port found')
    
    
    def command(self, cmdtext, param):
        """ Receive command and parameter, send appropriate control command """
        reply = ''
        if cmdtext == 'turn_on':
            reply = self.sendRGB(colors['white'])
        elif cmdtext == 'turn_off':
            reply = self.sendRGB(colors['black'])
        elif cmdtext == 'change_color':
            values = colors.get(param)
            if values:
                reply = self.sendRGB(values)
        elif cmdtext == 'rainbow':
            revolutions = int(param) if param.isdigit() else 2
            for h in range(255 * revolutions):
                self.sendRGB(rgb_from_hsv(h / 255.0, 1, 1))
            reply = 'ran rainbow for %d revolutions' % revolutions
        elif cmdtext == 'blink':
            color = param if param in colors else 'red'
            values = colors[color]
            for i in range(200):
                if i % 33 < 17:
                    self.sendRGB(values)
                else:
                    self.sendRGB(colors['black'])
            reply = 'blinked ' + color
        return reply
    
    
    def send(self, color, value):
        """ Send color ('R', 'G', or 'B') and value (0..255) to serial port """
        bytestring = (color + str(value) + '\n').encode()
        self.comport.write(bytestring)
        reply = self.comport.readline()
        return reply
    
    
    def sendRGB(self, rgb):
        """ Send commands to set color to rgb (tuple or list of 3 values 0 to 255) """
        r, g, b = rgb
        reply = self.send('R', r)
        reply += self.send('G', g)
        reply += self.send('B', b)
        return reply
    
