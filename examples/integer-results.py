
import pyparsing as pp

unsignedint = pp.Word(pp.nums).setResultsName('Unsigned Integer')

unsignedint.runTests("""
        1
""")

