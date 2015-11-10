from django.conf.urls import include, url
from api.views import ListCreateTodos, DetailUpdateTodo

urlpatterns = [
    url('^todos/(?P<pk>\d+)/?', DetailUpdateTodo.as_view()),
    url('^todos/', ListCreateTodos.as_view()),

]