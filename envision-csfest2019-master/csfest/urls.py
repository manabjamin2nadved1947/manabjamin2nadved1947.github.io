from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('events/', views.EventListView.as_view(),name='events'),
	path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
	path('register/',views.register, name='register'),
	path('profile/<int:pk>',views.ProfileDetailView.as_view(),name='profile'),
	path('participants/', views.ParticipantListView.as_view(),name='participants'),
	path('participant/<int:pk>', views.ParticipantDetailView.as_view(), name='participant-detail'),
	path('contacts/',views.contacts, name='contacts'),
	path('workforce/',views.workforce,name='workforce'),
	path('reach/',views.reach,name='reach'),
]

urlpatterns += [  
    path('participant/create/', views.ParticipantCreate.as_view(), name='participant_create'),
    path('participant/<int:pk>/update/', views.ParticipantUpdate.as_view(), name='participant_update'),
    path('participant/<int:pk>/delete/', views.ParticipantDelete.as_view(), name='participant_delete'),
]