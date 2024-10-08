import pytest
from main.main import *

def test_type_checking():
    type_check_test_inputs_fail = [None, "String", True, [], {}, (0,0), "1"]

    for test_input in type_check_test_inputs_fail:
        with pytest.raises(TypeError, match='Must enter a number.'):
            add_one(test_input)

        with pytest.raises(TypeError, match='Must enter a number.'):
            times_two(test_input)

        with pytest.raises(TypeError, match='Must enter a number.'):
            cube(test_input)

    type_check_test_inputs_succeed = [1, 3, 2.5, -1, -12, 0, 100000]

    for test_input in type_check_test_inputs_succeed:
        add_one(test_input)
        times_two(test_input)
        cube(test_input)

def test_add_one():

    add_one_test_cases = [(1, 2), 
                            (2, 3), 
                            (5, 6),
                            (10, 11), 
                            (-1, 0),
                            (0, 1),
                            (393, 394), 
                            (100000, 100001),
                            (1.5, 2.5),
                            (1.9, 2.9),
                            (7.956, 8.956)]

    for test_case in add_one_test_cases:
        assert add_one(test_case[0]) == test_case[1]


def test_times_two():

    times_two_test_cases = [(1, 2), 
                            (2, 4), 
                            (5, 10),
                            (10, 20), 
                            (-1, -2),
                            (0, 0),
                            (393, 786), 
                            (100000, 200000),
                            (1.5, 3.0),
                            (1.9, 3.8),
                            (7.956, 15.912)]

    for test_case in times_two_test_cases:
        assert times_two(test_case[0]) == test_case[1], \
        f"Unexpected Result for Times Two Test; Input: {test_case[0]}  " + \
        f"Returned Result: {times_two(test_case[0])}  " \
        f"Expected Result: {test_case[1]}"

def test_cube():
    cube_test_cases = [(1, 1), 
                        (2, 8), 
                        (5, 125),
                        (10, 1000), 
                        (-1, -1),
                        (0, 0),
                        (393, 60698457), 
                        (100000, 1000000000000000),
                        (1.5, 3.375),
                        (2.5, 15.625),
                        (8, 512)]

    for test_case in cube_test_cases:
        assert cube(test_case[0]) == test_case[1], \
        f"Unexpected Result for Cube Test; Input: {test_case[0]}  " + \
        f"Returned Result: {cube(test_case[0])}  " \
        f"Expected Result: {test_case[1]}"


def test_zero():
    zero_test_cases = [(1, 0), 
                        (2, 0), 
                        (5, 0),
                        (10, 0), 
                        (-1, 0),
                        (0, 0),
                        (393, 0), 
                        (100000, 0),
                        (1.5, 0),
                        (2.5, 0),
                        (8, 0),
                        ("", 0),
                        (None, 0),
                        ("one", 0),
                        ([], 0),
                        ({}, 0),
                        (True, 0),
                        ((0,0), 0)]
    
    for test_case in zero_test_cases:
        assert zero(test_case[0]) == test_case[1], \
        f"Unexpected Result for Zero Test; Input: {test_case[0]}  " + \
        f"Returned Result: {zero(test_case[0])}  " \
        f"Expected Result: {test_case[1]}"

def test_identity():
    identity_test_cases = [(1, 1), 
                        (2, 2), 
                        (5, 5),
                        (10, 10), 
                        (-1, -1),
                        (0, 0),
                        (393, 393), 
                        (100000, 100000),
                        (1.5, 1.5),
                        (2.5, 2.5),
                        (8, 8),
                        ("", ""),
                        (None, None),
                        ("one", "one"),
                        ([], []),
                        ({}, {}),
                        (True, True),
                        ((0,0), (0,0))]
    
    for test_case in identity_test_cases:
        assert identity(test_case[0]) == test_case[1], \
        f"Unexpected Result for Identity Test; Input: {test_case[0]}  " + \
        f"Returned Result: {identity(test_case[0])}  " \
        f"Expected Result: {test_case[1]}"

def test_changed_for_success():
    assert True == True, "This test should never fail"

if __name__ == "__main__":
    test_type_checking()
    test_add_one()
    test_times_two()
    test_cube()
    test_zero()
    test_identity()
    test_changed_for_success()

    