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
    start_userID = 2
    if request.GET.has_key('startUser'):
        try:
            start_userID = int(request.GET['startUser'])
            if start_userID< 1 or start_userID > 400:
                start_userID = 2
        except:
            start_userID = 2
    relatedList = recommend_friend_by_ID(start_userID)
    return render(request,"recommendationview.html",locals())

