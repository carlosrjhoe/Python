import pytest
from pytest import fixture
from src.service.service_user import ServiceUser


@fixture
def service_user_page():
    return ServiceUser()
