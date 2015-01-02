# This Python file uses the following encoding: utf-8
__author__ = 'xiaohe'

from py2neo import Graph
graph = Graph()
from py2neo import Node, Relationship, Path
from py2neo import neo4j
class User():
    def __init__(self,userID = None,tags = None,node = None):
        if userID != None and tags != None:
            self.node = Node("user", userID=userID,tags = tags)
            #graph.create(self.node)
        else:
            self.node = node
    def save(self,unique = True):
        if self.node:
            if unique:
                result = graph.find_one(label="user",property_key="userID",property_value=self.node["userID"])
                if result == None:
                    graph.create(self.node)
            else:
                graph.create(self.node)

    def follow(self,otherNode):
        if self.node == None or otherNode == None:
            return
        if not graph.match_one(start_node=self.node, rel_type="FOLLOWS", end_node=otherNode):
            followship = Relationship(self.node, "FOLLOWS", otherNode)
            graph.create(followship)

    def getFollowList(self,tags = None):

        followList = []
        for rel in graph.match(start_node=self.node, rel_type="FOLLOWS"):
            if tags:
                if rel.end_node["tags"] == tags:
                    followList.append(rel.end_node)
            else:
                followList.append(rel.end_node)
        return followList

    def getFanList(self,tags = None):
        if self.node == None:
            return []
        fanList = []
        for rel in graph.match(end_node=self.node, rel_type="FOLLOWS"):
            if tags:
                if rel.end_node["tags"] == tags:
                    fanList.append(rel.end_node)
            else:
                fanList.append(rel.end_node)
        return fanList

'''
def insertUserOfTags(tags,userID):
    #insert into users of the tags
    userNode = Node("user", userID=userID,tags = tags)
    graph.create(userNode)
'''
def get_user_by_ID(userID):
    return graph.find_one("user","userID", userID)

def get_followdList_by_ID(userID):
    result = graph.find_one("user","userID",userID)
    if not result:
        print "不能存在该用户"
        return []
    # 找到所有关注者的粉丝，记录共同关注者
    nodeCountDict = {}
    currentFollowdList = []
    for rel in graph.match(start_node=result, rel_type="FOLLOWS"):
        currentFollowdList.append(rel.end_node["userID"])
    return currentFollowdList
def recommend_friend_by_ID(userID,limit=10):
    related_list = []
    result = graph.find_one("user","userID",userID)
    if not result:
        print "不能存在该用户"
        return None
    # 找到所有关注者的粉丝，记录共同关注者
    nodeCountDict = {}
    currentFollowdList = []
    currentFollowMap = []

    for rel in graph.match(start_node=result, rel_type="FOLLOWS"):
        #print "start user",userID," end ",rel.end_node["userID"]
        currentFollowdList.append(rel.end_node["userID"])
        currentFollowMap.append({"start":userID,"end":rel.end_node["userID"]})
        startnodes = graph.match(end_node=rel.end_node,rel_type="FOLLOWS")
        for newrel in startnodes:
            startnode = newrel.start_node
            temp_user_ID = startnode["userID"]
            if(temp_user_ID == userID):
                continue
            if(nodeCountDict.has_key(temp_user_ID)):
                #print "count" ,temp_user_ID,">",rel.end_node["userID"]
                nodeCountDict[temp_user_ID] += 1
            else:
                nodeCountDict[temp_user_ID] = 1
    related_list.append(currentFollowMap)
    # 对所有粉丝按照共同关注者数量进行排序
    # 好像不需要排序啊
    #for nodeItem in sorted(nodeCountDict.items(),lambda t1,t2:cmp(t1[1],t2[1]),reverse=True):
    #    print '===node===='
    #    similarNodeId = nodeItem[0]
    #    recommendDegree = nodeItem[1]
    recommendationList = {}
    for nodeItem in nodeCountDict.items():
        similarNodeId = nodeItem[0]
        recommendDegree = nodeItem[1]
        if recommendDegree<2:
            continue
        # 共同关注者数量可以看做推荐度，推荐度可以叠加
        similarNode = graph.find_one("user","userID",similarNodeId)
        tempfollowedMap = []
        for rel in graph.match(start_node=similarNode, rel_type="FOLLOWS"):
            #print "start",similarNodeId," end ",rel.end_node["userID"]
            #tempfollowedMap.append({"start":similarNodeId,"end":rel.end_node["userID"]})
            if (not rel.end_node["userID"] in currentFollowdList):
                if(recommendationList.has_key(rel.end_node["userID"] )):
                    recommendationList[rel.end_node["userID"]]["degree"] += recommendDegree
                    if (recommendationList[rel.end_node["userID"]]["bridges"].has_key(similarNodeId)):
                        recommendationList[rel.end_node["userID"]]["bridges"][similarNodeId] += recommendDegree
                    else:
                        recommendationList[rel.end_node["userID"]]["bridges"][similarNodeId] = recommendDegree
                else:
                    recommendationList[rel.end_node["userID"]] = {}
                    recommendationList[rel.end_node["userID"]]["degree"] = recommendDegree
                    recommendationList[rel.end_node["userID"]]["bridges"] = {similarNodeId:recommendDegree}
    for recommendItem in sorted(recommendationList.items(),lambda t1,t2:cmp(t1[1]["degree"],t2[1]["degree"]),reverse=True):
        if limit <= 0:
            break
        if recommendItem[1]["degree"] > 2:
            print recommendItem[0],'>', recommendItem[1]
            for bridgeItem in recommendItem[1]["bridges"].items():
                tempfollowedMap.append({"start":bridgeItem[0],"end":recommendItem[0]})
                temp_start_node = get_user_by_ID(bridgeItem[0])
                for followedID in  currentFollowdList:
                    temp_followed_node = get_user_by_ID(followedID)
                    if graph.match_one(start_node=temp_start_node,end_node=temp_followed_node,rel_type="FOLLOWS"):
                        #print "temp",bridgeItem[0],followedID
                        tempfollowedMap.append({"start":bridgeItem[0],"end":followedID})

        related_list.append(tempfollowedMap)
        limit -= 1
    #return recommendationList
    return related_list
# 你可能认识的朋友，共同好友数量排序

def you_may_know(userID,limit):
    user = get_user_by_ID(userID)
    if user == None:
        return None
    currentFriendList = []
    recommendFriendList = {}
    for rel in graph.match(start_node=user, rel_type="FOLLOWS",bidirectional=False):
        #是好友
        #print rel.end_node["userID"]
        currentFriendList.append(rel.end_node["userID"])
    for rel in graph.match(start_node=user, rel_type="FOLLOWS",bidirectional=False):
        for newrel in graph.match(start_node=rel.end_node,rel_type="FOLLOWS",bidirectional=True):
            newstartnodeID = newrel.start_node["userID"]
            newendnodeID = newrel.end_node["userID"]
            if newendnodeID == userID or (newendnodeID in currentFriendList):
                continue
            if(recommendFriendList.has_key(newendnodeID)):
                recommendFriendList[newendnodeID]["degree"] += 1
                if (recommendFriendList[newendnodeID]["bridges"].has_key(newstartnodeID)):
                    recommendFriendList[newendnodeID]["bridges"][newstartnodeID] += 1
                else:
                    recommendFriendList[newendnodeID]["bridges"][newstartnodeID] = 1
            else:
                recommendFriendList[newendnodeID] = {}
                recommendFriendList[newendnodeID]["degree"] = 1
                recommendFriendList[newendnodeID]["bridges"] = {newstartnodeID:1}
    for recommendItem in sorted(recommendFriendList.items(),lambda t1,t2:cmp(t1[1]["degree"],t2[1]["degree"]),reverse=True):
        if(limit<=0):
            break
        print recommendItem[0],'>',recommendItem[1]
        limit -=1
def group_your_friend(userID):
    user = get_user_by_ID(userID)
    if user == None:
        return
    allFriends=[]
    for rel in graph.match(start_node=user, rel_type="FOLLOWS",bidirectional=False):
        allFriends.append(rel.end_node)
    if allFriends == []:
        return
    groups = []
    while(allFriends!=[]):
        newGroup = []
        currentFriend = allFriends[0]
        newGroup.append(currentFriend)
        allFriends.remove(currentFriend)
        for friend in allFriends:
            for currentMember in newGroup:
                a = currentMember._id
                b = friend._id
                if a == b:
                    continue
                query_string = "START beginning=node(%d), end=node(%d) MATCH p = shortestPath(beginning-[*..3]-end) RETURN p"%(a,b)
                result = graph.cypher.execute(query_string)
                isFriend = False
                if result:
                    result = result.to_subgraph()
                    isFriend = True
                    for node in result.nodes:
                        if node == user:
                            isFriend = False
                if isFriend:
                    #print friend["userID"]," is friend of ",currentMember["userID"]
                    allFriends.remove(friend)
                    newGroup.append(friend)
        groups.append(newGroup)
    for group in groups:
        print "===group"
        for member in group:
            print member


if __name__ == "__main__":
    userID=raw_input('请输入1-400 的用户ID：')
    userID = int(userID)
    if(userID>0 and userID <= 400):
        print "可能感兴趣的博主"
        recommend_friend_by_ID(userID,10)
        print "可能认识的好友"
        you_may_know(userID,10)
        print "好友分组"
        group_your_friend(userID)
    else:
        print "输入错误"