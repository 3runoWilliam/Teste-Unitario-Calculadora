from src.calculadora import Calculadora
from src.operations.add import AddOperation
from src.operations.sub import SubOperation

calc = Calculadora(AddOperation(), SubOperation())
op1 = calc.add(5, 5, True)
op2 = calc.sub(4, 3, True)

print(op1)
print(op2)
