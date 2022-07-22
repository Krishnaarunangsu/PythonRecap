import numpy as np

temperature = np.array([29.3, 42.1, 18.8, 16.1, 38.0, 12.5,
                        12.6, 49.9, 38.6, 31.3, 9.2, 22.2])
print(f'Shape of the array:\n{temperature.shape}')
temperature_reshaped = temperature.reshape(2, 2, 3)
print(f'The New Array:\n{temperature_reshaped}')
print(temperature_reshaped.shape[2])
