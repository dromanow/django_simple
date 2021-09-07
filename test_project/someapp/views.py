from django.shortcuts import render
from django.views.generic.list import ListView
from .models import SomeModel


class SomeModelView(ListView):
    model = SomeModel
    template_name = 'someapp/index.html'
    # queryset = SomeModel.objects.all()

    def get_queryset(self):
        return SomeModel.objects.select_related('other').prefetch_related('other1').all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'user': {'name': 'Denis', 'age': '40'}
        })
        return context


def index(request):
    site = request.site
    return render(request, 'someapp/index.html', context={
        'user': {'name': 'Denis', 'age': '40'},
        'object_list': SomeModel.objects.all()
        # 'object_list': SomeModel.on_site.all()
    })
