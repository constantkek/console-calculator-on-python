import sys, os
class Operator:
    def set(self):
        self.operator = input('Please, type the operation (+, -, *, /)\n')

    def get(self):
        return self.operator

class MyCalc:
    nums = []

    def __init__(self):
            print("Hello, I am console calculator!")
            print("Here is what you can do with me:")
            print("\ttype \"+\" if you want to sum 2 numbers.")
            print("\ttype \"-\" if you want to subtract 2 numbers.")
            print("\ttype \"*\" if you want to multiply 2 numbers.")
            print("\ttype \"/\" if you want to divide 2 numbers.")
            print("\ttype \"%\" if you want to find mod.")

    def calculate(self):
        sign = Operator()
        sign.set()

        if (sign.get() == '+') or (sign.get() == '-') or (sign.get() == '*') or (sign.get() == '/'):
            self.askForInput()
            if sign.get() == '+':
                print(self.add(self.nums))
                self.askForLog(self.add(self.nums))
            elif sign.get() == '-':
                print(self.sub(self.nums))
                self.askForLog(self.sub(self.nums))
            elif sign.get() == '*':
                print(self.mult(self.nums))
                self.askForLog(self.mult(self.nums))
            elif sign.get() == '/':
                print(self.divide(self.nums))
                self.askForLog(self.divide(self.nums))
        else:
            print('Invalid enter')
            fin = input('Would you like to exit? [y/n]\n')
            if fin == 'y':
                sys.exit()

        self.isCalcAgain() 
        
    def add(self, nums):
        resultString = ""
        sum = 0
        for num in nums:
            resultString += '{} + '.format(num)
            sum += num
        resultString = resultString[0:len(resultString) - 3]
        return '{} = {}'.format(resultString, sum)
    
    def sub(self, nums):
        resultString = str(nums[0]) + ' - '
        sub = nums[0]
        for num in nums[1:len(nums)]:
            resultString += '{} - '.format(num)
            sub -= num
        resultString = resultString[0:len(resultString) - 3]
        return '{} = {}'.format(resultString, sub)

    def mult(self, nums):
        resultString = ""
        mult = 1
        for num in nums:
            resultString += '{} * '.format(num)
            mult *= num
        resultString = resultString[0:len(resultString) - 3]
        return '{} = {}'.format(resultString, mult)

    def divide(self, nums):
        resultString = str(nums[0]) + ' / '
        div = nums[0]
        for num in nums[1:len(nums)]:
            resultString += '{} / '.format(num)
            div /= num
        resultString = resultString[0:len(resultString) - 3]
        return '{} = {}'.format(resultString, div)

    def askForInput(self):
        print('Enter the number. Type \'q\' to finish inputing.')
        while True:
            _input = input()
            if _input == 'q':
                break
            self.nums.append(int(_input))
        return
    
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