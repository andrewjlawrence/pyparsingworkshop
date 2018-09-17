import pyparsing as pp

@pp.traceParseAction
def dummyAction(toks):
     return None

unsignedint = pp.Word(pp.nums).setParseAction(dummyAction)

unsignedint.runTests("""
        1
""")

