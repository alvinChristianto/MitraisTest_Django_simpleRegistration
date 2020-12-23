from rest_framework import serializers 
from registerApp.models import Register
 
class RegisterSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Register
        fields = ('id',
                  'firstname',
                  'lastname',
                  'email',
                  'mobilenumber',
                  'dateofbirth',
                  'gender',
                  'created_time')