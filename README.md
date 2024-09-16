# Efficient Data Stream Anomaly Detection

## Algorithm Choice
Because **Z-score with EWMA** is easy to use and works well in real-time situations, we choose it for anomaly detection. This is why it's appropriate for this task:


- The **Z-score** makes it simple to identify extreme values that are probably anomalies by calculating the number of standard deviations a data point deviates from the mean.
- **Exponentially Weighted Moving Average (EWMA)** is used to adjust for seasonal fluctuations and concept drift. By giving more weight to more recent data points, it enables the detection process to adapt over time to changes in the data. Because Z-score and EWMA work well together computationally, they are the perfect combo for real-time anomaly identification in streaming data contexts.


## Directory Structure
