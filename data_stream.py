import numpy as np

def simulate_data_stream(num_points=1000, noise_level=0.1, anomaly_rate=0.05):

    seasonal = np.sin(np.linspace(0, 20 * np.pi, num_points)) #Sin wave to replicate seasonal variation in a consistent pattern
    
    
    noise = np.random.normal(0, noise_level, num_points)      # Adding random noise
    
    
    data_stream = seasonal + noise                            # Combining the regular pattern with noise
    
    # Injecting anomalies which includes spikes or drops in regular sin wave pattern
    anomaly_indices = np.random.choice(num_points, int(anomaly_rate * num_points), replace=False)
    data_stream[anomaly_indices] += np.random.choice([10, -10], len(anomaly_indices))  # Add large spikes or drops
    
    return data_stream
