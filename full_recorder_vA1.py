import obd
import time
from serial import SerialException
from time import sleep
from datetime import datetime

#Usar mesma função para callbacks e verificar unidade para colocar na posição correta do CSV
tries = 0

while tries<=3:
	try:
		connection = obd.Async('/dev/rfcomm1')
			
		initial_time = datetime.now()
		f = open('/home/pi/OBD_Logs/results_'+str(initial_time)[:19]+'.csv', 'w')
		f.write('time,rpm,thr_percent,speed,int_pressure')
		 
		def new_rpm(r):
			global cnt
			global f
			
			cnt += 1            
			current_time = datetime.now()
				
			dif = (current_time - initial_time).total_seconds()
			
			f.write('\n'+str(dif)+',')
				
			#Try-Except aqui serve para caso não se consiga ler a variável, ex.: OBD conectado e carro desligado
			try:
				response = str(r.value)
				response = response.split(' ')[0]
				f.write(response)
					
			except:
				cnt = 0
				
		def new_speed(r):
			global cnt
			global f
				
			cnt += 1
			f.write(',')
				
			try:
				response = str(r.value)
				response = response.split(' ')[0]
				f.write(response)
					
			except:
				cnt = 0
				
		def new_thr(r):
			global cnt
			global f
				
			cnt += 1
			f.write(',')
				
			try:
				response = str(r.value)
				response = response.split(' ')[0]
				f.write(response)
					
			except:
				cnt = 0
				
		def new_int(r):
			global cnt
			global f
				
			cnt += 1
			f.write(',')
				
			try:
				response = str(r.value)
				response = response.split(' ')[0]
				f.write(response)
					
			except:
				cnt = 0
				
		def new_load(r):
			global cnt
			global f
				
			cnt += 1
			f.write(',')
				
			try:
				response = str(r.value)
				response = response.split(' ')[0]
				f.write(response)
					
			except:
				cnt = 0
				
		def new_advance(r):
			global cnt
			global f
				
			cnt += 1
			f.write(',')
				
			try:
				response = str(r.value)
				response = response.split(' ')[0]
				f.write(response)
					
			except:
				cnt = 0
		  
		connection.watch(obd.commands.RPM, callback=new_rpm) ####################### rpm
		connection.watch(obd.commands.SPEED, callback=new_speed) ################### kph
		connection.watch(obd.commands.THROTTLE_POS, callback=new_thr) ############## Percent 
		connection.watch(obd.commands.INTAKE_PRESSURE, callback=new_int) ########### kPa
		#connection.watch(obd.commands.ENGINE_LOAD, callback=new_load) ############# Percent
		#connection.watch(obd.commands.TIMING_ADVANCE, callback=new_advance) ####### Degrees
		connection.start()
			
		#Caso não se consiga ler variável feche o log e reinicialize a conexão para verificar comportamento novamente
		while True:
			if cnt == 0:
				connection.stop()
				f.close()
				sleep(5)
				break
				
		tries = 0
		
	#Caso OBD não esteja conectado será apresentado um SerialException e deve, portanto, incrementar no número de tentativas (tries). Outro erro apenas tente novamente
	except Exception as e:
		if type(e) == SerialException:
			tries += 1
		sleep(5)