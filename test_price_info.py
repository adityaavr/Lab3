import price_info

def test_cost_of_fruits():
    fruit = "apple"
    quantity = 2
    expected_cost = 2.40
    assert price_info.cost_of_fruits(fruit, quantity) == expected_cost

    fruit = "pineapple"
    quantity = 1
    expected_cost = 2.70
    assert price_info.cost_of_fruits(fruit, quantity) == expected_cost

    fruit = "orange"
    quantity = 1
    expected_cost = 1.40
    assert price_info.cost_of_fruits(fruit, quantity) == expected_cost

def test_total_cost_shopping():
    expected_cost = 46.75
    assert price_info.total_cost_shopping() == expected_cost
