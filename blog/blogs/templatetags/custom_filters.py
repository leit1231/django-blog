from django import template

register = template.Library()


@register.filter
def add_class(field, class_name):
    return field.as_widget(attrs={'class': class_name})


@register.filter
def is_instance_of(view, class_name):
    from django.views.generic import View
    try:
        class_ = getattr(View, class_name)
        return isinstance(view, class_)
    except AttributeError:
        return False
