from django.views.generic import TodayArchiveView


class HomePageView(TemplateView):
    template_name = 'home.html'

