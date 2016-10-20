from rest_framework import serializers 
from expense_tracker.models import UserDetail, ExpenseDetail

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ('id', 'user',  'address', 'created_date', 'modified_date')
        
        
class ExpenseDetailSerializer(serializers.ModelSerializer):
    print "exserializeddtrrrrrrr==================="
    class Meta:
        model = ExpenseDetail
        
#         fields = ('id','user_detail','amount_spent',  'paid_for', 'paid_date', 'description','payment_mode',
#                   'balance','created_date', 'modified_date'
#                   )
        
       
        