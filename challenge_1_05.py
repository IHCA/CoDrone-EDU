from codrone_edu.drone import *
drone = Drone()
drone.pair()
x = 20
y = 30
drone.takeoff()

drone.set_pitch(y)
drone.move(1)
drone.set_pitch(0)
drone.set_roll(x)
drone.move(1)
drone.set_roll(0)
drone.set_pitch(y)
drone.move(1)
drone.set_pitch(0)
drone.set_roll(-x)
drone.move(1)
drone.set_roll(0)
drone.set_pitch(y)
drone.move(1)
drone.set_pitch(0)
drone.set_roll(x)
drone.move(1)
drone.set_roll(0)
drone.set_pitch(y)
drone.move(1)

drone.land()
drone.close()
