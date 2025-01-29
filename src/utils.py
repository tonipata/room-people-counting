import random
from typing import Union

def generate_random_float(min_value: float, max_value: float) -> float:
    return random.uniform(min_value, max_value)

def generate_value(node: str) -> Union[float, int]:
    if 'S1_Temp' == node:
        return round(generate_random_float(24.94, 26.38), 2)
    elif 'S2_Temp' == node:
        return round(generate_random_float(24.75, 29), 2)
    elif 'S3_Temp' == node:
        return round(generate_random_float(24.44, 26.19), 2)
    elif 'S4_Temp' == node:
        return round(generate_random_float(24.94, 26.56), 2)
    elif 'S1_Light' == node:
        return round(generate_random_float(0, 165), 2)
    elif 'S2_Light' == node:
        return round(generate_random_float(0, 258), 2)
    elif 'S3_Light' == node:
        return round(generate_random_float(0, 280), 2)
    elif 'S4_Light' == node:
        return round(generate_random_float(0, 74), 2)
    elif 'S1_Sound' == node:
        return round(generate_random_float(0.06, 3.88), 2)
    elif 'S2_Sound' == node:
        return round(generate_random_float(0.04, 3.44), 2)
    elif 'S3_Sound' == node:
        return round(generate_random_float(0.04, 3.67), 2)
    elif 'S4_Sound' == node:
        return round(generate_random_float(0.05, 3.4), 2)
    elif 'PIR' in node:
        return random.choice([0, 1])
    else:
        # CO2
        return round(generate_random_float(345, 1270), 2)