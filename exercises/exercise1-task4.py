
"""
<diceroll> ::= <numdice>"d"<numsides> 
"""

import pyparsing as pp

# Fill out the roll function below
def roll(numsides, numdice):
  pass

numdice = pp.Word(pp.nums)
numsides = pp.Word(pp.nums)
diceroll =  numdice("Number of dice") + pp.Literal("d").suppress() + numsides("Number of sides")

# Set the diceroll parse action to call roll.


diceroll.runTests("""
        2d6
        10d4
""")

