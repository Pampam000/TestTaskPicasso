from drf_yasg.utils import swagger_auto_schema
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import GenericViewSet

from .models import File
from .serializers import FileSerializer


class FileViewSet(CreateModelMixin,
                  ListModelMixin,
                  GenericViewSet):
    queryset = File.objects.all().order_by('-id')
    serializer_class = FileSerializer

    parser_classes = (MultiPartParser,)

    @swagger_auto_schema()
    def create(self, request, **kwargs):
        """ Uploading a file to the server

        ## Parameters:
        - #### file: file object (required) - The file to be uploaded to the server.

        ## Returns:
        - #### New file

        ## Example:

        #### POST /upload
        #### Content-Type: multipart/form-data

        #### {
        #### "file": \<file object\>
        #### }
        """
        return super().create(request, **kwargs)

    @swagger_auto_schema()
    def list(self, request, *args, **kwargs):
        """ Getting list of files

        ## Example:

        #### GET /files
        #### Content-Type: application/json

        ## Returns:
        - #### list of files in reverse order
        """
        return super().list(request, *args, **kwargs)
