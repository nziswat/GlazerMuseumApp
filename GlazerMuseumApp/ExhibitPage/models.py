from django.db import models






    

class PlayTypes(models.Model): #Contains all the plays perhaps in the future code to be specific to exhibit, for now just display all and allow all to be recorded(Proof of Concept)
    playList=[]
    setName = models.CharField(max_length=100, default='default')
    
    def __str__(self):
        return self.setName
            
#Apps>Exhibits>PlayTypes>Play

class Play(models.Model): #Each play itself, is an object maybe in the future admins decide they want more 
    playName = models.CharField(max_length=200, default='')
    playDescription = models.CharField(max_length=200, default='')
    votes = models.IntegerField(default=0) #This SHOULD NOT BE GLOBAL, this must be tied directly to an exhibit via PlayTypes
    playSet = models.ForeignKey(PlayTypes, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.playName

class ExText(models.Model): #perhaps change ExText to ExhibitData, since it's grown out of hand.
    titleText= models.CharField(max_length=200, default='')
    descText= models.CharField(max_length=200, default='')
    imagePath= models.CharField(max_length=200, default='')
    exhibitPlays = models.OneToOneField(PlayTypes, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.titleText