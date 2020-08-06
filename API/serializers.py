from rest_framework import serializers
from API.models import Posts

class PostSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ["post_title", "post_description"]