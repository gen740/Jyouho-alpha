import numpy as np
import matplotlib.pyplot as plt

G = 6.674 * 10 ** (-11)



class body:
    def __init__(self, default_position, mass, default_vel=None):
        if default_vel is None:
            default_vel = [0.0 for i in default_position]
        self.vel = [default_vel]
        self.position = [default_position]
        self.mass = mass

    def vel(self):
        return self.vel[-1]

    def position(self):
        return self.position[-1]


class TBP:
    def __init__(self, body1, body2, body3, dt=0.001):
        self.dt = dt
        self.body1 = body1
        self.body2 = body2
        self.body3 = body3


    def calculate_F(self):
        self.r1 = self.body1[-1] - self.body2[-1]
        self.r2 = self.body2[-1] - self.body3[-1]
        self.r3 = self.body3[-1] - self.body1[-1]

        self.d1 = abs(np.linalg.norm(self.r1))
        self.d2 = abs(np.linalg.norm(self.r2))
        self.d3 = abs(np.linalg.norm(self.r3))

        self.F =


if "__main__" == __name__:
    body1 = body([3, 3])
    print(body1.vel)
    print(np.linalg.norm([3, 4]))
