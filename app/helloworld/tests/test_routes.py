from flask import Flask, request, jsonify
import datetime
import json
import os
import sys
import unittest
from unittest.mock import patch

sys.path.append("./app/helloworld")
import helloworld


class TestRoutes(unittest.TestCase):
    def setUp(self):

        self.app = helloworld.app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_healthz(self):

        """Method to test webhook "/healthz" route"""

        result = self.app.get("/healthz")

        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data)["health"], "ok")

    def test_webhook(self):

        """Method to test webhook  "/" route"""

        with open("./testing/payload.json") as json_file:

            request_object_json = json.load(json_file)

            result = self.app.post(
                "/",
                data=json.dumps(request_object_json),
                headers={"Content-Type": "application/json"},
            )

            self.assertEqual(result.status_code, 200)
            self.assertEqual(json.loads(result.data)["name"], "test1")
            self.assertEqual(json.loads(result.data)["metadata"]["field1"], "value1")
            self.assertEqual(json.loads(result.data)["metadata"]["field2"], "value2")


if __name__ == "__main__":
    unittest.main()
