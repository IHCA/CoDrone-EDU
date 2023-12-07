from codrone_edu.drone import *
drone = Drone()
drone.pair()
drone.takeoff()

drone.set_pitch(20)
drone.set_throttle(20)
drone.move(1)
drone.set_throttle(-20)
drone.move(1)

drone.land()
drone.close()