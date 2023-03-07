import hid

# Get a list of all connected HID devices
devices = hid.enumerate()

# Loop through the devices and print their information
for device in devices:
    print(f"Device: {device['product_string']}, Vendor ID: {device['vendor_id']}, Product ID: {device['product_id']}")

