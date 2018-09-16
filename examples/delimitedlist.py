import pyparsing as pp

print(pp.delimitedList(pp.Word(pp.nums), ',').parseString("1,2,3"))