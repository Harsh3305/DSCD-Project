# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\x12\x06mapper\">\n\rMapperRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x1a\n\x12number_of_reducers\x18\x02 \x01(\x03\"\r\n\x0bMapperReply\"+\n\x0eReducerRequest\x12\x19\n\x11\x66ile_name_pattern\x18\x01 \x01(\t\"\x0e\n\x0cReducerReply2H\n\x06Mapper\x12>\n\x10SendFileLocation\x12\x15.mapper.MapperRequest\x1a\x13.mapper.MapperReply2J\n\x07Reducer\x12?\n\x0fSendFilePattern\x12\x16.mapper.ReducerRequest\x1a\x14.mapper.ReducerReplyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MAPPERREQUEST._serialized_start=25
  _MAPPERREQUEST._serialized_end=87
  _MAPPERREPLY._serialized_start=89
  _MAPPERREPLY._serialized_end=102
  _REDUCERREQUEST._serialized_start=104
  _REDUCERREQUEST._serialized_end=147
  _REDUCERREPLY._serialized_start=149
  _REDUCERREPLY._serialized_end=163
  _MAPPER._serialized_start=165
  _MAPPER._serialized_end=237
  _REDUCER._serialized_start=239
  _REDUCER._serialized_end=313
# @@protoc_insertion_point(module_scope)
