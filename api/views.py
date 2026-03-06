from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Work
from .serializers import TaskSerializer

@api_view(['GET'])
def g_t(request, pk):
    tasks = Work.objects.get(pk=pk)
    serializer = TaskSerializer(tasks)
    return Response(serializer.data)

@api_view(['POST'])
def c_t(request):
    serializer = TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)

@api_view(['PUT'])
def u_t(request, pk):
    task = Work.objects.get(pk=pk)
    serializer = TaskSerializer(task, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def d_t(request, pk):
    task = Work.objects.get(pk=pk)
    task.delete()
    return Response(status=204)