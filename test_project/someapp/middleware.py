from .models import HitCount


class PathCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        hc, created = HitCount.objects.get_or_create(url=request.path)
        hc.hits += 1
        hc.save()
        response = self.get_response(request)
        return response
