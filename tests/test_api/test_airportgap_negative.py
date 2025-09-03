import pytest

# negative
@pytest.mark.parametrize("status, page", [(404, 0), (404, -1)])
def test_get_airports_invalid_pagination(airport_api, status, page):
    airport_api.check_status_and_data(status, page)


# negative
@pytest.mark.parametrize("airport_id",
                         [("nRt"),
                          ("DUMMY"),
                          ("DOHA"),
                          ("cgk")])
def test_get_airports_by_invalid_id(airport_api, airport_id):
    get_invalid_airport = airport_api.get_airport_by_id(airport_id)
    assert get_invalid_airport.status_code == 404
    response = get_invalid_airport.json()
    assert response['errors'][0]['detail'] == "The page you requested could not be found"
# negative
@pytest.mark.parametrize("from_airport, to_airport",
                         [("CGK", ""),
                          ("", "CGK"),
                          ("cgk", "nrt"),
                          ("CGK", "DUMMY")])
def test_airports_distance_invalid_param(airport_api, from_airport, to_airport):
    get_distance = airport_api.post_airports_distance(from_airport, to_airport)
    assert get_distance.status_code == 422
    response = get_distance.json()
    assert response['errors'][0]['detail'] == "Please enter valid 'from' and 'to' airports."

def test_get_favorites_not_authorized(airport_api):
    get_favorites = airport_api.get_favorites()
    assert get_favorites.status_code == 401
    response = get_favorites.json()
    assert response['errors'][0]['detail'] == "You are not authorized to perform the requested action."

def test_invalid_token(auth_client):
    get_invalid_token = auth_client.get_token("mail@mail.com", "dummypassword")
    assert get_invalid_token.status_code ==401

# negative
def test_post_favorites_duplicate(authenticated_airport_api):
    post_fav = authenticated_airport_api.post_favorites("CGK")
    assert post_fav.status_code == 422
    response = post_fav.json()
    assert response['errors'][0]['detail'] == "Airport This airport is already in your favorites"

def test_delete_favorites(authenticated_airport_api):
    delete_fav = authenticated_airport_api.delete_favorites("37901")
    assert delete_fav.status_code == 404

