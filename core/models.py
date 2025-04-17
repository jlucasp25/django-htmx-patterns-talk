from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    email = models.EmailField()
    signup_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    customer = models.ForeignKey(Customer, related_name='projects', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        get_latest_by = 'created_on'

    def __str__(self):
        return self.title


class ProjectFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    project = models.ForeignKey(Project,related_name='files', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
