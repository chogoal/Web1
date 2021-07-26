from django.urls import path

from profileapp.views import ProfileCreateView

app_name = 'profileappp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create')

]