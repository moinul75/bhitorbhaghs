from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    # Ensure the field is an instance of a Django form field
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={'class': css_class})
    return field  # Fallback if field doesn't have 'as_widget'