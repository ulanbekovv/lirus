from django.urls import path

from lirus.views import CategoryView, SubcategoriesView, ProductView, AboutShopView, ComplaintsAndSuggestionsView, СontactsView, FeedbackView, StockView, CardView, OfferView

urlpatterns = [
    path('category/', CategoryView.as_view({'get': 'list'})),
    path('subcategories', SubcategoriesView.as_view({'get': 'list'})),
    path('subcategories/<int:pk>/', SubcategoriesView.as_view({'get': 'retrieve'})),
    path('product/', ProductView.as_view({'get': 'list'})),
    path('product/<int:pk>/', ProductView.as_view({'get': 'retrieve'})),
    path('about_shop', AboutShopView.as_view({'get': 'list'})),
    path('about_shop/<int:pk>/', AboutShopView.as_view({'get': 'retrieve'})),
    path('complaints_and_suggestions/', ComplaintsAndSuggestionsView.as_view({'get': 'list', 'post': 'create'})),
    path('complaints_and_suggestions/<int:pk>/', ComplaintsAndSuggestionsView.as_view({'get': 'retrieve'})),
    path('contacts/', СontactsView.as_view({'get': 'list'})),
    path('contacts/<int:pk>/', СontactsView.as_view({'get': 'retrieve'})),
    path('feedback/', FeedbackView.as_view({'get': 'list', 'post': 'create'})),
    path('feedback/<int:pk>/', FeedbackView.as_view({'get': 'retrieve'})),
    path('stock/', StockView.as_view({'get': 'list'})),
    path('stock/<int:pk>/', StockView.as_view({'get': 'retrieve'})),
    path('card/', CardView.as_view({'get': 'list'})),
    path('card/<int:pk>/', CardView.as_view({'get': 'retrieve'})),
    path('offer/', OfferView.as_view({'get': 'list'})),
    path('offer/<int:pk>/', OfferView.as_view({'get': 'retrieve'})),
]
