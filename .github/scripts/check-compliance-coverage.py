#!/usr/bin/env python3
"""Check JaCoCo line coverage for compliance-critical classes.

Exit codes:
  0 — all compliance classes meet the 70 % threshold (or at least 50 %).
  1 — aggregate compliance-path coverage is below 50 % (error).

A warning annotation is emitted when coverage is between 50 % and 70 %.
"""

import sys
import xml.etree.ElementTree as ET

REPORT_PATH = sys.argv[1] if len(sys.argv) > 1 else "target/site/jacoco/jacoco.xml"

COMPLIANCE_CLASSES = [
    "com/openbankproject/hydra/auth/controller/IndexController",
    "com/openbankproject/hydra/auth/VO/SessionData",
    "com/openbankproject/hydra/auth/controller/OtherController",
    "com/openbankproject/hydra/auth/VO/WellKnown",
    "com/openbankproject/model/Limit",
    "com/openbankproject/model/SepaCreditTransfersBerlinGroupV13",
    "com/openbankproject/hydra/auth/HydraConfig",
    "com/openbankproject/model/PostConsentJson",
    "com/openbankproject/model/FromAccount",
    "com/openbankproject/model/ToAccount",
    "com/openbankproject/model/PostConsentRequestVrpJson",
    "com/openbankproject/model/AccountAccess",
]

ERROR_THRESHOLD = 50
WARN_THRESHOLD = 70


def main():
    try:
        tree = ET.parse(REPORT_PATH)
    except FileNotFoundError:
        print(f"::error::JaCoCo report not found at {REPORT_PATH}")
        sys.exit(1)

    root = tree.getroot()

    total_missed = 0
    total_covered = 0
    results = []

    for cls in root.findall(".//class"):
        class_name = cls.get("name")
        if class_name not in COMPLIANCE_CLASSES:
            continue
        for counter in cls.findall("counter"):
            if counter.get("type") == "LINE":
                missed = int(counter.get("missed"))
                covered = int(counter.get("covered"))
                total = missed + covered
                pct = (covered / total * 100) if total > 0 else 0
                results.append((class_name, pct, covered, missed))
                total_missed += missed
                total_covered += covered

    total = total_missed + total_covered
    overall_pct = (total_covered / total * 100) if total > 0 else 0

    print(f"\n{'=' * 70}")
    print("Compliance-Path Coverage Report")
    print(f"{'=' * 70}")
    for name, pct, cov, miss in sorted(results):
        if pct >= WARN_THRESHOLD:
            status = "PASS"
        elif pct >= ERROR_THRESHOLD:
            status = "WARN"
        else:
            status = "FAIL"
        short = name.rsplit("/", 1)[-1]
        print(f"  [{status}] {short:45s} {pct:5.1f}% ({cov}/{cov + miss} lines)")
    print(f"{'=' * 70}")
    print(f"  Overall compliance-path coverage: {overall_pct:.1f}%")
    print(f"{'=' * 70}")

    if overall_pct < ERROR_THRESHOLD:
        print(f"::error::Compliance-path coverage ({overall_pct:.1f}%) is below {ERROR_THRESHOLD}%")
        sys.exit(1)
    elif overall_pct < WARN_THRESHOLD:
        print(f"::warning::Compliance-path coverage ({overall_pct:.1f}%) is below {WARN_THRESHOLD}%")

    sys.exit(0)


if __name__ == "__main__":
    main()
