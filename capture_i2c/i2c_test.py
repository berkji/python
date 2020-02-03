#
#I2C device event
import os
import sys
from array import array
import struct

import pickle


#==========================================================================
# HELPER FUNCTIONS
#==========================================================================
def array_u08 (n):  return array('B', [0]*n)
def array_u16 (n):  return array('H', [0]*n)
def array_u32 (n):  return array('I', [0]*n)
def array_u64 (n):  return array('K', [0]*n)
def array_s08 (n):  return array('b', [0]*n)
def array_s16 (n):  return array('h', [0]*n)
def array_s32 (n):  return array('i', [0]*n)
def array_s64 (n):  return array('L', [0]*n)


class i2c_event:
    i2c_addr = 0x0
    time_stamp = 0x0
    read_write_flag = 0x0
    event_data = 0x0
    error_code = 0x0
    def __init__(self,capline,input_time_stamp,input_error_code):
        self.i2c_addr = capline[0]
        self.time_stamp = input_time_stamp
        self.read_write_flag = capline[0]&0x8F
        self.event_data = capline[1:]
        self.error_code = input_error_code
    def __str__(self):
        i2c_info =  'i2c_addr=0x%x, time_stamp= %s, read_write=0x%x, error_code=0x%x, \ni2c_data= %s  \n\n\n' \
            % (self.i2c_addr,(self.time_stamp).tostring(),self.read_write_flag,self.error_code,self.event_data)
        return i2c_info


i2c_events = []

capline = array_u16(10)
thetimestamp = array_u32(2)
thetimestamp[0]=1
testevent = i2c_event(capline,thetimestamp,0)
i2c_events.append(testevent)

capline = array('B', [0x44]*11)
thetimestamp = array_u32(2)
thetimestamp[0]=2
testevent = i2c_event(capline,thetimestamp,0)
i2c_events.append(testevent)

capline = array('B', [0x23]*11)
thetimestamp = array_u32(2)
thetimestamp[0]=3
testevent = i2c_event(capline,thetimestamp,0)
i2c_events.append(testevent)



new_i2c_events=sorted(i2c_events, key=lambda i2c_event:i2c_event.i2c_addr)
for testevent in new_i2c_events:
    print(testevent)

print("Now test read/write\n")
fw = open("testi2c.dat",'wb')
pickle.dump(new_i2c_events,fw)
fw.close()

fr = open("testi2c.dat",'rb')
new_i2c_events=pickle.load(fr)
for testevent in new_i2c_events:
    print(testevent)
