from django.views.generic import ListView, TemplateView
from .models import Restaurant
from django.shortcuts import render
from django.db.models import Q

class SearchResultsView(ListView):
    model = Restaurant
    template_name = 'search/search_results.html'

    def post(self, request, *args, **kwargs):
        query = request.POST.get('q','')        
        if query:
            queryset = (Q(items__icontains=query))
            results = Restaurant.objects.filter(queryset).distinct()
        else:
            results = []
        return render(request, self.template_name, {'object_list':results, 'query':query})

    def get(self,request):
        return render(request,'search/home.html')


class HomePageView(TemplateView):
    template_name = 'search/home.html'

