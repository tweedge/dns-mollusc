import requests
from time import time, sleep


class doh_client(object):
    def __init__(
        self,
        server="https://cloudflare-dns.com/dns-query?",
        max_qps=100,
    ):
        self.server = server
        self.max_qps = max_qps

        self.client = requests.session()
        self.last_query_time = 0

    def query(self, query_input, query_type, get_dnssec=False, verbose=False):
        self._backoff()

        query_params = {
            "name": query_input,
            "type": query_type,
            "ct": "application/dns-json",
        }

        if get_dnssec:
            query_params["do"] = "true"

        code = 0
        error = ""
        results = {}

        try:
            raw_results = self.client.get(
                self.server,
                params=query_params,
                headers={"accept": "application/dns-json"},
            )
            code = raw_results.status_code
            results = raw_results.json()
        except Exception as e:
            error = e

        answer = {}
        if "Answer" in results.keys():
            answer = results["Answer"]

        return_data = {"answer": answer, "code": code, "error": error}

        if verbose:
            return_data["verbose"] = results

        return return_data

    def _backoff(self):
        now = time()
        backoff_for = (1 / self.max_qps) - (now - self.last_query_time)

        if backoff_for > 0:
            sleep(backoff_for)

        self.last_query_time = now
