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
        suggestions.append("   - Enable memory compression in the operating system to make more efficient use of available memory.")
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

cpu_range, memory_range, disk_range = analyze_telemetry(telemetry)
suggestions = optimization_suggestions(avg_cpu_power, cpu_range, avg_memory_power, memory_range, avg_disk_power, disk_range)
for suggestion in suggestions:
    print(suggestion)
