from .models import VisitorTag

def visitor_tags_loader(request):
	visitor_tags = VisitorTag.objects.all()
	return {'visitor_tags': visitor_tags}