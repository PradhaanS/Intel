def collect_telemetry_macos():
    telemetry_data = {}
    
    # CPU and energy data
    cpu_data = subprocess.run(['sudo', 'powermetrics', '-i', '2000', '-n', '1'], capture_output=True).stdout.decode('utf-8')
    telemetry_data['cpu'] = cpu_data
    
    # Memory usage
    memory_data = subprocess.run(['vm_stat'], capture_output=True).stdout.decode('utf-8')
    telemetry_data['memory'] = memory_data
    
    # Disk usage
    disk_data = subprocess.run(['iostat'], capture_output=True).stdout.decode('utf-8')
    telemetry_data['disk'] = disk_data
    
    # Network telemetry
    network_data = subprocess.run(['nettop', '-l', '1', '-x'], capture_output=True).stdout.decode('utf-8')
    telemetry_data['network'] = network_data
    
    return telemetry_data
