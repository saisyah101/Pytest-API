

class AirportPage:
    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session
        self.endpoint = f"{base_url}/airports"

    def get_airports(self, page=None):
        params = {}
        if page is not None:
            params['page'] = page
        return  self.session.get(self.endpoint, params=params)

    def check_status_and_data(self, expected_status, page=None):
        get_airport = self.get_airports(page)
        if isinstance(expected_status, int):
            expected_status = [expected_status]
        assert get_airport.status_code in expected_status, f"Expected {expected_status}, got {get_airport.status_code}"
        return get_airport

    def get_airport_by_id(self, airport_id):
        get_by_id_endpoint = f"{self.endpoint}/{airport_id}"
        return self.session.get(get_by_id_endpoint)

    def post_airports_distance(self, from_airport, to_airport):
        params = {'from': from_airport, 'to': to_airport}
        distance_endpoint = f"{self.endpoint}/distance"
        return self.session.post(distance_endpoint, params)

    def get_favorites(self):
        fav_endpoint = f"{self.base_url}/favorites"
        return self.session.get(fav_endpoint)

    def get_favorites_by_id(self, airport_id):
        fav_endpoint = f"{self.base_url}/favorites/{airport_id}"
        return self.session.get(fav_endpoint)

    def post_favorites(self, airport_id, note=None):
        fav_endpoint = f"{self.base_url}/favorites"
        params = {'airport_id': airport_id}
        if note is not None:
            params ['note'] = note
        return self.session.post(fav_endpoint, params)

    def delete_favorites(self, airport_id):
        delete_fav_endpoint = f"{self.base_url}/favorites/{airport_id}"
        return self.session.delete(delete_fav_endpoint)

    def patch_favorites(self, airport_id, note):
        params = {'note': note}
        patch_fav_endpoint = f"{self.base_url}/favorites/{airport_id}"
        return self.session.patch(patch_fav_endpoint, params)
