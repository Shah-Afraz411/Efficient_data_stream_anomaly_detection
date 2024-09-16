import matplotlib.pyplot as plt

def visualize_stream(data, anomalies):
    plt.plot(data, label='Data Stream')
    plt.scatter(anomalies, data[anomalies], color='red', label='Anomalies', marker='x')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show() 