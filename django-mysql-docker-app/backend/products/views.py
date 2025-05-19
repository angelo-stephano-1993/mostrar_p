from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer

class ProductoList(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)