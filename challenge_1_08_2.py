from codrone_edu.drone import * #引入CoDrone EDU的函式庫
from random import randint #引入random函式庫裡的randint
drone = Drone() #建立名為drone的CoDrone EDU物件
drone.pair() #把遙控器跟無人機配對
drone.takeoff() #讓無人機起飛並停在空中

yaw_array = [] #設定一個叫yaw_array的陣列紀錄旋轉的幅度
pitch_array = [] #設定一個叫pitch_array的陣列紀錄向前移動的幅度

for x in range(0, 3, 1): #在x等於0, 1, 2時分別跑一次裡面的程式
    yawRand = randint(-50,50) #yawRand會是-50到50之間隨機的數字
    pitchRand = randint(0,30) #pitchRand會是0到30之間隨機的數字
    yaw_array[x] = yawRand #把yawRand的值用陣列紀錄起來
    pitch_array[x] = pitchRand #把pitchRand的值用陣列紀錄起來

    drone.set_yaw(yaw_array[x]) #無人機旋轉的功率設為yawRand，因為yawRand可能是正/負數，所以會隨機逆/順時針旋轉
    drone.move(2) #旋轉2秒
    drone.set_yaw(0) #無人機旋轉的功率設為0
    drone.set_pitch(pitch_array[x]) #無人機向前移動的功率設為pitchRand
    drone.move(1) #向前移動1秒
    drone.set_pitch(0) #無人機向前移動的功率設為0

for y in range(2, -1, -1): #在y等於2, 1, 0時分別跑一次裡面的程式
    drone.set_pitch(-pitch_array[y]) #原本向前移動功率多少，現在向後移動功率多少
    drone.move(1) #向後移動1秒
    drone.set_pitch(0) #向後移動的功率設為0
    drone.set_yaw(-yaw_array[y]) #原本旋轉功率多少，現在反方向旋轉功率多少
    drone.move(2) #旋轉2秒
    drone.set_yaw(0) #無人機旋轉的功率設為0

drone.land() #讓無人機輕輕降落到地面
drone.close() #關閉無人機和遙控器的連線
