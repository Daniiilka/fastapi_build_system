from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_mock_tasks():
    response = client.post('get_tasks', json={"build": "test"})
    assert response.text == "[\"test2\",\"test3\",\"test1\",\"test2\",\"test3\",\"test6\",\"test5\",\"test4\"]"


def test_get_real_tasks():
    response = client.post('get_tasks', json={"build": "forward_interest"})
    assert response.text == '["build_teal_leprechauns","enable_yellow_centaurs","bring_olive_centaurs",' \
                            '"coloring_white_centaurs","create_teal_centaurs","design_lime_centaurs",' \
                            '"train_purple_centaurs","upgrade_navy_centaurs","create_maroon_centaurs",' \
                            '"bring_blue_centaurs","read_yellow_centaurs","upgrade_navy_centaurs",' \
                            '"create_olive_centaurs","coloring_aqua_centaurs","coloring_aqua_golems",' \
                            '"coloring_navy_golems","map_black_leprechauns","upgrade_white_leprechauns",' \
                            '"map_olive_leprechauns","enable_lime_leprechauns","map_black_leprechauns",' \
                            '"upgrade_white_leprechauns","map_olive_leprechauns","enable_lime_leprechauns",' \
                            '"create_aqua_humans","enable_olive_humans","build_maroon_humans","write_silver_humans",' \
                            '"write_white_humans","create_purple_humans","train_white_humans","write_teal_humans",' \
                            '"enable_silver_humans","bring_blue_ogres","design_white_ogres","train_green_ogres",' \
                            '"upgrade_aqua_ogres","write_silver_ogres","enable_fuchsia_ogres","bring_green_ogres",' \
                            '"build_yellow_ogres","create_maroon_ogres","design_green_ogres","upgrade_navy_ogres",' \
                            '"write_blue_ogres","write_fuchsia_golems"]'


def test_get_non_existent_build():
    response = client.post('get_tasks', json={"build": "None"})
    assert response.status_code == 404
    assert response.json() == {"detail": "No tasks found"}


def test_get_task_by_get_method():
    response = client.get('get_tasks')
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


def test_get_non_existed_endpoint():
    response = client.post('get_something_else', json={"build": "test"})
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}


def test_get_non_existent_field():
    response = client.post('get_tasks', json={"wrong_field": "forward_interest"})
    assert response.status_code == 422
    assert response.json() == {
        'detail': [{'loc': ['body', 'build'], 'msg': 'field required', 'type': 'value_error.missing'}]}


def test_get_empty_field():
    response = client.post('get_tasks', json={})
    assert response.status_code == 422
    assert response.json() == {
        'detail': [{'loc': ['body', 'build'], 'msg': 'field required', 'type': 'value_error.missing'}]}
