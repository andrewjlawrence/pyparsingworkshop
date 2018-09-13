#
# JSON Parser exercise
#

import pyparsing as pp

string = pp.Literal("\"").suppress() + pp.Word(pp.alphanums) + pp.Literal("\"").suppress()

string.runTests("""
        \"meh\"
""")

#
# It is also possible to use the quoted string class
#
string2 = pp.QuotedString('"', unquoteResults=True)
string2.runTests("""
        \"meh\"
""")


"""
<number> ::= <int> <frac>

<int> ::=  <digit> | <onenine> <digits> | - <digit> | - <onenine><digits>

<frac> ::= "" | . <digits>

<digits> ::= <digit> | <digit> <digits>

<digit> ::= 0 | <onenine>

<onenine> ::= 1-9
"""

def build_num(strnum):
    if "." in strnum:
        return float(strnum)
    else:
        return int(strnum)

onenine = pp.Word("123456789", exact=1)
digit = pp.Word(pp.nums, exact=1)
digits = pp.Word(pp.nums)
fraction = pp.Literal(".") + digits
integer = pp.Combine(onenine + digits) | digit
number = pp.Combine(pp.Optional(pp.Literal("-")) + integer + pp.Optional(fraction)).setParseAction(lambda t: build_num(t[0]))

number.runTests(
    """
    1
    1.0
    0.1
    911
    01.0
    -119
    """
)
class Null:
    def __init__(self):
        pass

    def __str__(self):
      return "<json null>"

    __repr__ = __str__

array = pp.Forward()
jobject = pp.Forward()
true = pp.Keyword("true").setParseAction(lambda t: True)
false = pp.Keyword("false").setParseAction(lambda t: False)
null = pp.Keyword("null").setParseAction(Null)
value = number("number") | string("string") | array("array") | jobject("object") | true("true") \
        | false("false") | null("null")

value.runTests("""
    true
    false
    null
    1.0
    \"meh\"
""")

LEFT_SBRACK = pp.Suppress("[")
RIGHT_SBRACK = pp.Suppress("]")
array << (pp.Group(LEFT_SBRACK + pp.delimitedList(value) + RIGHT_SBRACK) | pp.Group(LEFT_SBRACK + RIGHT_SBRACK))
array.setResultsName("array")

array.runTests("""
    [ \" meh \" , 1.0 , true , false , null ]
    []
""")
