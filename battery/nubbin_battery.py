from battery.battery import Battery

class NubbinBarrery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

# Nubbin batteries need to be replaced every 4 years
# If the due date for service is less than the current date, it means that the date for service has passed and the car is due for a battery replacement
# If not, the battery need not be replaced
    def needs_service(self):
        date_to_be_serviced_by = self.last_service_date + 4
        if date_to_be_serviced_by < self.current_date:
            return True
        else:
            return False
        