from django.urls import path

from app1.views import *

app_name='something'

urlpatterns=[
    path('dhoni/',dhoni, name='dhoni'),
    path('pandya/',pandya, name='pandya'),
]


