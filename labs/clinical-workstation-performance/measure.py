"""Observer timer for a fictional workstation workflow."""
import argparse
import csv
from pathlib import Path
from statistics import median
from time import perf_counter


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("station", choices=["clinic", "care"])
    station = parser.parse_args().station
    path = Path("trials.csv")
    fields = ["station", "desktop_seconds", "app_after_desktop_seconds", "total_seconds"]
    totals = []
    if path.exists() and path.stat().st_size:
        with path.open(newline="", encoding="utf-8") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != fields:
                parser.exit(1, "Unexpected trials.csv header. Use a fresh trial folder.\n")
            totals = [float(row["total_seconds"]) for row in reader if row["station"] == station]

    input("Press Enter when sign-in starts: ")
    start = perf_counter()
    input("Press Enter when the desktop is usable: ")
    desktop = perf_counter()
    input("Press Enter when the fictional task completes: ")
    finish = perf_counter()
    times = [desktop - start, finish - desktop, finish - start]
    with path.open("a", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        if stream.tell() == 0:
            writer.writerow(fields)
        writer.writerow([station, *[f"{value:.3f}" for value in times]])
    totals.append(times[-1])
    print(f"{station}: {len(totals)} trials, median {median(totals):.2f}s, slowest {max(totals):.2f}s")


if __name__ == "__main__":
    main()
