import pytest


def bmi_calc(h, w):
    if h <= 0:
        return "Invalid input."
    if w <= 0:
        return "Invalid input."

    h = h * 12
    bmi = w / (h * h) * 703

    if bmi <= 18.5:
        return "You are underweight."
    elif bmi <= 24.9:
        return "You are healthy."
    elif bmi <= 29.8:
        return "You are over weight."
    elif bmi <= 34.9:
        return "You are severely over weight."
    elif bmi <= 39.9:
        return "You are obese."
    else:
        return "You are severely obese."


def main():
    height = float(input("Enter your height in feet and inches: "))
    weight = float(input("Enter your weight in pounds: "))
    print(bmi_calc(height, weight))


if __name__ == "__main__":
    main()


def test_bmi_calc():
    # Tests regular input
    assert bmi_calc(5.11, 160) == 'You are severely over weight.'
    # Tests negatives for height
    assert bmi_calc(-5.11, 160) == 'Invalid input.'
    # Tests negatives for weight
    assert bmi_calc(5.11, -160) == 'Invalid input.'
    # Tests 0 for both inputs
    assert bmi_calc(0, 0) == 'Invalid input.'
