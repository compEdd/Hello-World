import sys
from django.conf import settings
from django.conf.urls import url #patterns
from perfis.views import index
from django.http import HttpResponse
from django.core.management import execute_from_command_line

settings.configure(
	DEBUG=True,
	SECRET_KEY='1234',
	ROOT_URLCONF=sys.modules[__name__],
)

def index(request):
	return HttpResponse('Hello, world')

urlpatterns = [
	url(r'$', index, name='index'),
]

if __name__ == "__main__":
	execute_from_command_line(sys.argv)
