# Auto generated Python source file from Ada sources
# Call 'make' in 'src/vhdl' to regenerate:
#
from enum import IntEnum, unique
from pyTooling.Decorators import export

from pyGHDL.libghdl._decorator import BindToLibGHDL


@export
@BindToLibGHDL("errorout__enable_warning")
def Enable_Warning(Id: int, Enable: bool) -> None:
    """"""


@export
@unique
class Msgid(IntEnum):
    Msgid_Note = 0
    Warnid_Library = 1
    Warnid_Deprecated_Option = 2
    Warnid_Unexpected_Option = 3
    Warnid_Missing_Xref = 4
    Warnid_Default_Binding = 5
    Warnid_Binding = 6
    Warnid_Port = 7
    Warnid_Reserved_Word = 8
    Warnid_Pragma = 9
    Warnid_Nested_Comment = 10
    Warnid_Parenthesis = 11
    Warnid_Vital_Generic = 12
    Warnid_Delayed_Checks = 13
    Warnid_Body = 14
    Warnid_Specs = 15
    Warnid_Universal = 16
    Warnid_Port_Bounds = 17
    Warnid_Runtime_Error = 18
    Warnid_Delta_Cycle = 19
    Warnid_Missing_Wait = 20
    Warnid_Shared = 21
    Warnid_Hide = 22
    Warnid_Unused = 23
    Warnid_Nowrite = 24
    Warnid_Logic_Loop = 25
    Warnid_Others = 26
    Warnid_Pure = 27
    Warnid_Analyze_Assert = 28
    Warnid_Attribute = 29
    Warnid_Useless = 30
    Warnid_Missing_Assoc = 31
    Warnid_Conformance = 32
    Warnid_Unkept_Attribute = 33
    Warnid_Unhandled_Attribute = 34
    Warnid_Static = 35
    Warnid_Elaboration = 36
    Msgid_Warning = 37
    Msgid_Error = 38
    Msgid_Fatal = 39
