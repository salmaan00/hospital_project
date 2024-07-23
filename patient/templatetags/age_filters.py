import datetime
from django import template

register = template.Library()

@register.filter
def calculate_age(birthdate):
    if not birthdate:
        return ""
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
