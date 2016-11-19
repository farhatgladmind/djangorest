from django.http.response import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from expense_tracker.models import UserDetail, ExpenseDetail
from django.views.decorators.csrf import csrf_exempt
from expense_tracker.serializers import UserDetailSerializer,\
    ExpenseDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
import json, sys
from rest_framework import status
#####API call URL::: http://127.0.0.1:8000/expensetracker/user
#####API call URL::: http://127.0.0.1:8000/expensetracker/expense

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
@api_view(['GET', 'POST', ])
def user_list(request):
    if request.method == 'GET':
        user_obj = UserDetail.objects.all()
        user_serializer = UserDetailSerializer(user_obj, many=True)
        #return JSONResponse(user_serializer.data)
        return Response(user_serializer.data)
    
    elif request.method == 'POST':
        print request.body
        data = JSONParser().parse(request)
        serializer = UserDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                 
        return JSONResponse(serializer.errors, status=400)
    
#@csrf_exempt
@api_view(['GET', 'POST', ])
def expense_details(request):
    print "===================="
    print request.method
    print request.GET.get('id')
    print "===================="
    if request.method == 'GET':
        expense_obj = ExpenseDetail.objects.all()#.select_related('user_detail')
        expense_serializer = ExpenseDetailSerializer(expense_obj, many=True)
        print expense_serializer.data
        return JSONResponse(expense_serializer.data)
        # return Response(expense_serializer.data)
    elif request.method == 'POST':
        serializer = ExpenseDetailSerializer(data=request.data)
        print serializer
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=500)
                 
'''
request.data= if you will select "json" in body in POSTMAN 
{u'amount_spent': u'200', u'paid_for': u'Maid', u'balance': u'800', u'user_detail': u'1', u'description': u'paid for maid'}
============request.body= if you will select "text" in body in POSTMAN"
{  
"user_detail" : "1",
"amount_spent": "200",
"description": "paid for maid",
"balance": "800",
"paid_for":"Maid"
}
data = JSONParser().parse(request)
{u'amount_spent': u'200', u'paid_for': u'Maid', u'balance': u'800', u'user_detail': u'1', u'description': u'paid for maid'}
'''
    



#ew2908904
#EW278112725IN
#5293750712000764








        
