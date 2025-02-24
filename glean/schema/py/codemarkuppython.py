# @generated
# To regenerate this file run fbcode//glean/schema/gen/sync
from typing import Optional, Tuple, Union, List, Dict, TypeVar
from thrift.py3 import Struct
from enum import Enum
import ast
from glean.schema.py.glean_schema_predicate import GleanSchemaPredicate , Just, InnerGleanSchemaPredicate
from glean.client.py3.angle_query import angle_for, R
from glean.schema.py.codepython import *
from glean.schema.py.codemarkuptypes import *
from glean.schema.py.python import *
from glean.schema.py.src import *


from glean.schema.codemarkup_python.types import (
    PythonEntityInfo,
    PythonEntityLocation,
    PythonResolveLocation,
    PythonContainsChildEntity,
    PythonFileEntityXRefLocations,
    PythonEntityKind,
    PythonEntityUses,
    NonImportPythonDeclarationInfo,
    NonImportPythonDeclarationKind,
    PythonEntityNameAndLocation,
)


class CodemarkupPythonPythonEntityInfo(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], entity: ast.Expr, info: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, entity, 'entity'), angle_for(__env, info, 'info')]))
    return f"codemarkup.python.PythonEntityInfo.2 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonEntityInfo

  @staticmethod
  def angle_query(*, entity: Optional["CodePythonEntity"] = None, info: Optional["CodemarkupTypesSymbolInfo"] = None) -> "CodemarkupPythonPythonEntityInfo":
    raise Exception("this function can only be called from @angle_query")



class CodemarkupPythonPythonEntityLocation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], entity: ast.Expr, location: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, entity, 'entity'), angle_for(__env, location, 'location')]))
    return f"codemarkup.python.PythonEntityLocation.2 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonEntityLocation

  @staticmethod
  def angle_query(*, entity: Optional["CodePythonEntity"] = None, location: Optional["CodemarkupTypesLocation"] = None) -> "CodemarkupPythonPythonEntityLocation":
    raise Exception("this function can only be called from @angle_query")



class CodemarkupPythonPythonResolveLocation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], location: ast.Expr, entity: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, location, 'location'), angle_for(__env, entity, 'entity')]))
    return f"codemarkup.python.PythonResolveLocation.2 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonResolveLocation

  @staticmethod
  def angle_query(*, location: Optional["CodemarkupTypesLocation"] = None, entity: Optional["CodePythonEntity"] = None) -> "CodemarkupPythonPythonResolveLocation":
    raise Exception("this function can only be called from @angle_query")



class CodemarkupPythonPythonContainsChildEntity(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], parent: ast.Expr, child: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, parent, 'parent'), angle_for(__env, child, 'child')]))
    return f"codemarkup.python.PythonContainsChildEntity.2 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonContainsChildEntity

  @staticmethod
  def angle_query(*, parent: Optional["CodePythonEntity"] = None, child: Optional["CodePythonEntity"] = None) -> "CodemarkupPythonPythonContainsChildEntity":
    raise Exception("this function can only be called from @angle_query")



class CodemarkupPythonPythonFileEntityXRefLocations(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, xref: ast.Expr, entity: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, xref, 'xref'), angle_for(__env, entity, 'entity')]))
    return f"codemarkup.python.PythonFileEntityXRefLocations.2 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonFileEntityXRefLocations

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, xref: Optional["CodemarkupTypesXRefLocation"] = None, entity: Optional["CodePythonEntity"] = None) -> "CodemarkupPythonPythonFileEntityXRefLocations":
    raise Exception("this function can only be called from @angle_query")



class CodemarkupPythonPythonEntityKind(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], entity: ast.Expr, kind: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, entity, 'entity'), angle_for(__env, kind, 'kind')]))
    return f"codemarkup.python.PythonEntityKind.2 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonEntityKind

  @staticmethod
  def angle_query(*, entity: Optional["CodePythonEntity"] = None, kind: Optional["CodemarkupTypesSymbolKind"] = None) -> "CodemarkupPythonPythonEntityKind":
    raise Exception("this function can only be called from @angle_query")



class CodemarkupPythonPythonEntityUses(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], target: ast.Expr, file: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, target, 'target'), angle_for(__env, file, 'file'), angle_for(__env, span, 'span')]))
    return f"codemarkup.python.PythonEntityUses.2 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonEntityUses

  @staticmethod
  def angle_query(*, target: Optional["CodePythonEntity"] = None, file: Optional["SrcFile"] = None, span: Optional["SrcByteSpan"] = None) -> "CodemarkupPythonPythonEntityUses":
    raise Exception("this function can only be called from @angle_query")



class CodemarkupPythonNonImportPythonDeclarationInfo(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, info: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, info, 'info')]))
    return f"codemarkup.python.NonImportPythonDeclarationInfo.2 { ('{ ' + query_fields + ' }') if query_fields else '_' }", NonImportPythonDeclarationInfo

  @staticmethod
  def angle_query(*, declaration: Optional["PythonDeclaration"] = None, info: Optional["CodemarkupTypesSymbolInfo"] = None) -> "CodemarkupPythonNonImportPythonDeclarationInfo":
    raise Exception("this function can only be called from @angle_query")



class CodemarkupPythonNonImportPythonDeclarationKind(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, kind: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, kind, 'kind')]))
    return f"codemarkup.python.NonImportPythonDeclarationKind.2 { ('{ ' + query_fields + ' }') if query_fields else '_' }", NonImportPythonDeclarationKind

  @staticmethod
  def angle_query(*, declaration: Optional["PythonDeclaration"] = None, kind: Optional["CodemarkupTypesSymbolKind"] = None) -> "CodemarkupPythonNonImportPythonDeclarationKind":
    raise Exception("this function can only be called from @angle_query")



class CodemarkupPythonPythonEntityNameAndLocation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], entity: ast.Expr, name: ast.Expr, file: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, entity, 'entity'), angle_for(__env, name, 'name'), angle_for(__env, file, 'file'), angle_for(__env, span, 'span')]))
    return f"codemarkup.python.PythonEntityNameAndLocation.2 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PythonEntityNameAndLocation

  @staticmethod
  def angle_query(*, entity: Optional["CodePythonEntity"] = None, name: Optional[str] = None, file: Optional["SrcFile"] = None, span: Optional["SrcByteSpan"] = None) -> "CodemarkupPythonPythonEntityNameAndLocation":
    raise Exception("this function can only be called from @angle_query")






