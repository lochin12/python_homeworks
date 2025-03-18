import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

vectorized_f_to_c = np.vectorize(fahrenheit_to_celsius)
temperatures_f = np.array([32, 68, 100, 212, 77])
temperatures_c = vectorized_f_to_c(temperatures_f)
print("Task 1 - Fahrenheit to Celsius:", temperatures_c)


def power_function(base, exponent):
    return base ** exponent

vectorized_power = np.vectorize(power_function)
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
power_results = vectorized_power(bases, exponents)
print("Task 2 - Power Calculation:", power_results)


coefficients_1 = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
constants_1 = np.array([7, 4, 5])
solution_1 = np.linalg.solve(coefficients_1, constants_1)
print("Task 3 - Solution to System of Equations:", solution_1)


coefficients_2 = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
constants_2 = np.array([12, -5, 15])
solution_2 = np.linalg.solve(coefficients_2, constants_2)
print("Task 4 - Electrical Circuit Solution:", solution_2)


def flip_image(image_array):
    flipped_h = np.flip(image_array, axis=1)
    flipped_v = np.flip(image_array, axis=0)
    return flipped_h, flipped_v


def add_noise(image_array):
    noise = np.random.randint(-30, 30, image_array.shape, dtype=np.int16)
    noisy_image = np.clip(image_array + noise, 0, 255).astype(np.uint8)
    return noisy_image


def brighten_channels(image_array, value=40):
    brightened = np.clip(image_array + value, 0, 255).astype(np.uint8)
    return brightened


def apply_mask(image_array, center_x, center_y, size=100):
    masked_image = image_array.copy()
    masked_image[center_y-size//2:center_y+size//2, center_x-size//2:center_x+size//2] = 0
    return masked_image


image_path = "images/birds.jpg"
image = Image.open(image_path)
image_array = np.array(image)

flipped_h, flipped_v = flip_image(image_array)
Image.fromarray(flipped_h).save("flipped_h.jpg")
Image.fromarray(flipped_v).save("flipped_v.jpg")

noisy_image = add_noise(image_array)
Image.fromarray(noisy_image).save("noisy.jpg")

brightened_image = brighten_channels(image_array)
Image.fromarray(brightened_image).save("brightened.jpg")

center_x, center_y = image_array.shape[1] // 2, image_array.shape[0] // 2
masked_image = apply_mask(image_array, center_x, center_y)
Image.fromarray(masked_image).save("masked.jpg")

