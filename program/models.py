from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from company.models import Company
from django.urls import reverse


# Create your models here.
class Program(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    program_description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='photos/programs')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def update_url(self):
        return reverse('update_program', args=[self.id])

    def delete_url(self):
        return reverse('delete_program', args=[self.id])

    def program_url(self):
        return reverse('program', args=[self.id])

    # def project_url(self):
    #     return reverse('project_slug', args=[self.slug])

    def __str__(self):
        return self.program_name

class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    program = ChainedForeignKey(
        Program,
        chained_field="company",
        chained_model_field="company",
        show_all=False,
        auto_choose=True,
        default=None)
    project_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    project_description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='photos/programs')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    project_objective = models.TextField(max_length=1000, blank=True)

    def update_url(self):
        return reverse('update_project', args=[self.id])

    def delete_url(self):
        return reverse('delete_project', args=[self.id])

    def project_url(self):
        return reverse('project', args=[self.id])

    # def project_url(self):
    #     return reverse('project_slug', args=[self.slug])

    def __str__(self):
        return self.project_name

class Activity(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    program = ChainedForeignKey(
        Program,
        chained_field="company",
        chained_model_field="company",
        show_all=False,
        auto_choose=True,
        default=None)
    project = ChainedForeignKey(
        Project,
        chained_field="program",
        chained_model_field="program",
        show_all=False,
        auto_choose=True,
        default=None)
    activity_name = models.CharField(max_length=50, unique=True)
    activity_description = models.TextField(max_length=500, blank=True)
    activity_video = models.CharField(max_length=50, blank=True, null=True)
    activity_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='photos/activity')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def update_url(self):
        return reverse('update_activity', args=[self.id])

    def delete_url(self):
        return reverse('delete_activity', args=[self.id])

    def activity_url(self):
        return reverse('activity', args=[self.id])

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.activity_name

class ActivityImage(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    program = ChainedForeignKey(
        Program,
        chained_field="company",
        chained_model_field="company",
        show_all=False,
        auto_choose=True,
        default=None)
    project = ChainedForeignKey(
        Project,
        chained_field="program",
        chained_model_field="program",
        show_all=False,
        auto_choose=True,
        default=None)
    activity = ChainedForeignKey(
        Activity,
        chained_field="project",
        chained_model_field="project",
        show_all=False,
        auto_choose=True,
        default=None)
    image_name = models.CharField(max_length=50, null=True)
    image_description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='photos/ActivityImage')

    def update_url(self):
        return reverse('update_activity_image', args=[self.id])

    def delete_url(self):
        return reverse('delete_activity_image', args=[self.id])

    class Meta:
        verbose_name = 'ActivityImages'
        verbose_name_plural = 'Activity Images'

    def __str__(self):
        return self.image_name
