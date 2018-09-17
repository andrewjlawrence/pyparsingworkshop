"""
Example parser based on the following grammar

<sum> ::= <sum> $\mathbf{+}$ <product> | <product>

<product> ::= <product> $\mathbf{*}$ <value> | <value>

<value> ::= <int> | \textit{id}

<int> ::= <unsignedint> | $\mathbf{-}$<unsignedint>

<unsignedint> ::= <digit> | <unsignedint><digit>

<digit> ::= $\mathbf{0}$ | $\mathbf{1}$ | $\mathbf{2}$ | $\mathbf{3}$ | $\mathbf{4}$ | $\mathbf{5}$ | $\mathbf{6}$ | $\mathbf{7}$ | $\mathbf{8}$ | $\mathbf{9}$
"""

import pyparsing as pp

class Sum:
    def __init__(self, leftop, rightop):
        self.leftop = leftop
        self.rightop = rightop

    def __str__(self):
        return "< Sum leftop: {0} rightop: {1}>".format(self.leftop, self.rightop)

    __repr__ = __str__


class Product:
    def __init__(self, leftop, rightop):
        self.leftop = leftop
        self.rightop = rightop

    def __str__(self):
        return "< Product leftop: {0} rightop: {1}>".format(self.leftop, self.rightop)

    __repr__ = __str__


def to_int(num):
    return int(num[0])

unsignedint = pp.Word(pp.nums)
integer = (pp.Combine(pp.Literal("-") + unsignedint) | unsignedint).setParseAction(lambda t: int(t[0]))
id = pp.Word(pp.alphanums)
value = integer | id

product = pp.Forward()
product_list = pp.Group(value + pp.Literal("*").suppress() + product).setParseAction(lambda t: Product(t[0][0], t[0][1]))
product << (product_list | value)

sum = pp.Forward()
sum_list = pp.Group(product + pp.Literal("+").suppress() + sum).setParseAction(lambda t: Sum(t[0][0], t[0][1]))
sum << (sum_list | product)


print(sum.parseString("1+3",True))
tests = """
    1+2
    1+3+7
    -1*43
    -1+16*4
    """

sum.runTests(tests)

print(unsignedint.parseString("123"))
integer.runTests("""
        1
        -1
""")


sum.setFailAction(lambda s,loc,expr,err: print("Sum Failed"))
print(sum.parseString("* abc123"))