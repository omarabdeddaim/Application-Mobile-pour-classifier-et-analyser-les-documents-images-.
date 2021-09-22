from rest_framework import serializers
from ..models import Photo
import base64 
import uuid
from django.core.files.base import ContentFile

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        print('data',data)
        _format, str_img = data.split(';base64')
        print('format',_format)
        print('str_img',str_img)
        print('type str_img',type( str_img))
        decoded_file = base64.b64decode(str_img)
        print('decoded_file',decoded_file)
        print('type decoded_file', type(decoded_file))
        fname = f"{str(uuid.uuid4())[:10]}.png"
        print('fname', fname)
        data = ContentFile(decoded_file, name=fname)
        return super().to_internal_value(data)
    

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image', 'result')
        
