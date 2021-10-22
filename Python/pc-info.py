import psutil
import platform
from datetime import datetime

f = open("sysinfo.txt", "w")

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}\n"
        bytes /= factor

f.write(f'{"="*40, "System Information", "="*40}\n')
uname = platform.uname()
f.write(f"System: {uname.system}\n")
f.write(f"Node Name: {uname.node}\n")
f.write(f"Release: {uname.release}\n")
f.write(f"Version: {uname.version}\n")
f.write(f"Machine: {uname.machine}\n")
f.write(f"Processor: {uname.processor}\n")

# Writing the CPU Information
f.write(f'{"="*40, "CPU Info", "="*40}\n')
# Writing the no. of cores
f.write(f'{"Physical cores:", psutil.cpu_count(logical=False)}\n')
f.write(f'{"Total cores:", psutil.cpu_count(logical=True)}\n')
# Writing CPU frequencies
cpufreq = psutil.cpu_freq()
f.write(f"Max Frequency: {cpufreq.max:.2f}Mhz")
f.write(f"Min Frequency: {cpufreq.min:.2f}Mhz")
f.write(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# Writing CPU usage
f.write("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    f.write(f"Core {i}: {percentage}%")
f.write(f"Total CPU Usage: {psutil.cpu_percent()}%")


# Memory Information
f.write(f'{"="*40, "Memory Information", "="*40}\n')
# Getting the memory details
svmem = psutil.virtual_memory()
f.write(f"Total: {get_size(svmem.total)}\n")
f.write(f"Available: {get_size(svmem.available)}\n")
f.write(f"Used: {get_size(svmem.used)}\n")
f.write(f"Percentage: {svmem.percent}%")
f.write(f'{"="*20, "SWAP", "="*20}\n')
# Get the Swap Memory Details (If it Exists)
swap = psutil.swap_memory()
f.write(f"Total: {get_size(swap.total)}\n")
f.write(f"Free: {get_size(swap.free)}\n")
f.write(f"Used: {get_size(swap.used)}\n")
f.write(f"Percentage: {swap.percent}%")

# Disk Information
f.write(f'{"="*40, "Disk Information", "="*40}\n')
f.write("Partitions and Usage:")
# get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    f.write(f"=== Device: {partition.device} ===")
    f.write(f"  Mountpoint: {partition.mountpoint}\n")
    f.write(f"  File system type: {partition.fstype}\n")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    f.write(f"  Total Size: {get_size(partition_usage.total)}\n")
    f.write(f"  Used: {get_size(partition_usage.used)}\n")
    f.write(f"  Free: {get_size(partition_usage.free)}\n")
    f.write(f"  Percentage: {partition_usage.percent}%")
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
f.write(f"Total read: {get_size(disk_io.read_bytes)}\n")
f.write(f"Total write: {get_size(disk_io.write_bytes)}\n")

# Network information
f.write(f'{"="*40, "Network Information", "="*40}\n')
# This snippet will get all network interfaces whether Physical or Virtual.
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        f.write(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            f.write(f"  IP Address: {address.address}\n")
            f.write(f"  Netmask: {address.netmask}\n")
            f.write(f"  Broadcast IP: {address.broadcast}\n")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            f.write(f"  MAC Address: {address.address}\n")
            f.write(f"  Netmask: {address.netmask}\n")
            f.write(f"  Broadcast MAC: {address.broadcast}\n")
# Getting the IO statistics since boot
net_io = psutil.net_io_counters()
f.write(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}\n")
f.write(f"Total Bytes Received: {get_size(net_io.bytes_recv)}\n")

f.close()
