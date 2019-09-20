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
* saveInFile() - appends the string to log.txt file and returns first line for testing
