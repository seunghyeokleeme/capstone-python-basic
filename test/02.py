import numpy as np
import matplotlib.pyplot as plt

########################################변수지정###############################################

q = 1.6e-19  # 전자의 전하량 (쿨롱)
E_g_eV = 1.12  # 실리콘의 에너지 밴드 갭 (전자볼트 단위)
k = 1.38 * 1e-23  # 볼츠만 상수 (J/K)

def V_a(T):
     Is_300 = 1e-14 # T = 300 (K) , Is = 10^(-14) (A)
     C = Is_300 / ( np.exp( - ( E_g_eV * q) / ( 300 * k ) ) ) #I_s = C * np.exp(-Eg*q/300*k)  # exp(J/J)
     I_d = 0.2 * 1e-3 # 0.2 (mA)
     Va = E_g_eV - ( k * T / q ) * np.log( C / I_d ) # (V)
     return Va # V (V)

T = np.arange(290 , 500 , 0.1) # 290K < T < 500K , 0.1씩
Va = V_a(T)

def I(V,T): # ni의 kT값도 고려
     ID = 0.1 * 1e-3 * np.exp(-( E_g_eV * q - q * V ) /( T * k )) 
     return ID

V = np.arange(0,1,0.001) # 0 ~ 1V , 1mV sweep
T_ID = [300, 400, 500]

# ID[0] = 300K일때, ID[1] = 350K일때, ID[2] = 400K일때, ID[3] = 450K일때, ID[4] = 500K일때
ID = [ I(V,T_ID[0]), I(V,T_ID[1]), I(V,T_ID[2])] # 정답

###################################### 그래프 출력 ############################################
fig = plt.figure(figsize=(15,7))

plt.subplot(131)
plt.plot(T,Va)
plt.xlabel("Temperature (K)")
plt.ylabel("Voltage (V)")
plt.title('V-T curve')

plt.subplot(132)
plt.plot(V ,ID[0]*1e9,label = "T = 300K")
plt.plot(V ,ID[1]*1e9,label = "T = 400K")
plt.plot(V ,ID[2]*1e9,label = "T = 500K")
plt.ylabel("ID (nA)")
plt.xlabel("Voltage (V)")
plt.ylim(0,2.0) # 0 ~ 2 nA
plt.title('ID-V curve solution')
plt.legend()


plt.show()