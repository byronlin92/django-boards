from django import template
register = template.Library()


# Documentation: {{ form.username|field_type }} will return 'TextInput'
@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__

# Documentation: {{ form.username|input_class }}
#
# <!-- if the form is not bound, it will simply return: -->
# 'form-control '
#
# <!-- if the form is bound and valid: -->
# 'form-control is-valid'
#
# <!-- if the form is bound and invalid: -->
# 'form-control is-invalid'
@register.filter
def input_class(bound_field):
    css_class=''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class='is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class='is-valid'
    return 'form-control {}'.format(css_class)
