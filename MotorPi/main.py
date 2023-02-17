from database import Database
from motor import Motor
from gpiozero import DigitalInputDevice
import time

ID = 0

def read_mannual(db):
    path = "mannual.json"
    query = "?orderBy=\"ID\"&equalTo={}&limitToLast={}".format(int(ID), int(1))

    data = db.read(path, query)
    for i in data:
        val = data[i]["position"]
        return val
    
def send_mannual(db, pos):

    type = "put"
    path = "mannual.json"
    data = {"position": pos}

    db.write(type, path, data)
    
def read_nightime(db):
    filter_size = 5

    path = "nighttime.json"
    query = "?orderBy=\"$key\"&limitToLast={}".format(int(filter_size))

    data = db.read(path, query)
    val = 0

    for i in data:
        val += data[i]["is_night"]
    
    return round(val/filter_size)

def read_voice(db):
    path = "voice.json"
    query = "?orderBy=\"ID\"&equalTo={}&limitToLast={}".format(int(ID), int(1))

    data = db.read(path, query)
    for i in data:
        val = data[i]["disabled"]
        return val

def main():
    db = Database()
    curtains = Motor()

    clapper = DigitalInputDevice(27, pull_up=False, active_state=None, bounce_time=0.5)

    nighttime = False
    mannual = 1

    while True:
        mannual = read_mannual(db)
        voice_disabled = read_voice(db)

        if not voice_disabled and clapper.value == 1:
            print("clap heard")
            if curtains.current_state <= 0.5:
                new_position = 1
            elif curtains.current_state > 0.5:
                new_position = 0    

            curtains.move(new_position)
            send_mannual(db, new_position)

        else:
            if 0 <= mannual <= 1:
                if curtains.current_state != mannual:
                    print("mannual")
                    curtains.move(mannual)
            else:
                nighttime = read_nightime(db)
                if nighttime:
                    if curtains.current_state != 0:
                        print("auto close")
                        curtains.move(0)
                else:
                    if curtains.current_state != 1:
                        print("auto open")
                        curtains.move(1)

        time.sleep(1)

if __name__ == "__main__":
    main()