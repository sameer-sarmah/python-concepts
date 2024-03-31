from abc import ABC, abstractmethod


class SyncProtocol(ABC):

    @abstractmethod
    def protocolData( self ):
        pass


class Http(SyncProtocol):
    # static variable
    protocol = 'HTTP'

    def __init__( self ):
        super().__init__()

    def protocolData( self ):
        return Http.protocol;

http = Http()
print(http.protocolData())