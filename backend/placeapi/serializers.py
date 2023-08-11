from rest_framework import serializers
from .models import *

# class PlaceSubInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PlaceSubInfo
#         fields = "__all__"
#         read_only_fields = ('place')

class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = '__all__'
    
    image = serializers.ImageField(
        use_url=True,
        max_length=None
    )

    def create(self, validated_data):
        img = PlaceImage(image=validated_data['image'])
        img.save()
        return img
    
class PlaceCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceComment
        fields = '__all__'
    def create(self, validated_data):
        comment = PlaceComment(comment=validated_data['comment'])
        comment.save()
        return comment
    
class PlaceOpenStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceOpenStatus
        fields = '__all__'
    def create(self, validated_data):
        open_status = PlaceOpenStatus(open_status=validated_data['open_status'])
        open_status.save()
        return open_status
    
class PlaceRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceRating
        fields = '__all__'
    def create(self, validated_data):
        rating = PlaceRating(rating=validated_data['rating'])
        rating.save()
        return rating

class PlaceInfoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        allow_empty_file=True,
        required=False,
        use_url=True,
        max_length=None
    )
    id=serializers.ReadOnlyField()
    # ManyToMany(M2M, 중첩) 필드들은 serializer에서 필수 X (최초 등록 시)
    comments = PlaceCommentSerializer(many=True, allow_null=True, required=False)
    open_statuses = PlaceOpenStatusSerializer(many=True, allow_null=True, required=False)
    sub_images = PlaceImageSerializer(many=True, allow_null=True, required=False)
    ratings = PlaceRatingSerializer(many=True, allow_null=True, required=False)
    class Meta:
        model = PlaceInfo
        fields = [
            'id',
            'image',
            'name',
            'uploader',
            'created_at',
            'updated_at',
            'lat',
            'lng',
            'address',
            'contact',
            'homepage',
            'time',
            'description',
            'comments',
            'open_statuses',
            'sub_images',
            'ratings'
        ]

    def create(self, validated_data):
        place = PlaceInfo(
            image=validated_data['image'],
            name=validated_data['name'],
            uploader=validated_data['uploader'],
            created_at=validated_data['created_at'],
            updated_at=validated_data['updated_at'],
            lat=validated_data['lat'],
            lng=validated_data['lng'],
            address=validated_data['address'],
            contact=validated_data['contact'],
            homepage=validated_data['homepage'],
            time=validated_data['time'],
            description=validated_data['description']
        )
        place.save()
        return place
    

    
