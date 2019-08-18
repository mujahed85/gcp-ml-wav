# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/iam/v1/options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/iam/v1/options.proto',
  package='google.iam.v1',
  syntax='proto3',
  serialized_options=_b('\n\021com.google.iam.v1B\014OptionsProtoP\001Z0google.golang.org/genproto/googleapis/iam/v1;iam\370\001\001\252\002\023Google.Cloud.Iam.V1\312\002\023Google\\Cloud\\Iam\\V1'),
  serialized_pb=_b('\n\x1bgoogle/iam/v1/options.proto\x12\rgoogle.iam.v1\x1a\x1cgoogle/api/annotations.proto\"4\n\x10GetPolicyOptions\x12 \n\x18requested_policy_version\x18\x01 \x01(\x05\x42\x84\x01\n\x11\x63om.google.iam.v1B\x0cOptionsProtoP\x01Z0google.golang.org/genproto/googleapis/iam/v1;iam\xf8\x01\x01\xaa\x02\x13Google.Cloud.Iam.V1\xca\x02\x13Google\\Cloud\\Iam\\V1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETPOLICYOPTIONS = _descriptor.Descriptor(
  name='GetPolicyOptions',
  full_name='google.iam.v1.GetPolicyOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requested_policy_version', full_name='google.iam.v1.GetPolicyOptions.requested_policy_version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=76,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['GetPolicyOptions'] = _GETPOLICYOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPolicyOptions = _reflection.GeneratedProtocolMessageType('GetPolicyOptions', (_message.Message,), {
  'DESCRIPTOR' : _GETPOLICYOPTIONS,
  '__module__' : 'google.iam.v1.options_pb2'
  ,
  '__doc__' : """Encapsulates settings provided to GetIamPolicy.
  
  
  Attributes:
      requested_policy_version:
          Optional. The policy format version to be returned. Acceptable
          values are 0 and 1. If the value is 0, or the field is
          omitted, policy format version 1 will be returned.
  """,
  # @@protoc_insertion_point(class_scope:google.iam.v1.GetPolicyOptions)
  })
_sym_db.RegisterMessage(GetPolicyOptions)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
