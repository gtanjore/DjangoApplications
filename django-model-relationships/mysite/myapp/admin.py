from django.contrib import admin

from .models import Person, Sport, League, Team, PersonRole, Person, TeamPerson

class TeamPersonAdminInline(admin.TabularInline):
    model = TeamPerson

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name']
    inlines = [TeamPersonAdminInline]

class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name']
    inlines = [TeamPersonAdminInline]


admin.site.register(Sport)
admin.site.register(League)
admin.site.register(PersonRole)
admin.site.register(Person)
