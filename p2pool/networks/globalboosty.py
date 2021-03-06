from p2pool.bitcoin import networks

PARENT=networks.nets['globalboosty']
SHARE_PERIOD=30
CHAIN_LENGTH=24*60*60//30
REAL_CHAIN_LENGTH=24*60*60//30
TARGET_LOOKBEHIND=20
SPREAD=10
IDENTIFIER='cf90e29bc82c60e7'.decode('hex')
PREFIX='ee87ca7f6c700ee8'.decode('hex')
P2P_PORT=5883
MIN_TARGET=0
MAX_TARGET=2**256//10000 - 1
PERSIST=False
WORKER_PORT=5853
BOOTSTRAP_ADDRS=''.split(' ')
ANNOUNCE_CHANNEL='#p2pool'
VERSION_CHECK=lambda v: True
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000