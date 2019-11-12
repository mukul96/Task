from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from tree.utility import Insertion,inOrderTraversal,postOrderTraversal,preOrderTraversal,childInsertion
from tree.models import *
from django.shortcuts import render,redirect,reverse
import string
# Create your views here.


@csrf_exempt
def treeMakingFirstInsertion(request):
    if request.method == 'POST':
        valueString= request.POST['values']
        valueList=valueString.split(',')
        print(valueList)
        invalid=string.ascii_letters
        for s in valueList:
            if s=="" or any(char in invalid for char in s) or len(valueList)<3:
                return HttpResponse("add a right value in comma separated form")
        valueList=[int(i) for i in valueList]
        Insertion(valueList)
        return redirect('alltreeView')
    return HttpResponse("Hello, world. You're at the polls index.")


def allTrees(request):
    trees=Tree.objects.all()
   
    finalList=[]
    for tree in trees:
        treeObjectNode=TreeImplementation.objects.filter(tree=tree)
        print(treeObjectNode)
        currDict={}
        
        
        
        currDict['id']=tree.treeId

        preOrderTraversalList=[]
        preOrderTraversal(treeObjectNode[0],preOrderTraversalList)
        currDict['preOrder']=preOrderTraversalList

        inOrderTraversalList=[]
        inOrderTraversal(treeObjectNode[0],inOrderTraversalList)
        currDict['inOrder']=inOrderTraversalList

        postOrderTraversalList=[]
        postOrderTraversal(treeObjectNode[0],postOrderTraversalList)
        currDict['postOrder']=postOrderTraversalList

        
        finalList.append(currDict)
    return render(request, 'index.html',{"finalList": finalList})


@csrf_exempt
def deleteTree(request):
    if request.method=='POST':
        treeId=request.POST.get('treeId')
        #print(treeId)
        Tree.objects.get(treeId=treeId).delete()
        return redirect('alltreeView')



def treeElementInsertion(request):
    if request.method=='POST':
        valueString= request.POST['values']
        valueList=valueString.split(',')
        print(valueList)
        invalid=string.ascii_letters
        for s in valueList:
            if s=="" or any(char in invalid for char in s) :
                return HttpResponse("add a right value in comma separated form")
        valueList=[int(i) for i in valueList]


        treeId=request.POST.get('treeId')
        tree=Tree.objects.get(treeId=treeId)


        treeObjectNodes=TreeImplementation.objects.filter(tree=tree)
        treeObjectNode=treeObjectNodes[0]
        rootId=treeObjectNode.valId

        childInsertion(tree,treeObjectNode,0,valueList,rootId)
        return redirect('alltreeView')