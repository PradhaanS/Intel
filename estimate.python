def estimate_power(telemetry_data):
    if platform.system() == 'Darwin':
        cpu_power = parse_cpu_power_macos(telemetry_data['cpu'])
        memory_power = parse_memory_power_macos(telemetry_data['memory'])
        disk_power = parse_disk_power_macos(telemetry_data['disk'])
    elif platform.system() == 'Windows':
        cpu_power = parse_cpu_power_windows(telemetry_data['cpu'])
        memory_power = parse_memory_power_windows(telemetry_data['memory'])
        disk_power = parse_disk_power_windows(telemetry_data['disk'])
    else:
        raise NotImplementedError("Unsupported OS")
    
    return cpu_power, memory_power, disk_power

avg_cpu_power, avg_memory_power, avg_disk_power = estimate_power(telemetry)
print(f"Average CPU Power Consumption: {avg_cpu_power} Watts")
print(f"Average Memory Power Consumption: {avg_memory_power} Watts")
print(f"Average Disk Power Consumption: {avg_disk_power} Watts")
