from django.shortcuts import render, get_object_or_404
from .models import Tag
from django.views import View
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
class TagViews(View):
  def get(self,request):
    all_tags = Tag.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 5)
    paginator = Paginator(all_tags, limit)
    try:
      tags = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
      tags = paginator.page(1)
    return render(request,'tags/list.html', {'all_tags': tags})

class TagDetailViews(View):
  def get(self,request,id):
    tag = get_object_or_404(Tag, id=id)
    return render(request, 'tags/show.html',{'tag':tag})
