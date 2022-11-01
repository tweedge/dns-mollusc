import pytest
from doh_client_py3 import doh_client


def test_google():
    """
    Google works as expected, and resolution of a basic query works
    """
    client = doh_client("https://dns.google/resolve?")
    result = client.query("dns.google", "A")
    
    expected_ips = ["8.8.8.8", "8.8.4.4"]
    got_ips = []
    for result in result["answer"]:
        got_ips.append(result["data"])

    assert expected_ips.sort() == got_ips.sort()


def test_cloudflare():
    """
    Cloudflare works as expected, and resolution of a basic query works
    """
    client = doh_client("https://cloudflare-dns.com/dns-query?")
    result = client.query("dns.google", "A")
    
    expected_ips = ["8.8.8.8", "8.8.4.4"]
    got_ips = []
    for result in result["answer"]:
        got_ips.append(result["data"])

    assert expected_ips.sort() == got_ips.sort()


def test_quad9():
    """
    Quad9 works as expected, and resolution of a basic query works
    """
    client = doh_client("https://dns.quad9.net/dns-query?")
    result = client.query("dns.google", "A")
    
    expected_ips = ["8.8.8.8", "8.8.4.4"]
    got_ips = []
    for result in result["answer"]:
        got_ips.append(result["data"])

    assert expected_ips.sort() == got_ips.sort()


def test_adguard():
    """
    Adguard works as expected, and resolution of a basic query works
    """
    client = doh_client("https://dns.adguard.com/dns-query?")
    result = client.query("dns.google", "A")
    
    expected_ips = ["8.8.8.8", "8.8.4.4"]
    got_ips = []
    for result in result["answer"]:
        got_ips.append(result["data"])

    assert expected_ips.sort() == got_ips.sort()


def test_cleanbrowsing():
    """
    Cleanbrowsing works as expected, and resolution of a basic query works
    """
    client = doh_client("https://doh.cleanbrowsing.org/doh/security-filter/?")
    result = client.query("dns.google", "A")
    
    expected_ips = ["8.8.8.8", "8.8.4.4"]
    got_ips = []
    for result in result["answer"]:
        got_ips.append(result["data"])

    assert expected_ips.sort() == got_ips.sort()


def test_umbrella():
    """
    Cisco Umbrella works as expected, and resolution of a basic query works
    """
    client = doh_client("https://doh.umbrella.com/dns-query?")
    result = client.query("dns.google", "A")
    
    expected_ips = ["8.8.8.8", "8.8.4.4"]
    got_ips = []
    for result in result["answer"]:
        got_ips.append(result["data"])

    assert expected_ips.sort() == got_ips.sort()


def test_default():
    """
    A reasonable DNS server is selected by default, and resolution of a basic query works
    """
    client = doh_client()
    result = client.query("dns.google", "A")
    
    expected_ips = ["8.8.8.8", "8.8.4.4"]
    got_ips = []
    for result in result["answer"]:
        got_ips.append(result["data"])

    assert expected_ips.sort() == got_ips.sort()

