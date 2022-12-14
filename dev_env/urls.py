from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from dev_env.settings import GRAPHENE_SUPPORT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_ledger.urls', namespace='django_ledger')),
]

try:
    if GRAPHENE_SUPPORT:
        # checking for graphene_django installation to provide and enable graphql services...
        from graphene_django.views import GraphQLView
        from django_ledger.contrib.django_ledger_graphene.api import schema

        urlpatterns += [
            path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)))
        ]
except ImportError:
    pass
