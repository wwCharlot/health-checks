import shutil
import sys

def check_disk_usage(disk, min_absolute, min_percent):
    'Returns True if enough free disk space, False otherwise'
    du = shutil.disk_usage(disk)
    # Calculate percentage of free space
    percent_free = 100 * du.free / du.total
    #  Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30

    if percent_free < min_percent or gigabytes_free > min_absolute:
        return False
    return True


# Check for at least 2 GB and 10% free
if not check_disk_usage('/',2,10):
    print('ERROR: not enought disk space')
    sys.exit(1)

print('Everything ok')
sys.exit(0)
