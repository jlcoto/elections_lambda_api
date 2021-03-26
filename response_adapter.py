class Adapter:
    def adapt_party_data(self, data):
        items = data["Items"]
        return [
            {"party": item["party"]["S"], "votes": int(item["votes"]["N"])}
            for item in items
        ]
