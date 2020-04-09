#!/usr/bin/env bash

# Run tests and get coverage
coverage run -m unittest discover -v -s app/helloworld/tests/

# Generate and output coverage report
coverage report --include app/helloworld/helloworld.py