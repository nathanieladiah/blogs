from .models import TechTag 

def tech_tags_loader(request):
	tech_tags = TechTag.objects.all()
	return {'tech_tags': tech_tags}
