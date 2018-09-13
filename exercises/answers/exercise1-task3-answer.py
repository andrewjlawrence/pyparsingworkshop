
"""
<diceroll> ::= <numdice>"d"<numsides> 
"""

import pyparsing as pp

# Add your solution below

numdice = pp.Word(pp.nums)
numsides = pp.Word(pp.nums)
diceroll =  numdice("Number of dice") + pp.Literal("d").suppress() + numsides("Number of sides")

diceroll.runTests("""
        2d6
        10d4
""")

