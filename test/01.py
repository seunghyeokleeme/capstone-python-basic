import numpy as np
import matplotlib.pyplot as plt

N_A = 5 * 1e18
N_D = 4 * 1e16
A = 5e-6 # 접합의 단면적
e_0 = 8.854 * 1e-14 #자유 공간의 유전상수
e_s = 11.7 # 실리콘의 유전상수
q = 1.6 * 1e-19


def C_dep(V_r,V_bi): # C_dep
    C = A * np.sqrt((e_s * e_0 * q * N_A * N_D) / (2 * (V_bi - V_r) * (N_A + N_D)))
    return C

def C2(V_r,V_bi): # 1/C^2
    C2 = (-2)/(A*A*(q * e_0 * e_s)) * ( 1 / N_A + 1 / N_D) * ( V_r - V_bi)
    return C2

def slope(x1,x2,y1,y2): # 기울기
    slope = (y1-y2)/(x1-x2) # Y증가량 / X증가량
    return slope

def Vbi():
    N_A = 5 * 1e18
    N_D = 4 * 1e16
    V_bi = 0.0259 * np.log(N_A * N_D/(1.5 * 1e10)**2)
    return V_bi

V_r1 = [ -1 , -3 , -5 ] # reverse bias
V_bi = Vbi()

C_1V = C_dep(V_r1[0],V_bi)
C_3V = C_dep(V_r1[1],V_bi)
C_5V = C_dep(V_r1[2],V_bi)


print("V_bi =",V_bi)

V_r = np.arange(-7,7.1,0.1) # -7 V ~ 7 V , 0.1 V sweep
C = C_dep(V_r,V_bi)
C_2 = C2(V_r,V_bi)

fitting_V = np.arange(-7,V_bi+0.1,0.1) # -10 V ~ V_bi V , 0.1 V sweep

slope_C2 = slope(V_r[0],V_r[-1],C_2[0],C_2[-1])
print("slope = " , slope_C2)
y = 1/C**2 # 1/C^2
y_V = slope_C2 * (fitting_V - V_bi)

plt.subplot(211)
plt.plot(V_r1[0],C_1V,"o")
plt.plot(V_r1[1],C_3V,"o")
plt.plot(V_r1[2],C_5V,"o")
plt.plot(V_r,C)
plt.axvline(x=0, color = 'k') # x축
plt.axhline(y=0, color = 'k') # y축
plt.xlabel(" V ")
plt.ylabel(" C ")
plt.xlim(-10,10)

plt.subplot(212)
plt.plot(V_r, C_2,"r")
plt.plot(V_r,y)
plt.plot(fitting_V,y_V,"r-.")
plt.axvline(x=0, color = 'k') # x축
plt.axhline(y=0, color = 'k') # y축
plt.xlim(-10,10)
plt.xlabel(" V ")
plt.ylabel(" 1/C^2 ")

plt.show()
