from codrone_edu.drone import *
drone = Drone()
drone.pair()
drone.takeoff()

print("Menu: ")
print(
    "2. Circle \n"
    "3. Triangle \n"
    "4. Square \n"
    "5. Pentagon \n"
    "6. Hexagon \n"
    )

option = input("Select an option: ")

if option == "2":
    drone.set_yaw(-20)
    #drone.set_pitch(20)
    drone.move(2)

elif option == "3":
#120度
    for x in range(0, 3, 1):
        drone.set_pitch(20)   
        drone.move(2) 
        drone.set_pitch(0)    
        #drone.set_yaw(-50)   
        drone.move(2)
        drone.set_yaw(0)  

elif option == "4":
#90度
    for x in range(0, 4, 1):
        drone.set_pitch(20)   
        drone.move(2) 
        drone.set_pitch(0)    
        #drone.set_yaw(-50)   
        drone.move(2)
        drone.set_yaw(0)  

elif option == "5":
#72
    for x in range(0, 5, 1):
        drone.set_pitch(20)   
        drone.move(2) 
        drone.set_pitch(0)    
        #drone.set_yaw(-50)   
        drone.move(2)
        drone.set_yaw(0)  

elif option == "6":
#60
    for x in range(0, 6, 1):
        drone.set_pitch(20)   
        drone.move(2) 
        drone.set_pitch(0)    
        #drone.set_yaw(-50)   
        drone.move(2)
        drone.set_yaw(0)  


drone.land()
drone.close()