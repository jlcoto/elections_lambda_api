from response_adapter import Adapter

adapter = Adapter()


def test_adapt_party_data():
    data = {
        "Items": [
            {
                "party": {
                    "S": "El Frente Amplio Por Justicia, Vida Y Libertad"
                },
                "partyId": {"S": "00000013"},
                "votes": {"N": "911700"},
            },
            {
                "party": {"S": "Partido Politico Nacional Peru Libre"},
                "partyId": {"S": "00000017"},
                "votes": {"N": "502898"},
            },
        ]
    }
