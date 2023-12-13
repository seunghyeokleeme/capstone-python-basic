import numpy as np
import matplotlib.pyplot as plt

w = 150e-6

# data
l = [4e-6, 8e-6, 12e-6, 20e-6, 50e-6]
r = [2.2, 6.5, 10.2, 13.5, 17.2]

# 기울기, y절편 구하기
d0, y0 = np.polyfit(l, r, 1)

# x 범위 설정
l_space = np.linspace(-8.276318554318132e-06 *2, max(l), 10)

# Rt 함수 설정
y_fit = d0 * l_space + y0

# 그래프 출력
plt.figure(figsize=(8, 6))
plt.plot(l, r, 'o', label='Data Points')  # Data points
plt.plot(l_space, y_fit, 'b-', label=f'Linear Fit: y = {d0:.2f}x + {y0:.2f}')  # 점 
# Calculating and plotting the x-intercept
x_intercept = -y0 / d0
plt.axvline(x_intercept, color='green', linestyle='--', label=f'x-intercept(-2L_t): {x_intercept:.2e}')

# 그래프 정보 출력
plt.xlabel('L (um)')
plt.ylabel('Rt (Ohms)')
plt.title('Linear Fit to Length vs. Resistance')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

# Returning the slope (d0) and y-intercept (y0) values
d0, y0, x_intercept

print("R_c: ");
print(y0/2);
print("R_s:");
print(d0*w);
print("L_t: ");
print(-x_intercept/2);