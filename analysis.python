def analyze_telemetry(telemetry_data):
    if platform.system() == 'Darwin':
        parse_cpu_power = parse_cpu_power_macos
        parse_memory_power = parse_memory_power_macos
        parse_disk_power = parse_disk_power_macos
    elif platform.system() == 'Windows':
        parse_cpu_power = parse_cpu_power_windows
        parse_memory_power = parse_memory_power_windows
        parse_disk_power = parse_disk_power_windows
    else:
        raise NotImplementedError("Unsupported OS")

    max_cpu_power = parse_cpu_power(telemetry_data['cpu'])
    min_cpu_power = parse_cpu_power(telemetry_data['cpu'])
    
    max_memory_power = parse_memory_power(telemetry_data['memory'])
    min_memory_power = parse_memory_power(telemetry_data['memory'])
    
    max_disk_power = parse_disk_power(telemetry_data['disk'])
    min_disk_power = parse_disk_power(telemetry_data['disk'])
    
    return (max_cpu_power, min_cpu_power), (max_memory_power, min_memory_power), (max_disk_power, min_disk_power)

cpu_range, memory_range, disk_range = analyze_telemetry(telemetry)
print(f"CPU Power Consumption Range: {cpu_range} Watts")
print(f"Memory Power Consumption Range: {memory_range} Watts")
print(f"Disk Power Consumption Range: {disk_range} Watts")
