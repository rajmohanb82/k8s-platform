
def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_readiness_endpoint(client):
    response = client.get("/ready")
    assert response.status_code == 200


def test_application_info(client):
    response = client.get("/api/info")

    assert response.status_code == 200

    data = response.get_json()

    assert data is not None
    assert data["application"] == "PlatformOps"
    assert "hostname" in data
    assert "timestamp" in data
    assert "version" in data



def test_application_version(monkeypatch):
    import importlib.util
    from pathlib import Path

    monkeypatch.setenv("APP_VERSION", "v1.1.0")

    app_path = (
        Path(__file__).resolve().parents[1]
        / "app"
        / "app.py"
    )

    spec = importlib.util.spec_from_file_location(
        "platformops_version_test", app_path
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    module.app.config["TESTING"] = True

    with module.app.test_client() as client:
        response = client.get("/api/info")

    assert response.status_code == 200
    assert response.get_json()["version"] == "v1.1.0"

