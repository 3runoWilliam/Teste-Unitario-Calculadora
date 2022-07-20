#from faker import Faker
from add import AddOperation

#fake = Faker()

def test_soma():
    addOperation = AddOperation()

    number1 = 4
    number2 = 11
#    expected = number1 + number2

    result = addOperation.soma(number1, number2)

    print(result)

    assert result == 15