from django import template
from contact.models import About, Social

register = template.Library()

@register.simple_tag()
def get_social_links():
    return Social.objects.all()

@register.simple_tag()
def get_about():
    return About.objects.last()