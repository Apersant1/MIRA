from django.urls import path
from .views import mira

urlpatterns = {
    path('', mira)
}
