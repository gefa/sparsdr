#!/usr/bin/env python3

from subprocess import *
import time, os
#subp1 = Popen(['/home/gnuradio/sparsdr/gr-sparsdr/sparsdr_pluto_900mhz_4band.py'])
#subp1 = Popen(['/home/gnuradio/sparsdr/gr-sparsdr/sparsdr_freq_900mhz_4band.py'])
#subp1.wait()
# time.sleep(3)
#subp2 = Popen(['/home/gnuradio/Zwave_908m4_40kbps_static3.py'])
# time.sleep(9)

# "tcp://127.0.0.1:55000"
import zmq
import numpy as np
#import mathpltlib.pyplot as plt
context =zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:55555")
socket.setsockopt(zmq.SUBSCRIBE, b'')

#subp3 = Popen(['/home/gnuradio/textgrc3.py'])
#time.sleep(6)

t_end = time.time() + 6 #60 * 15
while time.time() < t_end:
	if socket.poll(10) != 0:
	  msg=socket.recv()
	  print(len(msg))
	  data = np.frombuffer(msg, dtype=np.complex64, count=-1)
	  print(data[0:10])

#os.system("kill -9 {}".format(subp1.pid))
#os.system("kill -9 {}".format(subp2.pid))
#os.system("kill -9 {}".format(subp3.pid))
