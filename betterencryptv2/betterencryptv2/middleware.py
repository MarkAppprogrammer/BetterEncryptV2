from __future__ import annotations

from django.conf import settings


class DisableStaticCachingMiddleware:
    """
    In development, browsers will often revalidate static assets and Django will
    respond with 304 Not Modified. That's normal, but can look like an "error".

    This middleware disables caching for /static/ responses in DEBUG to force 200s.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if settings.DEBUG and request.path.startswith("/static/"):
            response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
            response.headers["Pragma"] = "no-cache"
            response.headers["Expires"] = "0"
            response.headers.pop("ETag", None)
            response.headers.pop("Last-Modified", None)

        return response

