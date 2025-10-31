# 📉 Anomaly Detection: Predictive Monitoring

This capability focuses on shifting monitoring from simple threshold-checking to intelligent, predictive pattern recognition, reducing the dependence on static configuration.

## Traditional IT Operations: Static Thresholds

* **The Challenge:** Traditional monitoring relies on operators setting **static thresholds** (e.g., "CPU > 80% is bad").
* **The Flaw:** This approach leads to two major issues:
    1.  **False Positives:** 80% CPU usage might be perfectly normal during peak business hours but abnormal at 3 AM, leading to unnecessary alerts.
    2.  **Missed Problems:** A slow memory leak causing gradual performance degradation (e.g., from 40% to 60% CPU over two weeks) might never hit a static 80% threshold but is a clear anomaly that should be flagged.

## The AIOps Solution: Machine Learning Baselines

AIOps uses unsupervised Machine Learning to build a **dynamic baseline** of "normal" behavior.

### Key AIOps Techniques Used:

1.  **Time-Series Analysis:** Models analyze historical metric data (CPU, latency, transactions) to learn patterns based on time of day, day of the week, and seasonal spikes (e.g., month-end reporting load).
2.  **Dynamic Baselines:** The system continuously generates an expected range of values. An **anomaly** is detected when the actual metric deviates statistically from this expected range, regardless of a static number.
3.  **Early Warning:** Anomaly detection allows operators to spot *slow-burn* issues or sudden, significant deviations that fall outside of known static thresholds, enabling **proactive intervention** before a critical threshold is breached.

This capability acts as the **intelligent filter** that feeds high-quality, relevant events into the Alert Management correlation engine.