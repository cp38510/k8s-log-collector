from app import log_parser
import unittest
import json
from jsonschema import validate

my_schema = {
    "type" : "object",
    "required": ["@timestamp", "stream", "log"],
    "properties" : {
        "@timestamp" : {"type" : "string"},
        "stream" : {"type" : "string"},
        "log" : {"type" : "string"},
    },
}

class BasicTestCase(unittest.TestCase):
  def test_valid_json_schema(self):
      parsed = log_parser("--log-file=./resources/cri-o_template_for_tests.log")
      json_data = json.loads(parsed)
      validate(instance=json_data, schema=my_schema)

  def test_json_output(self):
      parsed = log_parser("--log-file=./resources/cri-o_template_for_tests.log")
      json_data = json.loads(parsed)
      timestamp_key = json_data['@timestamp']
      self.assertEqual(timestamp_key, '2021-07-13T12:03:07.902859782Z')
      

if __name__ == '__main__':
  unittest.main()
