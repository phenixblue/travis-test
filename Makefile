REPO_ROOT := $(CURDIR)
APP_NAME ?= "helloworld.py"

.PHONY: unit
unit:

	hack/run_tests.sh

.PHONY: test
test: unit

.PHONY: coverage
coverage: echo

.PHONY: ci-lint
ci-lint:

	black --check app/helloworld/