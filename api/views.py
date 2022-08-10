from django.shortcuts import render,redirect
from django.http import JsonResponse,Http404


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(["GET"])
def apiOverview(request):

	api_urls = {
		'List[GET]': '/tasks/',
		'Create[POST]': '/tasks/',
		'Detail View[GET]': '/tasks/<int:pk>/',
		'Update[PUT]': '/tasks/<int:pk>/',
		'Delete[PUT]': '/tasks/<int:pk>/',
	}

	return Response(api_urls)


class TaskList(APIView):
	"""
	List all tasks, or create a new snippet.
	"""

	def get(self, request, format=None):
		tasks = Task.objects.all()
		serializer = TaskSerializer(tasks, many = True)

		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = TaskSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
	"""
	Retrieve, update or delete a snippet instance.
	"""
	def get_object(self, pk):
		try:
			return Task.objects.get(pk=pk)
		except Task.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		task = self.get_object(pk)
		serializer = TaskSerializer(task)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		task = self.get_object(pk)
		serializer = TaskSerializer(task, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		task = self.get_object(pk)
		task.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)