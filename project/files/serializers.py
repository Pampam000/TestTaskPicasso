from rest_framework import serializers

from .models import File
from .tasks import save_file_task


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'file', 'uploaded_at', 'processed')
        read_only_fields = ('processed',)

    def create(self, validated_data):
        file = validated_data.pop('file')
        instance = File.objects.create(file=file,
                                       **validated_data)

        save_file_task.delay(instance.id)
        return instance
