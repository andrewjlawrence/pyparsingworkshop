
import pyparsing as pp


print(pp.Keyword("if").parseString("if (1 + 1 = 2)"))

print(pp.Keyword("if").parseString("ifAndOnlyIf"))
