
import pyparsing as pp

unsignedint = pp.Word(pp.nums)

# We expect this parser to match unsigned ints
print(unsignedint.parseString("123"))

# but not strings
# print(unsignedint.parseString("abc"))

integer =  pp.Combine(pp.Literal("-") + unsignedint) \
           | unsignedint

integer.runTests("""
        1
        -1
""")

