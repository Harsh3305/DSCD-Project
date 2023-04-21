# DSCD Project
## Set up project
### Generate code from protos
```
python3 -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. proto/message.proto
```
### Delete `/intermediate` and `/output` directory
```commandline
rm -r intermediate
rm -r output
```
## Run code
### Step-1: Run Mapper
```
python3 mapper.py
```
### Step-2: Run Reducer
```
python3 reducer.py
```
### Step-3: Run Master
```
python3 main.py
```
Created with ❤️ by [Harsh](https://github.com/Harsh3305)