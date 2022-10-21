# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mesh.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import channel_pb2 as channel__pb2
from . import config_pb2 as config__pb2
from . import module_config_pb2 as module__config__pb2
from . import portnums_pb2 as portnums__pb2
from . import telemetry_pb2 as telemetry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmesh.proto\x1a\rchannel.proto\x1a\x0c\x63onfig.proto\x1a\x13module_config.proto\x1a\x0eportnums.proto\x1a\x0ftelemetry.proto\"\xb7\x05\n\x08Position\x12\x12\n\nlatitude_i\x18\x01 \x01(\x0f\x12\x13\n\x0blongitude_i\x18\x02 \x01(\x0f\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x05\x12\x0c\n\x04time\x18\x04 \x01(\x07\x12,\n\x0flocation_source\x18\x05 \x01(\x0e\x32\x13.Position.LocSource\x12,\n\x0f\x61ltitude_source\x18\x06 \x01(\x0e\x32\x13.Position.AltSource\x12\x11\n\ttimestamp\x18\x07 \x01(\x07\x12\x1f\n\x17timestamp_millis_adjust\x18\x08 \x01(\x05\x12\x14\n\x0c\x61ltitude_hae\x18\t \x01(\x11\x12#\n\x1b\x61ltitude_geoidal_separation\x18\n \x01(\x11\x12\x0c\n\x04PDOP\x18\x0b \x01(\r\x12\x0c\n\x04HDOP\x18\x0c \x01(\r\x12\x0c\n\x04VDOP\x18\r \x01(\r\x12\x14\n\x0cgps_accuracy\x18\x0e \x01(\r\x12\x14\n\x0cground_speed\x18\x0f \x01(\r\x12\x14\n\x0cground_track\x18\x10 \x01(\r\x12\x13\n\x0b\x66ix_quality\x18\x11 \x01(\r\x12\x10\n\x08\x66ix_type\x18\x12 \x01(\r\x12\x14\n\x0csats_in_view\x18\x13 \x01(\r\x12\x11\n\tsensor_id\x18\x14 \x01(\r\x12\x13\n\x0bnext_update\x18\x15 \x01(\r\x12\x12\n\nseq_number\x18\x16 \x01(\r\"N\n\tLocSource\x12\r\n\tLOC_UNSET\x10\x00\x12\x0e\n\nLOC_MANUAL\x10\x01\x12\x10\n\x0cLOC_INTERNAL\x10\x02\x12\x10\n\x0cLOC_EXTERNAL\x10\x03\"b\n\tAltSource\x12\r\n\tALT_UNSET\x10\x00\x12\x0e\n\nALT_MANUAL\x10\x01\x12\x10\n\x0c\x41LT_INTERNAL\x10\x02\x12\x10\n\x0c\x41LT_EXTERNAL\x10\x03\x12\x12\n\x0e\x41LT_BAROMETRIC\x10\x04\"\x81\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tlong_name\x18\x02 \x01(\t\x12\x12\n\nshort_name\x18\x03 \x01(\t\x12\x0f\n\x07macaddr\x18\x04 \x01(\x0c\x12 \n\x08hw_model\x18\x05 \x01(\x0e\x32\x0e.HardwareModel\x12\x13\n\x0bis_licensed\x18\x06 \x01(\x08\"\x1f\n\x0eRouteDiscovery\x12\r\n\x05route\x18\x01 \x03(\x07\"\xc5\x02\n\x07Routing\x12(\n\rroute_request\x18\x01 \x01(\x0b\x32\x0f.RouteDiscoveryH\x00\x12&\n\x0broute_reply\x18\x02 \x01(\x0b\x32\x0f.RouteDiscoveryH\x00\x12&\n\x0c\x65rror_reason\x18\x03 \x01(\x0e\x32\x0e.Routing.ErrorH\x00\"\xb4\x01\n\x05\x45rror\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08NO_ROUTE\x10\x01\x12\x0b\n\x07GOT_NAK\x10\x02\x12\x0b\n\x07TIMEOUT\x10\x03\x12\x10\n\x0cNO_INTERFACE\x10\x04\x12\x12\n\x0eMAX_RETRANSMIT\x10\x05\x12\x0e\n\nNO_CHANNEL\x10\x06\x12\r\n\tTOO_LARGE\x10\x07\x12\x0f\n\x0bNO_RESPONSE\x10\x08\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10 \x12\x12\n\x0eNOT_AUTHORIZED\x10!B\t\n\x07variant\"\x9c\x01\n\x04\x44\x61ta\x12\x19\n\x07portnum\x18\x01 \x01(\x0e\x32\x08.PortNum\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x15\n\rwant_response\x18\x03 \x01(\x08\x12\x0c\n\x04\x64\x65st\x18\x04 \x01(\x07\x12\x0e\n\x06source\x18\x05 \x01(\x07\x12\x12\n\nrequest_id\x18\x06 \x01(\x07\x12\x10\n\x08reply_id\x18\x07 \x01(\x07\x12\r\n\x05\x65moji\x18\x08 \x01(\x07\"\x82\x01\n\x08Waypoint\x12\n\n\x02id\x18\x01 \x01(\r\x12\x12\n\nlatitude_i\x18\x02 \x01(\x0f\x12\x13\n\x0blongitude_i\x18\x03 \x01(\x0f\x12\x0e\n\x06\x65xpire\x18\x04 \x01(\r\x12\x0e\n\x06locked\x18\x05 \x01(\x08\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\"\xcb\x03\n\nMeshPacket\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x07\x12\n\n\x02to\x18\x02 \x01(\x07\x12\x0f\n\x07\x63hannel\x18\x03 \x01(\r\x12\x18\n\x07\x64\x65\x63oded\x18\x04 \x01(\x0b\x32\x05.DataH\x00\x12\x13\n\tencrypted\x18\x05 \x01(\x0cH\x00\x12\n\n\x02id\x18\x06 \x01(\x07\x12\x0f\n\x07rx_time\x18\x07 \x01(\x07\x12\x0e\n\x06rx_snr\x18\x08 \x01(\x02\x12\x11\n\thop_limit\x18\t \x01(\r\x12\x10\n\x08want_ack\x18\n \x01(\x08\x12&\n\x08priority\x18\x0b \x01(\x0e\x32\x14.MeshPacket.Priority\x12\x0f\n\x07rx_rssi\x18\x0c \x01(\x05\x12$\n\x07\x64\x65layed\x18\r \x01(\x0e\x32\x13.MeshPacket.Delayed\"[\n\x08Priority\x12\t\n\x05UNSET\x10\x00\x12\x07\n\x03MIN\x10\x01\x12\x0e\n\nBACKGROUND\x10\n\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10@\x12\x0c\n\x08RELIABLE\x10\x46\x12\x07\n\x03\x41\x43K\x10x\x12\x07\n\x03MAX\x10\x7f\"B\n\x07\x44\x65layed\x12\x0c\n\x08NO_DELAY\x10\x00\x12\x15\n\x11\x44\x45LAYED_BROADCAST\x10\x01\x12\x12\n\x0e\x44\x45LAYED_DIRECT\x10\x02\x42\x11\n\x0fpayload_variant\"\x92\x01\n\x08NodeInfo\x12\x0b\n\x03num\x18\x01 \x01(\r\x12\x13\n\x04user\x18\x02 \x01(\x0b\x32\x05.User\x12\x1b\n\x08position\x18\x03 \x01(\x0b\x32\t.Position\x12\x0b\n\x03snr\x18\x04 \x01(\x02\x12\x12\n\nlast_heard\x18\x05 \x01(\x07\x12&\n\x0e\x64\x65vice_metrics\x18\x06 \x01(\x0b\x32\x0e.DeviceMetrics\"\x86\x03\n\nMyNodeInfo\x12\x13\n\x0bmy_node_num\x18\x01 \x01(\r\x12\x0f\n\x07has_gps\x18\x02 \x01(\x08\x12\x14\n\x0cmax_channels\x18\x03 \x01(\r\x12\x18\n\x10\x66irmware_version\x18\x04 \x01(\t\x12&\n\nerror_code\x18\x05 \x01(\x0e\x32\x12.CriticalErrorCode\x12\x15\n\rerror_address\x18\x06 \x01(\r\x12\x13\n\x0b\x65rror_count\x18\x07 \x01(\r\x12\x14\n\x0creboot_count\x18\x08 \x01(\r\x12\x0f\n\x07\x62itrate\x18\t \x01(\x02\x12\x1c\n\x14message_timeout_msec\x18\n \x01(\r\x12\x17\n\x0fmin_app_version\x18\x0b \x01(\r\x12\x15\n\rair_period_tx\x18\x0c \x03(\r\x12\x15\n\rair_period_rx\x18\r \x03(\r\x12\x10\n\x08has_wifi\x18\x0e \x01(\x08\x12\x1b\n\x13\x63hannel_utilization\x18\x0f \x01(\x02\x12\x13\n\x0b\x61ir_util_tx\x18\x10 \x01(\x02\"\xb5\x01\n\tLogRecord\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\x07\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x1f\n\x05level\x18\x04 \x01(\x0e\x32\x10.LogRecord.Level\"X\n\x05Level\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08\x43RITICAL\x10\x32\x12\t\n\x05\x45RROR\x10(\x12\x0b\n\x07WARNING\x10\x1e\x12\x08\n\x04INFO\x10\x14\x12\t\n\x05\x44\x45\x42UG\x10\n\x12\t\n\x05TRACE\x10\x05\"\xbc\x02\n\tFromRadio\x12\n\n\x02id\x18\x01 \x01(\r\x12\x1d\n\x06packet\x18\x02 \x01(\x0b\x32\x0b.MeshPacketH\x00\x12\x1e\n\x07my_info\x18\x03 \x01(\x0b\x32\x0b.MyNodeInfoH\x00\x12\x1e\n\tnode_info\x18\x04 \x01(\x0b\x32\t.NodeInfoH\x00\x12\x19\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\x07.ConfigH\x00\x12 \n\nlog_record\x18\x06 \x01(\x0b\x32\n.LogRecordH\x00\x12\x1c\n\x12\x63onfig_complete_id\x18\x07 \x01(\rH\x00\x12\x12\n\x08rebooted\x18\x08 \x01(\x08H\x00\x12%\n\x0cmoduleConfig\x18\t \x01(\x0b\x32\r.ModuleConfigH\x00\x12\x1b\n\x07\x63hannel\x18\n \x01(\x0b\x32\x08.ChannelH\x00\x42\x11\n\x0fpayload_variant\"\xca\x01\n\x07ToRadio\x12\x1d\n\x06packet\x18\x01 \x01(\x0b\x32\x0b.MeshPacketH\x00\x12&\n\tpeer_info\x18\x02 \x01(\x0b\x32\x11.ToRadio.PeerInfoH\x00\x12\x18\n\x0ewant_config_id\x18\x03 \x01(\rH\x00\x12\x14\n\ndisconnect\x18\x04 \x01(\x08H\x00\x1a\x35\n\x08PeerInfo\x12\x13\n\x0b\x61pp_version\x18\x01 \x01(\r\x12\x14\n\x0cmqtt_gateway\x18\x02 \x01(\x08\x42\x11\n\x0fpayload_variant\"5\n\nCompressed\x12\x19\n\x07portnum\x18\x01 \x01(\x0e\x32\x08.PortNum\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c*\xc3\x03\n\rHardwareModel\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08TLORA_V2\x10\x01\x12\x0c\n\x08TLORA_V1\x10\x02\x12\x12\n\x0eTLORA_V2_1_1P6\x10\x03\x12\t\n\x05TBEAM\x10\x04\x12\x0f\n\x0bHELTEC_V2_0\x10\x05\x12\x0e\n\nTBEAM_V0P7\x10\x06\x12\n\n\x06T_ECHO\x10\x07\x12\x10\n\x0cTLORA_V1_1P3\x10\x08\x12\x0b\n\x07RAK4631\x10\t\x12\x0f\n\x0bHELTEC_V2_1\x10\n\x12\r\n\tHELTEC_V1\x10\x0b\x12\x18\n\x14LILYGO_TBEAM_S3_CORE\x10\x0c\x12\x0c\n\x08RAK11200\x10\r\x12\x0b\n\x07NANO_G1\x10\x0e\x12\x0e\n\nSTATION_G1\x10\x19\x12\x11\n\rLORA_RELAY_V1\x10 \x12\x0e\n\nNRF52840DK\x10!\x12\x07\n\x03PPR\x10\"\x12\x0f\n\x0bGENIEBLOCKS\x10#\x12\x11\n\rNRF52_UNKNOWN\x10$\x12\r\n\tPORTDUINO\x10%\x12\x0f\n\x0b\x41NDROID_SIM\x10&\x12\n\n\x06\x44IY_V1\x10\'\x12\x15\n\x11NRF52840_PCA10059\x10(\x12\n\n\x06\x44R_DEV\x10)\x12\x0b\n\x07M5STACK\x10*\x12\x0f\n\nPRIVATE_HW\x10\xff\x01*,\n\tConstants\x12\x08\n\x04ZERO\x10\x00\x12\x15\n\x10\x44\x41TA_PAYLOAD_LEN\x10\xed\x01*\xee\x01\n\x11\x43riticalErrorCode\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0bTX_WATCHDOG\x10\x01\x12\x14\n\x10SLEEP_ENTER_WAIT\x10\x02\x12\x0c\n\x08NO_RADIO\x10\x03\x12\x0f\n\x0bUNSPECIFIED\x10\x04\x12\x15\n\x11UBLOX_UNIT_FAILED\x10\x05\x12\r\n\tNO_AXP192\x10\x06\x12\x19\n\x15INVALID_RADIO_SETTING\x10\x07\x12\x13\n\x0fTRANSMIT_FAILED\x10\x08\x12\x0c\n\x08\x42ROWNOUT\x10\t\x12\x12\n\x0eSX1262_FAILURE\x10\n\x12\x11\n\rRADIO_SPI_BUG\x10\x0b\x42G\n\x13\x63om.geeksville.meshB\nMeshProtosH\x03Z\"github.com/meshtastic/go/generatedb\x06proto3')

_HARDWAREMODEL = DESCRIPTOR.enum_types_by_name['HardwareModel']
HardwareModel = enum_type_wrapper.EnumTypeWrapper(_HARDWAREMODEL)
_CONSTANTS = DESCRIPTOR.enum_types_by_name['Constants']
Constants = enum_type_wrapper.EnumTypeWrapper(_CONSTANTS)
_CRITICALERRORCODE = DESCRIPTOR.enum_types_by_name['CriticalErrorCode']
CriticalErrorCode = enum_type_wrapper.EnumTypeWrapper(_CRITICALERRORCODE)
UNSET = 0
TLORA_V2 = 1
TLORA_V1 = 2
TLORA_V2_1_1P6 = 3
TBEAM = 4
HELTEC_V2_0 = 5
TBEAM_V0P7 = 6
T_ECHO = 7
TLORA_V1_1P3 = 8
RAK4631 = 9
HELTEC_V2_1 = 10
HELTEC_V1 = 11
LILYGO_TBEAM_S3_CORE = 12
RAK11200 = 13
NANO_G1 = 14
STATION_G1 = 25
LORA_RELAY_V1 = 32
NRF52840DK = 33
PPR = 34
GENIEBLOCKS = 35
NRF52_UNKNOWN = 36
PORTDUINO = 37
ANDROID_SIM = 38
DIY_V1 = 39
NRF52840_PCA10059 = 40
DR_DEV = 41
M5STACK = 42
PRIVATE_HW = 255
ZERO = 0
DATA_PAYLOAD_LEN = 237
NONE = 0
TX_WATCHDOG = 1
SLEEP_ENTER_WAIT = 2
NO_RADIO = 3
UNSPECIFIED = 4
UBLOX_UNIT_FAILED = 5
NO_AXP192 = 6
INVALID_RADIO_SETTING = 7
TRANSMIT_FAILED = 8
BROWNOUT = 9
SX1262_FAILURE = 10
RADIO_SPI_BUG = 11


_POSITION = DESCRIPTOR.message_types_by_name['Position']
_USER = DESCRIPTOR.message_types_by_name['User']
_ROUTEDISCOVERY = DESCRIPTOR.message_types_by_name['RouteDiscovery']
_ROUTING = DESCRIPTOR.message_types_by_name['Routing']
_DATA = DESCRIPTOR.message_types_by_name['Data']
_WAYPOINT = DESCRIPTOR.message_types_by_name['Waypoint']
_MESHPACKET = DESCRIPTOR.message_types_by_name['MeshPacket']
_NODEINFO = DESCRIPTOR.message_types_by_name['NodeInfo']
_MYNODEINFO = DESCRIPTOR.message_types_by_name['MyNodeInfo']
_LOGRECORD = DESCRIPTOR.message_types_by_name['LogRecord']
_FROMRADIO = DESCRIPTOR.message_types_by_name['FromRadio']
_TORADIO = DESCRIPTOR.message_types_by_name['ToRadio']
_TORADIO_PEERINFO = _TORADIO.nested_types_by_name['PeerInfo']
_COMPRESSED = DESCRIPTOR.message_types_by_name['Compressed']
_POSITION_LOCSOURCE = _POSITION.enum_types_by_name['LocSource']
_POSITION_ALTSOURCE = _POSITION.enum_types_by_name['AltSource']
_ROUTING_ERROR = _ROUTING.enum_types_by_name['Error']
_MESHPACKET_PRIORITY = _MESHPACKET.enum_types_by_name['Priority']
_MESHPACKET_DELAYED = _MESHPACKET.enum_types_by_name['Delayed']
_LOGRECORD_LEVEL = _LOGRECORD.enum_types_by_name['Level']
Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:Position)
  })
_sym_db.RegisterMessage(Position)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:User)
  })
_sym_db.RegisterMessage(User)

RouteDiscovery = _reflection.GeneratedProtocolMessageType('RouteDiscovery', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEDISCOVERY,
  '__module__' : 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:RouteDiscovery)
  })
_sym_db.RegisterMessage(RouteDiscovery)

Routing = _reflection.GeneratedProtocolMessageType('Routing', (_message.Message,), {
  'DESCRIPTOR' : _ROUTING,
  '__module__' : 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:Routing)
  })
_sym_db.RegisterMessage(Routing)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:Data)
  })
_sym_db.RegisterMessage(Data)

Waypoint = _reflection.GeneratedProtocolMessageType('Waypoint', (_message.Message,), {
  'DESCRIPTOR' : _WAYPOINT,
  '__module__' : 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:Waypoint)
  })
_sym_db.RegisterMessage(Waypoint)

MeshPacket = _reflection.GeneratedProtocolMessageType('MeshPacket', (_message.Message,), {
  'DESCRIPTOR' : _MESHPACKET,
  '__module__' : 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:MeshPacket)
  })
_sym_db.RegisterMessage(MeshPacket)

NodeInfo = _reflection.GeneratedProtocolMessageType('NodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _NODEINFO,
  '__module__' : 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:NodeInfo)
  })
_sym_db.RegisterMessage(NodeInfo)

MyNodeInfo = _reflection.GeneratedProtocolMessageType('MyNodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _MYNODEINFO,
  '__module__' : 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:MyNodeInfo)
  })
_sym_db.RegisterMessage(MyNodeInfo)

LogRecord = _reflection.GeneratedProtocolMessageType('LogRecord', (_message.Message,), {
  'DESCRIPTOR' : _LOGRECORD,
  '__module__' : 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:LogRecord)
  })
_sym_db.RegisterMessage(LogRecord)

FromRadio = _reflection.GeneratedProtocolMessageType('FromRadio', (_message.Message,), {
  'DESCRIPTOR' : _FROMRADIO,
  '__module__' : 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:FromRadio)
  })
_sym_db.RegisterMessage(FromRadio)

ToRadio = _reflection.GeneratedProtocolMessageType('ToRadio', (_message.Message,), {

  'PeerInfo' : _reflection.GeneratedProtocolMessageType('PeerInfo', (_message.Message,), {
    'DESCRIPTOR' : _TORADIO_PEERINFO,
    '__module__' : 'mesh_pb2'
    # @@protoc_insertion_point(class_scope:ToRadio.PeerInfo)
    })
  ,
  'DESCRIPTOR' : _TORADIO,
  '__module__' : 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:ToRadio)
  })
_sym_db.RegisterMessage(ToRadio)
_sym_db.RegisterMessage(ToRadio.PeerInfo)

Compressed = _reflection.GeneratedProtocolMessageType('Compressed', (_message.Message,), {
  'DESCRIPTOR' : _COMPRESSED,
  '__module__' : 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:Compressed)
  })
_sym_db.RegisterMessage(Compressed)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\nMeshProtosH\003Z\"github.com/meshtastic/go/generated'
  _HARDWAREMODEL._serialized_start=3348
  _HARDWAREMODEL._serialized_end=3799
  _CONSTANTS._serialized_start=3801
  _CONSTANTS._serialized_end=3845
  _CRITICALERRORCODE._serialized_start=3848
  _CRITICALERRORCODE._serialized_end=4086
  _POSITION._serialized_start=98
  _POSITION._serialized_end=793
  _POSITION_LOCSOURCE._serialized_start=615
  _POSITION_LOCSOURCE._serialized_end=693
  _POSITION_ALTSOURCE._serialized_start=695
  _POSITION_ALTSOURCE._serialized_end=793
  _USER._serialized_start=796
  _USER._serialized_end=925
  _ROUTEDISCOVERY._serialized_start=927
  _ROUTEDISCOVERY._serialized_end=958
  _ROUTING._serialized_start=961
  _ROUTING._serialized_end=1286
  _ROUTING_ERROR._serialized_start=1095
  _ROUTING_ERROR._serialized_end=1275
  _DATA._serialized_start=1289
  _DATA._serialized_end=1445
  _WAYPOINT._serialized_start=1448
  _WAYPOINT._serialized_end=1578
  _MESHPACKET._serialized_start=1581
  _MESHPACKET._serialized_end=2040
  _MESHPACKET_PRIORITY._serialized_start=1862
  _MESHPACKET_PRIORITY._serialized_end=1953
  _MESHPACKET_DELAYED._serialized_start=1955
  _MESHPACKET_DELAYED._serialized_end=2021
  _NODEINFO._serialized_start=2043
  _NODEINFO._serialized_end=2189
  _MYNODEINFO._serialized_start=2192
  _MYNODEINFO._serialized_end=2582
  _LOGRECORD._serialized_start=2585
  _LOGRECORD._serialized_end=2766
  _LOGRECORD_LEVEL._serialized_start=2678
  _LOGRECORD_LEVEL._serialized_end=2766
  _FROMRADIO._serialized_start=2769
  _FROMRADIO._serialized_end=3085
  _TORADIO._serialized_start=3088
  _TORADIO._serialized_end=3290
  _TORADIO_PEERINFO._serialized_start=3218
  _TORADIO_PEERINFO._serialized_end=3271
  _COMPRESSED._serialized_start=3292
  _COMPRESSED._serialized_end=3345
# @@protoc_insertion_point(module_scope)
