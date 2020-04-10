#!/usr/bin/env python

from flask import Flask, request, jsonify
import datetime
import os
import requests

app = Flask(__name__)


@app.route("/", methods=["POST"])
def webhook():

    request_info = request.json

    return jsonify(request_info)


@app.route("/healthz", methods=["GET"])
def healthz():

    """Function to return health info for app"""

    health_response = {"date_time": str(datetime.datetime.now()), "health": "ok"}

    # Return JSON formatted response object
    return jsonify(health_response)


################################################################################
################################################################################
################################################################################


def main():

    app.run(host="0.0.0.0", port=5000, debug=True)


################################################################################
################################################################################
################################################################################

if __name__ == "__main__":

    main()
