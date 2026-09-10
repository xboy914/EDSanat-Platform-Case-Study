from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Profile
from .serializers import OTPVerifySerializer, PhoneSerializer
from .services import consume_challenge, issue_challenge


class OTPRequestView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request) -> Response:
        serializer = PhoneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        challenge, code = issue_challenge(serializer.validated_data["phone_number"])
        payload = {"challenge_id": challenge.id, "expires_in": 300}
        if settings.DEBUG:
            payload["development_code"] = code
        return Response(payload, status=status.HTTP_201_CREATED)


class OTPVerifyView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request) -> Response:
        serializer = OTPVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data["phone_number"]
        if not consume_challenge(phone, serializer.validated_data["code"]):
            return Response({"detail": "Invalid or expired code."}, status=status.HTTP_401_UNAUTHORIZED)
        user, _ = User.objects.get_or_create(username=phone)
        profile, _ = Profile.objects.get_or_create(user=user, defaults={"phone_number": phone})
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {"phone_number": profile.phone_number, "role": profile.role},
        })


class MeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request) -> Response:
        profile = request.user.profile
        return Response({"phone_number": profile.phone_number, "role": profile.role})
