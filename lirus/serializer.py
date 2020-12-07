from rest_framework import serializers

from lirus.models import Category, Subcategories, Product, ProductImage, AboutShop, ComplaintsAndSuggestions, Сontacts, Feedback, Stock, News, Offer, Card

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('picture', 'id')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'id')

class SubcategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategories
        fields = ('name', 'category', 'id')

class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        
class AboutShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutShop
        fields = ('name', 'description', 'id')

class ComplaintsAndSuggestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintsAndSuggestions
        fields = ('name', 'phone_number', 'message', 'id')

class СontactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Сontacts
        fields = ('address', 'phone_number', 'whatsapp', 'email', 'instagram','instagram1', 'instagram2', 'id')

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'phone_number', 'message', 'id')

class StockSerializer(serializers.ModelSerializer):
    publish = serializers.DateTimeField(format="%d:%m:%Y-%H:%M:%S")

    class Meta:
        model = Stock
        fields = ('name', 'text', 'publish','id')

class NewsSerializer(serializers.ModelSerializer):
    publish = serializers.DateTimeField(format="%d:%m:%Y-%H:%M:%S")

    class Meta:
        model = News
        fields = ('name', 'text', 'publish','id')

class OfferSerializer(serializers.ModelSerializer):
    publish = serializers.DateTimeField(format="%d:%m:%Y-%H:%M:%S")

    class Meta:
        model = Offer
        fields = ('name', 'text', 'publish','id')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('number_card', 'balance', 'discount', 'id')