import pytest
from dns_mollusc import mollusc_client


http_ok = 200


def test_google():
    client = mollusc_client("https://dns.google/resolve?")
    result = client.query("dns.google")

    assert result.status_code == http_ok


def test_cloudflare():
    client = mollusc_client("https://cloudflare-dns.com/dns-query?")
    result = client.query("dns.google")

    assert result.status_code == http_ok


def test_cloudflare_security():
    client = mollusc_client("https://security.cloudflare-dns.com/dns-query?")
    result = client.query("dns.google")

    assert result.status_code == http_ok


def test_cloudflare_family():
    client = mollusc_client("https://family.cloudflare-dns.com/dns-query?")
    result = client.query("dns.google")

    assert result.status_code == http_ok


def test_adguard():
    client = mollusc_client("https://dns.adguard.com/resolve?")
    result = client.query("dns.google")

    assert result.status_code == http_ok


def test_nextdns():
    client = mollusc_client("https://dns.nextdns.io/dns-query?")
    result = client.query("dns.google")

    assert result.status_code == http_ok


def test_default():
    client = mollusc_client()
    result = client.query("dns.google")

    assert result.status_code == http_ok
