from django import template
from django.template.defaultfilters import stringfilter

import markdown as md
from markdown2 import Markdown

register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
	return md.markdown(value, extensions=['markdown.extensions.fenced_code'])

@register.filter()
@stringfilter
def markdowns(value):
	markdowner = Markdown()
	return markdowner.convert(value)