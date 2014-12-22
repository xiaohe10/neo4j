from django.shortcuts import render

# Create your views here.
from web.models import *
from web.neo4j_lib.userModel import *




def view(request):
    start_userID = 1
    followedList = get_followdList_by_ID(start_userID)
    #for result in results:
    #    print result
    return render(request,"view.html",locals())

def viewRecommendation(request):
    start_userID = 4
    relatedList = recommend_friend_by_ID(start_userID)
    return render(request,"recommendationview.html",locals())