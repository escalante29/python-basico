def test_division_entera():
    num1 = 10
    num2 = 3

    division_result = num1 // num2
    print(division_result)

    assert 3 == division_result


def test_division_exacta():
    num1 = 10
    num2 = 3

    division_result = num1 / num2
    print(division_result)

    assert 3.3333333333333335 == division_result
