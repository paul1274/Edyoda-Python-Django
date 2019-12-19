import datetime


class Customers:

    def __init__(self, stock=0):

        self.stock = stock

    def display_stock(self):

        print("We have currently {} bikes available to rent.".format(self.stock))
        return self.stock

    def hourly_basis(self, n):

        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $5 for each hour per bike.")
            print("Enjoy your Ride.")

            self.stock -= n
            return now

    def daily_basis(self, n):

        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on daily basis today at {} hours.".format(n, now.hour))
            print("You will be charged $20 for each day per bike.")
            print("Enjoy your Ride.")

            self.stock -= n
            return now

    def weekly_basis(self, n):

        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $60 for each week per bike.")
            print("Enjoy your Ride.")
            self.stock -= n

            return now

    def return_bike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
        rental_time, rental_basis, num_of_bikes = request
        bill = 0

        if rental_time and rental_basis and num_of_bikes:
            self.stock += num_of_bikes
            now = datetime.datetime.now()
            rental_period = now - rental_time

            # hourly bill calculation
            if rental_basis == 1:
                bill = round(rental_period.seconds / 3600) * 5 * num_of_bikes

            # daily bill calculation
            elif rental_basis == 2:
                bill = round(rental_period.days) * 20 * num_of_bikes

            # weekly bill calculation
            elif rental_basis == 3:
                bill = round(rental_period.days / 7) * 60 * num_of_bikes

            if 3 <= num_of_bikes <= 5:
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7

            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None


class Rentalshop:

    def __init__(self):

        self.bikes = 0
        self.rental_basis = 0
        self.rental_time = 0
        self.bill = 0

    def request_bike(self):

        bikes = input("How many bikes would you like to rent : ")
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def return_bike(self):

        if self.rental_basis and self.rental_time and self.bikes:
            return self.rental_time, self.rental_basis, self.bikes
        else:
            return 0, 0, 0


def main():
    customer = Customers(100)
    shop = Rentalshop()

    while True:
        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $20
        4. Request a bike on weekly basis $60
        5. Return a bike
        6. Exit
        """)

        choice = input("Enter choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue

        if choice == 1:
            customer.display_stock()

        elif choice == 2:
            shop.rentalTime = customer.hourly_basis(shop.request_bike())
            shop.rental_basis = 1

        elif choice == 3:
            shop.rentalTime = customer.daily_basis(shop.request_bike())
            shop.rental_basis = 2

        elif choice == 4:
            shop.rentalTime = customer.weekly_basis(shop.request_bike())
            shop.rental_basis = 3

        elif choice == 5:
            shop.bill = customer.return_bike(shop.return_bike())
            shop.rental_basis, shop.rental_time, shop.bikes = 0, 0, 0
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")
    print("Thank you for using the bike rental system.")


if __name__ == "__main__":
    main()
