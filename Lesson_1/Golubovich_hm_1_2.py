# Golubovich Igor for Python Course | homework №1 | task №2

def mul_replace(t_sting, replace_values):
    for i, j in replace_values.items():
        t_sting = t_sting.replace(i, j)
    return t_sting

replace_values = {'Uncle Styopa': 'Yan', 'Styopa': 'Yan', 'Uncle': 'Yan'}
my_str = str(input('Enter the text about Uncle Styopa:\n'))

my_str = mul_replace(my_str, replace_values)
print(my_str)