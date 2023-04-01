from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import FormationListView,dash,FormationDetailView
urlpatterns = [
    path("",FormationListView.as_view(),name="home"),
    path("<slug:slug>/",FormationDetailView.as_view(),name="formation"),
    path("dash/",dash,name="dash"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
