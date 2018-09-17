
import pyparsing as pp

unsignedint = pp.Word(pp.nums)
integer =  pp.Combine(pp.Literal("-") + unsignedint).setResultsName("integer") \
           | unsignedint("unsigned integer")

integer.setDebug(True)
integer.runTests("""
        1
        -1
""")

