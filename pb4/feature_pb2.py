# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rfeature.proto\x12\x0e\x64\x61ta_serialize\"\x1a\n\tBytesList\x12\r\n\x05value\x18\x01 \x03(\x0c\"\x1e\n\tFloatList\x12\x11\n\x05value\x18\x01 \x03(\x02\x42\x02\x10\x01\"\x1e\n\tInt64List\x12\x11\n\x05value\x18\x01 \x03(\x03\x42\x02\x10\x01\"\xa4\x01\n\x07\x46\x65\x61ture\x12/\n\nbytes_list\x18\x01 \x01(\x0b\x32\x19.data_serialize.BytesListH\x00\x12/\n\nfloat_list\x18\x02 \x01(\x0b\x32\x19.data_serialize.FloatListH\x00\x12/\n\nint64_list\x18\x03 \x01(\x0b\x32\x19.data_serialize.Int64ListH\x00\x42\x06\n\x04kind\"\x8b\x01\n\x08\x46\x65\x61tures\x12\x36\n\x07\x66\x65\x61ture\x18\x01 \x03(\x0b\x32%.data_serialize.Features.FeatureEntry\x1aG\n\x0c\x46\x65\x61tureEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.data_serialize.Feature:\x02\x38\x01\"7\n\x0b\x46\x65\x61tureList\x12(\n\x07\x66\x65\x61ture\x18\x01 \x03(\x0b\x32\x17.data_serialize.Feature\"\xa4\x01\n\x0c\x46\x65\x61tureLists\x12\x43\n\x0c\x66\x65\x61ture_list\x18\x01 \x03(\x0b\x32-.data_serialize.FeatureLists.FeatureListEntry\x1aO\n\x10\x46\x65\x61tureListEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.data_serialize.FeatureList:\x02\x38\x01\x62\x06proto3')



_BYTESLIST = DESCRIPTOR.message_types_by_name['BytesList']
_FLOATLIST = DESCRIPTOR.message_types_by_name['FloatList']
_INT64LIST = DESCRIPTOR.message_types_by_name['Int64List']
_FEATURE = DESCRIPTOR.message_types_by_name['Feature']
_FEATURES = DESCRIPTOR.message_types_by_name['Features']
_FEATURES_FEATUREENTRY = _FEATURES.nested_types_by_name['FeatureEntry']
_FEATURELIST = DESCRIPTOR.message_types_by_name['FeatureList']
_FEATURELISTS = DESCRIPTOR.message_types_by_name['FeatureLists']
_FEATURELISTS_FEATURELISTENTRY = _FEATURELISTS.nested_types_by_name['FeatureListEntry']
BytesList = _reflection.GeneratedProtocolMessageType('BytesList', (_message.Message,), {
  'DESCRIPTOR' : _BYTESLIST,
  '__module__' : 'feature_pb2'
  # @@protoc_insertion_point(class_scope:data_serialize.BytesList)
  })
_sym_db.RegisterMessage(BytesList)

FloatList = _reflection.GeneratedProtocolMessageType('FloatList', (_message.Message,), {
  'DESCRIPTOR' : _FLOATLIST,
  '__module__' : 'feature_pb2'
  # @@protoc_insertion_point(class_scope:data_serialize.FloatList)
  })
_sym_db.RegisterMessage(FloatList)

Int64List = _reflection.GeneratedProtocolMessageType('Int64List', (_message.Message,), {
  'DESCRIPTOR' : _INT64LIST,
  '__module__' : 'feature_pb2'
  # @@protoc_insertion_point(class_scope:data_serialize.Int64List)
  })
_sym_db.RegisterMessage(Int64List)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), {
  'DESCRIPTOR' : _FEATURE,
  '__module__' : 'feature_pb2'
  # @@protoc_insertion_point(class_scope:data_serialize.Feature)
  })
_sym_db.RegisterMessage(Feature)

Features = _reflection.GeneratedProtocolMessageType('Features', (_message.Message,), {

  'FeatureEntry' : _reflection.GeneratedProtocolMessageType('FeatureEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEATURES_FEATUREENTRY,
    '__module__' : 'feature_pb2'
    # @@protoc_insertion_point(class_scope:data_serialize.Features.FeatureEntry)
    })
  ,
  'DESCRIPTOR' : _FEATURES,
  '__module__' : 'feature_pb2'
  # @@protoc_insertion_point(class_scope:data_serialize.Features)
  })
_sym_db.RegisterMessage(Features)
_sym_db.RegisterMessage(Features.FeatureEntry)

FeatureList = _reflection.GeneratedProtocolMessageType('FeatureList', (_message.Message,), {
  'DESCRIPTOR' : _FEATURELIST,
  '__module__' : 'feature_pb2'
  # @@protoc_insertion_point(class_scope:data_serialize.FeatureList)
  })
_sym_db.RegisterMessage(FeatureList)

FeatureLists = _reflection.GeneratedProtocolMessageType('FeatureLists', (_message.Message,), {

  'FeatureListEntry' : _reflection.GeneratedProtocolMessageType('FeatureListEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEATURELISTS_FEATURELISTENTRY,
    '__module__' : 'feature_pb2'
    # @@protoc_insertion_point(class_scope:data_serialize.FeatureLists.FeatureListEntry)
    })
  ,
  'DESCRIPTOR' : _FEATURELISTS,
  '__module__' : 'feature_pb2'
  # @@protoc_insertion_point(class_scope:data_serialize.FeatureLists)
  })
_sym_db.RegisterMessage(FeatureLists)
_sym_db.RegisterMessage(FeatureLists.FeatureListEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FLOATLIST.fields_by_name['value']._options = None
  _FLOATLIST.fields_by_name['value']._serialized_options = b'\020\001'
  _INT64LIST.fields_by_name['value']._options = None
  _INT64LIST.fields_by_name['value']._serialized_options = b'\020\001'
  _FEATURES_FEATUREENTRY._options = None
  _FEATURES_FEATUREENTRY._serialized_options = b'8\001'
  _FEATURELISTS_FEATURELISTENTRY._options = None
  _FEATURELISTS_FEATURELISTENTRY._serialized_options = b'8\001'
  _BYTESLIST._serialized_start=33
  _BYTESLIST._serialized_end=59
  _FLOATLIST._serialized_start=61
  _FLOATLIST._serialized_end=91
  _INT64LIST._serialized_start=93
  _INT64LIST._serialized_end=123
  _FEATURE._serialized_start=126
  _FEATURE._serialized_end=290
  _FEATURES._serialized_start=293
  _FEATURES._serialized_end=432
  _FEATURES_FEATUREENTRY._serialized_start=361
  _FEATURES_FEATUREENTRY._serialized_end=432
  _FEATURELIST._serialized_start=434
  _FEATURELIST._serialized_end=489
  _FEATURELISTS._serialized_start=492
  _FEATURELISTS._serialized_end=656
  _FEATURELISTS_FEATURELISTENTRY._serialized_start=577
  _FEATURELISTS_FEATURELISTENTRY._serialized_end=656
# @@protoc_insertion_point(module_scope)