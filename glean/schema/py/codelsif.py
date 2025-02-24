# @generated
# To regenerate this file run fbcode//glean/schema/gen/sync
from typing import Optional, Tuple, Union, List, Dict, TypeVar
from thrift.py3 import Struct
from enum import Enum
import ast
from glean.schema.py.glean_schema_predicate import GleanSchemaPredicate , Just, InnerGleanSchemaPredicate
from glean.client.py3.angle_query import angle_for, R
from glean.schema.py.lsif import *


from glean.schema.code_lsif.types import (
    Entity,
)




class CodeLsifEntity(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], erlang: ast.Expr, fsharp: ast.Expr, go: ast.Expr, haskell: ast.Expr, java: ast.Expr, kotlin: ast.Expr, ocaml: ast.Expr, python: ast.Expr, rust: ast.Expr, scala: ast.Expr, swift: ast.Expr, typescript: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, erlang, 'erlang'), angle_for(__env, fsharp, 'fsharp'), angle_for(__env, go, 'go'), angle_for(__env, haskell, 'haskell'), angle_for(__env, java, 'java'), angle_for(__env, kotlin, 'kotlin'), angle_for(__env, ocaml, 'ocaml'), angle_for(__env, python, 'python'), angle_for(__env, rust, 'rust'), angle_for(__env, scala, 'scala'), angle_for(__env, swift, 'swift'), angle_for(__env, typescript, 'typescript')]))
    return f"code.lsif.Entity.2 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Entity

  @staticmethod
  def angle_query_erlang(*, erlang: Optional["LsifSomeEntity"] = None) -> "CodeLsifEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_fsharp(*, fsharp: Optional["LsifSomeEntity"] = None) -> "CodeLsifEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_go(*, go: Optional["LsifSomeEntity"] = None) -> "CodeLsifEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_haskell(*, haskell: Optional["LsifSomeEntity"] = None) -> "CodeLsifEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_java(*, java: Optional["LsifSomeEntity"] = None) -> "CodeLsifEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_kotlin(*, kotlin: Optional["LsifSomeEntity"] = None) -> "CodeLsifEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_ocaml(*, ocaml: Optional["LsifSomeEntity"] = None) -> "CodeLsifEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_python(*, python: Optional["LsifSomeEntity"] = None) -> "CodeLsifEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_rust(*, rust: Optional["LsifSomeEntity"] = None) -> "CodeLsifEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_scala(*, scala: Optional["LsifSomeEntity"] = None) -> "CodeLsifEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_swift(*, swift: Optional["LsifSomeEntity"] = None) -> "CodeLsifEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_typescript(*, typescript: Optional["LsifSomeEntity"] = None) -> "CodeLsifEntity":
    raise Exception("this function can only be called from @angle_query")





