import VL53L1X
import time
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open()


tof.start_ranging(3) 



x=0
while x!=10:
    distance_in_mm = tof.get_distance()
    print(distance_in_mm)
    x+=1
    time.sleep(5)
tof.stop_ranging()