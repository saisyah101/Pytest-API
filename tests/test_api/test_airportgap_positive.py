import pytest

def test_get_airports_success(airport_api):
    get_airport = airport_api.check_status_and_data(200)
    assert len(get_airport.json()['data']) > 0

@pytest.mark.parametrize("status, page",[(200,2),(200,20),(200,200),(200,203)])
def test_get_airports_valid_pagination(airport_api, status, page):
    get_airport = airport_api.check_status_and_data(status,page)
    response = get_airport.json()
    assert len(response['data']) > 0

@pytest.mark.parametrize("status, page",[(200,205),(200,300),(200,500)])
def test_get_airports_valid_pagination_no_data(airport_api, status, page):
    get_airport = airport_api.check_status_and_data(status,page)
    response = get_airport.json()
    assert len(response['data']) == 0


@pytest.mark.parametrize("airport_id, expected_name",
                         [("NRT", "Narita International Airport"),
                          ("SWQ", "Sumbawa Besar Airport"),
                          ("CGK", "Soekarno-Hatta International Airport"),
                          ("DOH", "Hamad International Airport"),
                          ("GRX", "Federico Garcia Lorca Airport")])
def test_get_airports_by_id(airport_api, airport_id, expected_name):
    get_airport_by_id = airport_api.get_airport_by_id(airport_id)
    assert get_airport_by_id.status_code == 200
    response = get_airport_by_id.json()
    assert response['data']['id'] == airport_id
    assert response['data']['attributes']['name'] == expected_name

@pytest.mark.parametrize("from_airport, to_airport, from_name, to_name",
                         [("CGK", "NRT", "Soekarno-Hatta International Airport", "Narita International Airport"),
                          ("CGK", "DOH", "Soekarno-Hatta International Airport", "Hamad International Airport"),
                          ("GRX", "CGK", "Federico Garcia Lorca Airport", "Soekarno-Hatta International Airport"),
                          ("SWQ", "CGK", "Sumbawa Besar Airport", "Soekarno-Hatta International Airport"),
                          ("DOH", "GRX", "Hamad International Airport", "Federico Garcia Lorca Airport")])
def test_airports_distance(airport_api, from_airport, to_airport, from_name, to_name):
    get_distance = airport_api.post_airports_distance(from_airport, to_airport)
    assert get_distance.status_code == 200
    response = get_distance.json()
    airport_id = f"{from_airport}-{to_airport}"
    assert response['data']['id'] == airport_id
    assert response['data']['attributes']['from_airport']['name'] == from_name
    assert response['data']['attributes']['to_airport']['name'] == to_name
    assert response['data']['attributes']['kilometers']>0


@pytest.mark.parametrize("airport_id, airport_name",
                         [("NRT", "Narita International Airport"),
                          ("CGK", "Soekarno-Hatta International Airport"),
                          ("GRX", "Federico Garcia Lorca Airport"),
                          ("SWQ", "Sumbawa Besar Airport"),
                          ("DOH", "Hamad International Airport")])
def test_airports_distance_zero(airport_api, airport_id, airport_name):
    get_distance = airport_api.post_airports_distance(airport_id, airport_id)
    assert get_distance.status_code == 200
    response = get_distance.json()
    airport_id = f"{airport_id}-{airport_id}"
    assert response['data']['id'] == airport_id
    assert response['data']['attributes']['from_airport']['name'] == airport_name
    assert response['data']['attributes']['to_airport']['name'] == airport_name
    assert response['data']['attributes']['kilometers'] == 0

def test_get_favorites(authenticated_airport_api):
    airport_code = ("CGK","NRT")
    get_favorites = authenticated_airport_api.get_favorites()
    assert get_favorites.status_code == 200
    response = get_favorites.json()
    assert response['data'][0]['attributes']['airport']['iata'] in airport_code

def test_get_favorites_by_id(authenticated_airport_api):
    fav_id = "37896"
    note = "International Airport in Jakarta Indonesia"
    get_fav_id = authenticated_airport_api.get_favorites_by_id(fav_id)
    assert get_fav_id.status_code == 200
    response = get_fav_id.json()
    assert response['data']['id'] == fav_id
    assert response['data']['type'] == "favorite"
    assert response['data']['attributes']['airport']['iata'] == "CGK"
    assert response['data']['attributes']['note'] == note

