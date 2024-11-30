# Default variables
DAY := $(shell date '+%d')
YEAR := $(shell date +%Y)

# Create the directory path with a zero padded day
WORKING_DIR = $(YEAR)/day$(shell printf "%02d" $(DAY))

.PHONY: fetch_input fetch_example fetch

# Fetch input for the specified day and year
fetch_input:
	@mkdir -p $(WORKING_DIR)
	@aocd $(DAY) $(YEAR) > "$(WORKING_DIR)/input.txt"
	@echo "Input fetched for Year $(YEAR), Day $(DAY)"

# Fetch example for the specified day and year
fetch_example:
	@mkdir -p $(WORKING_DIR)
	@aocd $(DAY) $(YEAR) --example > "$(WORKING_DIR)/example.txt"
	@echo "Example fetched for Year $(YEAR), Day $(DAY)"

fetch: fetch_input fetch_example

generate:
	python3 -m aoc_tools.generate.generate_files $(YEAR) $(DAY)