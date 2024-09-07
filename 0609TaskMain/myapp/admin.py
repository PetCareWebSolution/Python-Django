from django.contrib import admin

# Register your models here.
from django.contrib import admin

from . models import country,city,state,User,Actor,director,gener,movie,review,watchlist

# Register your models here.


class showcountry(admin.ModelAdmin):

    list_display = ['countryName']

admin.site.register(country,showcountry)


class showstate(admin.ModelAdmin):

    list_display = ['countryID','stateName']

admin.site.register(state,showstate)

class showcity(admin.ModelAdmin):

    list_display = ['stateID','cityName']

admin.site.register(city,showcity)

class showactor(admin.ModelAdmin):

    list_display = ['a_state','a_country','a_city','a_name','a_pic','a_photo','a_BIO','a_Nationality','a_awards','a_Gender','a_birthday']

admin.site.register(Actor,showactor)

class showuser(admin.ModelAdmin):

    list_display = ['u_state','u_country','u_city','u_name','u_DP','u_photo','u_Gender','u_status','u_date_joined']

admin.site.register(User,showuser)

class showd(admin.ModelAdmin):

    list_display = ['d_state','d_country','d_city','d_name','d_pic','d_photo','d_BIO','d_Nationality','d_Awards','d_gender']

admin.site.register(director,showd)

class showgener(admin.ModelAdmin):

    list_display = ['name']

admin.site.register(gener,showgener)


class showmovie(admin.ModelAdmin):
    list_display = ['Title', 'Description', 'Release_Year', 'Gener', 'get_actors', 'DIRECTOR', 'poster','m_photo', 'Trailer',
                    'Created_At']

    # Define a method to display ManyToManyField values
    def get_actors(self, obj):
        return ", ".join([actor.a_name for actor in obj.actors.all()])

    get_actors.short_description = 'Actors'  # Set a custom column title


admin.site.register(movie, showmovie)


class showreview(admin.ModelAdmin):

    list_display = ['movie','User','Rating','Comment','created_AT']

admin.site.register(review,showreview)

class showwl(admin.ModelAdmin):

    list_display = ['user','movie','Added_TO']

admin.site.register(watchlist,showwl)
