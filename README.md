# Kutta-Merson-method
Solution of the Cauchy problem by the Kutta-Merson method with a given accuracy for the differential equation: 

$$y'(x) = 2x(x^2 + y)$$

$$ \eta_1^0 = f(x_0, y_0) $$
    
$$ \eta_2^0 = f(x_0 + \frac{h}{3} , y_0 + \frac{h}{3}\eta_1^0) $$

$$ \eta_3^0 = f(x_0 + \frac{h}{3}, y_0 + \frac{h}{6}\eta_1^0 + \frac{h}{6}\eta_2^0) $$

$$ \eta_4^0 = f(x_0 + \frac{h}{2}, y_0 + \frac{h}{8}\eta_1^0 + \frac{3h}{8}\eta_2^0) $$

$$ \eta_5^0 = f(x_0 + h, y_0 + \frac{h}{2}\eta_1^0 + - \frac{3h}{2}\eta_3^0 + 2h\eta_4^0) $$

The result is obtained by:

$$ y_1 = y_0 + \frac{h}{6}(\eta_1^0 + 4\eta_4^0 + \eta_5^0) $$

$$ \widetilde{y}_1 = y_0 + \frac{h}{2}(\eta_1^0 - 3\eta_3^0 + 4\eta_4^0) $$		
	
After that , we calculate the value:
 
 $$ R = 0.2|y_{i+1} - \widetilde{y}_{i+1}|$$
 
![image](https://github.com/NikishinAndrey/Kutta-Merson-method/assets/113716137/d81a1505-ba8a-4128-bdf5-d1eee52553b0)

![image](https://github.com/NikishinAndrey/Kutta-Merson-method/assets/113716137/967d088a-d2a6-4d5a-8955-3f2a68a5a85e)

![image](https://github.com/NikishinAndrey/Kutta-Merson-method/assets/113716137/a3aaa3ed-0bc1-48ee-9a38-ac09cc80dace)

![image](https://github.com/NikishinAndrey/Kutta-Merson-method/assets/113716137/cd4f15db-896e-42f5-9305-0a631c9e2c44)
