from django.db import models
from account.models import Account
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=50)
    website_address = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=12)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='photos/logos')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_client = models.BooleanField(default=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)

    def address(self):
        return f'{self.address_line_1} {self.address_line_2}'

    def province(self):
        return f'{self.city} {self.state} {self.country}'

    def update_url(self):
        return reverse('update_company', args=[self.id])

    def delete_url(self):
        return reverse('delete_company', args=[self.id])

    # within the admin django pluralizes models by adding 's' to name
    # e.g. company = companys to correct this
    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.company_name

class CompanyOverview(models.Model):
    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
        unique=True,
    )
    business_overview = models.TextField(max_length=500, blank=True)
    competive_advantage = models.TextField(max_length=500, blank=True)
    mission_statement = models.TextField(max_length=500, blank=True)
    vision = models.TextField(max_length=500, blank=True)
    philosophy = models.TextField(max_length=500, blank=True)
    # id = models.AutoField(primary_key=True, default=None)

    def update_url(self):
        return reverse('update_business_overview', args=[self.company_id])

    def delete_url(self):
        return reverse('delete_business_overview', args=[self.company_id])

    def __str__(self):
        return self.company.company_name
