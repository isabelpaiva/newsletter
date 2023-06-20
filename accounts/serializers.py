from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    is_text_reviewer = serializers.BooleanField()
    is_superuser = serializers.BooleanField(default=False)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # create_user, create_superuser
        if validated_data.get('is_superuser'):
            account = Account.objects.create_superuser(**validated_data)
        else: 
            account = Account.objects.create_user(**validated_data)
        return account