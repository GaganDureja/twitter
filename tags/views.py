from django.shortcuts import render, get_object_or_404
from .models import Tag
from django.views import View

# Create your views here.
class TagViews(View):
  def get(self,request):
    all_tags = Tag.objects.all().order_by('-id')
    return render(request,'tags/list.html', {'all_tags': all_tags})

class TagDetailViews(View):
  def get(self,request,id):
    tag = get_object_or_404(Tag, id=id)
    return render(request, 'tags/show.html',{'tag':tag})
