import smbus2
import time

class Temp_Sensor:
    def __init__(self):
        self.si7021_ADD = 0x40
        self.si7021_READ_TEMPERATURE = 0xE3
        self.si7021_READ_RH = 0xE5
        self.bus = smbus2.SMBus(1)

        self.cmd_measure_tmp = smbus2.i2c_msg.write(self.si7021_ADD,[self.si7021_READ_TEMPERATURE])
        self.cmd_measure_rh = smbus2.i2c_msg.write(self.si7021_ADD,[self.si7021_READ_RH])

        self.tmp_result = smbus2.i2c_msg.read(self.si7021_ADD,2)
        self.rh_result = smbus2.i2c_msg.read(self.si7021_ADD,2)

    def convert_temp(self, sensor):
        return ((175.72*sensor) / 65536) - 46.85

    def convert_rh(self, sensor):
        conv = ((125*sensor) / 65536) - 6
        return max(0, min(100, conv))

    def read_temp(self):
        self.bus.i2c_rdwr(self.cmd_measure_tmp)
        time.sleep(0.1)
        self.bus.i2c_rdwr(self.tmp_result)
    
    def read_rh(self):
        self.bus.i2c_rdwr(self.cmd_measure_rh)
        time.sleep(0.1)
        self.bus.i2c_rdwr(self.rh_result)
    
    def measure(self, both="both"):
        if both != "tmp":
            self.read_rh()
        if both != "rh":
            self.read_temp()
        
        temperature_sensor = int.from_bytes(self.tmp_result.buf[0]+self.tmp_result.buf[1],'big')
        rh_sensor = int.from_bytes(self.rh_result.buf[0]+self.rh_result.buf[1],'big')

        temperature_degrees =  self.convert_temp(temperature_sensor)
        rh_percent = self.convert_rh(rh_sensor)

        return temperature_degrees, rh_percent
            
