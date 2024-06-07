import re

def parse_cpu_power_macos(cpu_data):
    match = re.search(r'Average C-state residency \(ms\):.*Pkg:\s+(\d+.\d+)', cpu_data, re.MULTILINE)
    if match:
        return float(match.group(1)) / 1000  # Example conversion to watts
    return 0

def parse_memory_power_macos(memory_data):
    page_size = 4096  # Page size in bytes
    matches = re.findall(r'Pages active:\s+(\d+)', memory_data, re.MULTILINE)
    if matches:
        total_active_memory = sum(int(match) for match in matches) * page_size
        return total_active_memory / (1024**3) * 0.5  # Example conversion to watts, assuming 0.5W per GB
    return 0

def parse_disk_power_macos(disk_data):
    matches = re.findall(r'disk0\s+(\d+.\d+)', disk_data, re.MULTILINE)
    if matches:
        total_disk_usage = sum(float(match) for match in matches)
        return total_disk_usage / 100  # Example conversion to watts
    return 0
