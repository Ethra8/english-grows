import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from individual_services.models import IndivService
# from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    # def update_total(self):
    #     """
    #     Update grand total each time a line item is added,
    #     accounting for delivery costs.
    #     """
    #     self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
    #     self.grand_total = self.order_total
    #     self.save()

    # def save(self, *args, **kwargs):
    #     """
    #     Override the original save method to set the order number
    #     if it hasn't been set already.
    #     """
    #         # self.update_total()
    #         # if not self.order_number:
    #         #     self.order_number = self._generate_order_number()
    #         # super().save(*args, **kwargs)
    #     if not self.pk:
    #         super().save(*args, **kwargs)
    #     if not self.order_number:
    #         self.order_number = self._generate_order_number()
    #     super().save(*args, **kwargs)
    #     self.update_total()

    def update_total(self):
        """
        Update grand total each time a line item is added.
        """
        order_total_sum = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        print(f"Calculated order total: {order_total_sum}")
        
        self.order_total = order_total_sum
        self.grand_total = self.order_total  # Adjust this if needed
        print(f"Updated order_total: {self.order_total}, grand_total: {self.grand_total}")

        # self.save()
        print("Order saved with updated totals")

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        
        if not self.pk:
            super().save(*args, **kwargs)
        if not self.order_number:
            self.order_number = self._generate_order_number()
        self.update_total(*args, **kwargs)
        # self.save()
        super().save(*args, **kwargs)

    def __str__(self):
        
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    service = models.ForeignKey(IndivService, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.service.price * self.quantity
        super().save(*args, **kwargs)