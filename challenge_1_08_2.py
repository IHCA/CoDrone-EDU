from codrone_edu.drone import *
from random import randint
drone = Drone()
drone.pair()
drone.takeoff() 

yaw_array = []
pitch_array = []

for x in range(0, 3, 1):
    yawRand = randint(-20,20)
    pitchRand = randint(-20,20)
    yaw_array[x] = yawRand
    pitch_array[x] = pitchRand

    drone.set_yaw(yawRand)
    drone.move(1)
    drone.set_yaw(0)
    drone.set_pitch(pitchRand)
    drone.move(1)
    drone.set_pitch(0)

for y in range(0, 3, 1):
    drone.set_pitch(-pitch_array[y])
    drone.move(1)
    drone.set_pitch(0)
    drone.set_yaw(-yaw_array[y])
    drone.move(1)
    drone.set_yaw(0)

drone.land()
drone.close()