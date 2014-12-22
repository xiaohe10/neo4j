# This Python file uses the following encoding: utf-8
__author__ = 'xiaohe'

from py2neo import Graph
graph = Graph()
from py2neo import Node, Relationship
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
def recommend_friend_by_ID(userID):
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
        print "start user",userID," end ",rel.end_node["userID"]
        currentFollowdList.append(rel.end_node["userID"])
        currentFollowMap.append({"start":userID,"end":rel.end_node["userID"]})
        startnodes = graph.match(end_node=rel.end_node,rel_type="FOLLOWS")
        for newrel in startnodes:
            startnode = newrel.start_node
            temp_user_ID = startnode["userID"]
            if(temp_user_ID == userID):
                continue
            if(nodeCountDict.has_key(temp_user_ID)):
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
        # 共同关注者数量可以看做推荐度，推荐度可以叠加
        similarNode = graph.find_one("user","userID",similarNodeId)
        tempfollowedMap = []
        for rel in graph.match(start_node=similarNode, rel_type="FOLLOWS"):
            #print "start",similarNodeId," end ",rel.end_node["userID"]
            #tempfollowedMap.append({"start":similarNodeId,"end":rel.end_node["userID"]})
            if (not rel.end_node["userID"] in currentFollowdList):
                if(recommendationList.has_key(rel.end_node["userID"] )):
                    recommendationList[rel.end_node["userID"]] += recommendDegree
                else:
                    recommendationList[rel.end_node["userID"]] = recommendDegree

    for recommendItem in sorted(recommendationList.items(),lambda t1,t2:cmp(t1[1],t2[1]),reverse=True):
        if recommendItem[1] > 4:
            print recommendItem[0],'>', recommendItem[1]
            tempfollowedMap.append({"start":userID,"end":recommendItem[0]})
        related_list.append(tempfollowedMap)
    #return recommendationList
    return related_list

if __name__ == "__main__":
    recommend_friend_by_ID(76392)