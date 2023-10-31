# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/api.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/api.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10protos/api.proto\"=\n\x07\x41\x64\x64\x43ube\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\x11\n\tblockType\x18\x04 \x01(\x05\"#\n\x08\x41\x64\x64\x43ubes\x12\x17\n\x05\x63ubes\x18\x01 \x03(\x0b\x32\x08.AddCube\"R\n\x08\x43learBox\x12\n\n\x02x1\x18\x01 \x01(\x02\x12\n\n\x02y1\x18\x02 \x01(\x02\x12\n\n\x02z1\x18\x03 \x01(\x02\x12\n\n\x02x2\x18\x04 \x01(\x02\x12\n\n\x02y2\x18\x05 \x01(\x02\x12\n\n\x02z2\x18\x06 \x01(\x02\"d\n\x07\x41\x64\x64Line\x12\n\n\x02x1\x18\x01 \x01(\x02\x12\n\n\x02y1\x18\x02 \x01(\x02\x12\n\n\x02z1\x18\x03 \x01(\x02\x12\n\n\x02x2\x18\x04 \x01(\x02\x12\n\n\x02y2\x18\x05 \x01(\x02\x12\n\n\x02z2\x18\x06 \x01(\x02\x12\x11\n\tintensity\x18\x07 \x01(\x02\"\xab\x01\n\nApiRequest\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.MessageType\x12\x1b\n\x07\x61\x64\x64\x43ube\x18\x02 \x01(\x0b\x32\x08.AddCubeH\x00\x12\x1d\n\x08\x63learBox\x18\x03 \x01(\x0b\x32\t.ClearBoxH\x00\x12\x1b\n\x07\x61\x64\x64Line\x18\x04 \x01(\x0b\x32\x08.AddLineH\x00\x12\x1d\n\x08\x61\x64\x64\x43ubes\x18\x05 \x01(\x0b\x32\t.AddCubesH\x00\x42\t\n\x07payload*G\n\x0bMessageType\x12\x0c\n\x08\x41\x44\x44_CUBE\x10\x00\x12\r\n\tCLEAR_BOX\x10\x01\x12\x0c\n\x08\x41\x44\x44_LINE\x10\x02\x12\r\n\tADD_CUBES\x10\x03\x62\x06proto3'
)

_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='MessageType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADD_CUBE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLEAR_BOX', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADD_LINE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADD_CUBES', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=480,
  serialized_end=551,
)
_sym_db.RegisterEnumDescriptor(_MESSAGETYPE)

MessageType = enum_type_wrapper.EnumTypeWrapper(_MESSAGETYPE)
ADD_CUBE = 0
CLEAR_BOX = 1
ADD_LINE = 2
ADD_CUBES = 3



_ADDCUBE = _descriptor.Descriptor(
  name='AddCube',
  full_name='AddCube',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='AddCube.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='AddCube.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='AddCube.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blockType', full_name='AddCube.blockType', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=20,
  serialized_end=81,
)


_ADDCUBES = _descriptor.Descriptor(
  name='AddCubes',
  full_name='AddCubes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cubes', full_name='AddCubes.cubes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=83,
  serialized_end=118,
)


_CLEARBOX = _descriptor.Descriptor(
  name='ClearBox',
  full_name='ClearBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x1', full_name='ClearBox.x1', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y1', full_name='ClearBox.y1', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z1', full_name='ClearBox.z1', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x2', full_name='ClearBox.x2', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y2', full_name='ClearBox.y2', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z2', full_name='ClearBox.z2', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=120,
  serialized_end=202,
)


_ADDLINE = _descriptor.Descriptor(
  name='AddLine',
  full_name='AddLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x1', full_name='AddLine.x1', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y1', full_name='AddLine.y1', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z1', full_name='AddLine.z1', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x2', full_name='AddLine.x2', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y2', full_name='AddLine.y2', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z2', full_name='AddLine.z2', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='intensity', full_name='AddLine.intensity', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=204,
  serialized_end=304,
)


_APIREQUEST = _descriptor.Descriptor(
  name='ApiRequest',
  full_name='ApiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ApiRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addCube', full_name='ApiRequest.addCube', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clearBox', full_name='ApiRequest.clearBox', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addLine', full_name='ApiRequest.addLine', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addCubes', full_name='ApiRequest.addCubes', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='ApiRequest.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=307,
  serialized_end=478,
)

_ADDCUBES.fields_by_name['cubes'].message_type = _ADDCUBE
_APIREQUEST.fields_by_name['type'].enum_type = _MESSAGETYPE
_APIREQUEST.fields_by_name['addCube'].message_type = _ADDCUBE
_APIREQUEST.fields_by_name['clearBox'].message_type = _CLEARBOX
_APIREQUEST.fields_by_name['addLine'].message_type = _ADDLINE
_APIREQUEST.fields_by_name['addCubes'].message_type = _ADDCUBES
_APIREQUEST.oneofs_by_name['payload'].fields.append(
  _APIREQUEST.fields_by_name['addCube'])
_APIREQUEST.fields_by_name['addCube'].containing_oneof = _APIREQUEST.oneofs_by_name['payload']
_APIREQUEST.oneofs_by_name['payload'].fields.append(
  _APIREQUEST.fields_by_name['clearBox'])
_APIREQUEST.fields_by_name['clearBox'].containing_oneof = _APIREQUEST.oneofs_by_name['payload']
_APIREQUEST.oneofs_by_name['payload'].fields.append(
  _APIREQUEST.fields_by_name['addLine'])
_APIREQUEST.fields_by_name['addLine'].containing_oneof = _APIREQUEST.oneofs_by_name['payload']
_APIREQUEST.oneofs_by_name['payload'].fields.append(
  _APIREQUEST.fields_by_name['addCubes'])
_APIREQUEST.fields_by_name['addCubes'].containing_oneof = _APIREQUEST.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['AddCube'] = _ADDCUBE
DESCRIPTOR.message_types_by_name['AddCubes'] = _ADDCUBES
DESCRIPTOR.message_types_by_name['ClearBox'] = _CLEARBOX
DESCRIPTOR.message_types_by_name['AddLine'] = _ADDLINE
DESCRIPTOR.message_types_by_name['ApiRequest'] = _APIREQUEST
DESCRIPTOR.enum_types_by_name['MessageType'] = _MESSAGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddCube = _reflection.GeneratedProtocolMessageType('AddCube', (_message.Message,), {
  'DESCRIPTOR' : _ADDCUBE,
  '__module__' : 'protos.api_pb2'
  # @@protoc_insertion_point(class_scope:AddCube)
  })
_sym_db.RegisterMessage(AddCube)

AddCubes = _reflection.GeneratedProtocolMessageType('AddCubes', (_message.Message,), {
  'DESCRIPTOR' : _ADDCUBES,
  '__module__' : 'protos.api_pb2'
  # @@protoc_insertion_point(class_scope:AddCubes)
  })
_sym_db.RegisterMessage(AddCubes)

ClearBox = _reflection.GeneratedProtocolMessageType('ClearBox', (_message.Message,), {
  'DESCRIPTOR' : _CLEARBOX,
  '__module__' : 'protos.api_pb2'
  # @@protoc_insertion_point(class_scope:ClearBox)
  })
_sym_db.RegisterMessage(ClearBox)

AddLine = _reflection.GeneratedProtocolMessageType('AddLine', (_message.Message,), {
  'DESCRIPTOR' : _ADDLINE,
  '__module__' : 'protos.api_pb2'
  # @@protoc_insertion_point(class_scope:AddLine)
  })
_sym_db.RegisterMessage(AddLine)

ApiRequest = _reflection.GeneratedProtocolMessageType('ApiRequest', (_message.Message,), {
  'DESCRIPTOR' : _APIREQUEST,
  '__module__' : 'protos.api_pb2'
  # @@protoc_insertion_point(class_scope:ApiRequest)
  })
_sym_db.RegisterMessage(ApiRequest)


# @@protoc_insertion_point(module_scope)
