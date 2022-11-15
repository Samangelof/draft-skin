from django.shortcuts import render
from django.forms import model_to_dict

from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from rest_framework.views import APIView

from django.contrib.auth.models import User


from friendship.models import Friend, Follow, Block

from django_messages_drf.views import InboxListApiView



from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import WarriorSerializer
from .models import Warrior, Category









# class WarriorViewSet(viewsets.ModelViewSet):
#     queryset = Warrior.objects.all()
#     serializer_class = WarriorSerializer

#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats':cats.name})

        
        



class WarriorAPIList(generics.ListCreateAPIView):
    queryset = Warrior.objects.all()[:3]    #первые три
    serializer_class = WarriorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class WarriorAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class WarriorAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
    permission_classes = (IsAdminOrReadOnly,)






# class WarriorAPIView(generics.ListAPIView):
#     queryset = Warrior.objects.all()
#     serializer_class = WarriorSerializer



# class WarriorAPIView(APIView):
#     def get(self, request):
#         all_warriors = Warrior.objects.all()
#         return Response({'warriors': WarriorSerializer(all_warriors, many=True).data})

#     def post(self, request):
#         serializer = WarriorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         warrior_new = Warrior.objects.create(
#             name = request.data['name'], 
#             specialization = request.data['specialization'],category_id = request.data['category_id'],)
#         return Response({'warrior': WarriorSerializer(warrior_new).data})


#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk: return Response({"error": "Method PUT not allowed"})

#         try: 
#             instance = Warrior.objects.get(pk=pk)
#         except: return Response({"error": "Object does not exists"})

#         serializer = WarriorSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk: return Response({"error": "Method DELETE not allowed"})
#         try: instance = Warrior.objects.get(pk=pk)
#         except: return Response({"error": "Object does not exists"})
#         instance.delete()
#         return Response({"delete": "Объект удален"})