from master import Master

if __name__ == "__main__":
    master = Master(
        input_dir="/home/harsh/Project/DSCD/DSCD-Project/input",
        mapper_addresses=["localhost:8080"],
        reducer_addresses=["localhost:3000"],
        output_dir="/home/harsh/Project/DSCD/DSCD-Project/output"
    )
    master.process_data()
