#要先算90度如何移動
#Pentagon
from codrone_edu.drone import *
drone = Drone()
drone.pair()
drone.takeoff()

for x in range(0, 5, 1):
    drone.set_pitch(15)
    drone.move(1)
    drone.set_pitch(0)
    drone.set_yaw(30)
    drone.move(2)
    drone.set_yaw(0)

drone.land()
drone.close()
