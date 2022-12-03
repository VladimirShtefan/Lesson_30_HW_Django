from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from ad.serializers import AdListSerializer, AdPostSerializer, AdPatchSerializer, AdDestroySerializer
from ad.serializers import Ad


def index(request):
    if request.method == 'GET':
        return JsonResponse({"status": "ok"}, status=200)


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def get(self, request, *args, **kwargs):
        search_query = None
        params = {
            'cat': 'category__id__exact',
            'text': 'name__icontains',
            'location': 'author__location__name__icontains',
            'price_from': 'price__gte',
            'price_to': 'price__lte',
        }
        for param, value in dict(request.GET).items():
            data_filter = params.get(param, None)
            if data_filter:
                temp_dict = {data_filter: value[0]}
                if search_query is None:
                    search_query = Q(**temp_dict)
                else:
                    search_query |= Q(**temp_dict)
        if search_query:
            self.queryset = self.queryset.select_related('author').prefetch_related('category').filter(search_query).\
                order_by('-price')
        return super(AdListView, self).get(request, *args, **kwargs)


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdPostSerializer


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdPatchSerializer


@method_decorator(csrf_exempt, name="dispatch")
class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
