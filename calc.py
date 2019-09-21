import sys, os, math
class Operator:
    def set(self):
        self.operator = input()

    def get(self):
        return self.operator

class MyCalc:
    nums = []
    res = ''

    def start(self):
            print("Hello, I am console calculator!")
            print("Here is what you can do with me:")
            print("\ttype \"+\" if you want to sum some numbers.")
            print("\ttype \"-\" if you want to subtract some numbers.")
            print("\ttype \"*\" if you want to multiply some numbers.")
            print("\ttype \"/\" if you want to divide some numbers.")
            print("\ttype \"%\" if you want to find mod.")
            print("\ttype \"his\" to see logs")
            print("\ttype \"sqrt\" to find square root")
            print("\ttype \"sin\" to find sinus")
            print("\ttype \"cos\" to find cosinus")

    def calculate(self):
        self.start()
        self.res = ''
        self.nums = []

        sign = Operator()
        sign.set()

        if sign.get() == '+':
            self.askForInput()
            self.res = self.add(self.nums)
            print(self.res)
        elif sign.get() == '-':
            self.askForInput()
            self.res = self.sub(self.nums)
            print(self.res)
        elif sign.get() == '*':
            self.askForInput()
            self.res = self.mult(self.nums)
            print(self.res)
        elif sign.get() == '/':
            self.askForInput()
            self.res = self.divide(self.nums)
            print(self.res)
        elif sign.get() == '%':
            self.askForInput()
            self.res = self.mod(self.nums)
            print(self.res)
        elif sign.get() == 'his':
            his = History()
            print(his.getHistory())
        elif sign.get() == 'sqrt':
            x = float(input('Enter the number:'))
            self.res = 'sqrt({}) = {}'.format(x, math.sqrt(x))
            print(self.res)
        elif sign.get() == 'sin':
            x = float(input('Enter the number:'))
            self.res = 'sin({}) = {}'.format(x, math.sin(x))
            print(self.res)
        elif sign.get() == 'cos':
            x = float(input('Enter the number:'))
            self.res = 'cos({}) = {}'.format(x, math.cos(x))
            print(self.res)
        else:
            print('Invalid enter')
            fin = input('Would you like to exit? [y/n]\n')
            if fin == 'y':
                sys.exit()

        self.askForLog()
        self.isCalcAgain() 
        
    def add(self, nums):
        sum = 0
        for num in nums:
            self.res += '{} + '.format(num)
            sum += num
        self.res = self.res[0:len(self.res) - 3]
        return '{} = {}'.format(self.res, sum)
    
    def sub(self, nums):
        self.res = str(nums[0]) + ' - '
        sub = nums[0]
        for num in nums[1:len(nums)]:
            self.res += '{} - '.format(num)
            sub -= num
        self.res = self.res[0:len(self.res) - 3]
        return '{} = {}'.format(self.res, sub)

    def mult(self, nums):
        self.res = ''
        mult = 1
        for num in nums:
            self.res += '{} * '.format(num)
            mult *= num
        self.res = self.res[0:len(self.res) - 3]
        return '{} = {}'.format(self.res, mult)

    def divide(self, nums):
        self.res = str(nums[0]) + ' / '
        div = nums[0]
        for num in nums[1:len(nums)]:
            self.res += '{} / '.format(num)
            div /= num
        self.res = self.res[0:len(self.res) - 3]
        return '{} = {}'.format(self.res, div)

    def mod(self, nums):
        self.res = str(nums[0]) + ' % '
        mod = nums[0]
        for num in nums[1:len(nums)]:
            self.res += '{} % '.format(num)
            mod %= num
        self.res = self.res[0:len(self.res) - 3]
        return '{} = {}'.format(self.res, mod)

    def askForInput(self):
        print('Enter the number. Type \'q\' to finish inputing.')
        while True:
            _input = input()
            if _input == 'q':
                break
            try:
                self.nums.append(int(_input))
            except:
                print('Wrong input. Numbers only.')
        return
    
    def isCalcAgain(self):
        flag = input('Would you like to calculate again? [y/n]\n')
        if flag == 'y':
            self.calculate()
        else:
            print('Bye!')

    def askForLog(self):
        if self.res == '':
            return
        log = Logger(self.res)
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

class History:
    def getHistory(self):
        reader = open('log.txt', 'r')
        res = reader.read()
        reader.close()
        return res



calc = MyCalc()
calc.calculate()