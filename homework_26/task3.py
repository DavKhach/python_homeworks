class Temperature:
    def __init__(self, celsius=0):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Temperature must be number")
        self.__celsius = value

    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Temperature must be number")
        self.celsius = (value - 32) * 5 / 9

temp = Temperature(16)
print(f"Temperature in Celsius: {temp.celsius}℃")
print(f"Temperature in Fahrenheit: {temp.fahrenheit}℉")

temp.fahrenheit = 76.2
print(f"Temperature in Celsius: {temp.celsius}℃")
print(f"Temperature in Fahrenheit: {temp.fahrenheit}℉")
