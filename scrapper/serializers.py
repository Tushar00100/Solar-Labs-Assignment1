from rest_framework import serializers
'''
This Function will create a serializers class to define the field to that want to include in JSON response

'''
class CountryInfoSerializer(serializers.Serializer): 
    flag_link = serializers.URLField() 
    capital = serializers.ListField(child=serializers.CharField()) 
    largest_city = serializers.CharField() 
    official_languages = serializers.ListField(child=serializers.CharField()) 
    area_total = serializers.IntegerField() 
    population = serializers.CharField() 
    GDP_nominal = serializers.CharField()
