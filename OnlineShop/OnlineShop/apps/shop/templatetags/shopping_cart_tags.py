from django import template
from django.db.models import Sum

register = template.Library()

@register.filter
def cart_product_count(user):
    if user.is_authenticated:
        order = user.order_set.filter(is_paid=False).first()
        if order:
            amount = order.orderproduct_set.aggregate(Sum('amount'))['amount__sum']
            if not amount:
                return 0
            else:
                return amount
    return 0

@register.filter
def get_subtotal(order_product):
    return order_product.product.final_price * order_product.amount