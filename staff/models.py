from django.db import models
from company.models import Company
from django.urls import reverse

# Create your models here.
class Staff(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/staff', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    employment_date = models.DateTimeField(blank=True, null=True)
    terminate_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_management = models.BooleanField(default=False)
    is_primary_contact = models.BooleanField(default=False)

    def update_url(self):
        return reverse('update_staff', args=[self.id])

    def delete_url(self):
        return reverse('delete_staff', args=[self.id])

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.first_name
