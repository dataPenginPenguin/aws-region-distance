# AWS Region Distance & Theoretical Latency Calculator

This repository provides a simple CLI tool to calculate **geographical distance** and **theoretical minimum network latency (RTT)** between AWS regions based on physical distance and an optical fiber propagation model.

The goal is **not to measure actual latency**, but to estimate the _physical lower bound_ of inter-region communication and use it as a reference for architecture design decisions.

---

## Motivation

When designing multi-region architectures on AWS (e.g. DR, active-active, data replication, global APIs), latency is often discussed based on **observed RTT values**.

However, actual latency is influenced by:

- Network routing
- Undersea cable paths
- Intermediate network devices
- Congestion and peering

This tool focuses on a simpler question:

> _What is the theoretical minimum RTT imposed by physical distance alone?_

Understanding this lower bound helps:

- Set realistic expectations for cross-region communication
- Compare region pairs objectively
- Identify designs that are physically latency-sensitive by nature

---

## What This Tool Does

- Uses official AWS region location data
- Calculates great-circle distance (Haversine formula)
- Estimates **theoretical round-trip latency (RTT)** using an optical fiber propagation model
- Outputs results as a sorted table (by distance)

---

## Latency Model

Theoretical RTT is calculated based on signal propagation speed in optical fiber:

- Speed of light in vacuum:  
  `c ≈ 299,792 km/s`
- Refractive index of fiber:  
  `n ≈ 1.47`
- Propagation speed in fiber:  
  `c / n`

### Formula

```

RTT(ms) = distance_km × 2 ÷ (299,792 / 1.47) × 1000

```

### Notes

- This is a **round-trip time (RTT)** estimate
- No routing inefficiency or network equipment delays are included
- Actual measured latency will always be **higher than this value**

---

## Repository Structure

```

.
├── regions.json   # AWS region metadata (name, latitude, longitude)
├── geo.py         # Distance & theoretical RTT calculation logic
├── main.py        # CLI entry point
└── README.md

```

---

## Usage

### 1. Run the CLI

```bash
python main.py
```

### 2. Select the origin region

The CLI will display an interactive list of AWS regions:

```
Select origin AWS region:

 1) us-east-2       Ohio
 2) us-east-1       N. Virginia
 3) us-west-1       N. California
 ...
17) ap-northeast-1  Tokyo
 ...

Enter number: 17
```

### 3. View the results

Distances and theoretical RTTs to all other regions are displayed, sorted by distance:

```
REGION            NAME                    DIST(km)  THEOR RTT(ms)
------------------------------------------------------------------
ap-northeast-1    Tokyo                         0          0.00
ap-northeast-3    Osaka                       396          3.89
ap-northeast-2    Seoul                      1153         11.30
ap-east-1         Hong Kong                  2880         28.24
ap-southeast-1    Singapore                  5315         52.12
...
sa-east-1         São Paulo                 18534        181.76

```

Results are sorted by distance in ascending order.

---

## Intended Use Cases

- Multi-region architecture design
- Disaster Recovery (DR) planning
- Evaluating region placement for latency-sensitive systems
- Educational purposes (understanding physical limits of networks)

---

## Non-Goals

This tool does **not**:

- Measure real network latency
- Account for AWS network topology or routing
- Replace tools like CloudPing or AWS Network Manager

It is intended to complement measured data, not replace it.

---

## Related Tools & References

- CloudPing (measured RTT)
- AWS Network Manager
- AWS Global Infrastructure documentation

---

## Disclaimer

This project provides **theoretical estimates only**.
Actual latency depends on many factors beyond physical distance.

Use this tool as a **baseline reference**, not as a performance guarantee.

---

## License

MIT License
