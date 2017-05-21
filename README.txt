This is a simple module for making a large text based version of a word/letter/phrase

I am currently working on a way to make the external database of letters unnecessary.

Below demonstrates what the file "big_letters.py" will do when run
====================================================================
Input a word/phrase/letter composed of the characters:
ABCDEFGHIJKLMNOPQRSTUVWXYZ and space " "
Input a word/phrase/letter: FOO
===================
XXXXX   XXX    XXX
X      X   X  X   X
XXXXX  X   X  X   X
X      X   X  X   X
X       XXX    XXX

===================
do again? (y -> continue, else -> quit): y
Input a word/phrase/letter composed of the characters:
ABCDEFGHIJKLMNOPQRSTUVWXYZ and space " "
Input a word/phrase/letter: BAR
===================
XXX     XXX   XXXX
X  X   X   X  X   X
XXXX   XXXXX  XXXX
X   X  X   X  X   X
XXXX   X   X  X   X

===================
do again? (y -> continue, else -> quit): y
Input a word/phrase/letter composed of the characters:
ABCDEFGHIJKLMNOPQRSTUVWXYZ and space " "
Input a word/phrase/letter: FOO BAR
===============================================
XXXXX   XXX    XXX          XXX     XXX   XXXX
X      X   X  X   X         X  X   X   X  X   X
XXXXX  X   X  X   X         XXXX   XXXXX  XXXX
X      X   X  X   X         X   X  X   X  X   X
X       XXX    XXX          XXXX   X   X  X   X

===============================================
do again? (y -> continue, else -> quit): i'm done
Enter to Exit