import re

def parse_cpu_power_windows(cpu_data):
    match = re.search(r'LoadPercentage\s+=\s+(\d+)', cpu_data, re.MULTILINE)
    if match:
        load_percentage = float(match.group(1))
        return load_percentage / 100 * 50  # Example conversion to watts, assuming max 50W at 100% load
    return 0

def parse_memory_power_windows(memory_data):
    match = re.search(r'TotalVisibleMemorySize\s+=\s+(\d+)', memory_data, re.MULTILINE)
    if match:
        total_memory_kb = float(match.group(1))
        total_memory_gb = total_memory_kb / (1024 * 1024)
        return total_memory_gb * 0.5  # Example conversion to watts, assuming 0.5W per GB
    return 0

def parse_disk_power_windows(disk_data):
    match = re.search(r'Size\s+=\s+(\d+)', disk_data, re.MULTILINE)
    if match:
        total_disk_size_gb = float(match.group(1)) / (1024 * 1024 * 1024)
        return total_disk_size_gb * 0.1  # Example conversion to watts, assuming 0.1W per GB
    return 0
