import numpy as np

class Mass_spring_damper:
    def __init__(self):
        self.m = 5
        self.k = 3
        self.b = .5
        self.Ts = .01

    def get_xdot(self,x_k,u_k):
        f = u_k
        z = x_k[0,0]
        zdot = x_k[1,0]
        zddot = (f-self.b*zdot-self.k*z)/self.m
        return np.array([[zdot],[zddot]])
    
    def get_next_xk(self,x,u):
        F1 = self.get_xdot(x, u)
        F2 = self.get_xdot(x + self.Ts/2*F1, u)
        F3 = self.get_xdot(x + self.Ts/2*F2, u)
        F4 = self.get_xdot(x + self.Ts*F3, u)
        next_xk = x + self.Ts/6 * (F1 + 2*F2 + 2*F3 + F4)
        return next_xk
    
    
# sys = Mass_spring_damper()
# for i in range(100):
#     x_k = sys.get_next_xk(np.array([[0],[0]]),1)