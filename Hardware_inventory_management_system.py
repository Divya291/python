#finalproject

class DeviceManager:
    device_db = {'mouse': {'m001', 'm002', 'm003'},
                 'keyboard': {'k001', 'k002', 'k003'},
                 'laptop': {'l001', 'l002', 'l003'},
                 'pc': {'pc001', 'pc002', 'pc003'}}

    allocations = {'l001': [1234, 2],
                   'm002': [4567, 3],
                   'pc003': [7890, 4]}

    def __init__(self):
        self.device_db = DeviceManager.device_db
        self.allocations = DeviceManager.allocations

    def add_category(self, new_category):
        self.device_db.setdefault(new_category, set())

    def add_device(self, category, device_ids):
        self.device_db.setdefault(category, set()).update(device_ids)

    def allocate_device(self, device_id, employee_id, days):
        if device_id in self.allocations:
            current_employee_id, current_days_allocated = self.allocations[device_id]
            print(f"Device {device_id} is already allocated to Employee {current_employee_id} for {current_days_allocated} days.")
            print(f"Device {device_id} is not available for allocation.")
        else:
            self.allocations[device_id] = [employee_id, days]
            print(f"Device {device_id} allocated to Employee {employee_id} for {days} days.")
            
    def remove_device(self, category, device_id):
        if device_id in self.device_db[category]:
            self.device_db[category].remove(device_id)
            print(f"Device {device_id} removed from category {category} and deallocated.")

            # Remove from allocations if present
            if device_id in self.allocations:
                del self.allocations[device_id]
                print(f"Device {device_id} deallocated from allocations.")
        else:
            print(f"Device {device_id} not found in category {category}.")
            
    def maintenance_schedule(self, device_id):
        found = False
        for category, devices in self.device_db.items():
            if device_id in devices:
                found = True
                break

        if found:
            if device_id in self.allocations:
                employee_id, days_allocated = self.allocations[device_id]
                print(f"Device {device_id} is currently allocated to Employee {employee_id} for {days_allocated} days and currently not available for maintenance.")
            else:
                print(f"Device {device_id} is currently not allocated and available for maintenance.")
        else:
            print(f"Device {device_id} is not present in the device database.")

device_manager = DeviceManager()

def handle_case(case):
    if case == '1':
        new_category_name = input("Enter new category name: ")
        device_manager.add_category(new_category_name)

        new_devices = [device.strip() for device in input("Enter devices to add (comma-separated): ").split(',')]
        device_manager.add_device(new_category_name, new_devices)
    elif case == '2':
        device_id_input = input("Enter device ID to allocate: ")
        employee_id_input = input("Enter employee ID: ")
        days_input = int(input("Enter number of days to allocate: "))
        device_manager.allocate_device(device_id_input, employee_id_input, days_input)
    elif case == '3':
        remove_category = input("Enter category to remove a device from: ")
        remove_device_id = input("Enter device ID to remove: ")
        device_manager.remove_device(remove_category, remove_device_id)
    elif case == '4':
        maintenance_device_id = input("Enter device ID to check maintenance status: ")
        device_manager.maintenance_schedule(maintenance_device_id)
    elif case == '5':
        exit()
    else:
        print("Invalid choice. Please try again.")

while True:
    print("\nHARDWARE INVENTORY MANAGEMENT SYSTEM")
    print("1. ADD CATEGORY AND DEVICE ID")
    print("2. ALLOCATE")
    print("3. REMOVE")
    print("4. MAINTENANCE SCHEDULE")
    print("5. EXIT")

    choice = input("Enter your choice: ")
    if choice == '5':
        break

    handle_case(choice)

    print("Updated device database:", device_manager.device_db)
    print("Updated allocations:", device_manager.allocations)
