import json
from geo import haversine_km, theoretical_rtt_ms


def select_origin_region(regions):
    """
    Let user select an origin AWS region.
    """
    region_codes = list(regions.keys())

    print("Select origin AWS region:\n")
    for i, code in enumerate(region_codes, 1):
        print(f"{i:2}) {code:15} {regions[code]['name']}")

    while True:
        try:
            idx = int(input("\nEnter number: ")) - 1
            if 0 <= idx < len(region_codes):
                return region_codes[idx]
        except ValueError:
            pass

        print("Invalid input. Please try again.")


def main():
    with open("regions.json", encoding="utf-8") as f:
        regions = json.load(f)

    origin = select_origin_region(regions)
    origin_info = regions[origin]

    rows = []

    for code, info in regions.items():
        distance = haversine_km(
            origin_info["lat"],
            origin_info["lon"],
            info["lat"],
            info["lon"],
        )
        rtt = theoretical_rtt_ms(distance)

        rows.append(
            (code, info["name"], distance, rtt)
        )
    rows.sort(key=lambda x: x[2])

    print("\nREGION            NAME                    DIST(km)  THEOR RTT(ms)")
    print("------------------------------------------------------------------")

    for code, name, dist, rtt in rows:
        print(
            f"{code:15} "
            f"{name:22} "
            f"{dist:8.0f} "
            f"{rtt:13.2f}"
        )


if __name__ == "__main__":
    main()
