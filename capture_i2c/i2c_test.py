#
#I2C device event
import array
import pickle

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
        i2c_info =  'i2c_addr=0x%x, time_stamp=0x%x, read_write=0x%x, error_code=0x%x, \ni2c_data= %s' \
            % (self.i2c_addr,self.time_stamp,self.read_write_flag,self.error_code,self.event_data)
        return i2c_info

i2c_events =[]

thetimestamp = 0

capline = array.array('B', [0x55]*10)
testevent = i2c_event(capline,thetimestamp,0)
i2c_events.append(testevent)
thetimestamp +=1

capline = array.array('B', [0x44]*11)
testevent = i2c_event(capline,thetimestamp,0)
i2c_events.append(testevent)
thetimestamp +=1

capline = array.array('B', [0x66]*10)
testevent = i2c_event(capline,thetimestamp,0)
i2c_events.append(testevent)
thetimestamp +=1

capline = array.array('B', [0x33]*16)
testevent = i2c_event(capline,thetimestamp,0)
i2c_events.append(testevent)

new_i2c_events=sorted(i2c_events, key=lambda i2c_event:i2c_event.i2c_addr)

capline = array.array('B', [0x12]*15)
testevent = i2c_event(capline,thetimestamp,0)
i2c_events.append(testevent)
thetimestamp +=1

capline = array.array('B', [0x34]*10)
testevent = i2c_event(capline,thetimestamp,0)
i2c_events.append(testevent)
thetimestamp +=1

capline = array.array('B', [0x67]*10)
testevent = i2c_event(capline,thetimestamp,0)
i2c_events.append(testevent)
thetimestamp +=1

capline = array.array('B', [0x88]*10)
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
