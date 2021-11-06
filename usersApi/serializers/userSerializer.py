from rest_framework import serializers
from usersApi.models.user import User
from usersApi.models.account import Account
from usersApi.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'role', 'account']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
            'email': user.email,
            'name': user.name,
            'role': user.role,
            'account': {
                'id': account.id,
                'balance': account.balance,
                'lastChangeDate': account.lastChangeDate,
                'isActive': account.isActive
            }
        }