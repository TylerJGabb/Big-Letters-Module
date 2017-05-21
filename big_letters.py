##All letters will be 5x5 matrix of positions, which
##will be populated with # to be part of a letter
'''
For Example:

the letter E

  1> #####  
  2> #
  3> #####  
  4> #
  5> #####  
     ^^^^^
     12345
        
     
Would be represented as the list of coordinates:

[(1,1),(1,2),(1,3),(1,4),(1,5),
(2,1),
(3,1),(3,2),(3,3),(3,4),(3,5),
(4,1),
(5,1),(5,2),(5,3),(5,4),(5,5)]   
'''
##MINUS ONE FROM ALL OF THAT....
import sys
import string
class BL: #BL stands for Big Letter
    SPACE = [[' ']*2]*5
    def __init__(self,letter = None):
        self.grid = [[' ' for i in range(5)]for j in range(5)] ##IS DEEP COPY
        self.letter = letter
        self.textual = self.to_text() if letter else None
        
    def to_text(self):
        #returns a list of lines, representative of the letters textual
        #form, line by line
        tuples = Input.letter_dict[self.letter]
        for tuple in tuples:
            x = tuple[0]
            y = tuple[1]
            self.grid[x][y] = 'X'
        lines = [''.join(peice) for peice in self.grid]
        return lines
        
    def __add__(self,other):
        T1 = self.textual
        T2 = other.textual
        new_text = [T1[i] + '  ' + T2[i] for i in range(5)]
        NEW = BL()
        NEW.textual = new_text
        return NEW
        
    def __repr__(self):
        ret = ''
        for line in self.textual:
            ret += line + '\n'
        return ret
        
    @classmethod
    def string_to_bigletter(cls,s):
        big_letter_list = [BL(x) for x in s]
        return sumList(big_letter_list)    
            
        


class Input:
    letter_dict = {}
    letter_dict[' '] = []   
    @classmethod
    def read_file_populate_letter_dict(cls):
        file = open('letters_DB.txt','r')
        line_num = 0
        for line in file:
            line_num += 1
            if not line.strip() or line.strip()[0] == '#': continue
            data = line.strip().split(':')
            assert len(data) == 6, 'INVALID ENTRY: Line '+str(line_num)+' in DB file'
            letter = data[0]
            sequences = [x.split(',') for x in data[1:]]
            sequences = [[int(x) for x in subseq if x != ''] for subseq in sequences]   
            
            tooples = [(a,b) for a in [0,1,2,3,4] for b in sequences[a]]
            cls.letter_dict[letter] = tooples
        file.close()
    
    @classmethod
    def get_sentence(cls):
        print('Input a word/phrase/letter composed of the characters:')
        print(string.ascii_uppercase,'and space " "')
        correct_input = False
        while not correct_input:
            s = input('Input a word/phrase/letter: ')
            try:
                for x in s:
                    assert x in string.ascii_uppercase + ' '
                assert bool(s)
            except AssertionError:
                if s:
                    print('INVALID CHARACTER GIVEN:',x) 
                else:
                    print('PLEASE GIVE NONEMPTY STRING')
                continue
            correct_input = True
        cls.sentence = s
        
        
def sumList(L):
    return L[0] + sumList(L[1:]) if len(L) > 1 else L[0]
    
 
def main():
    try:
        Input.read_file_populate_letter_dict()
    except FileNotFoundError:
        print('MISING FILES ERROR:')
        print('make sure you have "letters_DB.txt" in your directory')
        input('Enter to Exit')
        sys.exit(1)
        
    q = 'y'
    while q == 'y':
        Input.get_sentence()
        big_sentence = BL.string_to_bigletter(Input.sentence)
        x = len(big_sentence.textual[0])
        print('='*x)
        print(big_sentence)
        print('='*x)
        q = input('do again? (y -> continue, else -> quit): ')
    input('Enter to Exit')
    sys.exit(1)
main()
