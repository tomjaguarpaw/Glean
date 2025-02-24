# @generated
# To regenerate this file run fbcode//glean/schema/gen/sync
from typing import Optional, Tuple, Union, List, Dict, TypeVar
from thrift.py3 import Struct
from enum import Enum
import ast
from glean.schema.py.glean_schema_predicate import GleanSchemaPredicate , Just, InnerGleanSchemaPredicate
from glean.client.py3.angle_query import angle_for, R
from glean.schema.py.builtin import *
from glean.schema.py.src import *


from glean.schema.fbthrift.types import (
    TypeSpecification,
    FunctionName,
    FunctionSpecification,
    EnumValue,
    ServiceDefinition,
    TypeDefException,
    ServiceName,
    NamedDecl,
    FileXRefs,
    Constant,
    File,
    QualName,
    ServiceParent,
    ExceptionName,
    Identifier,
    ExceptionSpecName,
    IntegerLiteral,
    XRef,
    UnqualField,
    XRefTarget,
    NamedType,
    ExceptionSpecification,
    ResultStream,
    MapType,
    ContainerType,
    ResultType,
    Target,
    PrimitiveType,
    Loc,
    NamedKind,
)


class FbthriftTypeSpecification(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], primitive: ast.Expr, container: ast.Expr, named: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, primitive, 'primitive'), angle_for(__env, container, 'container'), angle_for(__env, named, 'named')]))
    return f"fbthrift.TypeSpecification.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TypeSpecification

  @staticmethod
  def angle_query_primitive(*, primitive: Optional["FbthriftPrimitiveType"] = None) -> "FbthriftTypeSpecification":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_container(*, container: Optional["FbthriftContainerType"] = None) -> "FbthriftTypeSpecification":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_named(*, named: Optional["FbthriftNamedType"] = None) -> "FbthriftTypeSpecification":
    raise Exception("this function can only be called from @angle_query")




class FbthriftFunctionName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], service_: ast.Expr, name: ast.Expr, locName: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, service_, 'service_'), angle_for(__env, name, 'name'), angle_for(__env, locName, 'locName')]))
    return f"fbthrift.FunctionName.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FunctionName

  @staticmethod
  def angle_query(*, service_: Optional["FbthriftServiceName"] = None, name: Optional["FbthriftIdentifier"] = None, locName: Optional["FbthriftLoc"] = None) -> "FbthriftFunctionName":
    raise Exception("this function can only be called from @angle_query")



class FbthriftFunctionSpecification(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, result: ast.Expr, arguments: ast.Expr, throws_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, result, 'result'), angle_for(__env, arguments, 'arguments'), angle_for(__env, throws_, 'throws_')]))
    return f"fbthrift.FunctionSpecification.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FunctionSpecification

  @staticmethod
  def angle_query(*, name: Optional["FbthriftFunctionName"] = None, result: Optional["FbthriftResultType"] = None, arguments: Optional[List["FbthriftUnqualField"]] = None, throws_: Optional[List["FbthriftExceptionSpecification"]] = None) -> "FbthriftFunctionSpecification":
    raise Exception("this function can only be called from @angle_query")



class FbthriftEnumValue(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], enum_: ast.Expr, name: ast.Expr, locName: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, enum_, 'enum_'), angle_for(__env, name, 'name'), angle_for(__env, locName, 'locName')]))
    return f"fbthrift.EnumValue.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", EnumValue

  @staticmethod
  def angle_query(*, enum_: Optional["FbthriftNamedType"] = None, name: Optional["FbthriftIdentifier"] = None, locName: Optional["FbthriftLoc"] = None) -> "FbthriftEnumValue":
    raise Exception("this function can only be called from @angle_query")



class FbthriftServiceDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, functions: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, functions, 'functions')]))
    return f"fbthrift.ServiceDefinition.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ServiceDefinition

  @staticmethod
  def angle_query(*, name: Optional["FbthriftServiceName"] = None, functions: Optional[List["FbthriftFunctionSpecification"]] = None) -> "FbthriftServiceDefinition":
    raise Exception("this function can only be called from @angle_query")



class FbthriftTypeDefException(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], alias: ast.Expr, type_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, alias, 'alias'), angle_for(__env, type_, 'type_')]))
    return f"fbthrift.TypeDefException.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TypeDefException

  @staticmethod
  def angle_query(*, alias: Optional["FbthriftNamedDecl"] = None, type_: Optional["FbthriftExceptionSpecName"] = None) -> "FbthriftTypeDefException":
    raise Exception("this function can only be called from @angle_query")



class FbthriftServiceName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, locName: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, locName, 'locName')]))
    return f"fbthrift.ServiceName.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ServiceName

  @staticmethod
  def angle_query(*, name: Optional["FbthriftQualName"] = None, locName: Optional["FbthriftLoc"] = None) -> "FbthriftServiceName":
    raise Exception("this function can only be called from @angle_query")



class FbthriftNamedDecl(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, locName: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, locName, 'locName')]))
    return f"fbthrift.NamedDecl.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", NamedDecl

  @staticmethod
  def angle_query(*, name: Optional["FbthriftNamedType"] = None, locName: Optional["FbthriftLoc"] = None) -> "FbthriftNamedDecl":
    raise Exception("this function can only be called from @angle_query")



class FbthriftFileXRefs(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, targets: ast.Expr, xrefs: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, targets, 'targets'), angle_for(__env, xrefs, 'xrefs')]))
    return f"fbthrift.FileXRefs.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FileXRefs

  @staticmethod
  def angle_query(*, file: Optional["FbthriftFile"] = None, targets: Optional[List["FbthriftTarget"]] = None, xrefs: Optional[List["FbthriftXRef"]] = None) -> "FbthriftFileXRefs":
    raise Exception("this function can only be called from @angle_query")



class FbthriftConstant(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, locName: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, locName, 'locName')]))
    return f"fbthrift.Constant.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Constant

  @staticmethod
  def angle_query(*, name: Optional["FbthriftQualName"] = None, locName: Optional["FbthriftLoc"] = None) -> "FbthriftConstant":
    raise Exception("this function can only be called from @angle_query")



class FbthriftFile(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"fbthrift.File.1 { query_fields if query_fields else '_' }", File

  @staticmethod
  def angle_query(*, arg: Optional["SrcFile"] = None) -> "FbthriftFile":
    raise Exception("this function can only be called from @angle_query")



class FbthriftQualName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, name, 'name')]))
    return f"fbthrift.QualName.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", QualName

  @staticmethod
  def angle_query(*, file: Optional["FbthriftFile"] = None, name: Optional["FbthriftIdentifier"] = None) -> "FbthriftQualName":
    raise Exception("this function can only be called from @angle_query")



class FbthriftServiceParent(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], child: ast.Expr, parent: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, child, 'child'), angle_for(__env, parent, 'parent')]))
    return f"fbthrift.ServiceParent.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ServiceParent

  @staticmethod
  def angle_query(*, child: Optional["FbthriftServiceName"] = None, parent: Optional["FbthriftServiceName"] = None) -> "FbthriftServiceParent":
    raise Exception("this function can only be called from @angle_query")



class FbthriftExceptionName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, locName: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, locName, 'locName')]))
    return f"fbthrift.ExceptionName.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ExceptionName

  @staticmethod
  def angle_query(*, name: Optional["FbthriftQualName"] = None, locName: Optional["FbthriftLoc"] = None) -> "FbthriftExceptionName":
    raise Exception("this function can only be called from @angle_query")



class FbthriftIdentifier(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"fbthrift.Identifier.1 { query_fields if query_fields else '_' }", Identifier

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "FbthriftIdentifier":
    raise Exception("this function can only be called from @angle_query")





class FbthriftExceptionSpecName(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], simple: ast.Expr, typedef_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, simple, 'simple'), angle_for(__env, typedef_, 'typedef_')]))
    return f"fbthrift.ExceptionSpecName.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ExceptionSpecName

  @staticmethod
  def angle_query_simple(*, simple: Optional["FbthriftExceptionName"] = None) -> "FbthriftExceptionSpecName":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_typedef_(*, typedef_: Optional["FbthriftTypeDefException"] = None) -> "FbthriftExceptionSpecName":
    raise Exception("this function can only be called from @angle_query")




class FbthriftIntegerLiteral(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], isNonNegative: ast.Expr, absValue: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, isNonNegative, 'isNonNegative'), angle_for(__env, absValue, 'absValue')]))
    return f"fbthrift.IntegerLiteral.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", IntegerLiteral

  @staticmethod
  def angle_query(*, isNonNegative: Optional[bool] = None, absValue: Optional[int] = None) -> "FbthriftIntegerLiteral":
    raise Exception("this function can only be called from @angle_query")



class FbthriftXRef(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], locRef: ast.Expr, target: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, locRef, 'locRef'), angle_for(__env, target, 'target')]))
    return f"fbthrift.XRef.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", XRef

  @staticmethod
  def angle_query(*, locRef: Optional["FbthriftLoc"] = None, target: Optional["FbthriftXRefTarget"] = None) -> "FbthriftXRef":
    raise Exception("this function can only be called from @angle_query")



class FbthriftUnqualField(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], id: ast.Expr, type_: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, id, 'id'), angle_for(__env, type_, 'type_'), angle_for(__env, name, 'name')]))
    return f"fbthrift.UnqualField.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", UnqualField

  @staticmethod
  def angle_query(*, id: Optional["FbthriftFieldId"] = None, type_: Optional["FbthriftTypeSpecification"] = None, name: Optional["FbthriftIdentifier"] = None) -> "FbthriftUnqualField":
    raise Exception("this function can only be called from @angle_query")



class FbthriftXRefTarget(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], include_: ast.Expr, named: ast.Expr, exception_: ast.Expr, service_: ast.Expr, constant: ast.Expr, enumValue: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, include_, 'include_'), angle_for(__env, named, 'named'), angle_for(__env, exception_, 'exception_'), angle_for(__env, service_, 'service_'), angle_for(__env, constant, 'constant'), angle_for(__env, enumValue, 'enumValue')]))
    return f"fbthrift.XRefTarget.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", XRefTarget

  @staticmethod
  def angle_query_include_(*, include_: Optional["FbthriftFile"] = None) -> "FbthriftXRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_named(*, named: Optional["FbthriftNamedDecl"] = None) -> "FbthriftXRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_exception_(*, exception_: Optional["FbthriftExceptionName"] = None) -> "FbthriftXRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_service_(*, service_: Optional["FbthriftServiceName"] = None) -> "FbthriftXRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_constant(*, constant: Optional["FbthriftConstant"] = None) -> "FbthriftXRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_enumValue(*, enumValue: Optional["FbthriftEnumValue"] = None) -> "FbthriftXRefTarget":
    raise Exception("this function can only be called from @angle_query")




class FbthriftNamedType(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, kind: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, kind, 'kind')]))
    return f"fbthrift.NamedType.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", NamedType

  @staticmethod
  def angle_query(*, name: Optional["FbthriftQualName"] = None, kind: Optional["FbthriftNamedKind"] = None) -> "FbthriftNamedType":
    raise Exception("this function can only be called from @angle_query")



class FbthriftExceptionSpecification(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], id: ast.Expr, type_: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, id, 'id'), angle_for(__env, type_, 'type_'), angle_for(__env, name, 'name')]))
    return f"fbthrift.ExceptionSpecification.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ExceptionSpecification

  @staticmethod
  def angle_query(*, id: Optional["FbthriftFieldId"] = None, type_: Optional["FbthriftExceptionSpecName"] = None, name: Optional["FbthriftIdentifier"] = None) -> "FbthriftExceptionSpecification":
    raise Exception("this function can only be called from @angle_query")



class FbthriftResultStream(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], response: ast.Expr, stream_: ast.Expr, throws_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, response, 'response'), angle_for(__env, stream_, 'stream_'), angle_for(__env, throws_, 'throws_')]))
    return f"fbthrift.ResultStream.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ResultStream

  @staticmethod
  def angle_query(*, response: Optional[Union[Just["FbthriftTypeSpecification"], Just[None]]] = None, stream_: Optional["FbthriftTypeSpecification"] = None, throws_: Optional[List["FbthriftExceptionSpecification"]] = None) -> "FbthriftResultStream":
    raise Exception("this function can only be called from @angle_query")



class FbthriftMapType(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], key_: ast.Expr, value: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, key_, 'key_'), angle_for(__env, value, 'value')]))
    return f"fbthrift.MapType.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", MapType

  @staticmethod
  def angle_query(*, key_: Optional["FbthriftTypeSpecification"] = None, value: Optional["FbthriftTypeSpecification"] = None) -> "FbthriftMapType":
    raise Exception("this function can only be called from @angle_query")



class FbthriftContainerType(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], list_: ast.Expr, set_: ast.Expr, map_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, list_, 'list_'), angle_for(__env, set_, 'set_'), angle_for(__env, map_, 'map_')]))
    return f"fbthrift.ContainerType.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ContainerType

  @staticmethod
  def angle_query_list_(*, list_: Optional["FbthriftTypeSpecification"] = None) -> "FbthriftContainerType":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_set_(*, set_: Optional["FbthriftTypeSpecification"] = None) -> "FbthriftContainerType":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_map_(*, map_: Optional["FbthriftMapType"] = None) -> "FbthriftContainerType":
    raise Exception("this function can only be called from @angle_query")




class FbthriftResultType(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], oneway_: ast.Expr, void_: ast.Expr, result: ast.Expr, stream_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, oneway_, 'oneway_'), angle_for(__env, void_, 'void_'), angle_for(__env, result, 'result'), angle_for(__env, stream_, 'stream_')]))
    return f"fbthrift.ResultType.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ResultType

  @staticmethod
  def angle_query_oneway_(*, oneway_: Optional["BuiltinUnit"] = None) -> "FbthriftResultType":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_void_(*, void_: Optional["BuiltinUnit"] = None) -> "FbthriftResultType":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_result(*, result: Optional["FbthriftTypeSpecification"] = None) -> "FbthriftResultType":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_stream_(*, stream_: Optional["FbthriftResultStream"] = None) -> "FbthriftResultType":
    raise Exception("this function can only be called from @angle_query")




class FbthriftTarget(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], locTarget: ast.Expr, target: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, locTarget, 'locTarget'), angle_for(__env, target, 'target')]))
    return f"fbthrift.Target.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Target

  @staticmethod
  def angle_query(*, locTarget: Optional["FbthriftLoc"] = None, target: Optional["FbthriftXRefTarget"] = None) -> "FbthriftTarget":
    raise Exception("this function can only be called from @angle_query")



class FbthriftPrimitiveType(Enum):
  bool_ = 0
  byte_ = 1
  i16_ = 2
  i32_ = 3
  i64_ = 4
  float_ = 5
  double_ = 6
  binary_ = 7
  string_ = 8

class FbthriftLoc(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], startLine: ast.Expr, startCol: ast.Expr, endLine: ast.Expr, endCol: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, startLine, 'startLine'), angle_for(__env, startCol, 'startCol'), angle_for(__env, endLine, 'endLine'), angle_for(__env, endCol, 'endCol')]))
    return f"fbthrift.Loc.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Loc

  @staticmethod
  def angle_query(*, startLine: Optional[int] = None, startCol: Optional[int] = None, endLine: Optional[int] = None, endCol: Optional[int] = None) -> "FbthriftLoc":
    raise Exception("this function can only be called from @angle_query")



class FbthriftNamedKind(Enum):
  typedef_ = 0
  enum_ = 1
  struct_ = 2
  union_ = 3



FbthriftFieldId = "FbthriftIntegerLiteral"
