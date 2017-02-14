from django.template import Library

register = Library()

@register.inclusion_tag('core/pagination.html')
def pagination(request, paginator, current_page):
  context = {
   'paginator': paginator,
   'request': request,
   'page_obj': current_page
  }
  getvars = request.GET.copy()
  if 'page' in getvars:
    del getvars['page']
  if len(getvars) > 0:
    context['getvars'] = '&{0}'.format(getvars.urlencode())
  return context
