# Default variables
DAY := $(shell date '+%d')
YEAR := $(shell date +%Y)

# Create the directory path with a zero padded day
WORKING_DIR = $(YEAR)/day$(shell printf "%02d" $(DAY))

.PHONY: fetch-input fetch-example fetch

# Fetch input for the specified day and year
fetch-input:
	@mkdir -p $(WORKING_DIR)
	@aocd $(DAY) $(YEAR) > "$(WORKING_DIR)/input.txt"
	@echo "Input fetched for Year $(YEAR), Day $(DAY)"

# Fetch example for the specified day and year
fetch-example:
	@mkdir -p $(WORKING_DIR)
	@aocd $(DAY) $(YEAR) --example > "$(WORKING_DIR)/example.txt"
	@echo "Example fetched for Year $(YEAR), Day $(DAY)"

fetch: fetch-input fetch-example

generate:
	@python3 -m aoc_tools.generate.generate_files $(YEAR) $(DAY)

run:
	@for dir in $(YEAR)/*/; do \
		python3 "$$dir/solution.py"; \
	done

run-day:
	@python3 $(WORKING_DIR)/solution.py

test:
	@python3 -m unittest discover $(YEAR) "*test.py"

test-day:
	@python3 -m unittest discover $(YEAR) "day$(shell printf "%02d" $(DAY))_test.py"

update-readme:
	@python3 -m aoc_tools.generate.update_readme $(YEAR)