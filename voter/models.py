from django.db import models
from django.urls import reverse
from smart_selects.db_fields import ChainedForeignKey
from account.models import Account
from location.models import State, LocalGovArea


# Create your models here.
gender_choice ={
    ('0','Select Gender'),
    ('Male','Male'),
    ('Female', 'Female'),
}

channel_choice = (
    ('0','Select How you heard about us'),
    ('Facebook','Facebook'),
    ('Instagram', 'Instagram'),
    ('Google','Google'),
    ('word of mouth','Word of Mouth'),
    ('youtube','Youtube'),
    ('Ads','Ads'),
    ('others','Others'),
)

PP_choice = (
    ('0','Select your political party'),
    ('Accord','Accord'),
    ('Action Alliance', 'Action Alliance'),
    ('Action Democratic Party', 'Action Democratic Party'),
    ('Action Peoples Party','Action Peoples Party'),
    ('African Action Congress','African Action Congress'),
    ('African Democratic Congress','African Democratic Congress'),
    ('All Progressives Congress','All Progressives Congress'),
    ('All Progressives Grand Alliance','All Progressives Grand Alliance'),
    ('Allied Peoples Movement', 'Allied Peoples Movement'),
    ('Boot Party', 'Boot Party'),
    ('Labour Party','Labour Party'),
    ('National Rescue Movement','National Rescue Movement'),
    ('New Nigeria Peoples Party','New Nigeria Peoples Partys'),
    ('Peoples Democratic Party','Peoples Democratic Party'),
    ('Peoples Redemption Party','Peoples Redemption Party'),
    ('Social Democratic Party','Social Democratic Party'),
    ('Young Progressive Party','Young Progressive Party'),
    ('Zenith Labour Party','Zenith Labour Party'),
    ('others','Others'),
)

class Voter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True, null=True, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True, unique=True)
    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    village = models.CharField(max_length=50)

    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    local_gov_area = ChainedForeignKey(
        LocalGovArea,
        chained_field="state",
        chained_model_field="state",
        show_all=False,
        auto_choose=True,
        default=None,  blank=True,)
    postal_code = models.CharField(max_length=12, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/voters', blank=True, null=True)

    is_registered = models.BooleanField(default=False)
    is_eligible = models.BooleanField(default=False)
    willing_to_register = models.BooleanField(default=False)
    political_party = models.CharField(max_length=100, choices=PP_choice, default='0')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    channel = models.CharField(max_length=100, choices=channel_choice, default='0')
    gender = models.CharField(max_length=10, choices=gender_choice, default='0')

    def update_url(self):
        return reverse('update_voter', args=[self.id])

    def delete_url(self):
        return reverse('delete_voter', args=[self.id])

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.first_name
