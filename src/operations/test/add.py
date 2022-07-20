
class AddOperationSpy:

    def __init__(self):
        self.soma_attributes = {}

    def soma(self, number1, number2):
        self.soma_attributes['number1'] = number1
        self.soma_attributes['number2'] = number2

        return number1, number2
