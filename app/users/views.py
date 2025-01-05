from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from users.serializers import UserSerializer, AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer

class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrive and return and authenticated user"""
        return self.request.user

# class CognitoAuthView(APIView):
#     """Handle Cognito authentication and user creation/update"""
    
#     def post(self, request):
#         try:
#             # Get the Cognito ID token from request
#             id_token = request.data.get('id_token')
            
#             # Verify token with Cognito
#             client = boto3.client('cognito-idp')
#             response = client.get_user(
#                 AccessToken=id_token
#             )
            
#             # Extract user attributes
#             user_attrs = {attr['Name']: attr['Value'] for attr in response['UserAttributes']}
#             email = user_attrs.get('email')
#             name = user_attrs.get('name', '')
            
#             # Create or update user
#             user, created = get_user_model().objects.get_or_create(
#                 email=email,
#                 defaults={'name': name}
#             )
            
#             # Generate or get token for Django authentication
#             token, _ = Token.objects.get_or_create(user=user)
            
#             return Response({
#                 'token': token.key,
#                 'user': UserSerializer(user).data
#             })
            
#         except Exception as e:
#             return Response(
#                 {'error': str(e)}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )


