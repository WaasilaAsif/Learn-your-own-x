#!/usr/bin/env bash
# Checkpoint 4: turn your one-liners into a reusable script.
#
# Finish this so that `bash report.sh logs/access.log` prints exactly these
# three lines (the numbers come from the sample log):
#
#   Total requests: <n>
#   Error responses: <n>      # responses with a 4xx or 5xx status code
#   Top client: <ip>          # the IP address that made the most requests
#
# Then run ./check.sh to verify. Replace each TODO with a command.
# You built every piece of this in checkpoints 2 and 3 — this just saves them.

set -euo pipefail   # stop on errors, unset variables, and failed pipes

log="${1:?usage: report.sh <logfile>}"   # first argument, or a usage error

total="TODO"     # count the lines in "$log"
errors="TODO"    # count lines whose status code starts with 4 or 5
top="TODO"       # the IP (first field) that appears most often

echo "Total requests: $total"
echo "Error responses: $errors"
echo "Top client: $top"
