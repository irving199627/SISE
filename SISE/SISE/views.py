from django.views.generic import TemplateView

class PaginaPrincipal(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_name = 'test.html'

class verPost(TemplateView):
    template_name = "post/post_list.html"
