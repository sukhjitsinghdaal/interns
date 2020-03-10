from .models import ProjectUser
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action

class UserViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = ProjectUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ProjectUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    @action(detail=False, methods=['post'], name='register-user', permission_classes=[])
    def register(self,request,pk=None):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                obj =  serializer.save()
                obj.set_password(request.data['password'])
                obj.save() 
                context = {"success": True, "message": "Register successfull"}
                return Response(context, status=status.HTTP_200_OK)
        
        except Exception as error:
            context = {'Success': False,"message":"Failed to create User","error":error }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=False ,methods = ['post'],name ="user-login" , permission_classes = [])
    # def login(self,request):
    #     try:
    #         # import ipdb; ipdb.set_trace()
    #         email = request.data['email']
    #         password = request.data['password']
    #         if not email and not password:
    #             raise("User or password missing")
    #         user = authenticate(username=email, password=password)
            
    #         if user is not None:
    #             try:
    #                 if user.is_active:
    #                     # import ipdb; ipdb.set_trace()
    #                     user_details = ProjectUser.objects.get(email=user.email)
    #                     update_last_login(None, user_details)
    #             except:
    #                 message = 'You are not intended to login into this system.'
    #                 context = {'success': False, 'message': message}
    #                 return Response(context, status.HTTP_403_FORBIDDEN)
    #             payload = jwt_payload_handler(user)
    #             token = jwt_encode_handler(payload)
    #             # expiration = datetime.utcnow(
    #             # ) + settings.JWT_AUTH['JWT_EXPIRATION_DELTA']
    #             # expiration_epoch = expiration.timestamp()
    #             serializer = self.serializer_class(user_details, fields=('id', 'email'))
    #             context = {'Success': True,"message":"login success" , "token":token,"token_type":"Bearer","data":serializer.data}
    #             return Response(context, status=status.HTTP_200_OK)
    #     except Exception as error:
    #         context = {'Success': False,"message":"Failed to login","error":error }
    #         return Response(context, status=status.HTTP_400_BAD_REQUEST)
    