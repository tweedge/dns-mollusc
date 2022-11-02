from dataclasses import dataclass


@dataclass
class doh_response:
    response: dict
    raw_response: str = ""
    status_code: int = 0
    server_error: str = ""
    server_used: str = ""

    def get_answers(self):
        answers = []
        if "Answer" in self.response.keys():
            for answer in self.response["Answer"]:
                answers.append(answer["data"])
        return answers

    def is_blocked_by_server(self):
        pass
