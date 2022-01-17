from django.http import HttpResponse
from django.views import generic


class PostView(generic.View):

    def get(self, request ,*args, **kargs):
        return HttpResponse('Hello World')