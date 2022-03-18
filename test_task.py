import json
from task import split_address


class TestSplitAddress:
    def test_simple_case(self):
        input_output_mapping = [
            {"input": "Winterallee 3", "output": json.dumps({"street": 'Winterallee', "housenumber": "3"})},
            {"input": "Musterstrasse 45", "output": json.dumps({"street": "Musterstrasse", "housenumber": "45"})},
            {"input": "Blaufeldweg 123B", "output": json.dumps({"street": "Blaufeldweg", "housenumber": "123B"})},
        ]

        for elem in input_output_mapping:
            assert split_address(elem["input"]) == elem["output"]

    def test_complicated_cases(self):
        input_output_mapping = [
            {"input": "Am Bächle 23", "output": json.dumps({"street": "Am Bächle", "housenumber": "23"})},
            {"input": "Auf der Vogelwiese 23 b", "output": json.dumps({"street": "Auf der Vogelwiese", "housenumber": "23 b"})},
        ]

        for elem in input_output_mapping:
            assert split_address(elem["input"]) == elem["output"]

    def test_complex_cases(self):
        input_output_mapping = [
            {"input": "4, rue de la revolution", "output": json.dumps({"street": "rue de la revolution", "housenumber": "4"})},
            {"input": "200 Broadway Av", "output": json.dumps({"street": "Broadway Av", "housenumber": "200"})},
            {"input": "Calle Aduana, 29", "output": json.dumps({"street": "Calle Aduana", "housenumber": "29"})},
            {"input": "Calle 39 No 1540", "output": json.dumps({"street": "Calle 39", "housenumber": "No 1540"})},
        ]

        for elem in input_output_mapping:
            assert split_address(elem["input"]) == elem["output"]

    def test_custom_cases(self):
        input_output_mapping = [
            {"input": "Winterallee 3    ", "output": json.dumps({"street": 'Winterallee', "housenumber": "3"})},
            {"input": "23 Musterstrasse", "output": json.dumps({"street": "Musterstrasse", "housenumber": "23"})},
            {"input": "23 B Musterstrasse", "output": json.dumps({"street": "Musterstrasse", "housenumber": "23 B"})},
            {"input": "23B Musterstrasse", "output": json.dumps({"street": "Musterstrasse", "housenumber": "23B"})},

        ]

        for elem in input_output_mapping:
            assert split_address(elem["input"]) == elem["output"]
