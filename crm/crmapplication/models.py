from django.db import models
# from six import python_2_unicode_compatible
# @python_2_unicode_compatibl


class Client(models.Model):
    first_name = models.fields.CharField(max_length=25)
    last_name = models.fields.CharField(max_length=25)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.fields.CharField(max_length=20)
    mobile = models.fields.CharField(max_length=20)
    company_name = models.fields.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(to=Sales, on_delete=models.CASCADE)


class Event(models.Model):
    TYPE_CHOICES = (
        ('1', 'En cours'),
        ('2', 'Cloturé'),
    )
    client= models.ForeignKey(to=Client, on_delete=models.CASCADE)
    Support_contact = models.ForeignKey(to=Support, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_status = models.IntegerField(choices=TYPE_CHOICES)
    attendees = models.IntegerField(blank=True)
    event_date = models.DateTimeField(auto_now=True)
    notes = models.TextField(max_length=200, blank=True)



class Contract(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    Sales_contact = models.ForeignKey(to=Sales, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(blank=True)
    amount = models.FloatField(blank=True)
    payment_due = models.DateTimeField(auto_now_add=True)

class Sales(models.Model):
    Sales_contact = models.IntegerField(blank=True)


class Support(models.Model):
    Support_contact = models.IntegerField(blank=True)

