from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
from . import views
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    RexineView,
    PuFoamView, 
    AdhesiveView,
    EpeSheetView,
    EpeRollView,
    NonWovenView,
    PowermaxView,
    AboutView,
    emailView,
    successView
    
    
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', emailView, name='email'),
    path('success/', successView, name='success'),
    path('pufoam-page/', PuFoamView.as_view(), name='pufoam-page'),
    path('adhesive-page/', AdhesiveView.as_view(), name='adhesive-page'),
    path('epesheet-page/', EpeSheetView.as_view(), name='epesheet-page'),
    path('eperoll-page/', EpeRollView.as_view(), name='eperoll-page'),
    path('nonwoven-page/', NonWovenView.as_view(), name='nonwoven-page'),
    path('powermax-page/', PowermaxView.as_view(), name='powermax-page'),
    path('rexine-page/', RexineView.as_view(), name='rexine-page'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
