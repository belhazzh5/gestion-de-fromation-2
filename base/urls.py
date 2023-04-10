from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import FormationListView,dash,FormationDetailView,join_formation,leave_formation
urlpatterns = [
    path("",FormationListView.as_view(),name="home"),
    path("<slug:slug>/",FormationDetailView.as_view(),name="formation"),
    path("dash/",dash,name="dash"),
    path('leave/<slug:slug>/',leave_formation, name='leave_formation'),
    path('join/<slug:slug>/',join_formation, name='join_formation'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
