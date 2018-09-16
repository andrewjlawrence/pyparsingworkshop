
import pyparsing as pp

sum = pp.infixNotation(pp.Word(pp.nums), [
     ("-", 1, pp.opAssoc.RIGHT),
     ("*", 2, pp.opAssoc.LEFT),
     ("+", 2, pp.opAssoc.LEFT),
    ])

sum.parseString("1*2")
tests = """
    1+2
    1+3+7
    -1*43
    -1+16*4
    """

sum.runTests(tests)
