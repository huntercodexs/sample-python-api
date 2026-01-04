from app.api.user_api_impl import UserApiImpl
from server.apis.default_api_base import BaseDefaultApi
from server.main import app as generated_app

generated_app.dependency_overrides[BaseDefaultApi] = UserApiImpl

app = generated_app