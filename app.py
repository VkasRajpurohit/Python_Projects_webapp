# Required libraries
import random, calendar, cmath

import logging as lg
import numpy as np

from flask import Flask, render_template, request
from flask_cors import cross_origin

app = Flask(__name__)  # app as object created

# Create and configure logger
lg.basicConfig(filename="logfile.log",
               filemode='w',
               level=lg.INFO,
               format='%(asctime)s %(levelname)s: %(message)s',
               datefmt='%Y-%m-%d %H:%M:%S')

lg.info('app start- working fine')


@app.route('/', methods=['GET', 'POST'])  # To render Home_Page
@cross_origin()
def home_page():
    """landing to home_page"""
    # render_template-- https://getbootstrap.com/
    lg.info('landing on home page- working fine')
    return render_template('index.html')


@app.route('/about')  # To render about page
@cross_origin()
def about():
    """about the app information"""
    lg.info('about page- working fine')
    return render_template('about.html')


@app.route('/contact')  # To render contact page
@cross_origin()
def contact():
    """contact information"""
    lg.info('contact page- working fine')
    return render_template('contact.html')


@app.route('/Project_1')  # To render Project_1 page
@cross_origin()
def project_1():
    """about the app information"""
    lg.info('project_1 page- working fine')
    return render_template('project_1.html')


# 1. Write a Python program to print & quot;Hello Python&quot?
@app.route('/Project_1_Q1', methods=['GET', 'POST'])
@cross_origin()
def print_user_name():
    """Project_1_Q1 page info"""
    if request.method == 'POST':
        try:
            user_name = request.form['user']
            lg.info('Project_1_Q1- working fine- input={}'.format(user_name))
        except Exception as e:
            lg.warning('Project_1_Q1- unable to complete request: {}'.format(e))
        return render_template('Project 1/P1Q1.html', user="Hi {} welcome !!".format(user_name))
    return render_template('Project 1/P1Q1.html')


# 2. Write a Python program to do arithmetical operations addition and division.?
@app.route('/Project_1_Q2', methods=['GET', 'POST'])
@cross_origin()
def math_operation():
    """Project_1_Q2 page info"""
    if request.method == 'POST':
        operation = request.form['operation']
        value1 = float(request.form['val1'])
        value2 = float(request.form['val2'])
        lg.info('Project_1_Q2- working fine- value1={} & value2={}'.format(value1, value2))
        try:
            if operation == 'add':
                result = value1 + value2
                lg.info('Project_1_Q2 result- working fine- addition={}'.format(result))
            if operation == 'div':
                result = value1 / value2
                lg.info('Project_1_Q2 result- working fine- division={}'.format(result))
        except Exception as e:
            lg.warning('Project_1_Q2- unable to complete request: {}'.format(e))
        return render_template('Project 1/P1Q2.html', result="Operation Result: {}".format(result))
    return render_template('Project 1/P1Q2.html')


# 3. Write a Python program to find the area of a triangle?
@app.route('/Project_1_Q3', methods=['GET', 'POST'])
@cross_origin()
def triangle_area():
    """Project_1_Q3 page info"""
    if request.method == 'POST':
        base = float(request.form['base'])
        height = float(request.form['height'])
        lg.info('Project_1_Q3- working fine- base={} & height={}'.format(base, height))
        try:
            area = (base * height) / 2
            lg.info('Project_1_Q3_result- working fine- area={}'.format(area))
        except Exception as e:
            lg.warning('Project_1_Q3_result- unable to complete request: {}'.format(e))
        return render_template('Project 1/P1Q3.html', area="Area of the Triangle: {}".format(area))
    return render_template('Project 1/P1Q3.html')


# 4. Write a Python program to swap two variables?
@app.route('/Project_1_Q4', methods=['GET', 'POST'])
@cross_origin()
def swap():
    """Project_1_Q4 page info"""
    if request.method == 'POST':
        var1 = int(request.form['val1'])
        var2 = int(request.form['val2'])
        input_var = 'Given variables: ' + str(var1) + ' & ' + str(var2)
        lg.info('Project_1_Q4- working fine- {}'.format(input_var))
        try:
            var1, var2 = var2, var1  # swapped
            swapped = 'After swap: ' + str(var1) + ' & ' + str(var2)
            lg.info('Project_1_Q4 result- working fine- {}'.format(swapped))
        except Exception as e:
            lg.warning('Project_1_Q4 result- unable to complete request: {}'.format(e))
        return render_template('Project 1/P1Q4.html', input_var= input_var, swapped=swapped)
    return render_template('Project 1/P1Q4.html')


# 5. Write a Python program to generate a random number?
@app.route('/Project_1_Q5', methods=['GET', 'POST'])
@cross_origin()
def generate_random_number():
    """Project_1_Q5 page info"""
    if request.method == 'POST':
        val1 = int(request.form['val1'])
        val2 = int(request.form['val2'])
        given_range = 'Range: (' + str(val1) + ', ' + str(val2) + ')'
        lg.info('Project_1_Q5- working fine- {}'.format(given_range))
        try:
            random_num = random.randint(val1, val2)
            lg.info('Project_1_Q5 result- working fine- random number: {}'.format(random_num))
        except Exception as e:
            lg.warning('Project_1_Q5 result- unable to complete request: {}'.format(e))
        return render_template('Project 1/P1Q5.html', given_range=given_range, result="Random number: {}".format(random_num))
    return render_template('Project 1/P1Q5.html')


@app.route('/Project_2')  # To render Project_2 page
@cross_origin()
def project_2():
    """Project_2 Submission page information"""
    lg.info('project_2 page- working fine')
    return render_template('project_2.html')


@app.route('/Project_2_Q1', methods=['GET', 'POST'])  # To render Project_2_Q1 page
@cross_origin()
def Project_2_Q1():
    """project_2_Q1 page: Convert kilometers to miles?"""
    # 1km = 0.62137119 miles
    if request.method == 'POST':
        km = float(request.form['kilometers'])
        lg.info('project_2_Q1- working fine- kilometers= {}'.format(km))
        try:
            miles = km * 0.62137119
            lg.info('project_2_Q1_result- working fine- miles= {}'.format(miles))
        except Exception as e:
            lg.warning('project_2_Q1_result- unable to complete request: {}'.format(e))
        return render_template('Project 2/P2Q1.html', result=" {} Kilometers = {} Miles.".format(km, np.round(miles, 2)))
    return render_template('Project 2/P2Q1.html')


@app.route('/Project_2_Q2', methods=['GET', 'POST'])  # To render Project_2_Q2 page
@cross_origin()
def Project_2_Q2():
    """project_2_Q2 page: Convert Celsius to Fahrenheit?"""
    # T (°F) = T (°C) × 1.8 + 32
    if request.method == 'POST':
        temp_celsius = float(request.form['temp_celsius'])
        lg.info('project_2_Q2- working fine- Temperature in Celsius= {}'.format(temp_celsius))
        try:
            temp_fahrenheit = temp_celsius * 1.8 + 32
            lg.info('project_2_Q2_result- working fine- Temperature in Fahrenheit= {}'.format(temp_fahrenheit))
        except Exception as e:
            lg.warning('project_2_Q2_result- unable to complete request: {}'.format(e))
        return render_template('Project 2/P2Q2.html', result=" {} °Celsius = {} °Fahrenheit."
                               .format(temp_celsius, np.round(temp_fahrenheit, 2)))
    return render_template('Project 2/P2Q2.html')


@app.route('/Project_2_Q3', methods=['GET', 'POST'])  # To render Project_2_Q3 page
@cross_origin()
def Project_2_Q3():
    """Project_2_Q3 page: Display Calendar."""
    # importing calendar module: import calendar
    if request.method == 'POST':
        yyyy = int(request.form['year'])
        lg.info('Project_2_Q3- working fine- year= {}'.format(yyyy))
        try:
            display_calendar = calendar.calendar(yyyy, w=3, l=2, c=3, m=4)
            # w controls the width;
            # l controls the length between each string;
            # c and m specify the number of rows and columns, respectively.
            lg.info('Project_2_Q3 result- display_calendar- working fine')
        except Exception as e:
            lg.warning('Project_2_Q3 result- unable to complete request: {}'.format(e))
        return render_template('Project 2/P2Q3.html', result=display_calendar)
    return render_template('Project 2/P2Q3.html')


@app.route('/Project_2_Q4', methods=['GET', 'POST'])  # To render Project_2_Q4 page
@cross_origin()
def Project_2_Q4():
    """Project_2_Q4 page: Solve Quadratic Equation."""
    # importing module: import cmath
    if request.method == 'POST':
        # Enter coefficients
        a = int(request.form['a'])
        b = int(request.form['b'])
        c = int(request.form['c'])
        lg.info('Project_2_Q4- working fine- coefficients: {}, {}, {}'.format(a, b, c))
        try:
            # solutions of this quadratic equation: (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
            d = (b ** 2) - (4 * a * c)   # calculate the discriminant

            # find two solutions
            sol1 = (-b - cmath.sqrt(d)) / (2 * a)
            sol2 = (-b + cmath.sqrt(d)) / (2 * a)

            solve = 'Solution: {} & {}'.format(np.round(sol1, 3), np.round(sol2, 3))
            lg.info('Project_2_Q4 result- working fine: {}'.format(solve))
        except Exception as e:
            lg.warning('Project_2_Q4 result- unable to complete request: {}'.format(e))
        return render_template('Project 2/P2Q4.html', equation= "Quadratic Equation: {}x² + {}x + {} = 0"
                               .format(a, b, c), result=solve)
    return render_template('Project 2/P2Q4.html')


@app.route('/Project_2_Q5', methods=['GET', 'POST'])  # To render Project_2_Q4 page
@cross_origin()
def Project_2_Q5():
    """Project_2_Q5 page: Swap two variables without temp variable."""
    # Already done in Project_1_Q4
    return render_template('Project 1/P1Q4.html')


if __name__ == '__main__':  # on running python app.py
    app.run(debug=True)     # run the flask app
