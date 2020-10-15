from rest_framework import serializers
from .models import Bank, Customer, LANGUAGE_CHOICES, STYLE_CHOICES

class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name', 'code']

        def create(self, validated_data):
            """
            Create and return a new `Bank` instance, given the validated data.
            """
            return Bank.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update and return an existing `Bank` instance, given the validated data.
            """
            instance.name = validated_data.get('name', instance.name)
            instance.code = validated_data.get('code', instance.code)
            instance.save()
            return instance

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name_customer', 'debit', 'credit']

        def create(self, validated_data):
            """
            Create and return a new `Customer` instance, given the validated data.
            """
            return Customer.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update and return an existing `Customer` instance, given the validated data.
            """
            instance.name_customer = validated_data.get('name_customer', instance.name_customer)
            instance.debit = validated_data.get('debit', instance.debit)
            instance.credit = validated_data.get('credit', instance.credit)
            instance.save()
            return instance


