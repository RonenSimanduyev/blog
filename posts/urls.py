from django.urls import path
from . import views

urlpatterns =[
    path('add',views.add,name='add'),
    path('edit/<str:id>',views.edit,name='edit'),
    path('remove/<str:id>',views.remove,name='remove'),
    path('',views.all ,name='all')



]