
"""
<diceroll> ::= <numdice>"d"<numsides>
"""

import pyparsing as pp

def roll(numsides, numdice):
    import random
    sum = 0
    for x in range(numdice):
        sum += random.randint(1, numsides)
    return sum

# Add your solution below
numdice = pp.Word(pp.nums)
numsides = pp.Word(pp.nums)
diceroll = (numdice("Number of dice") + pp.Literal("d").suppress() + numsides("Number of sides"))
diceroll.setParseAction(lambda t: roll(int(t[0]),int(t[1])))

diceroll.runTests("""
        2d6
        10d4
""")

