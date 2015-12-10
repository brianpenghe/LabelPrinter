# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>
import sys
import string

if len(sys.argv) < 6:
    print 'usage: python %s v6.5 3 v6.5mES p:15 Ram2014-05-28 ' % sys.argv[0]
    sys.exit(1)

# <codecell>
#########Brian Peng He###########
namePlease = ""+ sys.argv[3] + "\\&(" + sys.argv[4] + ")\\&" + sys.argv[5]
idPlease = sys.argv[1]
RepeatTimes = int(sys.argv[2])
if RepeatTimes < 1:
    print 'RepeatTimes must be a positive integer'
    sys.exit(1)

import time
#namePlease = "v6.5mES\\&(p:15)\\&Ram2014-05-28"
#idPlease = 'v6.5'
#RepeatTimes = 8
#########Brian Peng He###########




import socket

# <codecell>

PRINTER1_HOST='131.215.34.116'
PRINTER1_PORT=9100

# <codecell>

def print_zpl_socket(zpl_text,
                     host=PRINTER1_HOST,
                     port=PRINTER1_PORT):
    """
    Sends zpl_text to printer via a socket

    if zpl_text is a list of zpl_texts, it will print each one
    in that list.
    """


    # Process anyway if zpl_text is a list.
    if type(zpl_text) is list:
        zpl_text = '\n'.join(zpl_text)

    s = socket.socket()
    # PORT 9100 is default for Zebra tabletop/desktop printers
    # PORT 6101 is default for Zebra mobile printers
    s.connect((host, port))
    s.sendall(zpl_text)
    s.close()


# <codecell>

template = """^XA

^FX ---SIDE LABEL---
^LH 190,40
^CF 0,30

^FX------Sideways ID------
^FO 0,25
^TB R,100,40
^FD{id}^FS
^FX------Sideways Line------
^FO 50,0
^GB 5,200,5^FS

^FX-------Name----------
^FO 65,20
^FB 325,4
^FD{name}^FS

^FX ---TOP LABEL---
^LH 15,23
^CF 0,30

^FX----ID #----
^FO 5,25
^FB 145,1,,C
^FD{id}^FS

^FX----Name----
^CF 0,16
^FO 13,47
^TB N,130,30
^FD{name}1^FS

^FX--------Barcode--------
^FO 50,80
^BXN ,3,200
^FDl|0000000{id}|woldlab^FS

^FX-----Border-------
^FO 0,0
^GC 150,10
^FX ---End---
^XZ
"""

# <codecell>
for i in range(RepeatTimes):
    if(RepeatTimes > 10):
        print "Don't be too greedy!"
        sys.exit(1)
    print_zpl_socket(template.format(name=namePlease, id=idPlease))
    time.sleep(1)

# <codecell>
