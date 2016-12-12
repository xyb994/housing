from django import template

register = template.Library()

@register.filter
def removeUnderscore(word):
    formatedLabelText = word.title().replace("_", " ")
    return formatedLabelText

# @register.filter
# def addCss(field, css):
#     return field.as_widget(attrs={"class":css})

@register.filter(name='add_attributes')
def add_attributes(field, css):
    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            t, v = d.split(':')
            attrs[t] = v

    return field.as_widget(attrs=attrs)
