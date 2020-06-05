import numpy as np
import matplotlib.pyplot as plt

G = 1  # 6.674 * 10 ** (-11) todo


class body:
    def __init__(self, default_position, mass, default_vel=None):
        if default_vel is None:
            default_vel = [0.0 for i in default_position]
        self.velocity = np.array([default_vel])
        self.position = np.array([default_position])
        self.mass = mass

    def vel(self):
        return np.array(self.velocity[-1])

    def pos(self):
        return np.array(self.position[-1])


class TBP:
    def __init__(self, body1, body2, body3, dt=0.001):
        self.mass = np.array([body1.mass, body2.mass, body3.mass])
        self.dt = dt
        self.body1 = body1
        self.body2 = body2
        self.body3 = body3


    def calc_a(self):
        self.r = np.array([self.body1.pos() - self.body2.pos(),
                          self.body2.pos() - self.body3.pos(),
                          self.body3.pos() - self.body1.pos()])

        self.d = np.array(np.linalg.norm([self.r[0], self.r[1], self.r[2]], axis=1))

        self.abs_r = self.r / np.array([[self.d[i], self.d[i]] for i in range(3)])

        self.abs_F = -G*np.array([self.mass[0]*self.mass[1], self.mass[1]*self.mass[2], self.mass[2]*self.mass[0]])\
                 /self.d

        self.F_vec = np.array([[self.abs_F[i], self.abs_F[i]] for i in range(3)]) * self.abs_r
        self.F = self.F_vec - np.roll(self.F_vec, 2)
        self.a = self.F / np.array([[self.mass[i], self.mass[i]] for i in range(3)])

        return self.a

    def dx(self):
        self.calc_a()
        self.bodies = [self.body1, self.body2, self.body3]
        for i in self.bodies:
            i.position = np.append(i.position, np.array([i.pos() + i.vel() * self.dt]), axis=0)
            i.velocity = np.append(i.velocity, np.array([i.vel() + self.a[self.bodies.index(i)] * self.dt]), axis=0)

    def t_(self, t):
        repeat = int(t/self.dt)
        for i in range(repeat):
            self.dx()

    def show(self):
        fig, ax = plt.subplots()
        ax.plot(body1.position[:, 0], body1.position[:, 1], 'k-')
        ax.plot(body2.position[:, 0], body2.position[:, 1], 'k-')
        ax.plot(body3.position[:, 0], body3.position[:, 1], 'k-')
        fig.savefig("/Users/fujimotogen/Desktop/outuput/fig.png")
        fig.show()


def calc_TBP(arg):
    arg = arg.reshape()
    body1 = body(default_positions[0], mass[0], default_velocities[0])
    body2 = body(default_positions[1], mass[1], default_velocities[1])
    body3 = body(default_positions[2], mass[2], default_velocities[2])
    TBP_Prime = TBP(body1, body2, body3)
    TBP_Prime.t_(t)
    TBP_Prime.show()
    return [[body1.pos(), body2.pos(), body3.pos()], [body1.vel(), body2.vel(), body3.vel()]]

def random_default():
    return [[(np.random.random(size=(3, 2))-0.5)*4],
            [(np.random.random(size=(3, 2))-0.5)*4],
            [(np.random.random(size=(3))-0.5)*4],
            np.random.random()*3]

if "__main__" == __name__:
    body1 = body([0, 0], 6)
    body2 = body([2, 0], 2)
    body3 = body([0, 1], 2)
    TBP1 = TBP(body1=body1, body2=body2, body3=body3)


    print(random_default())
    print(calc_TBP(random_default()[0][0], random_default()[1][0], random_default()[2][0], random_default()[3]))

