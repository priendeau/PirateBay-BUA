from struct import *

class StructReference( object ):
    __allPass__={ 'StructReference':[] }

    class NotImplementedYet( Warning ):
        Msg='NotImplementedYet raised for Future developpment or schema not completed from function %s, class: %s'
        MsgClass='NotImplementedYet raised for Future developpment or schema not completed No Member Are registered in class %s'
        def __init__(self, value ):
            if len( value ) == 2:
                self.FuncName, self.ClassName = value
            if not self.ClassName in ObjectCodeAnalysisImplement.__allPass__.keys():
                Warning.__init__( self, self.MsgClass % ( value ) )
            else:
                if not self.FuncName in ObjectCodeAnalysisImplement[self.ClassName]:
                    Warning.__init__( self, self.Msg % ( self.FuncName, self.ClassName ) )
                else:
                  pass
    
    DictKeyDictReference=['symbol','type','size']
    DictAttrFromModule=['pack','unpack','calcsize']
    TypeAssociation={
      'char':{
        'symbol':'c',       'type':type(str()),     'size':1 },
      'signed char':{
        'symbol':'b',       'type':type(int()),     'size':1 },             
      'unsigned char':{
        'symbol':'B',       'type':type(int()),     'size':1 },
      'Bool':{
        'symbol':'?',       'type':type(bool()),    'size':1 },
      'short':{
        'symbol':'h',       'type':type(int()),     'size':2 },
      'unsigned short':{
        'symbol':'H',       'type':type(int()),     'size':2 },
      'int':{
        'symbol':'i',       'type':type(int()),     'size':4 },
      'unsigned int':{
        'symbol':'I',       'type':type(int()),     'size':4 },
      'long':{
        'symbol':'l',       'type':type(int()),     'size':4 },
      'unsigned long':{
        'symbol':'L',       'type':type(int()),     'size':4 },
      'long long':{
        'symbol':'q',       'type':type(int()),     'size':8 },
      'unsigned long long':{
        'symbol':'Q',       'type':type(int()),     'size':8 },
      'float':{
        'symbol':'f',       'type':type(float()),   'size':4 },
      'double':{
        'symbol':'d',       'type':type(float()),   'size':8 },
      'char[]':{
        'symbol':'s',       'type':type(str()),     'size':-1 },
      'char[]':{
        'symbol':'p',       'type':type(str()),     'size':-1 },
      'void *':{
        'symbol':'P',       'type':type(int()),     'size':-1 } }


    """
        Order 1s from Struct module to handle pack/unpack, Setting Dict Property which is
        implicit in this case ( non-essential TODO. ), Once None Essential is meeted,
        moving 1s from this def to processor property and Endian management and promoting
        this work of 'Setting Dict Property' has 2s, and 2s to 2p ... 
    """

    
    """
        Order 2s from Struct module to handle pack/unpack, dictionary definition before to
        produce a pack/unpack Getter/Setter. 
    """

    DefaultStructAttrType=None
    def GetStructAttrType( self ):
        raise self.NotImplementedYet, self.GetStructAttrType.__name__, self.__class__.__name__
      return self.TypeAssociation[ self.DefaultStructReprName ][ DefaultKey ]
    
    def SetStructAttrType( self, value ):
        raise self.NotImplementedYet, self.SetStructAttrType.__name__, self.__class__.__name__
      self.

    PropertyStructAttrType=property( GetStructAttrType, SetStructAttrType )

    DefaultStructSymbol=None
    def GetStructSymbol( self ):
        raise self.NotImplementedYet, self.GetStructSymbol.__name__, self.__class__.__name__
      return self.TypeAssociation[ self.DefaultStructReprName ][ self.DefaultStructSymbol ]

    def SetStructSymbol( self, value ):
        raise self.NotImplementedYet, self.SetStructSymbol.__name__, self.__class__.__name__
      self.

    PropertyStructSymbol=property( GetStructSymbol, SetStructSymbol )


    DefaultStructReprSize=None

    def GetStructSize( self ):
        raise self.NotImplementedYet, self.GetStructSize.__name__, self.__class__.__name__
      return self.TypeAssociation[ self.DefaultStructReprName ][ self.DefaultStructReprSize ]

    def SetStructSize( self, value ):
        raise self.NotImplementedYet, self.SetStructSize.__name__, self.__class__.__name__
      self.DefaultStructReprSize = value

    PropertyStructSize=property( GetStructSize, SetStructSize )

    DefaultStructReprName=None

    def GetStructName( self ):
        raise self.NotImplementedYet, self.GetStructName.__name__, self.__class__.__name__
      return self.DefaultStructReprName
    
    def SetStructName( self, value ):
        raise self.NotImplementedYet, self.SetStructName.__name__, self.__class__.__name__
        self.DefaultStructReprName = value
        valueKeysymbol, valueKeyType, valueKeysize = self.DictKeyDictReference
        self.PropertyStructSymbol=valueKeysymbol
        self.PropertyStructAttrType=valueKeyType
        self.PropertyStructSize=valueKeysize
        
        

    PropertyStructName=property( GetStructName, SetStructName )

    DefaultStructIdName=None
    
    def GetStruct( self ):
        raise self.NotImplementedYet, self.GetStruct.__name__, self.__class__.__name__          
    
    def SetStruct( self, value ):
        raise self.NotImplementedYet, self.SetStruct.__name__, self.__class__.__name__
        valueKeyName = value 
        
        
        
      
    PropertyStruct=property( GetStruct, SetStruct )

    """
        Order 2p
    """

    """
        Order 3s 
    """

    """
        Order 3p 
    """

    """ Order 3d """
    """ Order 4s """
    """ Order 4p """
    """ Order 4d """
    """ Order 4f """
    """ Order 5s """
    """ Order 5p """
    """ Order 5d """
    """ Order 5f """

