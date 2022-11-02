import pytest
from simple_doh_client import doh_client


expected_ips = ["8.8.8.8", "8.8.4.4"].sort()
http_ok = 200


def test_google():
    """
    Google works as expected, and resolution of a basic query works
    """
    client = doh_client("https://dns.google/resolve?")
    result = client.query("dns.google", "A")

    assert result.status_code == http_ok
    assert expected_ips == result.get_answers().sort()


def test_cloudflare():
    """
    Cloudflare works as expected, and resolution of a basic query works
    """
    client = doh_client("https://cloudflare-dns.com/dns-query?")
    result = client.query("dns.google", "A")

    assert result.status_code == http_ok
    assert expected_ips == result.get_answers().sort()


def test_adguard():
    """
    Adguard works as expected, and resolution of a basic query works
    """
    client = doh_client("https://dns.adguard.com/resolve?")
    result = client.query("dns.google", "A")

    assert result.status_code == http_ok
    assert expected_ips == result.get_answers().sort()


def test_nextdns():
    """
    NextDNS works as expected, and resolution of a basic query works
    """
    client = doh_client("https://dns.nextdns.io/dns-query?")
    result = client.query("dns.google", "A")

    assert result.status_code == http_ok
    assert expected_ips == result.get_answers().sort()


def test_default():
    """
    A DNS server is selected by default, and resolution of a basic query works
    """
    client = doh_client()
    result = client.query("dns.google", "A")

    assert result.status_code == http_ok
    assert expected_ips == result.get_answers().sort()
