import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="absolute.444", database="EVENTS")
cursor = connection.cursor(dictionary=True)

class EVENTSMANIPULATION:
    def filter(self, n, arg1, arg2):
        if n == 1:
            sql = "SELECT * FROM EVENT WHERE EVENTDATE BETWEEN %s AND %s"
            cursor.execute(sql, (arg1, arg2))
            events = cursor.fetchall()
            return events
        elif n == 2:
            sql = "SELECT * FROM TICKET WHERE TICKETPRICE BETWEEN %s AND %s"
            cursor.execute(sql, (arg1, arg2))
            tickets = cursor.fetchall()
            return tickets
        else:
            return None

events = EVENTSMANIPULATION()


n = int(input("Enter operation (1 for date filter, 2 for price filter): "))

if n == 1:
    date1 = input("Enter Date1 (YYYY-MM-DD): ")
    date2 = input("Enter Date2 (YYYY-MM-DD): ")

    filtered_events = events.filter(n, date1, date2)

    if filtered_events:
        for event in filtered_events:
            print(f"Event ID: {event['EVENTID']}, Event Name: {event['EVENTNAME']}, Event Date: {event['EVENTDATE']}")
    else:
        print("No events found for the given date range.")

elif n == 2:
    price1 = float(input("Enter Price1: "))
    price2 = float(input("Enter Price2: "))

    filtered_tickets = events.filter(n, price1, price2)

    if filtered_tickets:
        for ticket in filtered_tickets:
            print(f"Ticket ID: {ticket['TICKETID']}, Ticket Price: {ticket['TICKETPRICE']}, Ticket Number: {ticket['TICKETNUM']}, Event ID: {ticket['EVENTID']}")
    else:
        print("No tickets found for the given price range.")

#-----------------------------------------------------------------------------------------------------------------------------#

class BaseProduct:
    def init(self, name, category, price, description):
        self.name = name
        self.category = category
        self.price = price
        self.description = description
        category.add_product(self)

    def get_info(self):
        return f"Product(name={self.name}, price={self.price}, description={self.description})"

    def repr(self):
        return self.get_info()


class ElectronicProduct(BaseProduct):
    def init(self, name, category, price, description, warranty_period):
        super().init(name, category, price, description)
        self.warranty_period = warranty_period

    def get_info(self):
        return f"ElectronicProduct(name={self.name}, price={self.price}, description={self.description}, warranty_period={self.warranty_period})"


class ClothingProduct(BaseProduct):
    def init(self, name, category, price, description, size, material):
        super().init(name, category, price, description)
        self.size = size
        self.material = material

    def get_info(self):
        return f"ClothingProduct(name={self.name}, price={self.price}, description={self.description}, size={self.size}, material={self.material})"