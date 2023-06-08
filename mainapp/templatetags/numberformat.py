from django import template

register = template.Library()


@register.filter()
def formatize(val):
    try:
        if val is not None:
            val = float(val)
            return f'{val:,.2f}'

        return val
    except Exception:
        return val



@register.filter()
def show_title(val1, val2):
    return val1[:int(val2)]