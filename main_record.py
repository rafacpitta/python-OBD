import obd
import time

c = 0

def new(r):
	global c
	print r.value
	c += 1

def rpm(_hex):
    v = unhex(_hex) # helper function to convert hex to int
    v = v / 4.0
    return (v, obd.Unit.RPM)

def speed(_hex):
    v = unhex(_hex)
    return (v, obd.Unit.KPH)

commFastRPM = OBDCommand("RPM", "Engine RPM", "01", "0C1", 2, rpm)
commFastSpeed = OBDCommand("SPEED", "Speed", "01", "0D1", 1, speed)

connection = obd.Async('/dev/rfcomm1')
connection.watch(commFastSpeed, force=True, callback=new)
connection.watch(commFastRPM, force=True, callback=new)

#connection.watch(obd.commands.RPM, callback=new)
#connection.watch(obd.commands.SPEED, callback=new)

connection.start()

time.sleep(10)
print "Iterations: " + str(c/2)
connection.stop()

#	r = self.__send(b"AT CRA 7E8")
#        if not self.__isok(r):
#            self.__error("AT CRA 7E8 did not return 'OK'")
#            return
