from collections import defaultdict
from django.db import models
from django.utils import timezone






    

class PlayTypes(models.Model): #Contains all the plays perhaps in the future code to be specific to exhibit, for now just display all and allow all to be recorded(Proof of Concept)
    playList=[]
    setName = models.CharField(max_length=100, default='default')
    
    def __str__(self):
        return self.setName
            
#Apps>Exhibits>PlayTypes>Play



class Play(models.Model): #Each play itself, is an object maybe in the future admins decide they want more 
    playName = models.CharField(max_length=200, default='')
    playDescription = models.CharField(max_length=200, default='')
    votes = [] #store vote objects in hee'ah
    #votes = models.IntegerField(default=0) #This SHOULD NOT BE GLOBAL, this must be tied directly to an exhibit via PlayTypes
    playSet = models.ForeignKey(PlayTypes, on_delete=models.CASCADE) #figure this out because we don't want duplicate plays (we don't need it)
    #find a way to tie it into each exhibit     

    
    def __str__(self):
        return self.playName
    
    def addvote(self,exhibit,cookie): #proof of concept, no security no verification
        newvote = Vote(play=self,exhibit=exhibit,cookie=cookie)
        self.votes.append(newvote)
        

class ExText(models.Model): #perhaps change ExText to ExhibitData, since it's grown out of hand.
    titleText= models.CharField(max_length=200, default='')
    descText= models.CharField(max_length=200, blank=True)
    imagePath= models.CharField(max_length=200, blank=True)
    exhibitPlays = models.OneToOneField(PlayTypes, on_delete=models.CASCADE) #1:1, but figure out a possible handling for default

    
    def __str__(self):
        return self.titleText


class Vote(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    exhibit = models.ForeignKey(ExText, on_delete=models.CASCADE)  
    cookie = models.CharField(max_length=256)  # figure this out later, not all that important rn
    timestamp = models.DateTimeField(auto_now_add=True)  # automatically set the field to now when the object is first created.

    def __str__(self):
        return f"Vote for {self.play} on {self.timestamp}, {self.exhibit}"
    

