#This File was generated by Django and modified by: Kevin Panasiuk
#Log:
#4/1/24: Made this header.
#4/2/24: Added comments

from collections import defaultdict
from django.db import models
from django.utils import timezone


    
#TODO: Possibly rename to PlaySets, cause that makes more sense.
class PlayTypes(models.Model): #Contains plays that each exhibit can use
    plays = models.ManyToManyField('Play', blank=True) #many to many: allows admins to define playsets as they wish
    setName = models.CharField(max_length=100, default='default')
    
    def __str__(self):
        return self.setName
          

class Play(models.Model): #Each play itself, is an object maybe in the future admins decide they want more 
    playName = models.CharField(max_length=200, default='')
    playDescription = models.CharField(max_length=1024, default='') 

    def save(self, *args, **kwargs): #overwrites the regular save function
        is_new = self._state.adding
        super(Play, self).save(*args, **kwargs) #produces a regular save of itself
        if is_new: 
            default_playtype, created = PlayTypes.objects.get_or_create(setName='default') #and then throws it into the default playtype
            default_playtype.plays.add(self)
    
    def __str__(self):
        return self.playName

    def addvote(self,exhibit,cookie): #Create a vote object tied to this play
        newvote= Vote.objects.create(cookie=cookie,exhibit=exhibit,play=self) #re-add the votes back into the database

class ExText(models.Model): #perhaps change ExText to ExhibitData, since it's grown out of hand.
    titleText= models.CharField(max_length=200, default='')
    descText= models.CharField(max_length=1024, blank=True)
    imagePath= models.CharField(max_length=200, blank=True) #TODO: make this actually work
    playTypes = models.ForeignKey(PlayTypes, on_delete=models.SET_NULL, null=True, blank=True)
   
    #TODO: not to do this here but probably manipulate the admin options so that 'default' and '---' doesn't show up together and instead turn '---' to default
    #and make 'default' invisible
    def get_play_types(self): #Basically will either the set playset or just pick the default set (which has everything)
        if self.playTypes:
            return self.playTypes.plays.all()
        #otherwise, return the plays from the default playTypes
        default_playTypes = PlayTypes.objects.get(setName='default')
        return default_playTypes.plays.all()
    
    
    def __str__(self):
        return self.titleText


class Vote(models.Model): #the voting object, pretty simple
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    exhibit = models.ForeignKey(ExText, on_delete=models.CASCADE)  
    cookie = models.CharField(max_length=37)  # takes UUID4 = 36 chars long, 1 more just to be safe
    timestamp = models.DateTimeField(auto_now_add=True)  # automatically set the field to now when the object is first created.

    def __str__(self):
        return f"Vote for {self.play} on {self.timestamp}, at {self.exhibit} by {self.cookie}"