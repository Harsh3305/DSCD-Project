from master import Master


def take_input_address(type_of_system):
    number_of_system = int(input(f"Enter number of {type_of_system}: "))
    address = []
    for _ in range(number_of_system):
        address.append(input(f"Enter {type_of_system} address: "))
    return address


if __name__ == "__main__":
    master = Master(
        input_dir="/home/harsh/Project/DSCD/DSCD-Project/input",
        mapper_addresses=take_input_address("mapper"),
        reducer_addresses=take_input_address("reducer"),
        output_dir="/home/harsh/Project/DSCD/DSCD-Project/output"
    )
    master.process_data()
