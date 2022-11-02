# dns-mollusc

[![License](https://img.shields.io/github/license/tweedge/dns-mollusc)](https://github.com/tweedge/dns-mollusc)
[![Downloads](https://img.shields.io/pypi/dm/dns-mollusc)](https://pypi.org/project/dns-mollusc/)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

A simple, synchronous, rate-limiting DoH client to check if a given response is filtered by the specified resolver.

dns-mollusc does the bare minimum to reliably accomplish the above job, and is **not** intended as a general purpose DoH client. For excellent DNS shenanigans in Python, I'd recommend [dnspython](https://dnspython.readthedocs.io/).

### Usage

dns-mollusc uses Cloudflare's secure DNS as default, which blocks known-malicious domains, with a rate limit of 100 queries per second. If no query type is given, dns-mollusc will query for an A record (IPv4 address). The simplest usage of dns-mollusc would be:

```
from dns_mollusc import mollusc_client

client = mollusc_client()
result = client.query("malware.testcategory.com")
result.is_blocked_by_server()  # returns True
```

However, you can set your preferred resolver and/or rate limit, such as using Adguard DNS and a QPS limit of 10 requests/s:

```
client = mollusc_client("https://dns.adguard.com/resolve?", 10)
```

And when querying, you can request any record type (though resolvers may not filter all request types):

```
result = client.query("malware.testcategory.com", "AAAA")
```

### Known-Supported Resolvers

dns-mollusc uses a non-standard DoH JSON API popularized by Google's public DNS service. It does not (and will not in the future) implement RFC 8484, which limits the number of resolves that work with dns-mollusc. The following resolvers are tested and working, sorted by what they filter.

Filters malware:
* Cloudflare Secure DNS, `https://security.cloudflare-dns.com/dns-query?`

Filters adult content and malware:
* Cloudflare Family DNS, `https://family.cloudflare-dns.com/dns-query?`

Filters ads:
* Adguard DNS, `https://dns.adguard.com/resolve?`

Filters (almost) whatever you want:
* NextDNS, subscription-only (copy the "DNS-over-HTTPS" endpoint from your account's Setup tab)

Unfiltered:
* Google DNS (8.8.8.8), `https://dns.google/resolve?`
* Cloudflare DNS (1.1.1.1), `https://cloudflare-dns.com/dns-query?`
* NextDNS public, `https://dns.nextdns.io/dns-query?`

### Why?

A bot used on r/cybersecurity checks any live links in comments and posts for obviously malicious or unwanted content (the logic included here was originally ripped from that bot). This allows us to get low-grade but constantly-updated protection as a *supplement* to other tools that we have.

The name "dns-mollusc" stems from the fact that molluscs can be used to monitor water for contamination, often in conjunction with more sophisticated methods. From [Wikipedia](https://en.wikipedia.org/wiki/Mollusca):

> Bivalve molluscs are used as bioindicators to monitor the health of aquatic environments in both fresh water and the marine environments. Their population status or structure, physiology, behaviour or the level of contamination with elements or compounds can indicate the state of contamination status of the ecosystem. ... Potamopyrgus antipodarum is used by some water treatment plants to test for estrogen-mimicking pollutants from industrial agriculture.

I was going to go with "dns-clam" but didn't want people to associate it with ClamAV.