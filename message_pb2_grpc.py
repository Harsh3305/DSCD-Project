# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import message_pb2 as message__pb2


class MapperStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendFileLocation = channel.unary_unary(
                '/mapper.Mapper/SendFileLocation',
                request_serializer=message__pb2.MapperRequest.SerializeToString,
                response_deserializer=message__pb2.MapperReply.FromString,
                )


class MapperServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendFileLocation(self, request, context):
        """Unary
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MapperServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendFileLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.SendFileLocation,
                    request_deserializer=message__pb2.MapperRequest.FromString,
                    response_serializer=message__pb2.MapperReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mapper.Mapper', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Mapper(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendFileLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mapper.Mapper/SendFileLocation',
            message__pb2.MapperRequest.SerializeToString,
            message__pb2.MapperReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ReducerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendFilePattern = channel.unary_unary(
                '/mapper.Reducer/SendFilePattern',
                request_serializer=message__pb2.ReducerRequest.SerializeToString,
                response_deserializer=message__pb2.ReducerReply.FromString,
                )


class ReducerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendFilePattern(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReducerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendFilePattern': grpc.unary_unary_rpc_method_handler(
                    servicer.SendFilePattern,
                    request_deserializer=message__pb2.ReducerRequest.FromString,
                    response_serializer=message__pb2.ReducerReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mapper.Reducer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Reducer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendFilePattern(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mapper.Reducer/SendFilePattern',
            message__pb2.ReducerRequest.SerializeToString,
            message__pb2.ReducerReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
