import obd
import time
from datetime import datetime

cnt = 0

#Usar mesma função para callbacks e verificar unidade para colocar na posição correta do CSV

try:
    connection = obd.Async('/dev/rfcomm1')
    
    initial_time = datetime.now()
    f = open('/home/pi/OBD_Logs/results_'+str(initial_time)[:19]+'.csv', 'w')
    f.write('time,rpm,thr_percent,speed,int_pressure')
    
    def new_rpm(r):
        global cnt
        global f
        global now
                    
        current_time = datetime.now()
            
        dif = (current_time - initial_time).total_seconds()
        
        f.write('\n'+str(dif)+',')
        response = str(r.value)
        
        try:
            response = response.split(' ')[0]
            f.write(response)
            
        except:
            f.write('None')
        #print r.value
        cnt += 1
        
    def new_speed(r):
        global cnt
        global f
        
        f.write(',')
        response = str(r.value)
        
        try:
            response = response.split(' ')[0]
            f.write(response)
            
        except:
            f.write('None')
        #print r.value
        cnt += 1
        
    def new_thr(r):
        global cnt
        global f
        
        f.write(',')
        response = str(r.value)
        
        try:
            response = response.split(' ')[0]
            f.write(response)
            
        except:
            f.write('None')
        #print r.value
        cnt += 1
        
    def new_int(r):
        global cnt
        global f
        
        f.write(',')
        response = str(r.value)
        
        try:
            response = response.split(' ')[0]
            f.write(response)
            
        except:
            f.write('None')
        #print r.value
        cnt += 1
        
    def new_load(r):
        global cnt
        global f
        
        f.write(',')
        response = str(r.value)
        
        try:
            response = response.split(' ')[0]
            f.write(response)
            
        except:
            f.write('None')
        #print r.value
        cnt += 1
        
    def new_advance(r):
        global cnt
        global f
        
        f.write(',')
        response = str(r.value)
        
        try:
            response = response.split(' ')[0]
            f.write(response)
            
        except:
            f.write('None')
        
        cnt += 1
        

    connection.watch(obd.commands.RPM, callback=new_rpm)
    connection.watch(obd.commands.SPEED, callback=new_speed) ################## kph
    connection.watch(obd.commands.THROTTLE_POS, callback=new_thr) ############# Percent 
    connection.watch(obd.commands.INTAKE_PRESSURE, callback=new_int) ########## kPa
    #connection.watch(obd.commands.ENGINE_LOAD, callback=new_load) ############# Percent
    #connection.watch(obd.commands.TIMING_ADVANCE, callback=new_advance) ####### Degrees
    connection.start()

    time.sleep(5)
    connection.stop()
    #f.write('\nData size: '+str(cnt))
    f.close()

except:
    pass
