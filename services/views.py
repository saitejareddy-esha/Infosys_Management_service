from rest_framework import generics
from .models import Dataset, DataElement
from .serializers import DatasetSerializer, DataElementSerializer

class DatasetListCreateView(generics.ListCreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


class DatasetDetailView(generics.RetrieveAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


class DataElementListCreateView(generics.ListCreateAPIView):
    serializer_class = DataElementSerializer

    def get_queryset(self):
        return DataElement.objects.filter(dataset_id=self.kwargs['dataset_id'])

    def perform_create(self, serializer):
        serializer.save(dataset_id=self.kwargs['dataset_id'])
