from django.db import models

# Клиенты
class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, null=True)
    personal_account = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.first_name} {self.last_name} {self.patronymic}")

# Обращения
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, null=True)
    personal_account = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50)
    record = models.CharField(max_length=255, null=True)
    responsible_person = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=50, null=True, default="")
    status = models.CharField(max_length=50, null=True, default="in_progress")
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name} {self.patronymic}")

# Жалобы
class Complaint(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, null=True)
    personal_account = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50)
    complaint = models.CharField(max_length=255, null=True)
    responsible_person = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=50, null=True, default="")
    status = models.CharField(max_length=50, null=True, default="in_progress")

    def __str__(self):
        return(f"{self.first_name} {self.last_name} {self.patronymic}")
