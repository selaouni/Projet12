from django.db import models

# from six import python_2_unicode_compatible
# @python_2_unicode_compatibl

class Support(models.Model):
    support_id = models.IntegerField(blank=True)
    contact = models.IntegerField(blank=True)
    first_name = models.fields.CharField(max_length=25)
    last_name = models.fields.CharField(max_length=25)

class Event_status(models.Model):
    event_status_id = models.IntegerField(blank=True)
    Event_status = models.IntegerField(blank=True)

class Client(models.Model):
    client_id = models.IntegerField(blank=True)
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
    event_id = models.IntegerField(blank=True)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    Support_contact = models.ForeignKey(to=Support, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_status = models.ForeignKey(to=Event_status, on_delete=models.CASCADE)
    attendees = models.IntegerField(blank=True)
    event_date = models.DateTimeField(auto_now=True)
    notes = models.TextField(max_length=200, blank=True)

class Sales(models.Model):
    sales_id = models.IntegerField(blank=True)
    contact = models.IntegerField(blank=True)
    first_name = models.fields.CharField(max_length=25)
    last_name = models.fields.CharField(max_length=25)
class Contract(models.Model):
    contract_id = models.IntegerField(blank=True)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    Sales_contact = models.ForeignKey(to=Sales, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(blank=True)
    amount = models.FloatField(blank=True)
    payment_due = models.DateTimeField(auto_now_add=True)





