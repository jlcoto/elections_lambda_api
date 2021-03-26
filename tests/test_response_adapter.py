from response_adapter import Adapter

adapter = Adapter()


def test_adapt_party_data():
    data = {
        "Items": [
            {
                "party": {"S": "Frente Amplio"},
                "partyId": {"S": "00000013"},
                "votes": {"N": "911700"},
            },
            {
                "party": {"S": "Peru Libre"},
                "partyId": {"S": "00000017"},
                "votes": {"N": "502898"},
            },
        ]
    }

    expected_adapted_data = [
        {"party": "Frente Amplio", "votes": 911700},
        {"party": "Peru Libre", "votes": 502898},
    ]

    assert adapter.adapt_party_data(data) == expected_adapted_data
