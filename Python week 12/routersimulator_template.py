class Router:
    def __init__(self, router_name):
        self.router_name = router_name
        self.router_neighbor = []
        self.routing_table = {"network": "", "distance": "" }

    def print_info(self):
        """
            This method prints out the information of a specific Router object when called
        """
        print(self.router_name)
        print("   N: " + ",".join(router for router in sorted(self.router_neighbor)))
        print("   R: " + self.routing_table["network"] + ":" + self.routing_table["distance"])

    def add_neighbor(self, router2):
        """
            This method takes a Router object
        """
        self.router_neighbor.append(router2.router_name)

    def add_network(self, router_network, router_distance):
        self.routing_table["network"] = router_network
        self.routing_table["distance"] = router_distance




def main():

    # routerfile = input("Network file: ")
    list_of_routers = []

    while True:
        command = input("> ")
        command = command.upper()

        if command == "P":
            router_name = input("Enter router name: ")
            if router_name not in list_of_routers:
                print("Router was not found.")
            else:
                router_name.print_info()


        elif command == "PA":
            for router in list_of_routers:
                router.print_info()

        elif command == "S":
            pass

        elif command == "C":
            first_router = input("Enter 1st router: ")
            second_router = input("Enter 2nd router: ")
            first_router.add_neighbor(second_router)
            second_router.add_neighbor(first_router)

        elif command == "RR":
            pass

        elif command == "NR":
            router_name = input("Enter a new name: ")
            if router_name not in list_of_routers:
                new_router = Router(router_name)
                list_of_routers.append(router_name)
                return new_router
            else:
                print("Name is taken")

        elif command == "NN":
            router_name = input("Enter router name: ")
            router_network = input("Enter network: ")
            router_distance = input("Enter distance: ")
            router_name.add_network(router_network, router_distance)


        elif command == "Q":
            print("Simulator closes.")
            return

        else:
            print("Erroneous command!")
            print("Enter one of these commands:")
            print("NR (new router)")
            print("P (print)")  
            print("C (connect)")
            print("NN (new network)")
            print("PA (print all)")
            print("S (send routing tables)")
            print("RR (route request)")
            print("Q (quit)")

main()
