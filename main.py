import time
from database import Database
from sensors import Temp_Sensor, Light_Sensor

db = Database()
temp_sensor = Temp_Sensor()
light_sensor = Light_Sensor()


n=0
while n<10:

    light_sensor.measure()

    print(light_sensor.is_night)

    # sensor_data = temp_sensor.measure()

    # print(f'TEMPERATURE:    Degrees: {sensor_data[0]:.2f}')
    # print(f'RH:    Percentage: {sensor_data[1]:.2f}')


    # type = "put"
    # path = "nighttime/{}.json".format(time.ctime(time.time()))
    # data = {"n":n, "is_night": light_sensor.is_night}

    # # type = "post"
    # # path = "postlist.json"
    # # data = {"n":n, "time": time.ctime(time.time()),"tmp": sensor_data[0], "rh":sensor_data[1]}

    # path = "timeseries.json"
    # query = "?orderByChild=\"$time\"&startAt=\"{}\"&endAt=\"{}\"".format(int(time.time()-400), int(time.time())) # request between certain timeframe"

    # db.read(path, query)

    # db.write(type, path, data)

    
    time.sleep(1)
    n += 1
