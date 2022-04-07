# A simple script to calculate BMI
from pywebio.input import input, FLOAT
from pywebio.output import put_text


def bmi():
    height = input("Input your height(in)：", type=FLOAT)
    weight = input("Input your weight(lbs)：", type=FLOAT)

    # BMI = weight / (height / 100) ** 2
    BMI = round(((weight * 703) / (height * height)), 2)

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
            break


if __name__ == '__main__':
    bmi()
