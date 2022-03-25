from typing import Any, ClassVar, List

from typing import overload
janusDeltaInputOutputVariable: JanusVariableType
janusDeltaInputVariable: JanusVariableType
janusDeltaOutputVariable: JanusVariableType
janusIgnoreUnitsInputOutputVariable: JanusVariableType
janusIgnoreUnitsInputVariable: JanusVariableType
janusIgnoreUnitsOutputVariable: JanusVariableType
janusInputOutputVariable: JanusVariableType
janusInputVariable: JanusVariableType
janusMandatory: bool
janusOutputVariable: JanusVariableType
janusRequired: bool
janusString: JanusVariableType

class Janus:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, filename: str) -> None: ...
    def get_variabledef(self, *args, **kwargs) -> Any: ...
    @property
    def xml_filename(self) -> aFileString: ...

class JanusIndex:
    def __init__(self) -> None: ...

class JanusVariable:
    @overload
    def __init__(self, variable_name: str, variable_type: JanusVariableType, is_mandatory: bool, value: float) -> None: ...
    @overload
    def __init__(self, variable_name: str, variable_type: JanusVariableType, is_mandatory: bool, specific_units: str, value: float) -> None: ...
    def as_str(self) -> aString: ...
    def get_value(self) -> float: ...
    def is_available(self) -> bool: ...
    def is_initialised(self) -> bool: ...
    def is_mandatory(self) -> bool: ...
    def is_missing(self) -> bool: ...
    def set_value(self, arg0: float) -> bool: ...
    @property
    def initial_value(self) -> float: ...
    @property
    def name(self) -> aString: ...
    @property
    def units(self) -> aString: ...
    @property
    def var_id(self) -> aString: ...

class JanusVariableManager(Janus):
    def __init__(self, arg0: str) -> None: ...
    @overload
    def push_back(self, arg0: JanusVariable) -> JanusIndex: ...
    @overload
    def push_back(self, arg0: List[JanusVariable]) -> List[JanusIndex]: ...
    def __getitem__(self, arg0: JanusIndex) -> JanusVariable: ...

class JanusVariableType:
    __doc__: ClassVar[str] = ...  # read-only
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    janusDeltaInputOutputVariable: ClassVar[JanusVariableType] = ...
    janusDeltaInputVariable: ClassVar[JanusVariableType] = ...
    janusDeltaOutputVariable: ClassVar[JanusVariableType] = ...
    janusIgnoreUnitsInputOutputVariable: ClassVar[JanusVariableType] = ...
    janusIgnoreUnitsInputVariable: ClassVar[JanusVariableType] = ...
    janusIgnoreUnitsOutputVariable: ClassVar[JanusVariableType] = ...
    janusInputOutputVariable: ClassVar[JanusVariableType] = ...
    janusInputVariable: ClassVar[JanusVariableType] = ...
    janusOutputVariable: ClassVar[JanusVariableType] = ...
    janusString: ClassVar[JanusVariableType] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class VariableDef:
    def __init__(self, janus: Janus, element_definition) -> None: ...
    def get_value(self) -> float: ...
    def set_value(self, value: float, is_forced: bool = ...) -> None: ...
    @property
    def initial_value(self) -> float: ...
    @property
    def janus(self) -> Janus: ...
    @property
    def name(self) -> aString: ...
    @property
    def units(self) -> aString: ...
    @property
    def var_id(self) -> aString: ...

class aFileString(aString):
    def __init__(self, arg0: str) -> None: ...

class aString:
    def __init__(self, arg0: str) -> None: ...
