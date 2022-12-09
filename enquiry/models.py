from django.db import models
from program.models import Program

# Create your models here.

# Create your models here.
channel_chioce = (
    (0,'Select How you heard about us'),
    ('Facebook','Facebook'),
    ('Instagram', 'Instagram'),
    ('Google','Google'),
    ('word of mouth','Word of Mouth'),
    ('youtube','Youtube'),
    ('Ads','Ads'),
    ('others','Others'),
)

involvement_chioce = (
    (0,'Select how you would get involed'),
    ('partner','Partner'),
    ('volunteer', 'Volunteer'),
    ('employment', 'Employment'),
    ('others','Others'),
)

class Lead(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100, blank=True)
    channel = models.CharField(max_length=100, choices=channel_chioce, default=0)
    involvement = models.CharField(max_length=100, choices=involvement_chioce, default=0)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email
