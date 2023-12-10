from codrone_edu.drone import * #引入CoDrone EDU的函式庫

drone = Drone() #建立名為drone的CoDrone EDU物件

drone.pair() #把遙控器跟無人機配對

drone.takeoff() #讓無人機起飛並停在空中

drone.set_pitch(20)  #無人機向前方移動的功率設為20

drone.move(2)  #無人機移動2秒

drone.set_pitch(0)  #無人機向前方移動的功率設為0

drone.set_roll(20)  #無人機向右移動的功率設為20

drone.move(2)  #無人機移動2秒

drone.set_roll(0)  #無人機向右移動的功率設為0

drone.set_pitch(-20)  #無人機向後方移動的功率設為20

drone.move(2)  #無人機移動2秒

drone.set_pitch(0)  #無人機向後方移動的功率設為0

drone.set_roll(-20)  #無人機向左移動的功率設為20

drone.move(2)  #無人機移動2秒

drone.land() #讓無人機輕輕降落到地面

drone.close() #關閉無人機和遙控器的連線