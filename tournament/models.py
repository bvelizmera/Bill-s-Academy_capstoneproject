from django.db import models
from django.contrib.auth.models import User

#STATUS will define the options for the different categories
STATUS = ((1, "8U"), (2, "10U"), (3, "11U"), (4, "12U"), (5, "14U"), (6, "16U"), (7, "18U"), (8, "Open"))
# Create your models here.
class WebUser(models.Model):
    """
    Stores a single user for the website, either staff or player
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=50, unique=True)
    l_name = models.CharField(max_length=50)
    description = models.TextField()
    # tournament = models.ManyToManyField(Tournament, related_name="playing-tournaments", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # photo_url = models.CharField(max_length=500, blank=True)
    # photo = CloudinaryField('image', default='placeholder', blank=True)
    category = models.CharField(choices=STATUS, blank=True, null=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name} - {self.user}"



#This is the nournament model
class Tournament(models.Model):
    name = models.CharField(max_length=100, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tournament_created")
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)
    surface = models.CharField(max_length=200)
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2)
    prize_money = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    sponsor = models.CharField(max_length=50)
    description = models.TextField()
    participants = models.ManyToManyField(WebUser, related_name="participatiing", blank=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    max_participants = models.IntegerField()
    category = models.IntegerField(choices=STATUS, blank=True)

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return f"{self.name} starts on {self.start_date} and ends on {self.end_date}, played on {self.surface} | sponsored by {self.sponsor}"
    
    def number_particitipating(self):
        return self.participants.count()

OPTIONS = ((0,"Draft"), (1, "Published"))
class New(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=OPTIONS, default=0)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} was created on {self.created_on}. Last update {self.updated_on}"


