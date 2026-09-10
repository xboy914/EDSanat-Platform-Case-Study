import hashlib
import secrets
from datetime import timedelta

from django.conf import settings
from django.utils import timezone

from .models import OTPChallenge


def _digest(phone_number: str, code: str) -> str:
    value = f"{settings.SECRET_KEY}:{phone_number}:{code}".encode()
    return hashlib.sha256(value).hexdigest()


def issue_challenge(phone_number: str) -> tuple[OTPChallenge, str]:
    OTPChallenge.objects.filter(phone_number=phone_number, consumed_at=None).update(
        consumed_at=timezone.now()
    )
    code = f"{secrets.randbelow(1_000_000):06d}"
    challenge = OTPChallenge.objects.create(
        phone_number=phone_number,
        code_digest=_digest(phone_number, code),
        expires_at=timezone.now() + timedelta(minutes=5),
    )
    return challenge, code


def consume_challenge(phone_number: str, code: str) -> bool:
    challenge = (
        OTPChallenge.objects.filter(phone_number=phone_number, consumed_at=None)
        .order_by("-created_at")
        .first()
    )
    if challenge is None or challenge.expires_at <= timezone.now() or challenge.attempts >= 5:
        return False
    challenge.attempts += 1
    valid = secrets.compare_digest(challenge.code_digest, _digest(phone_number, code))
    if valid:
        challenge.consumed_at = timezone.now()
    challenge.save(update_fields=["attempts", "consumed_at"])
    return valid
