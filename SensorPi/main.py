import time
from database import Database
from sensors import Temp_Sensor, Light_Sensor

def send_nighttime(light_sensor, db):
    type = "put"
    path = "nighttime/{}.json".format(int(time.time()))
    data = {"is_night": light_sensor.is_night}

    db.write(type, path, data)

def send_temp_rh(sensor_data, db):
    type = "put"
    path = "temp_rh/{}.json".format(int(time.time()))
    data = {"temp": sensor_data[0], "rh":sensor_data[1]}

    db.write(type, path, data)

def main():
    db = Database()
    temp_sensor = Temp_Sensor()
    light_sensor = Light_Sensor()

    while True:

        light_sensor.measure()
        sensor_data = temp_sensor.measure()

        send_nighttime(light_sensor, db)
        send_temp_rh(sensor_data, db)

        print(light_sensor.is_night)
        print(f'TEMPERATURE:    Degrees: {sensor_data[0]:.2f}')
        print(f'RH:    Percentage: {sensor_data[1]:.2f}')

        time.sleep(1)

if __name__ == "__main__":
    main()