


print("***************************************")
print("****HOTEL NOVAXQF DDL**********")
print("****************************************")


class hotelnova():
    def __init__(self):
        self.name = ''
        self.address = ''
        self.cindate = ''
        self.coutdate = ''
        self.room_rent = 0
        self.food_bill = 0
        self.sub_total = 0
        self.additional_service = 0
        self.grand_total = 0

    def input(self):
        self.name = input("Enter your name: ")
        self.address = input("Enter your address: ")
        self.cindate = input("Enter your check-in date: ")
        self.coutdate = input("Enter your check-out date: ")
        print("Your room no is: 107")

    def room_rent_calculation(self):
        print("***WE HAVE THE FOLLOWING ROOMS FOR YOU***")
        print("1. Class A ------> Rs. 10000")
        print("2. Class B ------> Rs. 15000")
        print("3. Class C ------> Rs. 7000")
        print("4. Class D ------> Rs. 5000")

        room_choice = int(input("Enter your choice: "))
        nights_stay = int(input("Enter how many nights you will stay: "))

        if room_choice == 1:
            print("You chose room A")
            self.room_rent = 10000 * nights_stay
        elif room_choice == 2:
            print("You chose room B")
            self.room_rent = 15000 * nights_stay
        elif room_choice == 3:
            print("You chose room C")
            self.room_rent = 7000 * nights_stay
        elif room_choice == 4:
            print("You chose room D")
            self.room_rent = 5000 * nights_stay
        else:
            print("Invalid choice")

    def food_menu(self):
        print("--------------------------------")
        print("****RESTAURANT MENU****")
        print("1. Water ------> Rs. 20")
        print("2. Tea --------> Rs. 10")
        print("3. Breakfast --> Rs. 100")
        print("4. Lunch ------> Rs. 200")
        print("5. Dinner -----> Rs. 300")
        print("6. Exit")

        while True:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                quantity = int(input("Enter the quantity: "))
                self.food_bill += 20 * quantity
            elif choice == 2:
                quantity = int(input("Enter the quantity: "))
                self.food_bill += 10 * quantity
            elif choice == 3:
                quantity = int(input("Enter the quantity: "))
                self.food_bill += 100 * quantity
            elif choice == 4:
                quantity = int(input("Enter the quantity: "))
                self.food_bill += 200 * quantity
            elif choice == 5:
                quantity = int(input("Enter the quantity: "))
                self.food_bill += 300 * quantity
            elif choice == 6:
                break
            else:
                print("Invalid choice")

    def display(self):
        print("*******HOTEL BILL*********")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check-in date:", self.cindate)
        print("Check-out date:", self.coutdate)
        print("Room rent:", self.room_rent)
        print("Food bill:", self.food_bill)

        self.sub_total = self.room_rent + self.food_bill
        print("Subtotal:", self.sub_total)
        print("Additional service charge:", self.additional_service)
        self.grand_total = self.sub_total + self.additional_service
        print("Grand Total:", self.grand_total)


def main():
    p = hotelnova()

    while True:
        print("**************************************")
        print("1. Enter customer data")
        print("2. Calculate room rent")
        print("3. Calculate food purchased")
        print("4. Show total cost")
        print("5. Exit")

        choice = int(input("\nEnter the number of your choice: "))
        print("******************************************")

        if choice == 1:
            p.input()
        elif choice == 2:
            p.room_rent_calculation()
        elif choice == 3:
            p.food_menu()
        elif choice == 4:
            p.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice")


main()

