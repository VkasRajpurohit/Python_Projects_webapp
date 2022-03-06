import logging as lg
import random

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


# 1. Write a Python program to print & quot;Hello Python&quot?
@app.route('/Q1')
@cross_origin()
def print_hi():
    """Q1 page info"""
    return render_template('Q1.html')


@app.route('/Q1_result', methods=['POST'])
@cross_origin()
def Q1_result():
    """Q1 result page info"""
    if request.method == 'POST':
        try:
            user_name = request.form['user']
            lg.info('Q1_result- working fine- input={}'.format(user_name))
            return render_template('Q1_result.html', user=user_name)
        except Exception as e:
            lg.warning('Q1_result- unable to complete request: {}'.format(e))


# 2. Write a Python program to do arithmetical operations addition and division.?
@app.route('/Q2')
@cross_origin()
def math_operation():
    """Q2 page info"""
    return render_template('Q2.html')


@app.route('/Q2_result', methods=['POST'])
@cross_origin()
def math_operation_result():
    """Q2 result page info"""
    if request.method == 'POST':
        operation = request.form['operation']
        value1 = float(request.form['val1'])
        value2 = float(request.form['val2'])
        lg.info('Q2_result- working fine- value1={} & value2={}'.format(value1, value2))
        try:
            if operation == 'add':
                result = value1 + value2
                lg.info('Q3_result- working fine- addition={}'.format(result))
            if operation == 'div':
                result = value1 / value2
                lg.info('Q3_result- working fine- division={}'.format(result))
        except Exception as e:
            lg.warning('Q2_result- unable to complete request: {}'.format(e))
    return render_template('Q2_result.html', result=result)


# 3. Write a Python program to find the area of a triangle?
@app.route('/Q3')
@cross_origin()
def triangle_area():
    """Q3 page info"""
    return render_template('Q3.html')


@app.route('/Q3_result', methods=['POST'])
@cross_origin()
def Q3_result():
    """Q3 result page info"""
    if request.method == 'POST':
        base = float(request.form['base'])
        height = float(request.form['height'])
        lg.info('Q3- working fine- base={} & height={}'.format(base, height))
        try:
            area = (base * height) / 2
            lg.info('Q3_result- working fine- area={}'.format(area))
        except Exception as e:
            lg.warning('Q3_result- unable to complete request: {}'.format(e))
    return render_template('Q3_result.html', area=area)


# 4. Write a Python program to swap two variables?
@app.route('/Q4')
@cross_origin()
def swap():
    """Q4 page info"""
    return render_template('Q4.html')


@app.route('/Q4_result', methods=['POST'])
@cross_origin()
def Q4_result():
    """Q4 result page info"""
    if request.method == 'POST':
        var1 = int(request.form['val1'])
        var2 = int(request.form['val2'])
        input_var = 'Given variables: ' + str(var1) + ' & ' + str(var2)
        lg.info('Q4- working fine- {}'.format(input_var))
        try:
            var1, var2 = var2, var1  # swapped
            swapped = 'After swap: ' + str(var1) + ' & ' + str(var2)
            lg.info('Q4_result- working fine- {}'.format(swapped))
        except Exception as e:
            lg.warning('Q4_result- unable to complete request: {}'.format(e))
    return render_template('Q4_result.html', given_values=input_var, swap_result=swapped)


# 5. Write a Python program to generate a random number?
@app.route('/Q5')
@cross_origin()
def generate_random_number():
    """Q5 page info"""
    return render_template('Q5.html')


@app.route('/Q5_result', methods=['POST'])
@cross_origin()
def Q5_result():
    """Q5 result page info"""
    if request.method == 'POST':
        val1 = int(request.form['val1'])
        val2 = int(request.form['val2'])
        range_ = 'Range: (' + str(val1) + ', ' + str(val2) + ')'
        lg.info('Q5- working fine- {}'.format(range_))
        try:
            random_num = random.randint(val1, val2)
            lg.info('Q5_result- working fine- random number: {}'.format(random_num))
        except Exception as e:
            lg.warning('Q5_result- unable to complete request: {}'.format(e))
    return render_template('Q5_result.html', range=range_, result=random_num)


if __name__ == '__main__':  # on running python app.py
    app.run(debug=True)  # run the flask app
