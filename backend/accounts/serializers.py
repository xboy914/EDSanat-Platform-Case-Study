import re

from rest_framework import serializers


class PhoneSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=16)

    def validate_phone_number(self, value: str) -> str:
        normalized = value.replace(" ", "").replace("-", "")
        if not re.fullmatch(r"\+?[1-9]\d{9,14}", normalized):
            raise serializers.ValidationError("Use E.164-compatible phone format.")
        return normalized


class OTPVerifySerializer(PhoneSerializer):
    code = serializers.RegexField(r"^\d{6}$")
