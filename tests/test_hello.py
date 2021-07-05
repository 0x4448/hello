#!/usr/bin/env python3

import json


def test_limit_within_bounds(client, monkeypatch):
    monkeypatch.setenv("LIMIT", str(1))
    r = client.get("/")
    assert r.status == "200 OK"


def test_limit_exceeded(client, monkeypatch):
    monkeypatch.setenv("LIMIT", str(1))
    r = client.get("/")
    assert r.status == "500 INTERNAL SERVER ERROR"


def test_index_returns_valid_json(client):
    r = client.get("/")
    assert json.loads(r.data)


def test_index_error_rate_0_returns_200(client, monkeypatch):
    monkeypatch.setenv("ERROR_RATE", str(0))
    r = client.get("/")
    assert r.status == "200 OK"


def test_index_error_rate_100_returns_500(client, monkeypatch):
    monkeypatch.setenv("ERROR_RATE", str(100))
    r = client.get("/")
    assert r.status == "500 INTERNAL SERVER ERROR"


def test_index_invalid_error_rate_is_ignored(client, monkeypatch):
    monkeypatch.setenv("ERROR_RATE", "invalid")
    r = client.get("/")
    assert r.status == "200 OK"


def test_env_returns_valid_json(client):
    r = client.get("/env")
    assert json.loads(r.data)


def test_counter_increment(client):
    c1 = json.loads(client.get("/").data).get("counter")
    c2 = json.loads(client.get("/").data).get("counter")
    assert c2 == c1 + 1
