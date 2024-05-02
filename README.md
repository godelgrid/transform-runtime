# transform-runtime
Transform runtime side car that provides data transformation capabilities

Use below command to generate grpc code from proto files:

```
python -m grpc_tools.protoc -Iprotos --python_out=protocol/ --pyi_out=protocol/ --grpc_python_out=protocol/ protos/transform/v1/*
```
