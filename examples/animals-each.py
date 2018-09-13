import pyparsing as pp

animal_type = pp.oneOf("CAT DOG HORSE FISH RAT")
type_attr = "type:" + animal_type("type")

name = pp.Word(pp.alphas)
name_attr = "name:" + name("pet name")

pet_spec = name_attr & type_attr

pet_spec.runTests('''
    name: Brian type: DOG
    type: CAT name: Tom
    '''
                    )