import pytest
from dns_mollusc import mollusc_client


def test_google_A():
    client = mollusc_client("https://dns.google/resolve?")
    result = client.query("malware.testcategory.com", "A")

    assert result.is_blocked_by_server() == False


def test_google_AAAA():
    client = mollusc_client("https://dns.google/resolve?")
    result = client.query("malware.testcategory.com", "AAAA")

    assert result.is_blocked_by_server() == False


def test_cloudflare_A():
    client = mollusc_client("https://cloudflare-dns.com/dns-query?")
    result = client.query("malware.testcategory.com", "A")

    assert result.is_blocked_by_server() == False


def test_cloudflare_AAAA():
    client = mollusc_client("https://cloudflare-dns.com/dns-query?")
    result = client.query("malware.testcategory.com", "AAAA")

    assert result.is_blocked_by_server() == False


def test_cloudflare_security_A():
    client = mollusc_client("https://security.cloudflare-dns.com/dns-query?")
    result = client.query("malware.testcategory.com", "A")

    assert result.is_blocked_by_server() == True


def test_cloudflare_security_AAAA():
    client = mollusc_client("https://security.cloudflare-dns.com/dns-query?")
    result = client.query("malware.testcategory.com", "AAAA")

    assert result.is_blocked_by_server() == True


def test_cloudflare_family_A():
    client = mollusc_client("https://family.cloudflare-dns.com/dns-query?")
    result = client.query("nudity.testcategory.com", "A")

    assert result.is_blocked_by_server() == True


def test_cloudflare_family_AAAA():
    client = mollusc_client("https://family.cloudflare-dns.com/dns-query?")
    result = client.query("nudity.testcategory.com", "AAAA")

    assert result.is_blocked_by_server() == True


def test_adguard_A():
    client = mollusc_client("https://dns.adguard.com/resolve?")
    result = client.query("googleads.g.doubleclick.net", "A")

    assert result.is_blocked_by_server() == True


def test_adguard_AAAA():
    client = mollusc_client("https://dns.adguard.com/resolve?")
    result = client.query("googleads.g.doubleclick.net", "AAAA")

    assert result.is_blocked_by_server() == True


def test_default():
    client = mollusc_client()
    result = client.query("malware.testcategory.com", "A")

    assert result.is_blocked_by_server() == True
