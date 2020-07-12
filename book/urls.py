from django.urls import path 
#from root dicrectory import vies.oy
from . import views
# all urls must be added to the urlpatterns andmust be spelled the same in main url dictory
urlpatterns =[
              path('',views.index,name='index'),

              ]