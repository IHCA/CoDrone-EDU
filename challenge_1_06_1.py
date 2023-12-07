from codrone_edu.drone import *
drone = Drone()
drone.pair()
power = 20
duration = 1
drone.takeoff()

drone.set_pitch(power)
drone.move(duration)
drone.set_pitch(0)
power = power / 2
drone.set_roll(power)
drone.move(duration)
drone.set_roll(0)
power = power + 10
drone.set_pitch(-power)
drone.move(duration)
drone.set_pitch(0)
power = 30 - power
drone.set_roll(-power)
drone.move(duration)

drone.land()
drone.close()