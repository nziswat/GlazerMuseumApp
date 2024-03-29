from collections import defaultdict
from django.db import models
from django.utils import timezone






    

class PlayTypes(models.Model): #Contains all the plays perhaps in the future code to be specific to exhibit, for now just display all and allow all to be recorded(Proof of Concept)
    plays = models.ManyToManyField('Play', blank=True)
    setName = models.CharField(max_length=100, default='default')
    
    def __str__(self):
        return self.setName
            
#Apps>Exhibits>PlayTypes>Play



class Play(models.Model): #Each play itself, is an object maybe in the future admins decide they want more 
    playName = models.CharField(max_length=200, default='')
    playDescription = models.CharField(max_length=200, default='')
    #votes = models.IntegerField(default=0) #This SHOULD NOT BE GLOBAL, this must be tied directly to an exhibit via PlayTypes    


    def save(self, *args, **kwargs): #overwrites 
        is_new = self._state.adding
        super(Play, self).save(*args, **kwargs)
        if is_new:
            default_playtype, created = PlayTypes.objects.get_or_create(setName='default')
            default_playtype.plays.add(self)
    
    def __str__(self):
        return self.playName
    
    

    def addvote(self,exhibit,cookie): #Adds
        newvote= Vote.objects.create(cookie=cookie,exhibit=exhibit,play=self) #re-add the votes back into the database

class ExText(models.Model): #perhaps change ExText to ExhibitData, since it's grown out of hand.
    titleText= models.CharField(max_length=200, default='')
    descText= models.CharField(max_length=200, blank=True)
    imagePath= models.CharField(max_length=200, blank=True)
    playTypes = models.ForeignKey(PlayTypes, on_delete=models.SET_NULL, null=True, blank=True)
   

    def get_play_types(self): #Basically will either the set playset or just pick the default set (which has everything)
        if self.playTypes:
            return self.playTypes.plays.all()
        #otherwise, return the plays from the default playTypes
        default_playTypes = PlayTypes.objects.get(setName='default')
        return default_playTypes.plays.all()
    
    
    def __str__(self):
        return self.titleText


class Vote(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    exhibit = models.ForeignKey(ExText, on_delete=models.CASCADE)  
    cookie = models.CharField(max_length=256)  # figure this out later, not all that important rn
    timestamp = models.DateTimeField(auto_now_add=True)  # automatically set the field to now when the object is first created.

    def __str__(self):
        return f"Vote for {self.play} on {self.timestamp}, at {self.exhibit} by {self.cookie}"