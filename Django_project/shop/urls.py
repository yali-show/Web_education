from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from items.urls import urlpatterns as items_urlpatterns
from feedbacks.urls import urlpatterns as feedbacks_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(items_urlpatterns)),
    path('', include(feedbacks_urlpatterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
