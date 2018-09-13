#
# White space example
#
import pyparsing as pp

### Newline is consumed below
print(pp.OneOrMore(pp.Word(pp.nums)).parseString("100\n00"))

### Set the default white space characters so newline is not consumed
pp.ParserElement.setDefaultWhitespaceChars("\t")
print(pp.OneOrMore(pp.Word(pp.nums)).parseString("100\n00"))
