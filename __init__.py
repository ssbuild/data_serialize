# @Time    : 2022/9/15 13:51
# @Author  : tk
# @FileName: __init__.py
import inspect

try:
    from google.protobuf import __version__ as pb_ver

except:
    pb_ver = '3'

if pb_ver.startswith('5'):
    from .pb5.feature_pb2 import *
    from .pb5.example_pb2 import *
    from .pb5.numpyobject_pb2 import *

elif pb_ver.startswith('4') or pb_ver.startswith('3.20') or pb_ver.startswith('3.21') :
    from .pb4.feature_pb2 import *
    from .pb4.example_pb2 import *
    from .pb4.numpyobject_pb2 import *
else:
    from .pb.feature_pb2 import *
    from .pb.example_pb2 import *
    from .pb.numpyobject_pb2 import *
