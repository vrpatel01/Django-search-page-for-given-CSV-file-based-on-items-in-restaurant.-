from django.views.generic import TemplateView, ListView

# from .models import City


class HomePageView(TemplateView):
    template_name = 'search/home.html'

class SearchResultsView(ListView):
    # model = City
    template_name = 'search/search_results.html'