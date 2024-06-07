def collect_telemetry_windows():
    telemetry_data = {}
    
    # CPU usage
    cpu_data = subprocess.run(['powershell', 'Get-WmiObject', 'win32_processor'], capture_output=True).stdout.decode('utf-8')
    telemetry_data['cpu'] = cpu_data
    
    # Memory usage
    memory_data = subprocess.run(['powershell', 'Get-WmiObject', 'win32_OperatingSystem'], capture_output=True).stdout.decode('utf-8')
    telemetry_data['memory'] = memory_data
    
    # Disk usage
    disk_data = subprocess.run(['powershell', 'Get-PhysicalDisk'], capture_output=True).stdout.decode('utf-8')
    telemetry_data['disk'] = disk_data
    
    # Network telemetry
    network_data = subprocess.run(['powershell', 'Get-NetAdapterStatistics'], capture_output=True).stdout.decode('utf-8')
    telemetry_data['network'] = network_data
    
    return telemetry_data
