import pyparsing as pp

animal_type = pp.oneOf("CAT DOG HORSE FISH RAT")
type_attr = pp.Suppress("type:") + animal_type("type")

name = pp.Word(pp.alphas)
name_attr = pp.Literal("name:").suppress() + name("pet name")

pet_spec = name_attr + "," + type_attr

pets_dict = pp.Dict(pp.OneOrMore(pp.Group(pet_spec)))

pets_dict.runTests("""
    name: Brian , type: DOG \
    name: Tom , type: CAT 
""")

print(pets_dict.parseString("""
    name: Brian , type: DOG \
    name: Tom , type: CAT 
""").asDict())