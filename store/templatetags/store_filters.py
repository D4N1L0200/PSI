from django import template  # type: ignore

register = template.Library()


@register.filter
def replace(value, args):
    try:
        old, new = args.split("|")
        return str(value).replace(old, new)
    except Exception:
        return value
