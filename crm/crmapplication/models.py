from django.db import models
from django.conf import settings
# from six import python_2_unicode_compatible
# @python_2_unicode_compatible


class Support(models.Model):
    support_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact = models.IntegerField(blank=True)
    first_name = models.fields.CharField(max_length=25)
    last_name = models.fields.CharField(max_length=25)

    # class Meta:
    #     db_table = 'support'
    #     verbose_name = 'Support'

class Sales(models.Model):
    sales_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact = models.IntegerField(blank=True)
    first_name = models.fields.CharField(max_length=25)
    last_name = models.fields.CharField(max_length=25)

    def __str__(self):
        return self.first_name

    # class Meta:
    #     db_table = 'sales'
    #     verbose_name = 'Equipe commerciale'


class Event_status(models.Model):
    event_status_id = models.IntegerField(blank=True)
    Event_status = models.IntegerField(blank=True)

    # class Meta:
    #     db_table = 'event_status'
    #     verbose_name = 'Statut des évènement'


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
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE, related_name="author_client",
                                       blank=False, null=True)



class Event(models.Model):
    event_id = models.IntegerField(blank=True)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    support_contact = models.ForeignKey(to=Support, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_status = models.ForeignKey(to=Event_status, on_delete=models.CASCADE)
    attendees = models.IntegerField(blank=True)
    event_date = models.DateTimeField(auto_now=True)
    notes = models.TextField(max_length=200, blank=True)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE, related_name="author_event",
                                       blank=False, null=True)

    # class Meta:
    #     db_table = 'event'
    #     verbose_name = 'Evènement'


class Contract(models.Model):
    contract_id = models.IntegerField(blank=True)
    sales_contact = models.ForeignKey(to=Sales, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(blank=True)
    amount = models.FloatField(blank=True)
    payment_due = models.DateTimeField(auto_now=True)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE, related_name="author_contract",
                                       blank=False, null=True)




