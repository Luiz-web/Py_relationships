class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.__addresses = []

    def list_adresses(self):
        for address in self.__addresses:
            print(f"Adress: {address.address_name}\n{address.address_number}")

    def add_address(self, addr_name, addr_number):
        self.__addresses.append(Address(addr_name, addr_number))

    def __del__(self):
        print(f"Deleting {self.customer_name}")



class Address:
    def __init__(self, address_name, address_number):
        self.address_name = address_name
        self.address_number = address_number

    def __del__(self):
        print(f"Deleting {self.address_name}, {self.address_number}")

customer_1 = Customer("Maria")
customer_1.add_address("Rua B", 94)
customer_1.add_address("Rua Casa Nova", 48)
customer_1.list_adresses()
del customer_1
print("Fim do código")
