# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: exo/networking/grpc/file_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'exo/networking/grpc/file_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from exo.networking.grpc import node_service_pb2 as exo_dot_networking_dot_grpc_dot_node__service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&exo/networking/grpc/file_service.proto\x12\x13\x65xo.networking.grpc\x1a&exo/networking/grpc/node_service.proto\"a\n\x15GetShardStatusRequest\x12)\n\x05shard\x18\x01 \x01(\x0b\x32\x1a.exo.networking.grpc.Shard\x12\x1d\n\x15inference_engine_name\x18\x02 \x01(\t\"y\n\x16GetShardStatusResponse\x12\x11\n\thas_shard\x18\x01 \x01(\x08\x12\x17\n\nlocal_path\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tfile_size\x18\x03 \x01(\x03H\x01\x88\x01\x01\x42\r\n\x0b_local_pathB\x0c\n\n_file_size2\xd7\x01\n\x0b\x46ileService\x12k\n\x0eGetShardStatus\x12*.exo.networking.grpc.GetShardStatusRequest\x1a+.exo.networking.grpc.GetShardStatusResponse\"\x00\x12[\n\rTransferShard\x12\x1f.exo.networking.grpc.ShardChunk\x1a#.exo.networking.grpc.TransferStatus\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exo.networking.grpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETSHARDSTATUSREQUEST']._serialized_start=103
  _globals['_GETSHARDSTATUSREQUEST']._serialized_end=200
  _globals['_GETSHARDSTATUSRESPONSE']._serialized_start=202
  _globals['_GETSHARDSTATUSRESPONSE']._serialized_end=323
  _globals['_FILESERVICE']._serialized_start=326
  _globals['_FILESERVICE']._serialized_end=541
# @@protoc_insertion_point(module_scope)
