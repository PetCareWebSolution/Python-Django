from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

gen = [
    ('1','Male'),
    ('2','Female')
]

st = [
    ('0',"IN-ACTIVE"),
    ('1','ACTIVE')
]

class country(models.Model):

    countryName = models.CharField(max_length=30)

    def __str__(self):

        return self.countryName


class state(models.Model):

    countryID = models.ForeignKey(country,on_delete=models.CASCADE)

    stateName = models.CharField(max_length=30)

    def __str__(self):

        return self.stateName


class city(models.Model):

    stateID = models.ForeignKey(state,on_delete=models.CASCADE)

    cityName = models.CharField(max_length=30)

    def __str__(self):

        return self.cityName


class Actor(models.Model):

    a_state = models.ForeignKey(state,on_delete=models.CASCADE)

    a_country = models.ForeignKey(country,on_delete=models.CASCADE)

    a_city = models.ForeignKey(city,on_delete=models.CASCADE)

    a_name = models.CharField(max_length=30)

    a_pic = models.ImageField()

    a_BIO = models.TextField()

    a_Nationality = models.CharField(max_length=30)

    a_awards = models.CharField(max_length=30)

    a_Gender = models.CharField(max_length=30,choices=gen)

    a_birthday = models.DateField()

    def a_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.a_pic.url))

    a_photo.allow_tags = True

    def __str__(self):

        return self.a_name


class User(models.Model):

    u_state = models.ForeignKey(state, on_delete=models.CASCADE)

    u_country = models.ForeignKey(country, on_delete=models.CASCADE)

    u_city = models.ForeignKey(city, on_delete=models.CASCADE)

    u_name = models.CharField(max_length=30)

    u_DP = models.ImageField()

    u_Gender = models.CharField(max_length=30, choices=gen)

    u_status = models.CharField(max_length=30, choices=st)

    u_date_joined = models.DateField()

    def u_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.u_DP.url))

    u_photo.allow_tags = True

    def __str__(self):

        return self.u_name


class director(models.Model):

    d_state = models.ForeignKey(state,on_delete=models.CASCADE)

    d_country = models.ForeignKey(country,on_delete = models.CASCADE)

    d_city = models.ForeignKey(city,on_delete = models.CASCADE)

    d_name = models.CharField(max_length=30)

    d_pic = models.ImageField()

    d_BIO = models.TextField()

    d_Nationality = models.CharField(max_length=30)

    d_Awards = models.CharField(max_length=30)

    d_gender = models.CharField(max_length=30,choices=gen)

    def __str__(self):

        return self.d_name

    def d_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.d_pic.url))

    d_photo.allow_tags = True


class gener(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):

        return self.name

class movie(models.Model):
    Title = models.CharField(max_length=30)
    Description = models.TextField()
    Release_Year = models.DateTimeField()  # Keep only one Release_Year field
    Gener = models.ForeignKey(gener, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    DIRECTOR = models.ForeignKey(director, on_delete=models.CASCADE)
    poster = models.ImageField()
    Trailer = models.URLField(blank=True, null=True)
    Created_At = models.DateTimeField()

    def __str__(self):
        return self.Title

    def m_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.poster.url))

    m_photo.allow_tags = True


class review(models.Model):

    movie = models.ForeignKey(movie,on_delete = models.CASCADE)

    User = models.ForeignKey(User,on_delete = models.CASCADE)

    Rating = models.CharField(max_length=30)

    Comment = models.CharField(max_length=30)

    created_AT = models.DateTimeField()

class watchlist(models.Model):

    user = models.ForeignKey(User,on_delete = models.CASCADE)

    movie = models.ForeignKey(movie,on_delete = models.CASCADE)

    Added_TO = models.CharField(max_length=30)


































