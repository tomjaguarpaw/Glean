# @generated
# To regenerate this file run fbcode//glean/schema/gen/sync
from typing import Optional, Tuple, Union, List, Dict, TypeVar
from thrift.py3 import Struct
from enum import Enum
import ast
from glean.schema.py.glean_schema_predicate import GleanSchemaPredicate , Just, InnerGleanSchemaPredicate
from glean.client.py3.angle_query import angle_for, R
from glean.schema.py.src import *


from glean.schema.erlang.types import (
    DeclarationReference,
    DeclarationWithFqn,
    FunctionDeclaration,
    DeclarationToFqn,
    SearchByName,
    DeclarationsByFile,
    DeclarationLocation,
    NameLowerCase,
    XRefsViaFqnByFile,
    DeclarationUses,
    XRefViaFqn,
    Fqn,
    Declaration,
)


class ErlangDeclarationReference(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], target: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, target, 'target'), angle_for(__env, source, 'source')]))
    return f"erlang.DeclarationReference.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationReference

  @staticmethod
  def angle_query(*, target: Optional["ErlangDeclaration"] = None, source: Optional["ErlangDeclaration"] = None) -> "ErlangDeclarationReference":
    raise Exception("this function can only be called from @angle_query")



class ErlangDeclarationWithFqn(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], fqn: ast.Expr, declaration: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, fqn, 'fqn'), angle_for(__env, declaration, 'declaration')]))
    return f"erlang.DeclarationWithFqn.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationWithFqn

  @staticmethod
  def angle_query(*, fqn: Optional["ErlangFqn"] = None, declaration: Optional["ErlangDeclaration"] = None) -> "ErlangDeclarationWithFqn":
    raise Exception("this function can only be called from @angle_query")



class ErlangFunctionDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], fqn: ast.Expr, file: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, fqn, 'fqn'), angle_for(__env, file, 'file'), angle_for(__env, span, 'span')]))
    return f"erlang.FunctionDeclaration.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FunctionDeclaration

  @staticmethod
  def angle_query(*, fqn: Optional["ErlangFqn"] = None, file: Optional["SrcFile"] = None, span: Optional["SrcByteSpan"] = None) -> "ErlangFunctionDeclaration":
    raise Exception("this function can only be called from @angle_query")



class ErlangDeclarationToFqn(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"erlang.DeclarationToFqn.1 { query_fields if query_fields else '_' }", DeclarationToFqn

  @staticmethod
  def angle_query(*, arg: Optional["ErlangDeclaration"] = None) -> "ErlangDeclarationToFqn":
    raise Exception("this function can only be called from @angle_query")



class ErlangSearchByName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, func: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, func, 'func')]))
    return f"erlang.SearchByName.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", SearchByName

  @staticmethod
  def angle_query(*, name: Optional[str] = None, func: Optional["ErlangDeclaration"] = None) -> "ErlangSearchByName":
    raise Exception("this function can only be called from @angle_query")



class ErlangDeclarationsByFile(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, span: ast.Expr, declaration: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, span, 'span'), angle_for(__env, declaration, 'declaration')]))
    return f"erlang.DeclarationsByFile.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationsByFile

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, span: Optional["SrcByteSpan"] = None, declaration: Optional["ErlangDeclaration"] = None) -> "ErlangDeclarationsByFile":
    raise Exception("this function can only be called from @angle_query")



class ErlangDeclarationLocation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, file: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, file, 'file'), angle_for(__env, span, 'span')]))
    return f"erlang.DeclarationLocation.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationLocation

  @staticmethod
  def angle_query(*, declaration: Optional["ErlangDeclaration"] = None, file: Optional["SrcFile"] = None, span: Optional["SrcByteSpan"] = None) -> "ErlangDeclarationLocation":
    raise Exception("this function can only be called from @angle_query")



class ErlangNameLowerCase(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], nameLowercase: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, nameLowercase, 'nameLowercase'), angle_for(__env, name, 'name')]))
    return f"erlang.NameLowerCase.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", NameLowerCase

  @staticmethod
  def angle_query(*, nameLowercase: Optional[str] = None, name: Optional[str] = None) -> "ErlangNameLowerCase":
    raise Exception("this function can only be called from @angle_query")



class ErlangXRefsViaFqnByFile(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, xrefs: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, xrefs, 'xrefs')]))
    return f"erlang.XRefsViaFqnByFile.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", XRefsViaFqnByFile

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, xrefs: Optional[List["ErlangXRefViaFqn"]] = None) -> "ErlangXRefsViaFqnByFile":
    raise Exception("this function can only be called from @angle_query")



class ErlangDeclarationUses(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, file: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, file, 'file'), angle_for(__env, span, 'span')]))
    return f"erlang.DeclarationUses.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationUses

  @staticmethod
  def angle_query(*, declaration: Optional["ErlangDeclaration"] = None, file: Optional["SrcFile"] = None, span: Optional["SrcByteSpan"] = None) -> "ErlangDeclarationUses":
    raise Exception("this function can only be called from @angle_query")





class ErlangXRefViaFqn(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], target: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, target, 'target'), angle_for(__env, source, 'source')]))
    return f"erlang.XRefViaFqn.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", XRefViaFqn

  @staticmethod
  def angle_query(*, target: Optional["ErlangFqn"] = None, source: Optional["SrcByteSpan"] = None) -> "ErlangXRefViaFqn":
    raise Exception("this function can only be called from @angle_query")



class ErlangFqn(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], module: ast.Expr, name: ast.Expr, arity: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, module, 'module'), angle_for(__env, name, 'name'), angle_for(__env, arity, 'arity')]))
    return f"erlang.Fqn.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Fqn

  @staticmethod
  def angle_query(*, module: Optional[str] = None, name: Optional[str] = None, arity: Optional[int] = None) -> "ErlangFqn":
    raise Exception("this function can only be called from @angle_query")



class ErlangDeclaration(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], func: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, func, 'func')]))
    return f"erlang.Declaration.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Declaration

  @staticmethod
  def angle_query_func(*, func: Optional["ErlangFunctionDeclaration"] = None) -> "ErlangDeclaration":
    raise Exception("this function can only be called from @angle_query")





