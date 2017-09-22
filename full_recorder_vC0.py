import obd
from serial import SerialException
from time import sleep, strftime
from datetime import datetime
obd.logger.setLevel(obd.logging.DEBUG)
tries = 0
cnt = 0
commands = [obd.commands.RPM, obd.commands.SPEED, obd.commands.THROTTLE_POS, obd.commands.INTAKE_PRESSURE] #ENGINE_LOAD, TIMING_ADVANCE

while tries == 0:
	try:
		connection = obd.OBD('/dev/rfcomm1')
		initial_time = datetime.now()
		f = open('/home/pi/OBD_Logs/results_SYNC_'+initial_time.strftime('%Y-%m-%d %Hh%Mm%Ss')+'.csv', 'w')
		  
		while True:
			try:
				for cmd in commands:
					r = connection.query(cmd)
					cnt += 1
					
					if r == None:
						f.close()
						raster = 10000/(cnt)
						raise Exception
					
					else:
						dif = (datetime.now() - initial_time).total_seconds()
						f.write('\n'+str(dif)+','+str(r))
						
						if dif >= 120:
							f.close()
							raster = 10000/(cnt)
							raise Exception
			except:
				break

		print 'Raster = %d ms' %raster

	#Caso OBD nao esteja conectado sera apresentado um SerialException e deve, portanto, incrementar no numero de tentativas (tries). Outro erro apenas tente novamente
	except Exception as e:
		if type(e) == SerialException:
			tries += 1
			print 'SerialException -> closing recording!!!'