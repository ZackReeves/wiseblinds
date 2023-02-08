from database import Database
from motor import Motor
import time

def read_mannual(db):
    path = "mannual.json"
    query = "?orderBy=\"$key\"&limitToLast={}".format(int(1))

    data = db.read(path, query)
    for i in data:
        val = data[i]["position"]
        return val
    
def read_nightime(db):
    filter_size = 5

    path = "nighttime.json"
    query = "?orderBy=\"$key\"&limitToLast={}".format(int(filter_size))

    data = db.read(path, query)
    val = 0

    for i in data:
        val += data[i]["is_night"]
    
    return round(val/filter_size)

def main():
    db = Database()
    curtains = Motor()
    
    nighttime = False
    mannual = 1

    n = 0
    while n<10:
        mannual = read_mannual(db)

        if 0 <= mannual <= 1:
            print("mannual")
            curtains.move(mannual)

        else:
            nighttime = read_nightime(db)
            if nighttime:
                print("auto close")
                curtains.move(0)
            else:
                print("auto open")
                curtains.move(1)

        time.sleep(1)
        n += 1

if __name__ == "__main__":
    main()