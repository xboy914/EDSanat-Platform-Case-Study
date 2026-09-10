from django.test import override_settings
from rest_framework.test import APIClient

from .models import OTPChallenge


@override_settings(DEBUG=True)
def test_phone_otp_jwt_flow():
    client = APIClient()
    issued = client.post("/api/auth/otp/request/", {"phone_number": "+31612345678"}, format="json")
    assert issued.status_code == 201
    code = issued.json()["development_code"]

    verified = client.post(
        "/api/auth/otp/verify/",
        {"phone_number": "+31612345678", "code": code},
        format="json",
    )
    assert verified.status_code == 200
    assert verified.json()["user"]["role"] == "customer"

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {verified.json()['access']}")
    assert client.get("/api/auth/me/").json() == {
        "phone_number": "+31612345678",
        "role": "customer",
    }


@override_settings(DEBUG=False)
def test_production_response_never_exposes_code():
    response = APIClient().post(
        "/api/auth/otp/request/", {"phone_number": "+31612345679"}, format="json"
    )
    assert "development_code" not in response.json()


@override_settings(DEBUG=True)
def test_code_is_single_use():
    client = APIClient()
    issued = client.post("/api/auth/otp/request/", {"phone_number": "+31612345670"}, format="json")
    payload = {"phone_number": "+31612345670", "code": issued.json()["development_code"]}
    assert client.post("/api/auth/otp/verify/", payload, format="json").status_code == 200
    assert client.post("/api/auth/otp/verify/", payload, format="json").status_code == 401
    assert OTPChallenge.objects.get(phone_number="+31612345670").consumed_at is not None
