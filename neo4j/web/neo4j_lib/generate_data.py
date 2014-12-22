# This Python file uses the following encoding: utf-8
__author__ = 'xiaohe'

from userModel import *
import random
def generate_Users():
    #100 singers
    for i in range(1,101):
        user = User(userID = i,tags = "singer")
        user.save(unique= True)
    #100 athletes
    for i in range(101,201):
        user = User(userID = i,tags = "athlete")
        user.save()
    #100 scholars
    for i in range(201,301):
        user = User(userID = i,tags = "scholar")
        user.save()

    #100 scholars
    for i in range(301,401):
        user = User(userID = i,tags = "media")
        user.save()
def generate_Relationships():
    #every group have some random relationships
    for i in range(1,300):
        ID1 = random.randint(1,100)
        ID2 = random.randint(1,100)
        if(ID1 != ID2):
            userNode1 = get_user_by_ID(ID1)
            userNode2 = get_user_by_ID(ID2)
            user1 = User(node=userNode1)
            user1.follow(userNode2)
            user2 = User(node = userNode2)
            user2.follow(userNode1)
    for i in range(1,300):
        ID1 = random.randint(101,200)
        ID2 = random.randint(101,200)
        if(ID1 != ID2):
            userNode1 = get_user_by_ID(ID1)
            userNode2 = get_user_by_ID(ID2)
            user1 = User(node=userNode1)
            user1.follow(userNode2)
            user2 = User(node = userNode2)
            user2.follow(userNode1)
    for i in range(1,300):
        ID1 = random.randint(201,300)
        ID2 = random.randint(201,300)
        if(ID1 != ID2):
            userNode1 = get_user_by_ID(ID1)
            userNode2 = get_user_by_ID(ID2)
            user1 = User(node=userNode1)
            user1.follow(userNode2)
            user2 = User(node = userNode2)
            user2.follow(userNode1)
    for i in range(1,300):
        ID1 = random.randint(301,400)
        ID2 = random.randint(301,400)
        if(ID1 != ID2):
            userNode1 = get_user_by_ID(ID1)
            userNode2 = get_user_by_ID(ID2)
            user1 = User(node=userNode1)
            user1.follow(userNode2)
            user2 = User(node=userNode2)
            user2.follow(userNode1)

    for i in range(1,500):
        ID1 = random.randint(1,1000)
        ID1 = random.randint(1,1000)
        if(ID1 != ID2):
            userNode1 = get_user_by_ID(ID1)
            userNode2 = get_user_by_ID(ID2)
            user1 = User(node=userNode1)
            user1.follow(userNode2)
            user2 = User(node=userNode2)
            user2.follow(userNode1)

def show_Users():
    results = graph.find(label="user")
    for result in results:
        print result
def show_Relationships():
    start_node = get_user_by_ID(4)
    relationships = graph.match(start_node=start_node,rel_type="FOLLOWS")
    for rel in relationships:
        print rel.start_node["userID"],"->",rel.end_node["userID"]
    relationships = graph.match(end_node=start_node,rel_type="FOLLOWS")
    for rel in relationships:
        print rel.start_node["userID"],"->",rel.end_node["userID"]
#graph.delete_all()
#generate_Users()
#generate_Relationships()
#show_Users()
show_Relationships()