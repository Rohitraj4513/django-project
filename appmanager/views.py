from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import App
from .serializers import AppSerializer

@api_view(["POST"])
def add_app(request):
    serializer = AppSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_apps(request):
    apps = App.objects.all()
    serializer = AppSerializer(apps, many=True)
    return Response(serializer.data)

@api_view(["DELETE"])
def delete_app(request, id):
    try:
        app = App.objects.get(id=id)
        app.delete()
        return Response({"message": "App deleted"}, status=status.HTTP_204_NO_CONTENT)
    except App.DoesNotExist:
        return Response({"error": "App not found"}, status=status.HTTP_404_NOT_FOUND)
