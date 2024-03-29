from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField

# STATUS will define the options for the different categories
STATUS = ((1, "8U"), (2, "10U"),
          (3, "11U"), (4, "12U"),
          (5, "14U"), (6, "16U"),
          (7, "18U"), (8, "Open")
          )


# Create your models here.
class WebUser(models.Model):
    """
    Stores a single user for the website,
    either staff or player
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    """tournament = models.ManyToManyField(Tournament,
    related_name="playing-tournaments", blank=True)"""
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # photo_url = models.CharField(max_length=500, blank=True)
    # photo = CloudinaryField('image', default='placeholder', blank=True)
    category = models.IntegerField(choices=STATUS, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.user}"


# This is the nournament model
class Tournament(models.Model):
    name = models.CharField(max_length=100, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)
    surface = models.CharField(max_length=200)
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2)
    prize_money = models.DecimalField(max_digits=10, decimal_places=2)
    sponsor = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    participants = models.ManyToManyField(
        WebUser, related_name="participatiing", blank=True
        )
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    max_participants = models.IntegerField()
    category = models.IntegerField(choices=STATUS, blank=True, null=True)
    img_url = CloudinaryField('image')
    phone_number = PhoneNumberField()
    email = models.EmailField()

    class Meta:
        ordering = ["start_date"]
        # permissions = [
        #     ("add_tournament", "Can add tournament"),
        #     # ("change_tournament", "Can change tournament"),
        #     # ("delete_tournament", "Can delete tournament"),
        # ]

    def __str__(self):
        return f"{self.name} starts on {self.start_date} and ends on {self.end_date},played on {self.surface} | sponsored by {self.sponsor}"

    def number_particitipating(self):
        return self.participants.count()


OPTIONS = ((0, "Draft"), (1, "Published"))


class New(models.Model):
    title = models.CharField(max_length=200, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    status = models.IntegerField(choices=OPTIONS, default=0)
    img_url = CloudinaryField('image')

    class Meta:
        ordering = ["updated_on"]

    def __str__(self):
        return f"{self.title} was created on {self.created_on}. Last update {self.updated_on}"
        