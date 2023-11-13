import numpy as np
import matplotlib.pyplot as plt

# 상수 정의
E_g_eV = 1.12  # 실리콘의 에너지 밴드 갭 (전자볼트 단위)
e = 1.602e-19  # 전자의 전하량 (쿨롱)
E_g = E_g_eV * e  # 조울 단위로 변환
k = 1.381e-23  # 볼츠만 상수 (J/K)
I_D = 0.1e-3  # 다이오드 전류 (암페어)
I_S = 1e-15  # 포화 전류 (암페어)
KELVIN_CONVERSION = 273.15  # 켈빈 변환 상수
C_1 = I_S / np.exp(-E_g/(300*k)) # C_1 상수
print("C1 : ", C_1)
x = 0.0259 * np.log(I_D / I_S)
# x를 출력
print("x : ", x);

# Va를 계산하는 함수
def calculate_V_a(T_kelvin, I_D, I_S):
    return (E_g / e) - ((k * T_kelvin) / e) * np.log(C_1 / I_D)

# 온도 범위 정의 (20°C to 200°C), 켈빈으로 변환
T_min = 20 + KELVIN_CONVERSION
T_max = 200 + KELVIN_CONVERSION
temperatures = np.linspace(T_min, T_max, 400)  # 온도 범위 생성

# 온도 범위에 대한 Va 계산
V_a_values = calculate_V_a(temperatures, I_D, I_S)

# T = 300K에서의 Va값 계산
V_a_300K = calculate_V_a(300, I_D, I_S)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(temperatures - KELVIN_CONVERSION, V_a_values, label='$V_a$ vs $T$')
plt.scatter(300 - KELVIN_CONVERSION, V_a_300K, color='red', label='Value at $T=300$K')  # 300K에서의 값 표시
plt.xlabel('Temperature (°C)')
plt.ylabel('Voltage $V_a$ (Volts)')
plt.title('$V_a$ vs $T$ Graph')
plt.legend()
plt.grid(True)
plt.show()

# T=20K, 200K에서의 Va 값을 출력합니다.
V_a_20C = calculate_V_a(20+KELVIN_CONVERSION, I_D, I_S)
V_a_200C = calculate_V_a(200+KELVIN_CONVERSION, I_D, I_S)
print(f'V_a at T=20C: {V_a_20C:.3f} Volts')
print(f'V_a at T=200C: {V_a_200C:.3f} Volts')



