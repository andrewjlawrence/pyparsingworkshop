import pyparsing as pp

number = pp.Word(pp.nums) ^ pp.Combine(pp.Word(pp.nums) + '.' + pp.Word(pp.nums))
print(number.searchString("123 3.1416 789"))