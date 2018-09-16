
import pyparsing as pp

digit = pp.Word(pp.nums, exact=1)
digit2 = pp.Word(pp.nums, min=1, max=1)

digit.runTests("""
        123
        4
""")

digit2.runTests("""
        123
        4
""")
