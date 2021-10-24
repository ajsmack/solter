
import Adafruit_ADS1x15
import MySQLdb
import time
import datetime
import pymssql

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

time_sensor = time.time()
# Main loop.
sensor1 = [0]*4
sensor2 = [0]*4
sensor3 = [0]*4
sensor4 = [4]*4


for i in range(4):
    sensor1[i] = adc.start_adc(i, gain=GAIN)
    sensor2[i] = adc.start_adc(i, gain=GAIN)
    sensor3[i] = adc.start_adc(i, gain=GAIN)
    sensor4[i] = adc.start_adc(i, gain=GAIN)

connobj = pymssql.connect(server='192.168.0.240', user='vijay', password='vijay', database='tempdb', port='1433',autocommit=True)
cursor = connobj.cursor()
cursor.execute('SELECT * FROM temp_table')




while True:
        
        print("voltage")
        #curs=db.cursor()
        cursor.execute("""INSERT INTO temp_table(data1, data2, data3, data4) 
        values(%s,%s,%s,%s)""",(sensor1[i],sensor2[i],sensor3[i],sensor4[i]))
	connobj.commit()
        print(sensor1[i])
        print(sensor2[i])
        print(sensor3[i])
        print(sensor4[i])
	cursor.execute('SELECT * FROM temp_table')
	for row in cursor:
        print('row = %r' % (row,))
	time.sleep(20)
	
connobj.close()











