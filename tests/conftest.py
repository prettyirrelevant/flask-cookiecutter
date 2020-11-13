from pathlib import Path

import pytest
import settings
from src import create_app


@pytest.fixture
def app(tmp_path):
    app = create_app(settings)
    app.config["BASE_DIR"] = tmp_path

    yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        return client


@pytest.fixture
def cli_runner(app):
    return app.test_cli_runner()
