import pytest
from app import application

@pytest.fixture()
def app():
    app = application
    app.config.update({
        "TESTING": True,
    })
    yield application

@pytest.fixture()
def client(app):
    return app.test_client()

#test
def test_status_200(client):
    response = client.post("/rate", data={
        "rate[energy]" : "0.3", "rate[time]" : "2", "rate[transaction]" : "1", "cdr[meterStart]" : "1204307", "cdr[timestampStart]" : "2021-04-05T10:04", "cdr[meterStop]" : "1215230", "cdr[timestampStop]" : "2021-04-05T11:27"
    })
    assert response.status_code == 200

def test_status_400(client):
    response = client.post("/rate", data={
        "rate[energy]" : "", "rate[time]" : "2", "rate[transaction]" : "1", "cdr[meterStart]" : "1204307", "cdr[timestampStart]" : "2021-04-05T10:04", "cdr[meterStop]" : "1215230", "cdr[timestampStop]" : "2021-04-05T11:27"
    })
    assert response.status_code == 400

def test_response(client):
    response = client.post("/rate", data={
        "rate[energy]" : "0.3", "rate[time]" : "2", "rate[transaction]" : "1", "cdr[meterStart]" : "1204307", "cdr[timestampStart]" : "2021-04-05T10:04", "cdr[meterStop]" : "1215230", "cdr[timestampStop]" : "2021-04-05T11:27"
    })
    assert response.data == b'{"components":{"energy":3.277,"time":2.767,"transaction":1.0},"overall":7.04}\n'