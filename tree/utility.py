from tree.models import TreeImplementation,Tree


def childInsertion(treeObject,treeObjectNode,i,valueList,rootId):
    if i==len(valueList):
        return
    elif treeObjectNode.value>valueList[i]:
        print(valueList[i])
        if treeObjectNode.leftId==None:
            childNode=TreeImplementation(value=valueList[i],tree=treeObject)
            childNode.parent_id=treeObjectNode.valId
            childNode.save()
            TreeImplementation.objects.filter(valId=treeObjectNode.valId).update(leftId=childNode.valId)
            treeObjectNode=TreeImplementation.objects.get(valId=rootId)
            childInsertion(treeObject,treeObjectNode,i+1,valueList,rootId)
        else:
            treeObjectNode=TreeImplementation.objects.get(valId=treeObjectNode.leftId)
            childInsertion(treeObject,treeObjectNode,i,valueList,rootId)
    elif treeObjectNode.value<=valueList[i]:
        print(valueList[i])
        if treeObjectNode.rightId==None:
            childNode=TreeImplementation(value=valueList[i],tree=treeObject)
            childNode.parent_id=treeObjectNode.valId
            childNode.save()
            TreeImplementation.objects.filter(valId=treeObjectNode.valId).update(rightId=childNode.valId)
            treeObjectNode=TreeImplementation.objects.get(valId=rootId)
            childInsertion(treeObject,treeObjectNode,i+1,valueList,rootId)
        else:
            treeObjectNode=TreeImplementation.objects.get(valId=treeObjectNode.rightId)
            childInsertion(treeObject,treeObjectNode,i,valueList,rootId)




def Insertion(valueList):
    treeObject=Tree()
    treeObject.save()
    treeObjectNode=TreeImplementation(value=valueList[0],tree=treeObject)
    treeObjectNode.save()
    rootId=treeObjectNode.valId
    childInsertion(treeObject,treeObjectNode,1,valueList,rootId)
    return ("done successfully")




def postOrderTraversal(treeObjectNode,traversalList):
    if(treeObjectNode):
        
        if treeObjectNode.leftId:
            treeObjectNodeLeft=TreeImplementation.objects.get(valId=treeObjectNode.leftId)
            postOrderTraversal(treeObjectNodeLeft,traversalList)
        
        if treeObjectNode.rightId:
            treeObjectNodeRight=TreeImplementation.objects.get(valId=treeObjectNode.rightId)
            postOrderTraversal(treeObjectNodeRight,traversalList)
        traversalList.append(treeObjectNode.value)

    return("working")


def inOrderTraversal(treeObjectNode,traversalList):
    if(treeObjectNode):
        
        if treeObjectNode.leftId:
            treeObjectNodeLeft=TreeImplementation.objects.get(valId=treeObjectNode.leftId)
            inOrderTraversal(treeObjectNodeLeft,traversalList)
        traversalList.append(treeObjectNode.value)
        if treeObjectNode.rightId:
            treeObjectNodeRight=TreeImplementation.objects.get(valId=treeObjectNode.rightId)
            inOrderTraversal(treeObjectNodeRight,traversalList)
        

    return("working")


def preOrderTraversal(treeObjectNode,traversalList):
    if(treeObjectNode):
        traversalList.append(treeObjectNode.value)
        if treeObjectNode.leftId:
            treeObjectNodeLeft=TreeImplementation.objects.get(valId=treeObjectNode.leftId)
            preOrderTraversal(treeObjectNodeLeft,traversalList)
        
        if treeObjectNode.rightId:
            treeObjectNodeRight=TreeImplementation.objects.get(valId=treeObjectNode.rightId)
            preOrderTraversal(treeObjectNodeRight,traversalList)
        

    return("working")
