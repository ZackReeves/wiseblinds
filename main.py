import time
from database import Database
from temp_sensor import Temp_Sensor

def convert_temp(sensor):
    return ((175.72*sensor) / 65536) - 46.85

def convert_rh(sensor):
    return ((125*sensor) / 65536) - 6

db = Database()
sensor = Temp_Sensor()

n=0
while n<10:

    sensor_data = sensor.measure()

    print(f'TEMPERATURE:    Degrees: {sensor_data[0]:.2f}')
    print(f'RH:    Percentage: {sensor_data[1]:.2f}')

    # path = "timeseries/{}.json".format(int(time.time()))
    # data = {"n":n, "tmp": temperature_degrees, "rh":rh_percent}

    # type = "post"
    # path = "postlist.json"
    # data = {"n":n, "time": time.ctime(time.time()),"tmp": temperature_degrees, "rh":rh_percent}

    # db.send(type, path, data)

    
    time.sleep(1)
    n += 1
