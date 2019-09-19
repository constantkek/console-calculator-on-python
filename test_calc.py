import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        res = calc.MyCalc.add(self, 7, 6)
        self.assertEqual(res, '7 + 6 = 13')

    def test_sub(self):
        res = calc.MyCalc.sub(self, 9, 2)
        self.assertEqual(res, '9 - 2 = 7')
    
    def test_mult(self):
        res = calc.MyCalc.mult(self, 14, 5)
        self.assertEqual(res, '14 * 5 = 70')
    
    def test_divide(self):
        res = calc.MyCalc.divide(self, 24, 6)
        self.assertEqual(res, '24 / 6 = 4.0')

    def test_openFile(self):
        res = calc.Logger.saveInFile(calc.Logger, 'log.txt')
        self.assertEqual(res, '<log>\n')

if __name__ == '__main__':
    unittest.main()

# Windows HotKeys
# ctrl + /              ->      comments selected code
# ctrl + alt + arrow    ->      adds cursor up/down
# alt + arrow           ->      moves line up/down
# ctrl + l              ->      selects whole line
# ctrl + c              ->      copies selected code
# ctrl + v              ->      pastes selected code
# ctrl + s              ->      saves file
# ctrl + shift + p      ->      shows all comands
# ctrl + n              ->      creates new file
# ctrl + o              ->      opens file