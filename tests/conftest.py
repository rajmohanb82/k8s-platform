
import importlib.util
from pathlib import Path

import pytest


@pytest.fixture
def client():
    app_path = (
        Path(__file__).resolve().parents[1]
        / "app"
        / "app.py"
    )

    spec = importlib.util.spec_from_file_location(
        "platformops_app", app_path
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    module.app.config["TESTING"] = True

    with module.app.test_client() as test_client:
        yield test_client
