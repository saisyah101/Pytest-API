import pytest
import requests
from tests.pages.airport_page import AirportPage
from tests.pages.auth import AuthClient


@pytest.fixture()
def base_url():
    return "https://airportgap.com/api"

@pytest.fixture()
def session():
    return requests.session()

@pytest.fixture()
def airport_api(base_url, session):
    return AirportPage(base_url, session)

@pytest.fixture()
def auth_client(base_url, session):
    return AuthClient(base_url, session)

@pytest.fixture()
def authenticated_client_fav(auth_client):
    auth_client.get_token("apitestairports@mailinator.com","APItestDummy")
    return auth_client

@pytest.fixture()
def authenticated_airport_api(base_url, authenticated_client_fav):
    return AirportPage(base_url, authenticated_client_fav.session)





# @pytest.fixture(scope="session")
# def authorized_session(base_url):
#     session = requests.Session()
#     session.headers.update({"Accept": "application/json"})
#
#     auth = AuthClient(base_url, session)
#     token = auth.get_token("apitestairports@mailinator.com", "APItestDummy")
#
#     session.headers.update({"Authorization": f"Bearer {token}"})
#     return session

