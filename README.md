```
python3 -m grpc_tools.protoc -I src/proto --python_out=src/ --grpc_python_out=src/ src/proto/message.proto
```