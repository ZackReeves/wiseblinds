import time
from database import Database
from temp_sensor import Temp_Sensor

db = Database()
sensor = Temp_Sensor()

n=0
while n<10:

    sensor_data = sensor.measure()

    print(f'TEMPERATURE:    Degrees: {sensor_data[0]:.2f}')
    print(f'RH:    Percentage: {sensor_data[1]:.2f}')


    type = "put"
    path = "timeseries/{}.json".format(time.ctime(time.time()))
    data = {"n":n, "tmp": sensor_data[0], "rh":sensor_data[1]}

    # type = "post"
    # path = "postlist.json"
    # data = {"n":n, "time": time.ctime(time.time()),"tmp": sensor_data[0], "rh":sensor_data[1]}

    db.write(type, path, data)

    
    time.sleep(1)
    n += 1
