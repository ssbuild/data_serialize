# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: numpyobject.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='numpyobject.proto',
  package='data_serialize',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11numpyobject.proto\x12\x0e\x64\x61ta_serialize\"\x87\x01\n\x0bNumpyObject\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\r\n\x05shape\x18\x02 \x03(\x03\x12\r\n\x05\x64type\x18\x03 \x01(\t\x12\r\n\x05\x62ytes\x18\x04 \x01(\x0c\x12\x11\n\x05int64\x18\x05 \x03(\x03\x42\x02\x10\x01\x12\x13\n\x07\x66loat32\x18\x06 \x03(\x02\x42\x02\x10\x01\x12\x13\n\x07\x66loat64\x18\x07 \x03(\x01\x42\x02\x10\x01\"\xaa\x01\n\x0eNumpyObjectMap\x12\x46\n\x0cnumpyobjects\x18\x01 \x03(\x0b\x32\x30.data_serialize.NumpyObjectMap.NumpyobjectsEntry\x1aP\n\x11NumpyobjectsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.data_serialize.NumpyObject:\x02\x38\x01\"D\n\x0fNumpyObjectList\x12\x31\n\x0cnumpyobjects\x18\x01 \x03(\x0b\x32\x1b.data_serialize.NumpyObjectb\x06proto3')
)




_NUMPYOBJECT = _descriptor.Descriptor(
  name='NumpyObject',
  full_name='data_serialize.NumpyObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='data_serialize.NumpyObject.header', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='data_serialize.NumpyObject.shape', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='data_serialize.NumpyObject.dtype', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='data_serialize.NumpyObject.bytes', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64', full_name='data_serialize.NumpyObject.int64', index=4,
      number=5, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float32', full_name='data_serialize.NumpyObject.float32', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float64', full_name='data_serialize.NumpyObject.float64', index=6,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=173,
)


_NUMPYOBJECTMAP_NUMPYOBJECTSENTRY = _descriptor.Descriptor(
  name='NumpyobjectsEntry',
  full_name='data_serialize.NumpyObjectMap.NumpyobjectsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='data_serialize.NumpyObjectMap.NumpyobjectsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='data_serialize.NumpyObjectMap.NumpyobjectsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=346,
)

_NUMPYOBJECTMAP = _descriptor.Descriptor(
  name='NumpyObjectMap',
  full_name='data_serialize.NumpyObjectMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numpyobjects', full_name='data_serialize.NumpyObjectMap.numpyobjects', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NUMPYOBJECTMAP_NUMPYOBJECTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=346,
)


_NUMPYOBJECTLIST = _descriptor.Descriptor(
  name='NumpyObjectList',
  full_name='data_serialize.NumpyObjectList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numpyobjects', full_name='data_serialize.NumpyObjectList.numpyobjects', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=348,
  serialized_end=416,
)

_NUMPYOBJECTMAP_NUMPYOBJECTSENTRY.fields_by_name['value'].message_type = _NUMPYOBJECT
_NUMPYOBJECTMAP_NUMPYOBJECTSENTRY.containing_type = _NUMPYOBJECTMAP
_NUMPYOBJECTMAP.fields_by_name['numpyobjects'].message_type = _NUMPYOBJECTMAP_NUMPYOBJECTSENTRY
_NUMPYOBJECTLIST.fields_by_name['numpyobjects'].message_type = _NUMPYOBJECT
DESCRIPTOR.message_types_by_name['NumpyObject'] = _NUMPYOBJECT
DESCRIPTOR.message_types_by_name['NumpyObjectMap'] = _NUMPYOBJECTMAP
DESCRIPTOR.message_types_by_name['NumpyObjectList'] = _NUMPYOBJECTLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NumpyObject = _reflection.GeneratedProtocolMessageType('NumpyObject', (_message.Message,), {
  'DESCRIPTOR' : _NUMPYOBJECT,
  '__module__' : 'numpyobject_pb2'
  # @@protoc_insertion_point(class_scope:data_serialize.NumpyObject)
  })
_sym_db.RegisterMessage(NumpyObject)

NumpyObjectMap = _reflection.GeneratedProtocolMessageType('NumpyObjectMap', (_message.Message,), {

  'NumpyobjectsEntry' : _reflection.GeneratedProtocolMessageType('NumpyobjectsEntry', (_message.Message,), {
    'DESCRIPTOR' : _NUMPYOBJECTMAP_NUMPYOBJECTSENTRY,
    '__module__' : 'numpyobject_pb2'
    # @@protoc_insertion_point(class_scope:data_serialize.NumpyObjectMap.NumpyobjectsEntry)
    })
  ,
  'DESCRIPTOR' : _NUMPYOBJECTMAP,
  '__module__' : 'numpyobject_pb2'
  # @@protoc_insertion_point(class_scope:data_serialize.NumpyObjectMap)
  })
_sym_db.RegisterMessage(NumpyObjectMap)
_sym_db.RegisterMessage(NumpyObjectMap.NumpyobjectsEntry)

NumpyObjectList = _reflection.GeneratedProtocolMessageType('NumpyObjectList', (_message.Message,), {
  'DESCRIPTOR' : _NUMPYOBJECTLIST,
  '__module__' : 'numpyobject_pb2'
  # @@protoc_insertion_point(class_scope:data_serialize.NumpyObjectList)
  })
_sym_db.RegisterMessage(NumpyObjectList)


_NUMPYOBJECT.fields_by_name['int64']._options = None
_NUMPYOBJECT.fields_by_name['float32']._options = None
_NUMPYOBJECT.fields_by_name['float64']._options = None
_NUMPYOBJECTMAP_NUMPYOBJECTSENTRY._options = None
# @@protoc_insertion_point(module_scope)
