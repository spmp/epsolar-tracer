
# Fake version of modbus client with some predefetched request/reply data

from pymodbus.constants import Defaults
from pymodbus.factory import ClientDecoder
from pymodbus.client.sync import BaseModbusClient
from pymodbus.transaction import ModbusAsciiFramer, ModbusRtuFramer
from pymodbus.exceptions import ParameterException

#---------------------------------------------------------------------------#
# Logging
#---------------------------------------------------------------------------#
import logging
_logger = logging.getLogger(__name__)

class ModbusMockClient(BaseModbusClient):
    ''' Implementation of a modbus serial client
    '''

    def __init__(self, method='rtu', **kwargs):
        ''' Initialize a serial client instance

        The methods to connect are::

          - rtu

        :param method: The method to use for connection
        :param port: The serial port to attach to
        :param stopbits: The number of stop bits to use
        :param bytesize: The bytesize of the serial messages
        :param parity: Which kind of parity to use
        :param baudrate: The baud rate to use for the serial device
        :param timeout: The timeout between serial requests (default 3s)
        '''
        self.method   = method
        self.socket   = None
        BaseModbusClient.__init__(self, self.__implementation(method))

        self.port     = kwargs.get('port', 0)
        self.stopbits = kwargs.get('stopbits', Defaults.Stopbits)
        self.bytesize = kwargs.get('bytesize', Defaults.Bytesize)
        self.parity   = kwargs.get('parity',   Defaults.Parity)
        self.baudrate = kwargs.get('baudrate', Defaults.Baudrate)
        self.timeout  = kwargs.get('timeout',  Defaults.Timeout)

    @staticmethod
    def __implementation(method):
        ''' Returns the requested framer

        :method: The serial framer to instantiate
        :returns: The requested serial framer
        '''
        method = method.lower()
        if method == 'rtu':    return ModbusRtuFramer(ClientDecoder())
        raise ParameterException("Invalid framer method requested")

    def connect(self):
        ''' Connect to the modbus tcp server

        :returns: True if connection succeeded, False otherwise
        '''
        return True

    def close(self):
        ''' Closes the underlying socket connection
        '''

    def _send(self, request):
        ''' Sends data on the underlying socket

        :param request: The encoded request to send
        :return: The number of bytes written
        '''
        _logger.debug ("send " + repr(request))
        if testdata.has_key(request):
            self.data = testdata[request]
        else:
            self.data = ''
        return len(request)

    def _recv(self, size):
        ''' Reads data from the underlying descriptor

        :param size: The number of bytes to read
        :return: The bytes read
        '''
        data = self.data
        _logger.debug ("recv " + repr(data))
        self.data = ''
        return data
        
    def __str__(self):
        ''' Builds a string representation of the connection

        :returns: The string representation
        '''
        return "%s baud[%s]" % (self.method, self.baudrate)

#---------------------------------------------------------------------------#
# Exported symbols
#---------------------------------------------------------------------------#
__all__ = [
    "ModbusMockClient"
]


testdata = {
    '\x01+\x0e\x01\x00pw' : '\x01+\x0e\x01\x01\x00\x00\x03\x00\x15EPsolar Tech co., Ltd\x01\x0cTracer2215BN\x02\rV02.05+V07.12\xd7\xd8' ,
    '\x01\x03\x90\x13\x00\x03\xd9\x0e'
    : '\x01\x03\x06\x18\x05\x02\x02\x0f\x07\n\xe7'
, '\x01\x040\x00\x00\x01>\xca'
: '\x01\x04\x02:\x98\xaa:'
, '\x01\x030\x00\x00\x01\x8b\n'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x040\x01\x00\x01o\n'
: '\x01\x04\x02\x07\xd0\xba\x9c'
, '\x01\x030\x01\x00\x01\xda\xca'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x040\x02\x00\x01\x9f\n'
: '\x01\x04\x02\xcb \xef\xd8'
, '\x01\x030\x02\x00\x01*\xca'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x040\x03\x00\x01\xce\xca'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x030\x03\x00\x01{\n'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x040\x04\x00\x01\x7f\x0b'
: '\x01\x04\x02\t`\xbfH'
, '\x01\x030\x04\x00\x01\xca\xcb'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x040\x05\x00\x01.\xcb'
: '\x01\x04\x02\x07\xd0\xba\x9c'
, '\x01\x030\x05\x00\x01\x9b\x0b'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x040\x06\x00\x01\xde\xcb'
: '\x01\x04\x02\xc3P\xe9\xfc'
, '\x01\x030\x06\x00\x01k\x0b'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x040\x07\x00\x01\x8f\x0b'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x030\x07\x00\x01:\xcb'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x040\x08\x00\x01\xbf\x08'
: '\x01\x04\x02\x00\x028\xf1'
, '\x01\x030\x08\x00\x01\n\xc8'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x040\x0e\x00\x01_\t'
: '\x01\x04\x02\x07\xd0\xba\x9c'
, '\x01\x030\x0e\x00\x01\xea\xc9'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x00\x00\x01?6'
: '\x01\x04\x02\x00\xc5yc'
, '\x01\x031\x00\x00\x01\x8a\xf6'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x01\x00\x01n\xf6'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x031\x01\x00\x01\xdb6'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x02\x00\x01\x9e\xf6'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x031\x02\x00\x01+6'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x03\x00\x01\xcf6'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x031\x03\x00\x01z\xf6'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x04\x00\x01~\xf7'
: '\x01\x04\x02\x05\x10\xbb\xac'
, '\x01\x031\x04\x00\x01\xcb7'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x05\x00\x01/7'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x031\x05\x00\x01\x9a\xf7'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x06\x00\x01\xdf7'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x031\x06\x00\x01j\xf7'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x07\x00\x01\x8e\xf7'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x031\x07\x00\x01;7'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x0c\x00\x01\xff5'
: '\x01\x04\x02\x05\x0f\xfad'
, '\x01\x031\x0c\x00\x01J\xf5'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\r\x00\x01\xae\xf5'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x031\r\x00\x01\x1b5'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x0e\x00\x01^\xf5'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x031\x0e\x00\x01\xeb5'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x0f\x00\x01\x0f5'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x031\x0f\x00\x01\xba\xf5'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x10\x00\x01>\xf3'
: '\x01\x04\x02\t\xc4\xbe\xf3'
, '\x01\x031\x10\x00\x01\x8b3'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x11\x00\x01o3'
: '\x01\x04\x02\x0bI\x7f\xf6'
, '\x01\x031\x11\x00\x01\xda\xf3'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x12\x00\x01\x9f3'
: '\x01\x04\x02\x0bI\x7f\xf6'
, '\x01\x031\x12\x00\x01*\xf3'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x1a\x00\x01\x1e\xf1'
: '\x01\x04\x02\x00F8\xc2'
, '\x01\x031\x1a\x00\x01\xab1'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x1b\x00\x01O1'
: '\x01\x04\x02\t\xc4\xbe\xf3'
, '\x01\x031\x1b\x00\x01\xfa\xf1'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x041\x1d\x00\x01\xaf0'
: '\x01\x04\x02\x04\xb0\xbaD'
, '\x01\x031\x1d\x00\x01\x1a\xf0'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x042\x00\x00\x01?r'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x032\x00\x00\x01\x8a\xb2'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x042\x01\x00\x01n\xb2'
: '\x01\x04\x02\x00\x01x\xf0'
, '\x01\x032\x01\x00\x01\xdbr'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x00\x00\x01>\x8e'
: '\x01\x04\x02\x00\xcc\xb9e'
, '\x01\x033\x00\x00\x01\x8bN'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x01\x00\x01oN'
: '\x01\x04\x02\x00\xbe9@'
, '\x01\x033\x01\x00\x01\xda\x8e'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x02\x00\x01\x9fN'
: '\x01\x04\x02\x05\x12:m'
, '\x01\x033\x02\x00\x01*\x8e'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x03\x00\x01\xce\x8e'
: '\x01\x04\x02\x05\x0f\xfad'
, '\x01\x033\x03\x00\x01{N'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x04\x00\x01\x7fO'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x033\x04\x00\x01\xca\x8f'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x05\x00\x01.\x8f'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x033\x05\x00\x01\x9bO'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x06\x00\x01\xde\x8f'
: '\x01\x04\x02\x00\x028\xf1'
, '\x01\x033\x06\x00\x01kO'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x07\x00\x01\x8fO'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x033\x07\x00\x01:\x8f'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x08\x00\x01\xbfL'
: '\x01\x04\x02\x00\xa28\x89'
, '\x01\x033\x08\x00\x01\n\x8c'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\t\x00\x01\xee\x8c'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x033\t\x00\x01[L'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\n\x00\x01\x1e\x8c'
: '\x01\x04\x02\x00\xa28\x89'
, '\x01\x033\n\x00\x01\xabL'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x0b\x00\x01OL'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x033\x0b\x00\x01\xfa\x8c'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x0c\x00\x01\xfe\x8d'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x033\x0c\x00\x01KM'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\r\x00\x01\xafM'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x033\r\x00\x01\x1a\x8d'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x0e\x00\x01_M'
: '\x01\x04\x02\x00\x0b\xf8\xf7'
, '\x01\x033\x0e\x00\x01\xea\x8d'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x0f\x00\x01\x0e\x8d'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x033\x0f\x00\x01\xbbM'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x10\x00\x01?K'
: '\x01\x04\x02\x01\x169n'
, '\x01\x033\x10\x00\x01\x8a\x8b'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x11\x00\x01n\x8b'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x033\x11\x00\x01\xdbK'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x12\x00\x01\x9e\x8b'
: '\x01\x04\x02\x01\x169n'
, '\x01\x033\x12\x00\x01+K'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x13\x00\x01\xcfK'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x033\x13\x00\x01z\x8b'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x14\x00\x01~\x8a'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x033\x14\x00\x01\xcbJ'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x15\x00\x01/J'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x033\x15\x00\x01\x9a\x8a'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x1b\x00\x01N\x89'
: '\x01\x04\x02\x00\x00\xb90'
, '\x01\x033\x1b\x00\x01\xfbI'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x1c\x00\x01\xffH'
: '\x01\x04\x02\xff\xff\xb8\x80'
, '\x01\x033\x1c\x00\x01J\x88'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x1d\x00\x01\xae\x88'
: '\x01\x04\x02\t\xc4\xbe\xf3'
, '\x01\x033\x1d\x00\x01\x1bH'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x043\x1e\x00\x01^\x88'
: '\x01\x04\x02\t\xc4\xbe\xf3'
, '\x01\x033\x1e\x00\x01\xebH'
: '\x01\x83\x02\xc0\xf1'
, '\x01\x04\x90\x00\x00\x01\x1c\xca'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x00\x00\x01\xa9\n'
: '\x01\x03\x02\x00\x01y\x84'
, '\x01\x04\x90\x01\x00\x01M\n'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x01\x00\x01\xf8\xca'
: '\x01\x03\x02\x00d\xb9\xaf'
, '\x01\x04\x90\x02\x00\x01\xbd\n'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x02\x00\x01\x08\xca'
: '\x01\x03\x02\x01,\xb8\t'
, '\x01\x04\x90\x03\x00\x01\xec\xca'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x03\x00\x01Y\n'
: '\x01\x03\x02\x06@\xba\x14'
, '\x01\x04\x90\x04\x00\x01]\x0b'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x04\x00\x01\xe8\xcb'
: '\x01\x03\x02\x05\xdc\xba\x8d'
, '\x01\x04\x90\x05\x00\x01\x0c\xcb'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x05\x00\x01\xb9\x0b'
: '\x01\x03\x02\x05\xdc\xba\x8d'
, '\x01\x04\x90\x06\x00\x01\xfc\xcb'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x06\x00\x01I\x0b'
: '\x01\x03\x02\x05\xb4\xbbc'
, '\x01\x04\x90\x07\x00\x01\xad\x0b'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x07\x00\x01\x18\xcb'
: '\x01\x03\x02\x05\xa0\xbbl'
, '\x01\x04\x90\x08\x00\x01\x9d\x08'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x08\x00\x01(\xc8'
: '\x01\x03\x02\x05d\xba\xff'
, '\x01\x04\x90\t\x00\x01\xcc\xc8'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\t\x00\x01y\x08'
: '\x01\x03\x02\x05(\xbb\n'
, '\x01\x04\x90\n\x00\x01<\xc8'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\n\x00\x01\x89\x08'
: '\x01\x03\x02\x04\xec\xbb\t'
, '\x01\x04\x90\x0b\x00\x01m\x08'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x0b\x00\x01\xd8\xc8'
: '\x01\x03\x02\x04\xc4\xbb\x17'
, '\x01\x04\x90\x0c\x00\x01\xdc\xc9'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x0c\x00\x01i\t'
: '\x01\x03\x02\x04\xb0\xbb0'
, '\x01\x04\x90\r\x00\x01\x8d\t'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\r\x00\x018\xc9'
: '\x01\x03\x02\x04V:\xba'
, '\x01\x04\x90\x0e\x00\x01}\t'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x0e\x00\x01\xc8\xc9'
: '\x01\x03\x02\x04$\xba\x9f'
, '\x01\x04\x90\x13\x00\x01\xed\x0f'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x13\x00\x01X\xcf'
: '\x01\x03\x02\x1a\x1e3,'
, '\x01\x04\x90\x14\x00\x01\\\xce'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x14\x00\x01\xe9\x0e'
: '\x01\x03\x02\x02\x028\xe5'
, '\x01\x04\x90\x15\x00\x01\r\x0e'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x15\x00\x01\xb8\xce'
: '\x01\x03\x02\x0f\x07\xfcv'
, '\x01\x04\x90\x16\x00\x01\xfd\x0e'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x16\x00\x01H\xce'
: '\x01\x03\x02\x00\x1e8L'
, '\x01\x04\x90\x17\x00\x01\xac\xce'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x17\x00\x01\x19\x0e'
: '\x01\x03\x02\x19d\xb2?'
, '\x01\x04\x90\x18\x00\x01\x9c\xcd'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x18\x00\x01)\r'
: '\x01\x03\x02\xf0`\xfcl'
, '\x01\x04\x90\x19\x00\x01\xcd\r'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x19\x00\x01x\xcd'
: '\x01\x03\x02!4\xa1\xc3'
, '\x01\x04\x90\x1a\x00\x01=\r'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x1a\x00\x01\x88\xcd'
: '\x01\x03\x02\x1dL\xb0\xe1'
, '\x01\x04\x90\x1b\x00\x01l\xcd'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x1b\x00\x01\xd9\r'
: '\x01\x03\x02!4\xa1\xc3'
, '\x01\x04\x90\x1c\x00\x01\xdd\x0c'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x1c\x00\x01h\xcc'
: '\x01\x03\x02\x1dL\xb0\xe1'
, '\x01\x04\x90\x1d\x00\x01\x8c\xcc'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x1d\x00\x019\x0c'
: '\x01\x03\x02\x00\x00\xb8D'
, '\x01\x04\x90\x1e\x00\x01|\xcc'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x1e\x00\x01\xc9\x0c'
: '\x01\x03\x02\x01\xf4\xb8S'
, '\x01\x04\x90\x1f\x00\x01-\x0c'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90\x1f\x00\x01\x98\xcc'
: '\x01\x03\x02\x00\n8C'
, '\x01\x04\x90 \x00\x01\x1d\x00'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90 \x00\x01\xa8\xc0'
: '\x01\x03\x02\x02X\xb8\xde'
, '\x01\x04\x90!\x00\x01L\xc0'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90!\x00\x01\xf9\x00'
: '\x01\x03\x02\x00\n8C'
, '\x01\x04\x90=\x00\x01\x8d\x06'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90=\x00\x018\xc6'
: '\x01\x03\x02\x00\x00\xb8D'
, '\x01\x04\x90>\x00\x01}\x06'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90>\x00\x01\xc8\xc6'
: '\x01\x03\x02\x01\x00\xb9\xd4'
, '\x01\x04\x90?\x00\x01,\xc6'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90?\x00\x01\x99\x06'
: '\x01\x03\x02\x01\x00\xb9\xd4'
, '\x01\x04\x90B\x00\x01\xbc\xde'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90B\x00\x01\t\x1e'
: '\x01\x03\x02\x00\x00\xb8D'
, '\x01\x04\x90C\x00\x01\xed\x1e'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90C\x00\x01X\xde'
: '\x01\x03\x02\x00\x00\xb8D'
, '\x01\x04\x90D\x00\x01\\\xdf'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90D\x00\x01\xe9\x1f'
: '\x01\x03\x02\x00\x13\xf9\x89'
, '\x01\x04\x90E\x00\x01\r\x1f'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90E\x00\x01\xb8\xdf'
: '\x01\x03\x02\x00\x00\xb8D'
, '\x01\x04\x90F\x00\x01\xfd\x1f'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90F\x00\x01H\xdf'
: '\x01\x03\x02\x00\x00\xb8D'
, '\x01\x04\x90G\x00\x01\xac\xdf'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90G\x00\x01\x19\x1f'
: '\x01\x03\x02\x00\x068F'
, '\x01\x04\x90H\x00\x01\x9c\xdc'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90H\x00\x01)\x1c'
: '\x01\x03\x02\x00\x00\xb8D'
, '\x01\x04\x90I\x00\x01\xcd\x1c'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90I\x00\x01x\xdc'
: '\x01\x03\x02\x00\x00\xb8D'
, '\x01\x04\x90J\x00\x01=\x1c'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90J\x00\x01\x88\xdc'
: '\x01\x03\x02\x00\x13\xf9\x89'
, '\x01\x04\x90K\x00\x01l\xdc'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90K\x00\x01\xd9\x1c'
: '\x01\x03\x02\x00\x00\xb8D'
, '\x01\x04\x90L\x00\x01\xdd\x1d'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90L\x00\x01h\xdd'
: '\x01\x03\x02\x00\x00\xb8D'
, '\x01\x04\x90M\x00\x01\x8c\xdd'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90M\x00\x019\x1d'
: '\x01\x03\x02\x00\x068F'
, '\x01\x04\x90e\x00\x01\x0c\xd5'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90e\x00\x01\xb9\x15'
: '\x01\x03\x02\x03\x0f\xf8\xb0'
, '\x01\x04\x90g\x00\x01\xad\x15'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90g\x00\x01\x18\xd5'
: '\x01\x03\x02\x00\x00\xb8D'
, '\x01\x04\x90i\x00\x01\xcc\xd6'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90i\x00\x01y\x16'
: '\x01\x03\x02\x00\x00\xb8D'
, '\x01\x04\x90j\x00\x01<\xd6'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90j\x00\x01\x89\x16'
: '\x01\x03\x02\x00\x01y\x84'
, '\x01\x04\x90k\x00\x01m\x16'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90k\x00\x01\xd8\xd6'
: '\x01\x03\x02\x00x\xb8f'
, '\x01\x04\x90l\x00\x01\xdc\xd7'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90l\x00\x01i\x17'
: '\x01\x03\x02\x00x\xb8f'
, '\x01\x04\x90m\x00\x01\x8d\x17'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90m\x00\x018\xd7'
: '\x01\x03\x02\x00\x1e8L'
, '\x01\x04\x90n\x00\x01}\x17'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90n\x00\x01\xc8\xd7'
: '\x01\x03\x02\x00d\xb9\xaf'
, '\x01\x04\x90p\x00\x01\x1d\x11'
: '\x01\x84\x02\xc2\xc1'
, '\x01\x03\x90p\x00\x01\xa8\xd1'
: '\x01\x03\x02\x00\x00\xb8D'
, '\x01\x01\x00\x02\x00\x01\\\n'
: '\x01\x01\x01\x01\x90H'
, '\x01\x02\x00\x02\x00\x01\x18\n'
: '\x01\x82\x02\xc1a'
, '\x01\x01\x00\x05\x00\x01\xed\xcb'
: '\x01\x01\x01\x00Q\x88'
, '\x01\x02\x00\x05\x00\x01\xa9\xcb'
: '\x01\x82\x02\xc1a'
, '\x01\x01\x00\x06\x00\x01\x1d\xcb'
: '\x01\x01\x01\x00Q\x88'
, '\x01\x02\x00\x06\x00\x01Y\xcb'
: '\x01\x82\x02\xc1a'
, '\x01\x01 \x00\x00\x01\xf6\n'
: '\x01\x81\x02\xc1\x91'
, '\x01\x02 \x00\x00\x01\xb2\n'
: '\x01\x02\x01\x00\xa1\x88'
, '\x01\x01 \x0c\x00\x016\t'
: '\x01\x81\x02\xc1\x91'
, '\x01\x02 \x0c\x00\x01r\t'
: '\x01\x02\x01\x01`H'
}
