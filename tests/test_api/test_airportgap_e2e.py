import pytest

def test_post_favorites_then_delete(authenticated_airport_api):
    airport_id = "HLP"
    note = "Next travel destination"
    get_fav = authenticated_airport_api.get_favorites()
    assert len(get_fav.json()['data']) == 2
    post_fav = authenticated_airport_api.post_favorites(airport_id, note)
    assert post_fav.status_code == 201
    response = post_fav.json()
    assert response['data']['attributes']['airport']['iata'] == airport_id
    assert response['data']['attributes']['note'] == note
    id_to_delete = response['data']['id']
    delete_fav = authenticated_airport_api.delete_favorites(id_to_delete)
    assert delete_fav.status_code == 204
    get_fav = authenticated_airport_api.get_favorites()
    assert len(get_fav.json()['data']) == 2

def test_post_favorites_no_note_patch_note_then_delete(authenticated_airport_api):
    airport_id = "HLP"
    edited_note = "Note edited successfully"
    get_fav = authenticated_airport_api.get_favorites()
    assert len(get_fav.json()['data']) == 2
    post_fav = authenticated_airport_api.post_favorites(airport_id)
    assert post_fav.status_code == 201
    post_response = post_fav.json()
    assert post_response['data']['attributes']['airport']['iata'] == airport_id
    assert post_response['data']['attributes']['note'] is None
    new_fav_id = post_response['data']['id']
    patch_fav = authenticated_airport_api.patch_favorites(new_fav_id, edited_note)
    assert patch_fav.status_code == 200
    patch_response = patch_fav.json()
    assert patch_response['data']['attributes']['note'] == edited_note
    delete_fav = authenticated_airport_api.delete_favorites(new_fav_id)
    assert delete_fav.status_code == 204
    get_fav = authenticated_airport_api.get_favorites()
    assert len(get_fav.json()['data']) == 2