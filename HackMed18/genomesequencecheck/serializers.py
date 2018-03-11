from rest_framework import serializers

from .models import GenomeIndicator, Bacteria, FileUpload

class GenomeIndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenomeIndicator
        fields = "__all__"

class BacteriaSerializer(serializers.ModelSerializer):
    genomes = GenomeIndicatorSerializer(read_only=True, many=True)

    class Meta:
        model = Bacteria
        fields = "__all__"

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ('pk', 'encodedFile', )
