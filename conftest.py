#!/usr/bin/env python3

import pytest

from hello import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client
