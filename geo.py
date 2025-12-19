import math

def haversine_km(lat1, lon1, lat2, lon2):
    """
    Calculate great-circle distance between two points on Earth.
    Returns distance in kilometers.
    """
    R = 6371  # Earth radius in km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def theoretical_rtt_ms(distance_km, fiber_index=1.47):
    """
    Calculate theoretical round-trip latency (ms)
    based on fiber optic propagation speed.
    """
    c = 299_792  # speed of light in vacuum (km/s)
    fiber_speed = c / fiber_index

    # RTT (round-trip)
    return (distance_km * 2) / fiber_speed * 1000
