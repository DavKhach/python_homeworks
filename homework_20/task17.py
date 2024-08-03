def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


temperature_operations = {
    ('celsius', 'fahrenheit'): celsius_to_fahrenheit,
    ('fahrenheit', 'celsius'): fahrenheit_to_celsius,
    ('celsius', 'kelvin'): celsius_to_kelvin,
    ('kelvin', 'celsius'): kelvin_to_celsius,
    ('fahrenheit', 'kelvin'): fahrenheit_to_kelvin,
    ('kelvin', 'fahrenheit'): kelvin_to_fahrenheit
}

def convert_temperature(value, from_unit, to_unit):
    if (from_unit, to_unit) not in temperature_operations:
        raise ValueError("Invalid conversion")
    
    conversion_func = temperature_operations[(from_unit, to_unit)]
    
    return conversion_func(value)


print(convert_temperature(100, 'celsius', 'fahrenheit'))
print(convert_temperature(32, 'fahrenheit', 'celsius'))
print(convert_temperature(0, 'celsius', 'kelvin'))
print(convert_temperature(273.15, 'kelvin', 'celsius'))
print(convert_temperature(212, 'fahrenheit', 'kelvin'))
print(convert_temperature(373.15, 'kelvin', 'fahrenheit'))
