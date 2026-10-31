#!/usr/bin/env bash
# Checkpoint 4 checker. Runs your report.sh against the sample log and
# confirms the three summary lines are correct.
set -uo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
script="$here/report.sh"
log="$here/logs/access.log"

[ -f "$script" ] || { echo "FAIL: report.sh not found in starter/"; exit 1; }
[ -f "$log" ]    || { echo "FAIL: logs/access.log not found"; exit 1; }

out="$(bash "$script" "$log" 2>/dev/null)"

pass=0
check() { if echo "$out" | grep -qF "$1"; then echo "ok   $1"; else echo "MISS $1"; pass=1; fi; }

check "Total requests: 120"
check "Error responses: 48"
check "Top client: 203.0.113.7"

echo
if [ "$pass" -eq 0 ]; then echo "PASS — checkpoint 4 complete ✅"; else echo "Not yet. Fix the lines marked MISS."; exit 1; fi
