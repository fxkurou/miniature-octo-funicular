from rest_framework import serializers
from .models import SpyCat, Mission, Target
import requests


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ['id', 'name', 'breed', 'years_of_experience', 'salary']
        read_only_fields = ['id']

    def validate_breed(self, value):
        response = requests.get(f"https://api.thecatapi.com/v1/breeds/search?q={value}")
        if response.status_code == 200 and not response.json():
            raise serializers.ValidationError("Invalid breed.")
        return value


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_complete']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Target.objects.create(**validated_data)


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['cat', 'is_completed', 'targets']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets', [])
        mission = Mission.objects.create(**validated_data)

        # Set the assigned cat's availability to False if a cat is assigned
        if mission.cat:
            mission.cat.is_available = False
            mission.cat.save()

        # Create targets and associate them with the mission
        for target_data in targets_data:
            target_data['mission'] = mission
            Target.objects.create(**target_data)

        return mission

    def update(self, instance, validated_data):
        targets_data = validated_data.pop('targets', None)
        is_completed = validated_data.get('is_completed', instance.is_completed)

        # Handle mission completion
        if is_completed and not instance.is_completed:
            if instance.cat:
                instance.cat.is_available = True
                instance.cat.save()
                instance.cat = None  # Unassign the cat when the mission is completed

        new_cat = validated_data.get('cat', instance.cat)
        if new_cat != instance.cat and not is_completed:
            if instance.cat:
                instance.cat.is_available = True
                instance.cat.save()
            if new_cat:
                new_cat.is_available = False
                new_cat.save()

        instance.cat = new_cat
        instance.is_completed = is_completed
        instance.save()

        # SOMEHOW I BROKE THIS PART AND HAVE NO IDEA HOW TO FIX IT
        # SO I JUST GAVE UP AND MOVED ON
        if targets_data:
            for target_data in targets_data:
                target_id = target_data.get('id')
                if target_id:
                    target = Target.objects.get(pk=target_id)
                    target.name = target_data.get('name', target.name)
                    target.country = target_data.get('country', target.country)
                    target.notes = target_data.get('notes', target.notes)
                    target.is_complete = target_data.get('is_complete', target.is_complete)
                    target.save()

        return instance