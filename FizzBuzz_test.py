from FizzBuzz import FizzBuzz

def test_1_gives_1():
    assert FizzBuzz().answer(1) == 1
    
def test_2_gives_2():
    assert FizzBuzz().answer(2) == 2
    
def test_3_gives_fizz():
    assert FizzBuzz().answer(3) == 'Fizz'
    
def test_5_gives_buzz():
    assert FizzBuzz().answer(5) == 'Buzz'
    
def test_15_gives_fizzbuzz():
    assert FizzBuzz().answer(15) == 'FizzBuzz'
    
def test_another_multiple_of_3_gives_fizz():
    assert FizzBuzz().answer(36) == 'Fizz'
    
def test_another_multiple_of_5_gives_buzz():
    assert FizzBuzz().answer(55) == 'Buzz'
    
def test_another_multiple_of_15_gives_fizzbuzz():
    assert FizzBuzz().answer(45) == 'FizzBuzz'