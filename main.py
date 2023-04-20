from src.master.master import Master

if __name__ == "__main__":
    master = Master(
        input_dir="/home/harsh/Project/DSCD/AProject/input",
        mapper_addresses=["localhost:8080", "localhost:8081"],
        reducer_addresses=["localhost:3000", "localhost:3001", "localhost:3002"],
        output_dir="/home/harsh/Project/DSCD/AProject/output"
    )
    master.process_data()
