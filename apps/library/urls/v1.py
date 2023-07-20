from django.urls import path, include

from apps.library.views.v1 import BookAPIView, ModifyBookAPIView

urlpatterns = [
    path('', include([
        path('', BookAPIView.as_view(), name='book'),
        path('actions/', ModifyBookAPIView.as_view(), name='book actions')
    ]))
]
