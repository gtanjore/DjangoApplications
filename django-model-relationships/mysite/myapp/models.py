from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.lookups import IsNull

class Sport(models.Model):
    sport_name = models.CharField(max_length=200)
    sport_description = models.CharField(max_length=1000)
    
    class meta:
        table_name = "Sport"
    
    def __str__(self):
        return self.sport_name

class League(models.Model):
    league_name = models.CharField(max_length=200)
    sport = models.OneToOneField(Sport,on_delete=models.CASCADE)
    
    class meta:
        table_name = "League"
    
    def __str__(self):
        return f"{self.league_name} - ({self.sport})"

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created')   
    league = models.ForeignKey(League, on_delete=models.CASCADE) 

    class meta:
        table_name = "team"
    
    def __str__(self):
        if self.league is None:
            return f"{self.team_name}"
        else:
            return f"{self.team_name} -({self.league})"

# class Player(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)


#     class meta:
#         table_name = "player"
    
#     def __str__(self):
#         return f"{self.first_name}, {self.last_name}"

class PersonRole(models.Model):
    person_role = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created')    

    class meta:
        table_name = "person_role"
    
    def __str__(self):
        return self.person_role
    
class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    person_role =  models.ForeignKey(PersonRole, null=True,on_delete=models.SET_NULL)

    class meta:
        table_name = "person"
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

class TeamPerson(models.Model):
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class meta:
        table_name = "team_person"

    def __str__(self):
        return f"{self.person.first_name}, {self.person.last_name} - ({self.person.person_role})"
