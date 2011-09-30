from django.forms import ChoiceField, FileField
from django.utils.safestring import mark_safe
from django import template

register = template.Library()

@register.filter(name='field_value')
def field_value(field):
    """
     Returns the value for this BoundField, as rendered in widgets.
     """
    if field.form.is_bound:
        if isinstance(field.field, FileField) and field.data is None:
            val = field.form.initial.get(field.name, field.field.initial)
        else:
            val = field.data
    else:
        val = field.form.initial.get(field.name, field.field.initial)
        if callable(val):
            val = val()
    if val is None:
        val = ''
    return val

@register.filter(name='display_value')
def display_value(field):
    """
     Returns the displayed value for this BoundField, as rendered in widgets.
     """
    value = field_value(field)
    if isinstance(field.field, ChoiceField):
        for (val, desc) in field.field.choices:
            if val == value:
                return desc
    return value

@register.filter
def money(value, arg=None):
    try:
        tmp = "%d" % value
        newvalue = []
        while tmp:
            newvalue.insert(0, tmp[-3:])
            tmp = tmp[:-3]
        newvalue = ' '.join(newvalue)
        if arg and arg=="i":
            tmpl = "%s<sup><i>%02d</i></sup>"
        else:
            tmpl = "%s<sup>%02d</sup>"
        result =  tmpl % (newvalue, int(round((value - int(value))*100)))
        return mark_safe(result)
    except (TypeError, ValueError):
        return value