from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from lirus.models import Category, Subcategories, Product, AboutShop, ComplaintsAndSuggestions, Сontacts, Feedback, Stock, Card, Offer
from lirus.serializer import CategorySerializer, SubcategoriesSerializer, ProductSerializer, AboutShopSerializer, ComplaintsAndSuggestionsSerializer, СontactsSerializer, FeedbackSerializer, StockSerializer, CardSerializer, OfferSerializer

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]

class SubcategoriesView(ModelViewSet):
    queryset = Subcategories.objects.all()
    serializer_class = SubcategoriesSerializer
    lookup_field = 'pk'

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ('title', 'price', 'the_size')

    def get_queryset(self):
        queryset = Product.objects.all()
        order_field = self.request.GET.get('order')
        filter_fields = {}

        if self .request.GET.get('price'):
            filter_fields['price'] = self .request.GET.get('price')     
            
        if self .request.GET.get('the_size'):
            filter_fields['the_size'] = self .request.GET.get('the_size')          

        if order_field:
            queryset = queryset.order_by(order_field)

        if filter_fields:
            queryset = queryset.filter(**filter_fields)

        return queryset

class AboutShopView(ModelViewSet):
    queryset = AboutShop.objects.all()
    serializer_class = AboutShopSerializer
    lookup_field = 'pk'

class ComplaintsAndSuggestionsView(ModelViewSet):
    queryset = ComplaintsAndSuggestions.objects.all()
    serializer_class = ComplaintsAndSuggestionsSerializer
    lookup_field = 'pk'

class СontactsView(ModelViewSet):
    queryset = Сontacts.objects.all()
    serializer_class = СontactsSerializer
    lookup_field = 'pk'

class FeedbackView(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    lookup_field = 'pk'

class StockView(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'pk'

class CardView(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    lookup_field = 'pk'

class OfferView(ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    lookup_field = 'pk'