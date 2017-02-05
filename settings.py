
# In each proto file, the max count of message defines.
MAX_ID_COUNT_PER_FILE = 1000

# Name space / module of MsgID.
NAME_SPACE = 'PBX'
# Name space of c# MsgID.
NAME_SPACE_CS = 'Lite'

# Auto copy generated file to dest folders.
AUTO_COPY_FILE = True

# use protobuf-net or only use google.protobuf to generate cs files.
USE_PROTOBUF_NET = True

# Generated c# files will be copied to this folder.
CS_DEST_DIR = ['/../LiteServer/LiteServer/Source/Logic/Protocol/auto_gen/']#, '/../uLab/uLab/Assets/Scripts/Network/Protocol/auto_gen/']

# Generated lua files will be copied to this folder.
LUA_DEST_DIR = '/../uLab/uLab/Assets/Lua/protocol/'

# Generated javascript files will be copied to this folder.
JS_DEST_DIR = '/../LiteServer/IOClient/assets/scripts/protobuf/'

# Generated python files will be copied to this folder.
PY_DEST_DIR = ''