from django.db import models

# Create your models here.
class Tree(models.Model):
    treeId=models.AutoField(primary_key=True)

class TreeImplementation(models.Model):
    valId=models.AutoField(primary_key=True)  
    parent_id=models.IntegerField(default=None,null=True)
    value=models.IntegerField()
    tree=models.ForeignKey(Tree,on_delete=models.CASCADE)
    leftId=models.IntegerField(default=None,null=True)
    rightId=models.IntegerField(default=None,null=True)
    