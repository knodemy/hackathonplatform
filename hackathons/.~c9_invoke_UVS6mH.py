from django.db import models
from django import forms
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField

#note: optional/required fields

#access code: allows the user to get to the program flow on

#note: should create guideline document for users on how to use these forms and the django admin site.
class Manage_Event(models.Model): #change to "manage events"
    event_name = models.CharField(max_length=75, blank = True)
    event_theme = models.CharField(max_length=75, blank = True)
    #change to min/max grade
    min_grade = models.IntegerField(choices = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), 
                                                    (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)), 
                                                    null = True, blank = True)
    max_grade = models.IntegerField(choices = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), 
                                                    (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)), 
                                                    null = True, blank = True)
    time_zone = models.CharField(max_length = 15, help_text = "ex: PST", blank = True)
    start_time = models.DateTimeField(help_text = "Please use 24 hour time.", null = True, blank = True)
    end_time = models.DateTimeField(help_text = "Please use 24 hour time.", null = True, blank = True)
    location_name = models.CharField(max_length=75, help_text = "ex: Pleasanton Library", blank = True)
    location_address_1 = models.CharField(max_length=75, help_text = "ex: 400 Old Bernal Ave", blank = True)
    location_address_2 = models.CharField(max_length=75, help_text = "ex: Building 2, Lobby, etc.", blank = True)
    city = models.CharField(max_length=75, help_text = "ex: Pleasanton", blank = True)
    state = models.CharField(max_length=2, help_text = "ex: CA", blank = True)
    zip_code = models.CharField(max_length = 5, help_text = "ex: 94566", blank = True)
    country = models.CharField(max_length = 75, help_text = "ex: United States", blank = True)
    event_details = HTMLField(default = None, help_text="Detailed description of your event goes here.")
    optional_event_details = HTMLField(help_text = "Additional detailed description of your event goes here.", default = None)
    event_FAQ = HTMLField(help_text = "FAQs go here.", default = None)
    event_contact_name = models.CharField(max_length = 30, help_text = "Name of the contact for your event.", blank = True)
    event_contact_phone = models.CharField(max_length = 30, help_text = "Phone number of the contact for your event.", blank = True)
    event_contact_email = models.CharField(max_length = 255, help_text = "Email of the contact for your event.", blank = True)
    event_banner = models.FileField(upload_to='images/', 
                    help_text = "Dimensions: minimum 2160 x 1080px. File Type: JPEG, PNG, BMP, or GIF. File Size: no larger than 10 MB.", 
                    null = True, blank = True)
    event_access_code = models.CharField(max_length=10, help_text = "clarify: 10 or fewer character access code for your event.", blank = True)
    
    def __str__(self):
        return self.event_name
    
class Event_Flow(models.Model): #change to "program flow"
    event_name = models.CharField(max_length=75, help_text = "Must match event name given when creating event page.", blank = True)
    welcome_slide_file = models.FileField(upload_to='slides/', null = True, blank = True)
    welcome_talking_points = HTMLField(default = None, null = True)
    guest_speaker_slide_file = models.FileField(upload_to='slides/', null = True, blank = True)
    guest_speaker_talking_points = HTMLField(default = None, null = True, blank = True)
    workshop_slide_file = models.FileField(upload_to='slides/', null = True, blank = True)
    workshop_talking_points = HTMLField(default = None, null = True)
    number_of_teams = models.IntegerField(null = True, blank = True)
    team_project_slide_file = models.FileField(upload_to='slides/', null = True, blank = True)
    team_project_talking_points = HTMLField(default = None, null = True)
    team_slideshow_slide_file = models.FileField(upload_to='slides/', null = True, blank = True)
    team_slideshow_talking_points = HTMLField(default = None, null = True)
    judging_slide_file = models.FileField(upload_to='slides/', null = True, blank = True)
    judging_talking_points = HTMLField(default = None, null = True)
    
    def __str__(self):
        return self.event_name
        
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
