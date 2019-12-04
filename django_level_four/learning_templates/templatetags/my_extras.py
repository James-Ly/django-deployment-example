from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg, '')


'''
Register the function
The first one is the string to call the function in template tag, the second is the name of the function
This one can be replace by the decorator @register.filter(name='cut')
'''
# register.filter('cut', cut)