# @generated
# To regenerate this file run fbcode//glean/schema/gen/sync
from typing import Optional, Tuple, Union, List, Dict, TypeVar
from thrift.py3 import Struct
from enum import Enum
import ast
from glean.schema.py.glean_schema_predicate import GleanSchemaPredicate , Just, InnerGleanSchemaPredicate
from glean.client.py3.angle_query import angle_for, R
from glean.schema.py.buck import *
from glean.schema.py.builtin import *
from glean.schema.py.cxx1 import *
from glean.schema.py.scm import *
from glean.schema.py.src import *


from glean.schema.thrift.types import (
    ToPython,
    FunctionSpecification,
    ExceptionType,
    TypeDefType,
    FromCpp2,
    FromHack,
    FileDeclaration,
    PythonField,
    FileError,
    PythonModule,
    ConstantType,
    FunctionName,
    TypeSpecification,
    NamespaceName,
    ExceptionVal,
    HackRecord,
    PythonMethod,
    PythonName,
    Namespace,
    ServiceName,
    IncludeStatement,
    TargetX,
    PythonClassContains,
    PythonFileModule,
    TypeDefException,
    EnumValue,
    ServiceDefinition,
    NamespaceValue,
    CompileTarget,
    PythonModuleFile,
    FileTarget,
    EnumValueDef,
    HackRecordContains,
    PythonValue,
    StructType,
    ServiceChild,
    Includes,
    QualName,
    OutputTarget,
    PythonFunction,
    StructuredAnnotation,
    File,
    HackMethod,
    Constant,
    HackName,
    NamedDecl,
    PythonModuleContains,
    HackMap,
    IncludeSpecial,
    FileXRefs,
    Mangle,
    StructVal,
    IncludeSplice,
    Lang,
    Literal,
    Identifier,
    UnionType,
    DeclarationNameSpan,
    FromPython,
    PythonClass,
    ToCpp2,
    ToHack,
    EnumerationType,
    FileOutput,
    ServiceParent,
    MangleLang,
    ExceptionName,
    EnumVal,
    UnionVal,
    Cpp2ItemNamed,
    StructFieldVal,
    Item,
    IntegerLiteral,
    ExceptionSpecName,
    HackRecordKind,
    KeyValue,
    Cpp2Item,
    NamedType,
    UnionFieldVal,
    ExceptionSpecification,
    XRef,
    GenRole,
    UnqualField,
    XRefTarget,
    ContainerType,
    FieldSpecification,
    StructFieldValValue,
    ResultStream,
    TypedConstT,
    HackMapKind,
    MapType,
    NamedKind,
    FloatLiteral,
    TypedConst,
    PrimitiveType,
    ResultType,
    PythonItem,
    Target,
    HackKind,
    Qualifier,
    Loc,
)


class ThriftToPython(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], thrift: ast.Expr, lang: ast.Expr, python: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, thrift, 'thrift'), angle_for(__env, lang, 'lang'), angle_for(__env, python, 'python')]))
    return f"thrift.ToPython.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ToPython

  @staticmethod
  def angle_query(*, thrift: Optional["ThriftFile"] = None, lang: Optional["ThriftLang"] = None, python: Optional[List["ThriftFromPython"]] = None) -> "ThriftToPython":
    raise Exception("this function can only be called from @angle_query")



class ThriftFunctionSpecification(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, result: ast.Expr, arguments: ast.Expr, throws_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, result, 'result'), angle_for(__env, arguments, 'arguments'), angle_for(__env, throws_, 'throws_')]))
    return f"thrift.FunctionSpecification.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FunctionSpecification

  @staticmethod
  def angle_query(*, name: Optional["ThriftFunctionName"] = None, result: Optional["ThriftResultType"] = None, arguments: Optional[List["ThriftUnqualField"]] = None, throws_: Optional[List["ThriftExceptionSpecification"]] = None) -> "ThriftFunctionSpecification":
    raise Exception("this function can only be called from @angle_query")



class ThriftExceptionType(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, fields: ast.Expr, structuredAnnotations: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, fields, 'fields'), angle_for(__env, structuredAnnotations, 'structuredAnnotations')]))
    return f"thrift.ExceptionType.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ExceptionType

  @staticmethod
  def angle_query(*, name: Optional["ThriftQualName"] = None, fields: Optional[List["ThriftFieldSpecification"]] = None, structuredAnnotations: Optional[List["ThriftStructuredAnnotation"]] = None) -> "ThriftExceptionType":
    raise Exception("this function can only be called from @angle_query")



class ThriftTypeDefType(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], alias: ast.Expr, type_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, alias, 'alias'), angle_for(__env, type_, 'type_')]))
    return f"thrift.TypeDefType.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TypeDefType

  @staticmethod
  def angle_query(*, alias: Optional["ThriftQualName"] = None, type_: Optional["ThriftTypeSpecification"] = None) -> "ThriftTypeDefType":
    raise Exception("this function can only be called from @angle_query")



class ThriftFromCpp2(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], cpp2: ast.Expr, thrift: ast.Expr, role: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, cpp2, 'cpp2'), angle_for(__env, thrift, 'thrift'), angle_for(__env, role, 'role')]))
    return f"thrift.FromCpp2.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FromCpp2

  @staticmethod
  def angle_query(*, cpp2: Optional["ThriftCpp2Item"] = None, thrift: Optional["ThriftItem"] = None, role: Optional["ThriftGenRole"] = None) -> "ThriftFromCpp2":
    raise Exception("this function can only be called from @angle_query")



class ThriftFromHack(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], hack: ast.Expr, thrift: ast.Expr, role: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, hack, 'hack'), angle_for(__env, thrift, 'thrift'), angle_for(__env, role, 'role')]))
    return f"thrift.FromHack.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FromHack

  @staticmethod
  def angle_query(*, hack: Optional["ThriftHackKind"] = None, thrift: Optional["ThriftItem"] = None, role: Optional["ThriftGenRole"] = None) -> "ThriftFromHack":
    raise Exception("this function can only be called from @angle_query")



class ThriftFileDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, decl: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, decl, 'decl')]))
    return f"thrift.FileDeclaration.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FileDeclaration

  @staticmethod
  def angle_query(*, file: Optional["ThriftFile"] = None, decl: Optional["ThriftDeclaration"] = None) -> "ThriftFileDeclaration":
    raise Exception("this function can only be called from @angle_query")



class ThriftPythonField(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, class_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, class_, 'class_')]))
    return f"thrift.PythonField.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonField

  @staticmethod
  def angle_query(*, name: Optional["ThriftPythonName"] = None, class_: Optional["ThriftPythonClass"] = None) -> "ThriftPythonField":
    raise Exception("this function can only be called from @angle_query")



class ThriftFileError(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, error: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, error, 'error')]))
    return f"thrift.FileError.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FileError

  @staticmethod
  def angle_query(*, file: Optional["ThriftFile"] = None, error: Optional[str] = None) -> "ThriftFileError":
    raise Exception("this function can only be called from @angle_query")



class ThriftPythonModule(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"thrift.PythonModule.7 { query_fields if query_fields else '_' }", PythonModule

  @staticmethod
  def angle_query(*, arg: Optional["ThriftPythonName"] = None) -> "ThriftPythonModule":
    raise Exception("this function can only be called from @angle_query")



class ThriftConstantType(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, type_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, type_, 'type_')]))
    return f"thrift.ConstantType.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ConstantType

  @staticmethod
  def angle_query(*, name: Optional["ThriftQualName"] = None, type_: Optional["ThriftTypeSpecification"] = None) -> "ThriftConstantType":
    raise Exception("this function can only be called from @angle_query")



class ThriftFunctionName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], service_: ast.Expr, name: ast.Expr, locName: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, service_, 'service_'), angle_for(__env, name, 'name'), angle_for(__env, locName, 'locName')]))
    return f"thrift.FunctionName.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FunctionName

  @staticmethod
  def angle_query(*, service_: Optional["ThriftServiceName"] = None, name: Optional["ThriftIdentifier"] = None, locName: Optional["ThriftLoc"] = None) -> "ThriftFunctionName":
    raise Exception("this function can only be called from @angle_query")



class ThriftTypeSpecification(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], primitive: ast.Expr, container: ast.Expr, named: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, primitive, 'primitive'), angle_for(__env, container, 'container'), angle_for(__env, named, 'named')]))
    return f"thrift.TypeSpecification.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TypeSpecification

  @staticmethod
  def angle_query_primitive(*, primitive: Optional["ThriftPrimitiveType"] = None) -> "ThriftTypeSpecification":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_container(*, container: Optional["ThriftContainerType"] = None) -> "ThriftTypeSpecification":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_named(*, named: Optional["ThriftNamedType"] = None) -> "ThriftTypeSpecification":
    raise Exception("this function can only be called from @angle_query")




class ThriftNamespaceName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"thrift.NamespaceName.7 { query_fields if query_fields else '_' }", NamespaceName

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "ThriftNamespaceName":
    raise Exception("this function can only be called from @angle_query")



class ThriftExceptionVal(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"thrift.ExceptionVal.7 { query_fields if query_fields else '_' }", ExceptionVal

  @staticmethod
  def angle_query(*, arg: Optional["ThriftStructVal"] = None) -> "ThriftExceptionVal":
    raise Exception("this function can only be called from @angle_query")



class ThriftHackRecord(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, kind: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, kind, 'kind')]))
    return f"thrift.HackRecord.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", HackRecord

  @staticmethod
  def angle_query(*, name: Optional["ThriftHackName"] = None, kind: Optional["ThriftHackRecordKind"] = None) -> "ThriftHackRecord":
    raise Exception("this function can only be called from @angle_query")



class ThriftPythonMethod(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, class_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, class_, 'class_')]))
    return f"thrift.PythonMethod.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonMethod

  @staticmethod
  def angle_query(*, name: Optional["ThriftPythonName"] = None, class_: Optional["ThriftPythonClass"] = None) -> "ThriftPythonMethod":
    raise Exception("this function can only be called from @angle_query")



class ThriftPythonName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"thrift.PythonName.7 { query_fields if query_fields else '_' }", PythonName

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "ThriftPythonName":
    raise Exception("this function can only be called from @angle_query")



class ThriftNamespace(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], target: ast.Expr, name: ast.Expr, namespace_: ast.Expr, quoted: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, target, 'target'), angle_for(__env, name, 'name'), angle_for(__env, namespace_, 'namespace_'), angle_for(__env, quoted, 'quoted')]))
    return f"thrift.Namespace.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Namespace

  @staticmethod
  def angle_query(*, target: Optional["ThriftFile"] = None, name: Optional["ThriftNamespaceName"] = None, namespace_: Optional["ThriftNamespaceValue"] = None, quoted: Optional[bool] = None) -> "ThriftNamespace":
    raise Exception("this function can only be called from @angle_query")



class ThriftServiceName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, locName: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, locName, 'locName')]))
    return f"thrift.ServiceName.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ServiceName

  @staticmethod
  def angle_query(*, name: Optional["ThriftQualName"] = None, locName: Optional["ThriftLoc"] = None) -> "ThriftServiceName":
    raise Exception("this function can only be called from @angle_query")



class ThriftIncludeStatement(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], target: ast.Expr, source: ast.Expr, locSource: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, target, 'target'), angle_for(__env, source, 'source'), angle_for(__env, locSource, 'locSource')]))
    return f"thrift.IncludeStatement.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", IncludeStatement

  @staticmethod
  def angle_query(*, target: Optional["ThriftFile"] = None, source: Optional["ThriftFile"] = None, locSource: Optional["ThriftLoc"] = None) -> "ThriftIncludeStatement":
    raise Exception("this function can only be called from @angle_query")



class ThriftTargetX(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], target: ast.Expr, fileRef: ast.Expr, locRef: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, target, 'target'), angle_for(__env, fileRef, 'fileRef'), angle_for(__env, locRef, 'locRef')]))
    return f"thrift.TargetX.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TargetX

  @staticmethod
  def angle_query(*, target: Optional["ThriftXRefTarget"] = None, fileRef: Optional["ThriftFile"] = None, locRef: Optional["ThriftLoc"] = None) -> "ThriftTargetX":
    raise Exception("this function can only be called from @angle_query")



class ThriftPythonClassContains(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], class_: ast.Expr, methods: ast.Expr, fields: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, class_, 'class_'), angle_for(__env, methods, 'methods'), angle_for(__env, fields, 'fields')]))
    return f"thrift.PythonClassContains.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonClassContains

  @staticmethod
  def angle_query(*, class_: Optional["ThriftPythonClass"] = None, methods: Optional[List["ThriftPythonMethod"]] = None, fields: Optional[List["ThriftPythonField"]] = None) -> "ThriftPythonClassContains":
    raise Exception("this function can only be called from @angle_query")



class ThriftPythonFileModule(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, module: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, module, 'module')]))
    return f"thrift.PythonFileModule.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonFileModule

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, module: Optional["ThriftPythonModule"] = None) -> "ThriftPythonFileModule":
    raise Exception("this function can only be called from @angle_query")



class ThriftTypeDefException(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], alias: ast.Expr, type_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, alias, 'alias'), angle_for(__env, type_, 'type_')]))
    return f"thrift.TypeDefException.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TypeDefException

  @staticmethod
  def angle_query(*, alias: Optional["ThriftNamedDecl"] = None, type_: Optional["ThriftExceptionSpecName"] = None) -> "ThriftTypeDefException":
    raise Exception("this function can only be called from @angle_query")



class ThriftEnumValue(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], enum_: ast.Expr, name: ast.Expr, locName: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, enum_, 'enum_'), angle_for(__env, name, 'name'), angle_for(__env, locName, 'locName')]))
    return f"thrift.EnumValue.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", EnumValue

  @staticmethod
  def angle_query(*, enum_: Optional["ThriftNamedType"] = None, name: Optional["ThriftIdentifier"] = None, locName: Optional["ThriftLoc"] = None) -> "ThriftEnumValue":
    raise Exception("this function can only be called from @angle_query")



class ThriftServiceDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, functions: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, functions, 'functions')]))
    return f"thrift.ServiceDefinition.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ServiceDefinition

  @staticmethod
  def angle_query(*, name: Optional["ThriftServiceName"] = None, functions: Optional[List["ThriftFunctionSpecification"]] = None) -> "ThriftServiceDefinition":
    raise Exception("this function can only be called from @angle_query")



class ThriftNamespaceValue(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"thrift.NamespaceValue.7 { query_fields if query_fields else '_' }", NamespaceValue

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "ThriftNamespaceValue":
    raise Exception("this function can only be called from @angle_query")



class ThriftCompileTarget(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], includes: ast.Expr, lang: ast.Expr, compile: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, includes, 'includes'), angle_for(__env, lang, 'lang'), angle_for(__env, compile, 'compile')]))
    return f"thrift.CompileTarget.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", CompileTarget

  @staticmethod
  def angle_query(*, includes: Optional["ThriftFileTarget"] = None, lang: Optional["ThriftFbcodeLang"] = None, compile: Optional["BuckTarget"] = None) -> "ThriftCompileTarget":
    raise Exception("this function can only be called from @angle_query")



class ThriftPythonModuleFile(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], module: ast.Expr, file: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, module, 'module'), angle_for(__env, file, 'file')]))
    return f"thrift.PythonModuleFile.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonModuleFile

  @staticmethod
  def angle_query(*, module: Optional["ThriftPythonModule"] = None, file: Optional["SrcFile"] = None) -> "ThriftPythonModuleFile":
    raise Exception("this function can only be called from @angle_query")



class ThriftFileTarget(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, target: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, target, 'target')]))
    return f"thrift.FileTarget.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FileTarget

  @staticmethod
  def angle_query(*, file: Optional["ThriftFile"] = None, target: Optional["BuckTarget"] = None) -> "ThriftFileTarget":
    raise Exception("this function can only be called from @angle_query")



class ThriftEnumValueDef(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, value: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, value, 'value')]))
    return f"thrift.EnumValueDef.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", EnumValueDef

  @staticmethod
  def angle_query(*, name: Optional["ThriftEnumValue"] = None, value: Optional["ThriftIntegerLiteral"] = None) -> "ThriftEnumValueDef":
    raise Exception("this function can only be called from @angle_query")



class ThriftHackRecordContains(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], record: ast.Expr, methods: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, record, 'record'), angle_for(__env, methods, 'methods')]))
    return f"thrift.HackRecordContains.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", HackRecordContains

  @staticmethod
  def angle_query(*, record: Optional["ThriftHackRecord"] = None, methods: Optional[List["ThriftHackMethod"]] = None) -> "ThriftHackRecordContains":
    raise Exception("this function can only be called from @angle_query")



class ThriftPythonValue(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, module: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, module, 'module')]))
    return f"thrift.PythonValue.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonValue

  @staticmethod
  def angle_query(*, name: Optional["ThriftPythonName"] = None, module: Optional["ThriftPythonModule"] = None) -> "ThriftPythonValue":
    raise Exception("this function can only be called from @angle_query")



class ThriftStructType(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, fields: ast.Expr, structuredAnnotations: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, fields, 'fields'), angle_for(__env, structuredAnnotations, 'structuredAnnotations')]))
    return f"thrift.StructType.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", StructType

  @staticmethod
  def angle_query(*, name: Optional["ThriftQualName"] = None, fields: Optional[List["ThriftFieldSpecification"]] = None, structuredAnnotations: Optional[List["ThriftStructuredAnnotation"]] = None) -> "ThriftStructType":
    raise Exception("this function can only be called from @angle_query")



class ThriftServiceChild(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], parent: ast.Expr, child: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, parent, 'parent'), angle_for(__env, child, 'child')]))
    return f"thrift.ServiceChild.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ServiceChild

  @staticmethod
  def angle_query(*, parent: Optional["ThriftServiceName"] = None, child: Optional["ThriftServiceName"] = None) -> "ThriftServiceChild":
    raise Exception("this function can only be called from @angle_query")



class ThriftIncludes(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], source: ast.Expr, target: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, source, 'source'), angle_for(__env, target, 'target')]))
    return f"thrift.Includes.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Includes

  @staticmethod
  def angle_query(*, source: Optional["ThriftFile"] = None, target: Optional["ThriftFile"] = None) -> "ThriftIncludes":
    raise Exception("this function can only be called from @angle_query")



class ThriftQualName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, name, 'name')]))
    return f"thrift.QualName.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", QualName

  @staticmethod
  def angle_query(*, file: Optional["ThriftFile"] = None, name: Optional["ThriftIdentifier"] = None) -> "ThriftQualName":
    raise Exception("this function can only be called from @angle_query")



class ThriftOutputTarget(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], compile: ast.Expr, output: ast.Expr, out: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, compile, 'compile'), angle_for(__env, output, 'output'), angle_for(__env, out, 'out')]))
    return f"thrift.OutputTarget.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", OutputTarget

  @staticmethod
  def angle_query(*, compile: Optional["ThriftCompileTarget"] = None, output: Optional["BuckTarget"] = None, out: Optional["SrcFile"] = None) -> "ThriftOutputTarget":
    raise Exception("this function can only be called from @angle_query")



class ThriftPythonFunction(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, module: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, module, 'module')]))
    return f"thrift.PythonFunction.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonFunction

  @staticmethod
  def angle_query(*, name: Optional["ThriftPythonName"] = None, module: Optional["ThriftPythonModule"] = None) -> "ThriftPythonFunction":
    raise Exception("this function can only be called from @angle_query")



class ThriftStructuredAnnotation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], type_: ast.Expr, value: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, type_, 'type_'), angle_for(__env, value, 'value')]))
    return f"thrift.StructuredAnnotation.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", StructuredAnnotation

  @staticmethod
  def angle_query(*, type_: Optional["ThriftTypeSpecification"] = None, value: Optional["ThriftStructVal"] = None) -> "ThriftStructuredAnnotation":
    raise Exception("this function can only be called from @angle_query")



class ThriftFile(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"thrift.File.7 { query_fields if query_fields else '_' }", File

  @staticmethod
  def angle_query(*, arg: Optional["SrcFile"] = None) -> "ThriftFile":
    raise Exception("this function can only be called from @angle_query")



class ThriftHackMethod(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, record: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, record, 'record')]))
    return f"thrift.HackMethod.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", HackMethod

  @staticmethod
  def angle_query(*, name: Optional["ThriftHackName"] = None, record: Optional["ThriftHackRecord"] = None) -> "ThriftHackMethod":
    raise Exception("this function can only be called from @angle_query")



class ThriftConstant(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, locName: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, locName, 'locName')]))
    return f"thrift.Constant.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Constant

  @staticmethod
  def angle_query(*, name: Optional["ThriftQualName"] = None, locName: Optional["ThriftLoc"] = None) -> "ThriftConstant":
    raise Exception("this function can only be called from @angle_query")



class ThriftHackName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"thrift.HackName.7 { query_fields if query_fields else '_' }", HackName

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "ThriftHackName":
    raise Exception("this function can only be called from @angle_query")



class ThriftNamedDecl(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, locName: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, locName, 'locName')]))
    return f"thrift.NamedDecl.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", NamedDecl

  @staticmethod
  def angle_query(*, name: Optional["ThriftNamedType"] = None, locName: Optional["ThriftLoc"] = None) -> "ThriftNamedDecl":
    raise Exception("this function can only be called from @angle_query")



class ThriftPythonModuleContains(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], module: ast.Expr, classes: ast.Expr, functions: ast.Expr, values: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, module, 'module'), angle_for(__env, classes, 'classes'), angle_for(__env, functions, 'functions'), angle_for(__env, values, 'values')]))
    return f"thrift.PythonModuleContains.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonModuleContains

  @staticmethod
  def angle_query(*, module: Optional["ThriftPythonModule"] = None, classes: Optional[List["ThriftPythonClass"]] = None, functions: Optional[List["ThriftPythonFunction"]] = None, values: Optional[List["ThriftPythonValue"]] = None) -> "ThriftPythonModuleContains":
    raise Exception("this function can only be called from @angle_query")



class ThriftHackMap(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], source: ast.Expr, repoCode: ast.Expr, path: ast.Expr, kind: ast.Expr, mangledsvcs: ast.Expr, rest: ast.Expr, server: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, source, 'source'), angle_for(__env, repoCode, 'repoCode'), angle_for(__env, path, 'path'), angle_for(__env, kind, 'kind'), angle_for(__env, mangledsvcs, 'mangledsvcs'), angle_for(__env, rest, 'rest'), angle_for(__env, server, 'server')]))
    return f"thrift.HackMap.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", HackMap

  @staticmethod
  def angle_query(*, source: Optional[Union[Just["SrcFile"], Just[None]]] = None, repoCode: Optional["ScmRepoName"] = None, path: Optional[str] = None, kind: Optional["ThriftHackMapKind"] = None, mangledsvcs: Optional[bool] = None, rest: Optional[bool] = None, server: Optional[bool] = None) -> "ThriftHackMap":
    raise Exception("this function can only be called from @angle_query")



class ThriftIncludeSpecial(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], source: ast.Expr, special: ast.Expr, target: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, source, 'source'), angle_for(__env, special, 'special'), angle_for(__env, target, 'target')]))
    return f"thrift.IncludeSpecial.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", IncludeSpecial

  @staticmethod
  def angle_query(*, source: Optional["ThriftFile"] = None, special: Optional[str] = None, target: Optional["ThriftIncludeSplice"] = None) -> "ThriftIncludeSpecial":
    raise Exception("this function can only be called from @angle_query")



class ThriftFileXRefs(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, targets: ast.Expr, xrefs: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, targets, 'targets'), angle_for(__env, xrefs, 'xrefs')]))
    return f"thrift.FileXRefs.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FileXRefs

  @staticmethod
  def angle_query(*, file: Optional["ThriftFile"] = None, targets: Optional[List["ThriftTarget"]] = None, xrefs: Optional[List["ThriftXRef"]] = None) -> "ThriftFileXRefs":
    raise Exception("this function can only be called from @angle_query")



class ThriftMangle(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], _from: ast.Expr, to: ast.Expr, lang: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, _from, 'from'), angle_for(__env, to, 'to'), angle_for(__env, lang, 'lang')]))
    return f"thrift.Mangle.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Mangle

  @staticmethod
  def angle_query(*, _from: Optional["ScmCommit"] = None, to: Optional["ScmCommit"] = None, lang: Optional["ThriftMangleLang"] = None) -> "ThriftMangle":
    raise Exception("this function can only be called from @angle_query")



class ThriftStructVal(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], fields: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, fields, 'fields')]))
    return f"thrift.StructVal.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", StructVal

  @staticmethod
  def angle_query(*, fields: Optional[List["ThriftStructFieldVal"]] = None) -> "ThriftStructVal":
    raise Exception("this function can only be called from @angle_query")



class ThriftIncludeSplice(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"thrift.IncludeSplice.7 { query_fields if query_fields else '_' }", IncludeSplice

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "ThriftIncludeSplice":
    raise Exception("this function can only be called from @angle_query")



class ThriftLang(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"thrift.Lang.7 { query_fields if query_fields else '_' }", Lang

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "ThriftLang":
    raise Exception("this function can only be called from @angle_query")



class ThriftLiteral(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], byte_: ast.Expr, i16_: ast.Expr, i32_: ast.Expr, i64_: ast.Expr, float_: ast.Expr, double_: ast.Expr, bool_: ast.Expr, string_: ast.Expr, binary_: ast.Expr, set_: ast.Expr, hashSet_: ast.Expr, list_: ast.Expr, map_: ast.Expr, hashMap_: ast.Expr, newtype_: ast.Expr, struct_: ast.Expr, exception_: ast.Expr, union_: ast.Expr, enum_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, byte_, 'byte_'), angle_for(__env, i16_, 'i16_'), angle_for(__env, i32_, 'i32_'), angle_for(__env, i64_, 'i64_'), angle_for(__env, float_, 'float_'), angle_for(__env, double_, 'double_'), angle_for(__env, bool_, 'bool_'), angle_for(__env, string_, 'string_'), angle_for(__env, binary_, 'binary_'), angle_for(__env, set_, 'set_'), angle_for(__env, hashSet_, 'hashSet_'), angle_for(__env, list_, 'list_'), angle_for(__env, map_, 'map_'), angle_for(__env, hashMap_, 'hashMap_'), angle_for(__env, newtype_, 'newtype_'), angle_for(__env, struct_, 'struct_'), angle_for(__env, exception_, 'exception_'), angle_for(__env, union_, 'union_'), angle_for(__env, enum_, 'enum_')]))
    return f"thrift.Literal.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Literal

  @staticmethod
  def angle_query_byte_(*, byte_: Optional["ThriftIntegerLiteral"] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_i16_(*, i16_: Optional["ThriftIntegerLiteral"] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_i32_(*, i32_: Optional["ThriftIntegerLiteral"] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_i64_(*, i64_: Optional["ThriftIntegerLiteral"] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_float_(*, float_: Optional["ThriftFloatLiteral"] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_double_(*, double_: Optional["ThriftFloatLiteral"] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_bool_(*, bool_: Optional[bool] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_string_(*, string_: Optional[str] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_binary_(*, binary_: Optional[bytes] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_set_(*, set_: Optional[List["ThriftTypedConst"]] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_hashSet_(*, hashSet_: Optional[List["ThriftTypedConst"]] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_list_(*, list_: Optional[List["ThriftTypedConst"]] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_map_(*, map_: Optional[List["ThriftKeyValue"]] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_hashMap_(*, hashMap_: Optional[List["ThriftKeyValue"]] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_newtype_(*, newtype_: Optional["ThriftLiteral"] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_struct_(*, struct_: Optional["ThriftStructVal"] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_exception_(*, exception_: Optional["ThriftExceptionVal"] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_union_(*, union_: Optional["ThriftUnionVal"] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_enum_(*, enum_: Optional["ThriftEnumVal"] = None) -> "ThriftLiteral":
    raise Exception("this function can only be called from @angle_query")




class ThriftIdentifier(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"thrift.Identifier.7 { query_fields if query_fields else '_' }", Identifier

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "ThriftIdentifier":
    raise Exception("this function can only be called from @angle_query")



class ThriftUnionType(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, alts: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, alts, 'alts')]))
    return f"thrift.UnionType.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", UnionType

  @staticmethod
  def angle_query(*, name: Optional["ThriftQualName"] = None, alts: Optional[List["ThriftUnqualField"]] = None) -> "ThriftUnionType":
    raise Exception("this function can only be called from @angle_query")



class ThriftDeclarationNameSpan(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, name: ast.Expr, file: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, name, 'name'), angle_for(__env, file, 'file'), angle_for(__env, span, 'span')]))
    return f"thrift.DeclarationNameSpan.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationNameSpan

  @staticmethod
  def angle_query(*, decl: Optional["ThriftDeclaration"] = None, name: Optional["ThriftIdentifier"] = None, file: Optional["ThriftFile"] = None, span: Optional["ThriftLoc"] = None) -> "ThriftDeclarationNameSpan":
    raise Exception("this function can only be called from @angle_query")



class ThriftFromPython(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], python: ast.Expr, thrift: ast.Expr, role: ast.Expr, lang: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, python, 'python'), angle_for(__env, thrift, 'thrift'), angle_for(__env, role, 'role'), angle_for(__env, lang, 'lang')]))
    return f"thrift.FromPython.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FromPython

  @staticmethod
  def angle_query(*, python: Optional["ThriftPythonItem"] = None, thrift: Optional["ThriftItem"] = None, role: Optional["ThriftGenRole"] = None, lang: Optional["ThriftLang"] = None) -> "ThriftFromPython":
    raise Exception("this function can only be called from @angle_query")



class ThriftPythonClass(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, module: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, module, 'module')]))
    return f"thrift.PythonClass.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonClass

  @staticmethod
  def angle_query(*, name: Optional["ThriftPythonName"] = None, module: Optional["ThriftPythonModule"] = None) -> "ThriftPythonClass":
    raise Exception("this function can only be called from @angle_query")



class ThriftToCpp2(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], thrift: ast.Expr, cpp2: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, thrift, 'thrift'), angle_for(__env, cpp2, 'cpp2')]))
    return f"thrift.ToCpp2.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ToCpp2

  @staticmethod
  def angle_query(*, thrift: Optional["ThriftFile"] = None, cpp2: Optional[List["ThriftFromCpp2"]] = None) -> "ThriftToCpp2":
    raise Exception("this function can only be called from @angle_query")



class ThriftToHack(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], thrift: ast.Expr, hack: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, thrift, 'thrift'), angle_for(__env, hack, 'hack')]))
    return f"thrift.ToHack.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ToHack

  @staticmethod
  def angle_query(*, thrift: Optional["ThriftFile"] = None, hack: Optional[List["ThriftFromHack"]] = None) -> "ThriftToHack":
    raise Exception("this function can only be called from @angle_query")



class ThriftEnumerationType(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, value: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, value, 'value')]))
    return f"thrift.EnumerationType.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", EnumerationType

  @staticmethod
  def angle_query(*, name: Optional["ThriftQualName"] = None, value: Optional[List["ThriftEnumValueDef"]] = None) -> "ThriftEnumerationType":
    raise Exception("this function can only be called from @angle_query")



class ThriftFileOutput(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], output: ast.Expr, origin: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, output, 'output'), angle_for(__env, origin, 'origin')]))
    return f"thrift.FileOutput.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FileOutput

  @staticmethod
  def angle_query(*, output: Optional["SrcFile"] = None, origin: Optional["ThriftOutputTarget"] = None) -> "ThriftFileOutput":
    raise Exception("this function can only be called from @angle_query")



class ThriftServiceParent(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], child: ast.Expr, parent: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, child, 'child'), angle_for(__env, parent, 'parent')]))
    return f"thrift.ServiceParent.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ServiceParent

  @staticmethod
  def angle_query(*, child: Optional["ThriftServiceName"] = None, parent: Optional["ThriftServiceName"] = None) -> "ThriftServiceParent":
    raise Exception("this function can only be called from @angle_query")



class ThriftMangleLang(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"thrift.MangleLang.7 { query_fields if query_fields else '_' }", MangleLang

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "ThriftMangleLang":
    raise Exception("this function can only be called from @angle_query")



class ThriftExceptionName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, locName: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, locName, 'locName')]))
    return f"thrift.ExceptionName.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ExceptionName

  @staticmethod
  def angle_query(*, name: Optional["ThriftQualName"] = None, locName: Optional["ThriftLoc"] = None) -> "ThriftExceptionName":
    raise Exception("this function can only be called from @angle_query")



class ThriftEnumVal(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, loc: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, loc, 'loc')]))
    return f"thrift.EnumVal.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", EnumVal

  @staticmethod
  def angle_query(*, name: Optional["ThriftQualName"] = None, loc: Optional["ThriftLoc"] = None) -> "ThriftEnumVal":
    raise Exception("this function can only be called from @angle_query")



class ThriftUnionVal(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], field: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, field, 'field')]))
    return f"thrift.UnionVal.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", UnionVal

  @staticmethod
  def angle_query(*, field: Optional["ThriftUnionFieldVal"] = None) -> "ThriftUnionVal":
    raise Exception("this function can only be called from @angle_query")





class ThriftCpp2ItemNamed(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, kind: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, kind, 'kind'), angle_for(__env, name, 'name')]))
    return f"thrift.Cpp2ItemNamed.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Cpp2ItemNamed

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, kind: Optional[str] = None, name: Optional[str] = None) -> "ThriftCpp2ItemNamed":
    raise Exception("this function can only be called from @angle_query")



class ThriftStructFieldVal(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, value: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, value, 'value')]))
    return f"thrift.StructFieldVal.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", StructFieldVal

  @staticmethod
  def angle_query(*, name: Optional["ThriftIdentifier"] = None, value: Optional["ThriftStructFieldValValue"] = None) -> "ThriftStructFieldVal":
    raise Exception("this function can only be called from @angle_query")



class ThriftItem(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, namespace_: ast.Expr, service_: ast.Expr, function_: ast.Expr, decl: ast.Expr, exception_: ast.Expr, constant: ast.Expr, enumValue: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, namespace_, 'namespace_'), angle_for(__env, service_, 'service_'), angle_for(__env, function_, 'function_'), angle_for(__env, decl, 'decl'), angle_for(__env, exception_, 'exception_'), angle_for(__env, constant, 'constant'), angle_for(__env, enumValue, 'enumValue')]))
    return f"thrift.Item.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Item

  @staticmethod
  def angle_query_file(*, file: Optional["ThriftFile"] = None) -> "ThriftItem":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_namespace_(*, namespace_: Optional["ThriftNamespace"] = None) -> "ThriftItem":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_service_(*, service_: Optional["ThriftServiceName"] = None) -> "ThriftItem":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_function_(*, function_: Optional["ThriftFunctionName"] = None) -> "ThriftItem":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_decl(*, decl: Optional["ThriftNamedDecl"] = None) -> "ThriftItem":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_exception_(*, exception_: Optional["ThriftExceptionName"] = None) -> "ThriftItem":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_constant(*, constant: Optional["ThriftConstant"] = None) -> "ThriftItem":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_enumValue(*, enumValue: Optional["ThriftEnumValue"] = None) -> "ThriftItem":
    raise Exception("this function can only be called from @angle_query")




class ThriftIntegerLiteral(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], isNonNegative: ast.Expr, absValue: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, isNonNegative, 'isNonNegative'), angle_for(__env, absValue, 'absValue')]))
    return f"thrift.IntegerLiteral.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", IntegerLiteral

  @staticmethod
  def angle_query(*, isNonNegative: Optional[bool] = None, absValue: Optional[int] = None) -> "ThriftIntegerLiteral":
    raise Exception("this function can only be called from @angle_query")



class ThriftExceptionSpecName(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], simple: ast.Expr, typedef_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, simple, 'simple'), angle_for(__env, typedef_, 'typedef_')]))
    return f"thrift.ExceptionSpecName.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ExceptionSpecName

  @staticmethod
  def angle_query_simple(*, simple: Optional["ThriftExceptionName"] = None) -> "ThriftExceptionSpecName":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_typedef_(*, typedef_: Optional["ThriftTypeDefException"] = None) -> "ThriftExceptionSpecName":
    raise Exception("this function can only be called from @angle_query")




class ThriftHackRecordKind(Enum):
  class_ = 0
  abstract_class = 1
  interface_ = 2
  trait_ = 3
  shape_ = 4

class ThriftKeyValue(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], key: ast.Expr, value: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, key, 'key'), angle_for(__env, value, 'value')]))
    return f"thrift.KeyValue.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", KeyValue

  @staticmethod
  def angle_query(*, key: Optional["ThriftTypedConst"] = None, value: Optional["ThriftTypedConst"] = None) -> "ThriftKeyValue":
    raise Exception("this function can only be called from @angle_query")



class ThriftCpp2Item(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, decl: ast.Expr, named: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, decl, 'decl'), angle_for(__env, named, 'named')]))
    return f"thrift.Cpp2Item.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Cpp2Item

  @staticmethod
  def angle_query_file(*, file: Optional["SrcFile"] = None) -> "ThriftCpp2Item":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_decl(*, decl: Optional["Cxx1Declaration"] = None) -> "ThriftCpp2Item":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_named(*, named: Optional["ThriftCpp2ItemNamed"] = None) -> "ThriftCpp2Item":
    raise Exception("this function can only be called from @angle_query")




class ThriftNamedType(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, kind: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, kind, 'kind')]))
    return f"thrift.NamedType.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", NamedType

  @staticmethod
  def angle_query(*, name: Optional["ThriftQualName"] = None, kind: Optional["ThriftNamedKind"] = None) -> "ThriftNamedType":
    raise Exception("this function can only be called from @angle_query")



class ThriftUnionFieldVal(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, value: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, value, 'value')]))
    return f"thrift.UnionFieldVal.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", UnionFieldVal

  @staticmethod
  def angle_query(*, name: Optional["ThriftIdentifier"] = None, value: Optional["ThriftTypedConstT"] = None) -> "ThriftUnionFieldVal":
    raise Exception("this function can only be called from @angle_query")



class ThriftExceptionSpecification(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], id: ast.Expr, type_: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, id, 'id'), angle_for(__env, type_, 'type_'), angle_for(__env, name, 'name')]))
    return f"thrift.ExceptionSpecification.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ExceptionSpecification

  @staticmethod
  def angle_query(*, id: Optional["ThriftFieldId"] = None, type_: Optional["ThriftExceptionSpecName"] = None, name: Optional["ThriftIdentifier"] = None) -> "ThriftExceptionSpecification":
    raise Exception("this function can only be called from @angle_query")



class ThriftXRef(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], locRef: ast.Expr, target: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, locRef, 'locRef'), angle_for(__env, target, 'target')]))
    return f"thrift.XRef.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", XRef

  @staticmethod
  def angle_query(*, locRef: Optional["ThriftLoc"] = None, target: Optional["ThriftXRefTarget"] = None) -> "ThriftXRef":
    raise Exception("this function can only be called from @angle_query")



class ThriftGenRole(Enum):
  helper = 0
  server = 1
  client = 2
  type = 3
  constant = 4

class ThriftUnqualField(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], id: ast.Expr, type_: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, id, 'id'), angle_for(__env, type_, 'type_'), angle_for(__env, name, 'name')]))
    return f"thrift.UnqualField.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", UnqualField

  @staticmethod
  def angle_query(*, id: Optional["ThriftFieldId"] = None, type_: Optional["ThriftTypeSpecification"] = None, name: Optional["ThriftIdentifier"] = None) -> "ThriftUnqualField":
    raise Exception("this function can only be called from @angle_query")



class ThriftXRefTarget(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], include_: ast.Expr, named: ast.Expr, exception_: ast.Expr, service_: ast.Expr, constant: ast.Expr, enumValue: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, include_, 'include_'), angle_for(__env, named, 'named'), angle_for(__env, exception_, 'exception_'), angle_for(__env, service_, 'service_'), angle_for(__env, constant, 'constant'), angle_for(__env, enumValue, 'enumValue')]))
    return f"thrift.XRefTarget.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", XRefTarget

  @staticmethod
  def angle_query_include_(*, include_: Optional["ThriftFile"] = None) -> "ThriftXRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_named(*, named: Optional["ThriftNamedDecl"] = None) -> "ThriftXRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_exception_(*, exception_: Optional["ThriftExceptionName"] = None) -> "ThriftXRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_service_(*, service_: Optional["ThriftServiceName"] = None) -> "ThriftXRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_constant(*, constant: Optional["ThriftConstant"] = None) -> "ThriftXRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_enumValue(*, enumValue: Optional["ThriftEnumValue"] = None) -> "ThriftXRefTarget":
    raise Exception("this function can only be called from @angle_query")




class ThriftContainerType(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], list_: ast.Expr, set_: ast.Expr, map_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, list_, 'list_'), angle_for(__env, set_, 'set_'), angle_for(__env, map_, 'map_')]))
    return f"thrift.ContainerType.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ContainerType

  @staticmethod
  def angle_query_list_(*, list_: Optional["ThriftTypeSpecification"] = None) -> "ThriftContainerType":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_set_(*, set_: Optional["ThriftTypeSpecification"] = None) -> "ThriftContainerType":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_map_(*, map_: Optional["ThriftMapType"] = None) -> "ThriftContainerType":
    raise Exception("this function can only be called from @angle_query")




class ThriftFieldSpecification(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], id: ast.Expr, qualifier: ast.Expr, type_: ast.Expr, name: ast.Expr, value: ast.Expr, structuredAnnotations: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, id, 'id'), angle_for(__env, qualifier, 'qualifier'), angle_for(__env, type_, 'type_'), angle_for(__env, name, 'name'), angle_for(__env, value, 'value'), angle_for(__env, structuredAnnotations, 'structuredAnnotations')]))
    return f"thrift.FieldSpecification.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FieldSpecification

  @staticmethod
  def angle_query(*, id: Optional["ThriftFieldId"] = None, qualifier: Optional["ThriftQualifier"] = None, type_: Optional["ThriftTypeSpecification"] = None, name: Optional["ThriftIdentifier"] = None, value: Optional[Union[Just["ThriftTypedConst"], Just[None]]] = None, structuredAnnotations: Optional[List["ThriftStructuredAnnotation"]] = None) -> "ThriftFieldSpecification":
    raise Exception("this function can only be called from @angle_query")



class ThriftStructFieldValValue(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], val: ast.Expr, default_: ast.Expr, just: ast.Expr, nothing: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, val, 'val'), angle_for(__env, default_, 'default_'), angle_for(__env, just, 'just'), angle_for(__env, nothing, 'nothing')]))
    return f"thrift.StructFieldValValue.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", StructFieldValValue

  @staticmethod
  def angle_query_val(*, val: Optional["ThriftTypedConstT"] = None) -> "ThriftStructFieldValValue":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_default_(*, default_: Optional["ThriftTypeSpecification"] = None) -> "ThriftStructFieldValValue":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_just(*, just: Optional["ThriftTypedConstT"] = None) -> "ThriftStructFieldValValue":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_nothing(*, nothing: Optional['ThriftStructFieldValValue_nothing'] = None) -> "ThriftStructFieldValValue":
    raise Exception("this function can only be called from @angle_query")


ThriftStructFieldValValue_nothing = Tuple[()]



class ThriftResultStream(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], response: ast.Expr, stream_: ast.Expr, throws_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, response, 'response'), angle_for(__env, stream_, 'stream_'), angle_for(__env, throws_, 'throws_')]))
    return f"thrift.ResultStream.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ResultStream

  @staticmethod
  def angle_query(*, response: Optional[Union[Just["ThriftTypeSpecification"], Just[None]]] = None, stream_: Optional["ThriftTypeSpecification"] = None, throws_: Optional[List["ThriftExceptionSpecification"]] = None) -> "ThriftResultStream":
    raise Exception("this function can only be called from @angle_query")



class ThriftTypedConstT(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], const_: ast.Expr, type_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, const_, 'const_'), angle_for(__env, type_, 'type_')]))
    return f"thrift.TypedConstT.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TypedConstT

  @staticmethod
  def angle_query(*, const_: Optional["ThriftTypedConst"] = None, type_: Optional["ThriftTypeSpecification"] = None) -> "ThriftTypedConstT":
    raise Exception("this function can only be called from @angle_query")



class ThriftHackMapKind(Enum):
  core = 0
  intern = 1

class ThriftMapType(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], key_: ast.Expr, value: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, key_, 'key_'), angle_for(__env, value, 'value')]))
    return f"thrift.MapType.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", MapType

  @staticmethod
  def angle_query(*, key_: Optional["ThriftTypeSpecification"] = None, value: Optional["ThriftTypeSpecification"] = None) -> "ThriftMapType":
    raise Exception("this function can only be called from @angle_query")



class ThriftNamedKind(Enum):
  typedef_ = 0
  enum_ = 1
  struct_ = 2
  union_ = 3

class ThriftFloatLiteral(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], isNaN: ast.Expr, isPositive: ast.Expr, exponent: ast.Expr, significand: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, isNaN, 'isNaN'), angle_for(__env, isPositive, 'isPositive'), angle_for(__env, exponent, 'exponent'), angle_for(__env, significand, 'significand')]))
    return f"thrift.FloatLiteral.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FloatLiteral

  @staticmethod
  def angle_query(*, isNaN: Optional[bool] = None, isPositive: Optional[bool] = None, exponent: Optional[int] = None, significand: Optional[int] = None) -> "ThriftFloatLiteral":
    raise Exception("this function can only be called from @angle_query")



class ThriftTypedConst(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], literal: ast.Expr, identifier: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, literal, 'literal'), angle_for(__env, identifier, 'identifier')]))
    return f"thrift.TypedConst.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TypedConst

  @staticmethod
  def angle_query_literal(*, literal: Optional["ThriftLiteral"] = None) -> "ThriftTypedConst":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_identifier(*, identifier: Optional["ThriftConstant"] = None) -> "ThriftTypedConst":
    raise Exception("this function can only be called from @angle_query")




class ThriftPrimitiveType(Enum):
  bool_ = 0
  byte_ = 1
  i16_ = 2
  i32_ = 3
  i64_ = 4
  float_ = 5
  double_ = 6
  binary_ = 7
  string_ = 8

class ThriftResultType(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], oneway_: ast.Expr, void_: ast.Expr, result: ast.Expr, stream_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, oneway_, 'oneway_'), angle_for(__env, void_, 'void_'), angle_for(__env, result, 'result'), angle_for(__env, stream_, 'stream_')]))
    return f"thrift.ResultType.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ResultType

  @staticmethod
  def angle_query_oneway_(*, oneway_: Optional["BuiltinUnit"] = None) -> "ThriftResultType":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_void_(*, void_: Optional["BuiltinUnit"] = None) -> "ThriftResultType":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_result(*, result: Optional["ThriftTypeSpecification"] = None) -> "ThriftResultType":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_stream_(*, stream_: Optional["ThriftResultStream"] = None) -> "ThriftResultType":
    raise Exception("this function can only be called from @angle_query")




class ThriftPythonItem(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, module: ast.Expr, class_: ast.Expr, method: ast.Expr, field: ast.Expr, function_: ast.Expr, value: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, module, 'module'), angle_for(__env, class_, 'class_'), angle_for(__env, method, 'method'), angle_for(__env, field, 'field'), angle_for(__env, function_, 'function_'), angle_for(__env, value, 'value')]))
    return f"thrift.PythonItem.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonItem

  @staticmethod
  def angle_query_file(*, file: Optional["SrcFile"] = None) -> "ThriftPythonItem":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_module(*, module: Optional["ThriftPythonModule"] = None) -> "ThriftPythonItem":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_class_(*, class_: Optional["ThriftPythonClass"] = None) -> "ThriftPythonItem":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_method(*, method: Optional["ThriftPythonMethod"] = None) -> "ThriftPythonItem":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_field(*, field: Optional["ThriftPythonField"] = None) -> "ThriftPythonItem":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_function_(*, function_: Optional["ThriftPythonFunction"] = None) -> "ThriftPythonItem":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_value(*, value: Optional["ThriftPythonValue"] = None) -> "ThriftPythonItem":
    raise Exception("this function can only be called from @angle_query")




class ThriftTarget(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], locTarget: ast.Expr, target: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, locTarget, 'locTarget'), angle_for(__env, target, 'target')]))
    return f"thrift.Target.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Target

  @staticmethod
  def angle_query(*, locTarget: Optional["ThriftLoc"] = None, target: Optional["ThriftXRefTarget"] = None) -> "ThriftTarget":
    raise Exception("this function can only be called from @angle_query")



class ThriftHackKind(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, record: ast.Expr, method: ast.Expr, namespace_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, record, 'record'), angle_for(__env, method, 'method'), angle_for(__env, namespace_, 'namespace_')]))
    return f"thrift.HackKind.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", HackKind

  @staticmethod
  def angle_query_file(*, file: Optional["SrcFile"] = None) -> "ThriftHackKind":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_record(*, record: Optional["ThriftHackRecord"] = None) -> "ThriftHackKind":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_method(*, method: Optional["ThriftHackMethod"] = None) -> "ThriftHackKind":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_namespace_(*, namespace_: Optional["ThriftHackName"] = None) -> "ThriftHackKind":
    raise Exception("this function can only be called from @angle_query")




class ThriftQualifier(Enum):
  default_ = 0
  optional_ = 1
  required_ = 2

class ThriftLoc(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], startLine: ast.Expr, startCol: ast.Expr, endLine: ast.Expr, endCol: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, startLine, 'startLine'), angle_for(__env, startCol, 'startCol'), angle_for(__env, endLine, 'endLine'), angle_for(__env, endCol, 'endCol')]))
    return f"thrift.Loc.7 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Loc

  @staticmethod
  def angle_query(*, startLine: Optional[int] = None, startCol: Optional[int] = None, endLine: Optional[int] = None, endCol: Optional[int] = None) -> "ThriftLoc":
    raise Exception("this function can only be called from @angle_query")





ThriftFieldId = "ThriftIntegerLiteral"

ThriftFbcodeLang = str

ThriftDeclaration = "ThriftXRefTarget"
