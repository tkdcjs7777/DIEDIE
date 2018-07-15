from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import GameUserInfo, Ranking
import json

@csrf_exempt 
def Login(request):
     if request.method == "POST":
         user_id = request.POST['user_id']
         user_password = request.POST['user_password']
         user_obj = GameUserInfo.objects.get(user_id=user_id)
         if user_obj:
             if user_obj.user_id == user_id and user_obj.user_password == user_password:
                 return JsonResponse({'sucess': 'true'})
         else:
             return JsonResponse({'sucess': 'false'})
                 
@csrf_exempt 
def Account(request):
     if request.method == "POST":
         user_id = request.POST['user_id']
         user_password = request.POST['user_password']
         GameUserInfo.objects.create(user_id=user_id, user_password=user_password)
         return JsonResponse({'sucess': 'true'})

@csrf_exempt
def GetRanking(request):

    #클리어 순서대로 가져오기
    rankingObj = Ranking.objects.all().order_by("clear_time")
    #json은 순서, 아이디, 클리어시간 
    JsonRankData = dict()
    seq = 1
    for obj in rankingObj:
        #temp = {'seq': seq, 'user_id': obj.user_id.user_id, 'clear_time': str(obj.clear_time)}
        #JsonRankData.update(temp)
        if len(JsonRankData) == 0:
            JsonRankData["rank"] = [{'seq': str(seq),'user_id': obj.user_id.user_id, 'clear_time': str(obj.clear_time)}]
        else:
            JsonRankData["rank"].append({'seq': str(seq),'user_id': obj.user_id.user_id, 'clear_time': str(obj.clear_time)})
        seq = seq+1
    print(json.dumps(JsonRankData))
    return JsonResponse(JsonRankData)
        


    




    
