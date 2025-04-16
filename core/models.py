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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class ProjectFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name