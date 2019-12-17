from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product, OrderProduct, Order, Review

# Create your views here.

class shop_view(ListView):
    model = Product
    paginate_by = 8
    template_name = 'shop.html'

    def get_queryset(self):
        category = self.request.GET.get('category', 'All')
        sort_order = self.request.GET.get('orderby', 'title')

        if category == 'All':
            return Product.objects.all().order_by(sort_order)
        else:
            return Product.objects.filter(category=category).order_by(sort_order)

    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['categories'] = [("All", "All")]
        context['categories'].extend(Product.PRODUCT_CATEGORY)
        context['current_category'] = self.request.GET.get('category', 'All')

        context['sort_orders'] = [
            ('title', 'Title'),
            ('category', 'Category'),
            ('final_price', 'Price'),
            ('rating', 'Rating')
        ]
        context['current_sort_order'] = self.request.GET.get('orderby', 'title')
        return context

class product_view(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['reviews'] = Review.objects.filter(product=self.object)
        return context

@login_required
def add_to_cart_view(request, slug):
    product_to_be_added = get_object_or_404(Product, slug=slug)

    order = Order.objects.filter(user=request.user, is_paid=False).first()
    if order:
        order_product = order.orderproduct_set.filter(order=order, product=product_to_be_added).first()
        if order_product:
            order_product.amount += 1
            order_product.save()
        else:
            order_product = OrderProduct.objects.create(order=order, product=product_to_be_added, amount=1)
    else:
        order = Order.objects.create(user=request.user, is_paid=False)
        order_product = OrderProduct.objects.create(order=order, product=product_to_be_added, amount=1)

    order_product.save()
    messages.info(request, 'This product was added to your cart!')
    return redirect('shop')

@login_required
def cart_screen_view(request):
    context = {
        'cart_products': []
    }

    order = request.user.order_set.filter(is_paid=False).first()
    if order:
        cart_products = order.orderproduct_set.all()
    else:
        cart_products = OrderProduct.objects.none()

    for order_product in cart_products:
        cart_products_with_subtotal = \
        {
            'order_product': order_product,
            'subtotal': order_product.amount * order_product.product.final_price
        }
        context['cart_products'].append(cart_products_with_subtotal)

    total = 0
    for cart_product in context['cart_products']:
        total += cart_product['subtotal']
    context['total'] = total

    return render(request, 'shopping_cart.html', context)

@login_required
def remove_from_cart(request, slug):
    OrderProduct.objects.filter\
    (
        product__slug=slug,
        order__is_paid=False,
        order__user=request.user
    ).delete()
    return redirect('shopping_cart')