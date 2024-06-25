import platform
import subprocess
import re
import tkinter as tk
from tkinter import scrolledtext

# Function to collect telemetry data for macOS
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
    
    return telemetry_data

# Function to collect telemetry data for Windows
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
    
    return telemetry_data

# Function to parse CPU power for macOS
def parse_cpu_power_macos(cpu_data):
    match = re.search(r'Average C-state residency \(ms\):.*Pkg:\s+(\d+.\d+)', cpu_data, re.MULTILINE)
    if match:
        return float(match.group(1)) / 1000  # Example conversion to watts
    return 0

# Function to parse memory power for macOS
def parse_memory_power_macos(memory_data):
    page_size = 4096  # Page size in bytes
    matches = re.findall(r'Pages active:\s+(\d+)', memory_data, re.MULTILINE)
    if matches:
        total_active_memory = sum(int(match) for match in matches) * page_size
        return total_active_memory / (1024**3) * 0.5  # Example conversion to watts, assuming 0.5W per GB
    return 0

# Function to parse disk power for macOS
def parse_disk_power_macos(disk_data):
    matches = re.findall(r'disk0\s+(\d+.\d+)', disk_data, re.MULTILINE)
    if matches:
        total_disk_usage = sum(float(match) for match in matches)
        return total_disk_usage / 100  # Example conversion to watts
    return 0

# Function to parse CPU power for Windows
def parse_cpu_power_windows(cpu_data):
    match = re.search(r'LoadPercentage\s+=\s+(\d+)', cpu_data, re.MULTILINE)
    if match:
        load_percentage = float(match.group(1))
        return load_percentage / 100 * 50  # Example conversion to watts, assuming max 50W at 100% load
    return 0

# Function to parse memory power for Windows
def parse_memory_power_windows(memory_data):
    match = re.search(r'TotalVisibleMemorySize\s+=\s+(\d+)', memory_data, re.MULTILINE)
    if match:
        total_memory_kb = float(match.group(1))
        total_memory_gb = total_memory_kb / (1024 * 1024)
        return total_memory_gb * 0.5  # Example conversion to watts, assuming 0.5W per GB
    return 0

# Function to parse disk power for Windows
def parse_disk_power_windows(disk_data):
    match = re.search(r'Size\s+=\s+(\d+)', disk_data, re.MULTILINE)
    if match:
        total_disk_size_gb = float(match.group(1)) / (1024 * 1024 * 1024)
        return total_disk_size_gb * 0.1  # Example conversion to watts, assuming 0.1W per GB
    return 0

# Function to analyze telemetry data
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

# Function to estimate average power consumption
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

# Function to generate optimization suggestions
def optimization_suggestions(avg_cpu_power, cpu_range, avg_memory_power, memory_range, avg_disk_power, disk_range):
    suggestions = []
    
    # CPU Optimization
    if avg_cpu_power > 50:
        suggestions.append("Optimization Suggestion (High CPU Power): Reduce CPU Frequency")
        suggestions.append("\nExplanation:")
        suggestions.append("1. Determine the Current CPU Governor Setting:")
        suggestions.append("   - Check the current CPU governor setting using the following command:")
        suggestions.append("     $ cpupower frequency-info --policy")
        suggestions.append("2. Set CPU Governor to 'powersave' Mode:")
        suggestions.append("   - Open a terminal and run the following command with sudo privileges:")
        suggestions.append("     $ sudo cpupower frequency-set -g powersave")
        suggestions.append("3. Verify the CPU Governor Setting:")
        suggestions.append("   - Confirm that the CPU governor is set to 'powersave' mode by executing:")
        suggestions.append("     $ cpupower frequency-info --policy")
        suggestions.append("4. Monitor Power Consumption:")
        suggestions.append("   - Monitor the power consumption to observe the impact of the frequency reduction.")
    elif avg_cpu_power < 20:
        suggestions.append("Optimization Suggestion (Low CPU Power): Increase CPU Frequency")
        suggestions.append("\nExplanation:")
        suggestions.append("1. Determine the Current CPU Governor Setting:")
        suggestions.append("   - Check the current CPU governor setting using the following command:")
        suggestions.append("     $ cpupower frequency-info --policy")
        suggestions.append("2. Set CPU Governor to 'performance' Mode:")
        suggestions.append("   - Open a terminal and run the following command with sudo privileges:")
        suggestions.append("     $ sudo cpupower frequency-set -g performance")
        suggestions.append("3. Verify the CPU Governor Setting:")
        suggestions.append("   - Confirm that the CPU governor is set to 'performance' mode by executing:")
        suggestions.append("     $ cpupower frequency-info --policy")
        suggestions.append("4. Monitor Power Consumption:")
        suggestions.append("   - Monitor the power consumption to observe the impact of the frequency increase.")
    
    # Memory Optimization
    if avg_memory_power > 15:
        suggestions.append("Optimization Suggestion (High Memory Power): Reduce Memory Usage")
        suggestions.append("\nExplanation:")
        suggestions.append("1. Identify Memory-Intensive Applications:")
        suggestions.append("   - Use task manager or system monitor to identify memory-intensive applications.")
        suggestions.append("2. Close Unnecessary Applications:")
        suggestions.append("   - Close applications that are not in use to free up memory.")
        suggestions.append("3. Optimize Running Applications:")
        suggestions.append("   - Optimize applications to use less memory where possible.")
        suggestions.append("4. Upgrade Hardware:")
        suggestions.append("   - Consider upgrading to more efficient memory modules if the hardware is outdated.")
    elif avg_memory_power < 5:
        suggestions.append("Optimization Suggestion (Low Memory Power): Increase Memory Efficiency")
        suggestions.append("\nExplanation:")
        suggestions.append("1. Upgrade to Faster Memory Modules:")
        suggestions.append("   - Upgrade to memory modules with higher speed and lower power consumption.")
        suggestions.append("2. Enable Memory Compression:")
        suggestions.append("   - Enable memory compression to make efficient use of available memory.")
        suggestions.append("3. Monitor Memory Usage:")
        suggestions.append("   - Regularly monitor memory usage to ensure efficient utilization.")
    
    # Disk Optimization
    if avg_disk_power > 10:
        suggestions.append("Optimization Suggestion (High Disk Power): Reduce Disk Usage")
        suggestions.append("\nExplanation:")
        suggestions.append("1. Identify Disk-Intensive Processes:")
        suggestions.append("   - Use disk usage tools to identify processes that are heavily using the disk.")
        suggestions.append("2. Optimize Disk Usage:")
        suggestions.append("   - Optimize applications and processes to reduce disk usage.")
        suggestions.append("3. Upgrade to SSD:")
        suggestions.append("   - Consider upgrading from HDD to SSD for lower power consumption and better performance.")
    elif avg_disk_power < 3:
        suggestions.append("Optimization Suggestion (Low Disk Power): Increase Disk Efficiency")
        suggestions.append("\nExplanation:")
        suggestions.append("1. Defragment Disk (HDD only):")
        suggestions.append("   - Regularly defragment the disk to improve efficiency.")
        suggestions.append("2. Enable TRIM (SSD only):")
        suggestions.append("   - Ensure TRIM is enabled on SSDs for better performance and longevity.")
        suggestions.append("3. Monitor Disk Usage:")
        suggestions.append("   - Regularly monitor disk usage to ensure efficient utilization.")
    
    return suggestions

# Function to display power consumption and optimization suggestions in GUI
def display_suggestions(cpu_range, memory_range, disk_range, avg_cpu_power, avg_memory_power, avg_disk_power, suggestions):
    window = tk.Tk()
    window.title("Power Consumption and Optimization Suggestions")
    
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=30, font=("Times New Roman", 12))
    text_area.pack(padx=10, pady=10)
    
    text_area.insert(tk.END, f"CPU Power Consumption Range: {cpu_range} Watts\n")
    text_area.insert(tk.END, f"Memory Power Consumption Range: {memory_range} Watts\n")
    text_area.insert(tk.END, f"Disk Power Consumption Range: {disk_range} Watts\n\n")
    
    text_area.insert(tk.END, f"Average CPU Power Consumption: {avg_cpu_power} Watts\n")
    text_area.insert(tk.END, f"Average Memory Power Consumption: {avg_memory_power} Watts\n")
    text_area.insert(tk.END, f"Average Disk Power Consumption: {avg_disk_power} Watts\n\n")
    
    for suggestion in suggestions:
        text_area.insert(tk.END, suggestion + "\n\n")
    
    text_area.configure(state='disabled')
    
    window.mainloop()

# Example usage
if platform.system() == 'Darwin':
    telemetry = collect_telemetry_macos()
elif platform.system() == 'Windows':
    telemetry = collect_telemetry_windows()
else:
    raise NotImplementedError("Unsupported OS")

cpu_range, memory_range, disk_range = analyze_telemetry(telemetry)
avg_cpu_power, avg_memory_power, avg_disk_power = estimate_power(telemetry)
suggestions = optimization_suggestions(avg_cpu_power, cpu_range, avg_memory_power, memory_range, avg_disk_power, disk_range)

# Display the suggestions in a GUI
display_suggestions(cpu_range, memory_range, disk_range, avg_cpu_power, avg_memory_power, avg_disk_power, suggestions)
