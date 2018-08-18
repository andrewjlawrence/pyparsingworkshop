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

unsignedint = pp.Word(pp.nums)
integer = pp.Combine(pp.Literal("-") + unsignedint) | unsignedint
id = pp.Word(pp.alphanums)
value = integer | id

product = pp.Forward()
product_list = value + pp.Literal("*") + product
product << (product_list | value)

sum = pp.Forward()
sum_list = product + pp.Literal("+") + sum
sum << (sum_list | product)


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

