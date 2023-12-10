from codrone_edu.drone import * #引入CoDrone EDU的函式庫
from random import randint #引入random函式庫裡的randint
drone = Drone() #建立名為drone的CoDrone EDU物件
drone.pair() #把遙控器跟無人機配對
drone.takeoff() #讓無人機起飛並停在空中

drone.set_throttle(50) #往前移動duration秒，也就是1秒
drone.move(2) #往上移動2秒
drone.hover(1) #在空中停留1秒

for x in range(0, 3, 1): #重複執行3次
    powerRand = randint(10,30) #powerRand會是10到30之間隨機的數字
    timeRand = randint(1,3) #timeRand會是1到3之間隨機的數字
    drone.set_throttle(-powerRand) #無人機向下移動的功率設為powerRand
    drone.move(timeRand) #無人機向下移動的時間設為timeRand
    drone.hover(1) #在空中停留1秒
    drone.set_throttle(powerRand) #無人機向上移動的功率設為powerRand
    drone.move(timeRand) #無人機向上移動的時間設為timeRand
    drone.hover(1) #在空中停留1秒
  
drone.land() #讓無人機輕輕降落到地面
drone.close() #關閉無人機和遙控器的連線
