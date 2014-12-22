# This Python file uses the following encoding: utf-8
__author__ = 'xiaohe'

from userModel import *
import json

def read_data_from_file():
    file = open('/Users/xiaohe/Desktop/users_relation.json')
    for line in file.readlines():

        record = json.loads(line)
        userID =  record["_id"]
        followlist =  record["ids"]
        if(followlist == []):
            continue
        # 判断userNode 是否已经存在 graph中了
        user = get_user_by_ID(userID)
        if(not user):
            print userID
            userNode = Node("user", userID=userID)
            graph.create(userNode)
        for follow in followlist:
            try:
                follow = int(follow)
            except:
                follow = int(follow[u"$numberLong"])
            followed = get_user_by_ID(follow)
            if(not followed):
                print "--",follow
                followNode =  Node("user", userID=follow)
                graph.create(followNode)
            followship = Relationship(userNode, "FOLLOWS", followNode)
            graph.create(followship)

if __name__ == "__main__":
    graph.delete_all()
    #read_data_from_file()