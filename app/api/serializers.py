from rest_framework import serializers

from cers.models import User, Attendance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'number', 'is_current_in')


class AttendanceSerializer(serializers.ModelSerializer):
    number = serializers.CharField(source='user.number')
    name = serializers.CharField(source='user.name')

    class Meta:
        model = Attendance
        fields = ('number', 'name', 'is_in', 'accepted_at')

    def create(self, validated_data):
        if not User.objects.all().filter(**validated_data['user']).exists():
            User.objects.create(**validated_data['user'])
        
        user = User.objects.all().filter(**validated_data['user']).get()
        attendance = Attendance.objects.create(
            user = user,
            is_in = validated_data['is_in'],
            accepted_at = validated_data['accepted_at']
        )

        return attendance
