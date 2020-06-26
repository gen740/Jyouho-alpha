import numpy as np
import matplotlib.pyplot as plt

G = 1  # 6.674 * 10 ** (-11) todo



"""
    オブジェクトの定義、返り値は物体の位置、速度のリスト
"""
class body:
    def __init__(self, default_position, default_vel, mass):
        self.velocity = np.array([default_vel])
        self.position = np.array([default_position])
        self.mass = mass

    def vel(self):
        return np.array(self.velocity[-1])

    def pos(self):
        return np.array(self.position[-1])


"""
    定義したオブジェクトクラスを用い三体問題を計算する。dtは積分間隔
"""
class TBP:
    def __init__(self, body1, body2, body3, dt=0.0001):
        self.mass = np.array([body1.mass, body2.mass, body3.mass])
        self.dt = dt
        self.body1 = body1
        self.body2 = body2
        self.body3 = body3

    def calc_a(self):
        # 物体間の距離ベクトル shape(3, 2)
        self.r = np.array([self.body1.pos() - self.body2.pos(),
                           self.body2.pos() - self.body3.pos(),
                           self.body3.pos() - self.body1.pos()])
        
        # 物体間の距離shape(3,)
        self.abs_r = np.array(np.linalg.norm([self.r[0],
                                          self.r[1],
                                          self.r[2]], axis=1))
        

        self.F_vec = -G * np.tile((np.array([self.mass[0] * self.mass[1],
                           self.mass[1] * self.mass[2],
                           self.mass[2] * self.mass[0]]) / 
                           self.abs_r ** 2).reshape(3,1),2) * self.r 
                                        

        self.F = self.F_vec - np.roll(self.F_vec, -2)
        self.a = self.F / np.array([[self.mass[i],
                                     self.mass[i]] for i in range(3)])

        return self.a

    def dx(self):
        self.calc_a()
        self.bodies = [self.body1, self.body2, self.body3]
        for i in self.bodies:
            i.position = np.append(i.position,
                                   np.array([i.pos() + i.vel() * self.dt]),
                                   axis=0)

            i.velocity = np.append(i.velocity,
                np.array([i.vel() + self.a[self.bodies.index(i)] * self.dt]),
                axis=0)

    def t_(self, t):
        t = t * 10
        repeat = int(t / self.dt)
        for i in range(repeat):
            self.dx()

    def show(self, to_file):
        self.fig, self.ax = plt.subplots()

        #self.ax.set_ylim(-1, 1)
        #self.ax.set_xlim(-1, 1)
        print(self.body1.position)
        print(self.body2.position)
        print(self.body3.position)
        self.ax.plot(self.body1.position[:, 0], self.body1.position[:, 1], 'k-')
        self.ax.plot(self.body2.position[:, 0], self.body2.position[:, 1], 'k-')
        self.ax.plot(self.body3.position[:, 0], self.body3.position[:, 1], 'k-')
        self.fig.savefig(to_file)
        self.fig.show()


counter = 0


def calc_TBP(arg, to_file):
    global counter
    counter = counter + 1
    # print(arg[12])
    body1 = body(arg[0:2], arg[2:4], arg[4])
    body2 = body(arg[5:7], arg[7:9], arg[9])
    body3 = body(arg[10:12], arg[12:14], arg[14])
    TBP_Prime = TBP(body1, body2, body3)
    TBP_Prime.t_(arg[15])
    TBP_Prime.show(to_file)
    print(counter)
    return np.array([[body1.pos(), 
                      body2.pos(),
                      body3.pos()],
                     [body1.vel(),
                      body2.vel(),
                      body3.vel()]]).flatten()

def random_default():
    rand_mass = [np.random.rand()/2 + 0.5 for i in range(3)]
    rand_position1 = np.random.rand(2)*2 - 1.
    rand_position2 = np.random.rand(2)*2 - 1.
    rand_position3 = np.random.rand(2)*2 - 1. 
    rand_velocity1 = np.random.rand(2)*2 - 1.
    rand_velocity2 = np.random.rand(2)*2 - 1.
    rand_velocity3 = np.random.rand(2)*2 - 1. 

    return np.array([rand_position1[0], rand_position1[1],
                     rand_velocity1[0], rand_velocity1[1], rand_mass[0],
                     rand_position2[0], rand_position2[1],
                     rand_velocity2[0], rand_velocity2[1], rand_mass[1],
                     rand_position3[0], rand_position3[1],
                     rand_velocity3[0], rand_velocity3[1], 0, 1])

if "__main__" == __name__:
    for i in range(1):
        print(random_default())
        print(calc_TBP(random_default(),
            f"/Users/fujimotogen/Desktop/outuput/fig{i+1}.png"))
