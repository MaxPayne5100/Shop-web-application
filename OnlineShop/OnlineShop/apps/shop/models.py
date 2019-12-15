import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# Create your models here.

class Product(models.Model):
    PRODUCT_CATEGORY = (
        ('VEGETABLES', 'Vegetables'),
        ('FRUITS', 'Fruits'),
        ('JUICE', 'Juice'),
        ('DRIED', 'Dried'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=15, choices=PRODUCT_CATEGORY)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    rating = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
    )

    def __str__(self):
        return self.title


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ship_to = models.CharField(max_length=255)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


class ProductOrderTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    amount = models.PositiveIntegerField()

    def get_full_price(self):
        return self.amount * self.product.price

    def __str__(self):
        return f'{self.order} : {self.product} - {self.amount}'
