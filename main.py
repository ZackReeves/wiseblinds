import time
import smbus2
from database import Database

def convert_temp(sensor):
    return ((175.72*sensor) / 65536) - 46.85

def convert_rh(sensor):
    return ((125*sensor) / 65536) - 6

db = Database()

si7021_ADD = 0x40
si7021_READ_TEMPERATURE = 0xE3
si7021_READ_RH = 0xE5

bus = smbus2.SMBus(1)

#Set up a write transaction that sends the command to measure temperature
cmd_measure_temp_rh = smbus2.i2c_msg.write(si7021_ADD,[si7021_READ_TEMPERATURE, si7021_READ_RH])

#Set up a read transaction that reads two bytes of data
read_result = smbus2.i2c_msg.read(si7021_ADD,4)

n=0
while n<10:

    #Execute the two transactions with a small delay between them
    bus.i2c_rdwr(cmd_measure_temp_rh)
    time.sleep(0.1)
    bus.i2c_rdwr(read_result)

    temperature_sensor = int.from_bytes(read_result.buf[0]+read_result.buf[1],'big')
    rh_sensor = int.from_bytes(read_result.buf[2]+read_result.buf[3],'big')

    temperature_degrees = convert_temp(temperature_sensor)
    rh_percent = convert_rh(rh_sensor)

    print(f'TEMPERATURE:    Sensor: {temperature_sensor} Degrees: {temperature_degrees:.2f}')
    print(f'RH:    Sensor: {rh_sensor} Percentage: {rh_percent:.2f}')

    # path = "timeseries/{}.json".format(int(time.time()))
    # data = {"n":n, "tmp": temperature_degrees, "rh":rh_percent}

    type = "post"
    path = "postlist.json"
    data = {"n":n, "time": time.ctime(time.time()),"tmp": temperature_degrees, "rh":rh_percent}

    db.send(type, path, data)

    
    time.sleep(1)
    n += 1
