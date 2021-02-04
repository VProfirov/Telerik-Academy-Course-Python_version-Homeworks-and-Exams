multilineVar = """line1
line2
line3"""
print(multilineVar)
"""
This seems to be a multi
line comment since it is literal string not assigned to any variableiable
and will be skipped by the interpreter
"""
print("hi...")

# someInput_withPrompt = input("Insert and integer: ")
# print(someInput_withPrompt + "of type: " + type(someInput_withPrompt))
variable = 5
print(str(variable) + " of type: " + str(type(variable)))
print(type(variable))
print(variable + variable)
print("some str", "some string literal", sep=" ")


# LITERAL INTERPOLATION
fn = 'Pesho'
ln = 'Goshev'
print(f'Hello {fn} {ln}! Nice to meet you, {fn}!')

# NOTE: Descriptive NOTATIONS

# FIXME: 
# NOTE:
# TODO:
# REVIEW:

from package01 import module01_aka_filename_with_no_dotPY as shorter_name_OR_nonConflicting_alias