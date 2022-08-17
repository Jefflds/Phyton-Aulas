from msilib.schema import Class

#declarar método

def soma (a, b):
    return a + b

def sub (a, b):
    return a - b

def multi (a, b):
    return a * b

def div (a, b):
    return a / b

def resto (a, b):
    return a % b
    
    
#print (soma (1, 2))

#criar uma classe

class Calculadora:
    
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2
    
    def soma (self):
        return self.a + self.b

    def sub (self):
        return self.a - self.b

    def multi (self):
        return self.a * self.b

    def div (self):
        return self.a / self.b

    def resto (self):
        return self.a % self.b    
    

calculadora = Calculadora (10, 5)
print (calculadora.a)
print (calculadora.soma())
print (calculadora.sub())
print (calculadora.multi())
print (calculadora.div ())
print (calculadora.resto())
