# Console calculator
This is my project of a console calculator I've made using python

## Main file
The program stores in calc.py file. 

## Classes
* Operator - stores the function you chose for a calculation
* Logger - works with saving calculations in a log.txt file.
* MyCalc - calculator itself

## Methods inside classes
### Class Operator:
* set() - sets the operator
* get() - gets the operator

### Class Logger:
* __init__() - sets string to store
* askUser() - asks your preference to store value
* saveInFile(string) - appends the string to log.txt file and returns first line for testing

### Class MyCalc:
* start() - outputs welcome message in terminal
* calculate() - main function. Makes a calculations. Peep-beep-boop-peep-peep.
* add(nums) - adds all numbers and returns final string
* sub(nums) - subtract all numbers from nums[0]
* mult(nums) - multiplies all numbers and returns final string.
* divide(nums) - divide all numbers from nums[0]
* mod(nums) - calculate the modification of numbers
* askForInput() - asks you to type numbers, checks input to be numerical
* isCalcAgain() - asks you to calculate again
* askForLog() - asks you whether you want to store calculation
