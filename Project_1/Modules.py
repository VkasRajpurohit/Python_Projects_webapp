import random
import logging as lg


class Q2:
    """Project_Q2: Write a Python program to do arithmetical operations addition and division"""

    def __init__(self, operation, value1, value2):
        self.value1 = value1
        self.value2 = value2
        self.operation = operation

    def math_operation(self):
        """Method Name: math_operation
           Description: It will return result of the math_operation"""
        try:
            if self.operation == 'add':
                result = self.value1 + self.value2
                lg.info('Project_1_Q2 result- working fine- addition={}'.format(result))
            if self.operation == 'div':
                result = self.value1 / self.value2
                lg.info('Project_1_Q2 result- working fine- division={}'.format(result))
        except Exception as e:
            lg.warning('Project_1_Q2- unable to complete request: {}'.format(e))

        return result


class Q3:
    """Project_1_Q3: Write a Python program to find the area of a triangle"""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def find_area(self):
        """Method Name: find_area
           Description: It will return the area of a triangle"""
        try:
            area = (self.base * self.height) / 2
            lg.info('Project_1_Q3_result- working fine- area={}'.format(area))
        except Exception as e:
            lg.warning('Project_1_Q3_result- unable to complete request: {}'.format(e))

        return area


class Q4:
    """Project_Q4: Write a Python program to swap two variables"""

    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def swap(self):
        """Method Name: swap
           Description: It will return the swapped values."""
        try:
            var1, var2 = self.var2, self.var1  # swapped
            swapped = 'After swap: ' + str(var1) + ' & ' + str(var2)
            lg.info('Project_1_Q4 result- working fine- {}'.format(swapped))
        except Exception as e:
            lg.warning('Project_1_Q4 result- unable to complete request: {}'.format(e))

        return swapped


class Q5:
    """Project_Q5: Write a Python program to generate a random number"""

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def generate_random_number(self):
        """Method Name: generate_random_number
           Description: It will generate random numbers between between the given range."""
        try:
            random_num = random.randint(self.val1, self.val2)
            lg.info('Project_1_Q5 result- working fine- random number: {}'.format(random_num))
        except Exception as e:
            lg.warning('Project_1_Q5 result- unable to complete request: {}'.format(e))

        return random_num

