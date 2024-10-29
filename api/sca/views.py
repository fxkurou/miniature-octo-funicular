from rest_framework import generics, mixins, status
from rest_framework.response import Response

from .serializers import SpyCatSerializer, MissionSerializer, TargetSerializer
from .models import SpyCat, Mission, Target


class SpyCatListCreateView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SpyCatDetailView(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
):

    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MissionListCreateView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MissionDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


