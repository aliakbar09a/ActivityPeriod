from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Count
from .models import ActivityPeriod
import hashlib
import json

# def send(request):
#     activities = ActivityPeriod.objects.
#     # act_list = serializers.serialize('json', activities)
#     print(activities)
#     return HttpResponse(activities, content_type="text/json")

def convertTime(date):
    return date.strftime("%b %d %Y %I:%M%p")

def send(request):
    final = {'ok':True, 'members':[]}
    users = {}
    activities = ActivityPeriod.objects.all()
    for obj in activities:
        # print(obj.real_name)
        user, tz = obj.real_name, obj.tz
        entry = {'start_time':convertTime(obj.start_time), 'end_time':convertTime(obj.end_time)}
        if (user, tz) not in users:
            users[(user, tz)] = []
        users[(user, tz)].append(entry)
    for user in users:
        unique = hashlib.sha224(json.dumps((user, tz)).encode()).hexdigest()[:10]
        member = {'id':unique, 'real_name': user[0], 'tz':user[1], 'activity_periods':users[user]}
        final['members'].append(member)
    # output = serializers.serialize('json', final)
    output = json.dumps(final, indent=4)
    return HttpResponse(output, content_type="application/json")