# @generated
# To regenerate this file run fbcode//glean/schema/gen/sync
from typing import Optional, Tuple, Union, List, Dict, TypeVar
from thrift.py3 import Struct
from enum import Enum
import ast
from glean.schema.py.glean_schema_predicate import GleanSchemaPredicate , Just, InnerGleanSchemaPredicate
from glean.client.py3.angle_query import angle_for, R
from glean.schema.py.buck import *
from glean.schema.py.cxx1 import *
from glean.schema.py.src import *


from glean.schema.buckuses.types import (
    UsesOfTargetHeader,
    UsesOfTarget,
)


class BuckusesUsesOfTargetHeader(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], locator: ast.Expr, exportedHeader: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, locator, 'locator'), angle_for(__env, exportedHeader, 'exportedHeader')]))
    return f"buckuses.UsesOfTargetHeader.4 { ('{ ' + query_fields + ' }') if query_fields else '_' }", UsesOfTargetHeader

  @staticmethod
  def angle_query(*, locator: Optional["BuckLocator"] = None, exportedHeader: Optional["SrcFile"] = None) -> "BuckusesUsesOfTargetHeader":
    raise Exception("this function can only be called from @angle_query")



class BuckusesUsesOfTarget(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], locator: ast.Expr, use_xref: ast.Expr, use_file: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, locator, 'locator'), angle_for(__env, use_xref, 'use_xref'), angle_for(__env, use_file, 'use_file')]))
    return f"buckuses.UsesOfTarget.4 { ('{ ' + query_fields + ' }') if query_fields else '_' }", UsesOfTarget

  @staticmethod
  def angle_query(*, locator: Optional["BuckLocator"] = None, use_xref: Optional["Cxx1XRefTarget"] = None, use_file: Optional["SrcFile"] = None) -> "BuckusesUsesOfTarget":
    raise Exception("this function can only be called from @angle_query")






