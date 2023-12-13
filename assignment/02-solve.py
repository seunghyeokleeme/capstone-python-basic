import numpy as np
import matplotlib.pyplot as plt

########################################변수지정###############################################

q = 1.6 * 1e-19 # C
Eg = 1.12 # 1.12 (eV)
k = 1.38 * 1e-23 # 1.38 * 10^(-23) J/K

##############################################################################################

############################### V - T curve ##################################################

def V_a(T):
     Is_300 = 1e-15 # T = 300 (K) , Is = 10^(-15) (A)
     C = Is_300 / ( np.exp( - ( Eg * q) / ( 300 * k ) ) ) #I_s = C * np.exp(-Eg*q/300*k)  # exp(J/J)
     I_d = 0.1 * 1e-3 # 0.1 (mA)
     Va = Eg - ( k * T / q ) * np.log( C / I_d ) # (V)
     return Va # V (V)

T = np.arange(20 + 273 , 200 + 273 , 0.1) # 20'C < T < 200'C , 0.1씩
Va = V_a(T)

print(Va)

##############################################################################################

######################################## ID - V curve ########################################

def I(V,T): # ni의 kT값도 고려
     ID = 1e-3 * np.exp(-( Eg * q - q * V ) /( T * k )) 
     return ID

def I_wa(V,T): # ni의 kT값 고려x
     ID = 1e-15 * np.exp( q * V / (k * T ))
     return ID

V = np.arange(0,1,0.001) # 0 ~ 1V , 1mV sweep
T_ID = [300 , 350 , 400 , 450 , 500]

# ID[0] = 300K일때, ID[1] = 350K일때, ID[2] = 400K일때, ID[3] = 450K일때, ID[4] = 500K일때
ID = [ I(V,T_ID[0]), I(V,T_ID[1]), I(V,T_ID[2]), I(V,T_ID[3]), I(V,T_ID[4])] # 정답
ID_w = [ I_wa(V,T_ID[0]), I_wa(V,T_ID[1]), I_wa(V,T_ID[2]), I_wa(V,T_ID[3]), I_wa(V,T_ID[4])] # 오답

##############################################################################################

###################################### 그래프 출력 ############################################
fig = plt.figure(figsize=(15,7))

plt.subplot(131)
plt.plot(T,Va)
plt.xlabel("Temperature (K)")
plt.ylabel("Voltage (V)")
plt.title('V-T curve')

plt.subplot(132)
plt.plot(V ,ID[0]*1e9,label = "T = 300K")
plt.plot(V ,ID[1]*1e9,label = "T = 350K")
plt.plot(V ,ID[2]*1e9,label = "T = 400K")
plt.plot(V ,ID[3]*1e9,label = "T = 450K")
plt.plot(V ,ID[4]*1e9,label = "T = 500K")
plt.ylabel("ID (nA)")
plt.xlabel("Voltage (V)")
plt.ylim(0,2.0) # 0 ~ 2 nA
plt.title('ID-V curve solution')
plt.legend()

plt.subplot(133)
plt.plot(V ,ID_w[0]*1e9,label = "T = 300K")
plt.plot(V ,ID_w[1]*1e9,label = "T = 350K")
plt.plot(V ,ID_w[2]*1e9,label = "T = 400K")
plt.plot(V ,ID_w[3]*1e9,label = "T = 450K")
plt.plot(V ,ID_w[4]*1e9,label = "T = 500K")
plt.ylabel("ID (nA)")
plt.xlabel("Voltage (V)")
plt.title('ID-V curve wrong answer')
plt.ylim(0,2.0)
plt.legend()

plt.show()