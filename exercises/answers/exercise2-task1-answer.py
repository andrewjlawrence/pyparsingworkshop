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
