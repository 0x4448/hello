#!/usr/bin/env python3


def test_live_probe(client):
    r = client.get("/probes/live")
    assert r.status == "200 OK"


def test_ready_probe(client):
    r = client.get("/probes/ready")
    assert r.status == "200 OK"


def test_startup_probe(client):
    r = client.get("/probes/startup")
    assert r.status == "200 OK"
