import data_stream
import visualization
import numpy as np
def ewma_anomaly_detection(data, alpha=0.3, threshold=3):  # alpha: determines weight of recent data points compared to older data points.
                                                           # threshold: cutoff value for the Z-score, to indicate anomaly
    # EWMA calculation
    ewma = [data[0]]         # Initialize with the first data point
    for i in range(1, len(data)):
        ewma.append(alpha * data[i] + (1 - alpha) * ewma[i-1])
    
  
    anomalies = []            # Z-score based anomaly detection
    for i in range(len(data)):
        z_score = (data[i] - ewma[i]) / np.std(ewma)
        if np.abs(z_score) > threshold:
            anomalies.append(i)
    
    return anomalies

data = data_stream.simulate_data_stream()

DetectedAnomaly = ewma_anomaly_detection(data)

visualization.visualize_stream(data,DetectedAnomaly)

