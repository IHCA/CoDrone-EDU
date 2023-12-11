from codrone_edu.drone import * #引入CoDrone EDU的函式庫
drone = Drone() #建立名為drone的CoDrone EDU物件
drone.pair() #把遙控器跟無人機配對
drone.takeoff() #讓無人機起飛並停在空中

drone.set_pitch(20) #無人機向前方移動的功率設為20
drone.set_throttle(30) #無人機向上移動的功率設為30
drone.move(1) #無人機移動1秒，因為pitch跟throttle都是正數所以會同時往前跟往上移動
drone.set_throttle(-40) #無人機向下移動的功率設為40，本來應該要是30才會顯示sin波，但因為飛行中的偏差讓往下飛的幅度看起來比較小，不像sin波，因此將數值稍微調大
drone.move(1) #無人機移動1秒，因為pitch為正，throttle為負，所以會同時往前跟往下移動
drone.set_throttle(30) #無人機向上移動的功率設為30
drone.move(1) #無人機移動1秒，因為pitch跟throttle都是正數所以會同時往前跟往上移動
drone.set_throttle(-40) #無人機向下移動的功率設為40，本來應該要是30才會顯示sin波，但因為飛行中的偏差讓往下飛的幅度看起來比較小，不像sin波，因此將數值稍微調大
drone.move(1) #無人機移動1秒，因為pitch為正，throttle為負，所以會同時往前跟往下移動
drone.set_throttle(30) #無人機向上移動的功率設為30
drone.move(1) #無人機移動1秒，因為pitch跟throttle都是正數所以會同時往前跟往上移動
drone.set_throttle(-40) #無人機向下移動的功率設為40，本來應該要是30才會顯示sin波，但因為飛行中的偏差讓往下飛的幅度看起來比較小，不像sin波，因此將數值稍微調大
drone.move(1) #無人機移動1秒，因為pitch為正，throttle為負，所以會同時往前跟往下移動

drone.land() #讓無人機輕輕降落到地面
drone.close() #關閉無人機和遙控器的連線
