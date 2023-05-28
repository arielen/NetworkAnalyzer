from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_ping():
    response = client.post(
        "/ping", params={"res": "google.com", "count_pkt": 1})
    assert response.status_code == 200


def test_about_network_myip():
    response = client.get("/about_network/myip")
    assert response.status_code == 200
    assert response.json().get("external_ip")


def test_about_network_get_interfaces():
    response = client.get("/about_network/get_interfaces")
    assert response.status_code == 200
    assert len(response.json().get("interfaces")) > 0


def test_about_network_get_traffic():
    response = client.get("/about_network/get_traffic",
                          params={"strg_unit": "MB"})
    assert response.status_code == 200
    for param in ("bytes_sent", "bytes_recv", "begin_time", "end_time"):
        assert response.json().get(param, None)


def test_about_network_get_traffic_with_bad_params():
    response = client.get("/about_network/get_traffic",
                          params={"strg_unit": "asB"})
    assert response.status_code == 422


def test_eth_dump():
    response = client.get("/eth_dump/")
    assert response.status_code == 200


def test_eth_dump_extended():
    response = client.get("/eth_dump/port")
    assert response.status_code == 200


def test_eth_dump_bad_params():
    response = client.get("/eth_dump/get_traffic", params={"strg_unit": "asB"})
    assert response.status_code == 404
