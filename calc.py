import sys, os
class Operator:
    def set(self):
        self.operator = input('Please, type the operation (+, -, *, /)\n')

    def get(self):
        return self.operator

class MyCalc:
    num1 = 0
    num2 = 0
    def calculate(self):
        sign = Operator()
        sign.set()

        if (sign.get() == '+') or (sign.get() == '-') or (sign.get() == '*') or (sign.get() == '/'):
            self.num1, self.num2 = self.askForInput()
            if sign.get() == '+':
                print(self.add(self.num1, self.num2))
                self.askForLog(self.add(self.num1, self.num2))
            elif sign.get() == '-':
                print(self.sub(self.num1, self.num2))
                self.askForLog(self.sub(self.num1, self.num2))
            elif sign.get() == '*':
                print(self.mult(self.num1, self.num2))
                self.askForLog(self.mult(self.num1, self.num2))
            elif sign.get() == '/':
                print(self.divide(self.num1, self.num2))
                self.askForLog(self.divide(self.num1, self.num2))
        else:
            print('Invalid enter')
            fin = input('Would you like to exit? [y/n]\n')
            if fin == 'y':
                sys.exit()

        self.isCalcAgain() 
        
    def add(self, number1, number2):
        return '{} + {} = {}'.format(number1, number2, number1 + number2)
    
    def sub(self, number1, number2):
        return '{} - {} = {}'.format(number1, number2, number1 - number2)

    def mult(self, number1, number2):
        return '{} * {} = {}'.format(number1, number2, number1 * number2)

    def divide(self, number1, number2):
        return '{} / {} = {}'.format(number1, number2, number1 / number2)
    
    def askForInput(self):
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        return num1, num2
    
    def isCalcAgain(self):
        flag = input('Would you like to calculate again? [y/n]\n')
        if flag == 'y':
            self.calculate()
        else:
            print('Bye!')

    def askForLog(self, res):
        log = Logger(res)
        log.askUser('Would you like to save the result into the log.txt? [y/n]\n')

class Logger:
    res = ''
    def __init__(self, res):
        self.res = res

    def askUser(self, string):
        self.choice = input(string)
        if self.choice == 'y':
            self.saveInFile('log.txt')

    def saveInFile(self, fileName):
        append = open(fileName, 'a')
        reader = open(fileName, 'r')
        append.write(self.res + '\n')
        append.close()
        return reader.readline()

calc = MyCalc()
calc.calculate()