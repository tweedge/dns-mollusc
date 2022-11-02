import pytest
from dns_mollusc import mollusc_client


def test_google():
    client = mollusc_client("https://dns.google/resolve?")
    result = client.query("malware.testcategory.com", "A")

    assert result.is_blocked_by_server() == False


def test_cloudflare():
    client = mollusc_client("https://cloudflare-dns.com/dns-query?")
    result = client.query("malware.testcategory.com", "A")

    assert result.is_blocked_by_server() == False


def test_cloudflare_security():
    client = mollusc_client("https://security.cloudflare-dns.com/dns-query?")
    result = client.query("malware.testcategory.com", "A")

    assert result.is_blocked_by_server() == True


def test_cloudflare_family():
    client = mollusc_client("https://family.cloudflare-dns.com/dns-query?")
    result = client.query("nudity.testcategory.com", "A")

    assert result.is_blocked_by_server() == True


def test_adguard():
    client = mollusc_client("https://dns.adguard.com/resolve?")
    result = client.query("googleads.g.doubleclick.net", "A")

    assert result.is_blocked_by_server() == True


def test_nextdns():
    client = mollusc_client("https://dns.nextdns.io/dns-query?")
    result = client.query("googleads.g.doubleclick.net", "A")

    assert result.is_blocked_by_server() == False


def test_default():
    client = mollusc_client()
    result = client.query("malware.testcategory.com", "A")

    assert result.is_blocked_by_server() == True
