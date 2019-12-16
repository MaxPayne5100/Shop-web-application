from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product

# Create your views here.

def products_view(request):
    context = {}
    context["products"] = Product.objects.all()
    return render(request, 'shop.html', context)

class shop_view(ListView):
    model = Product
    paginate_by = 4
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
