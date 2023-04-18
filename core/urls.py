from captcha import fields
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


class LoginForm(AuthenticationForm):
    captcha = fields.ReCaptchaField()

    def clean(self):
        captcha = self.cleaned_data.get("captcha")
        if not captcha:
            return
        return super().clean()


admin.site.login_form = LoginForm
admin.site.login_template = "login.html"

schema_view = get_schema_view(
    openapi.Info(
        title="HR Management API",
        default_version="v1",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("apps.users.urls", namespace="accounts")),
]

swagger_patterns = [
    re_path(r"^doc(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("doc/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns += swagger_patterns
