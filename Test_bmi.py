import Lab2.bmi
import Lab2.bmi as bmi

def test_bmi_underweight():
    # Test for a person who is underweight
    weight, height = 50, 1.65
    result = bmi.calculate_bmi(weight, height)
    assert (result == -1)

def test_bmi_normalweight():
    # Test for a person who is normal weight
    weight, height = 72, 1.72
    result = bmi.calculate_bmi(weight, height)
    assert (result == 0)

def test_bmi_overweight():
    # Test for a person who is over weight
    weight, height = 200, 1.46
    result = bmi.calculate_bmi(weight, height)
    assert (result == 1)
