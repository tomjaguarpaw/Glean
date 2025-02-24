# @generated
# To regenerate this file run fbcode//glean/schema/gen/sync
from typing import Optional, Tuple, Union, List, Dict, TypeVar
from thrift.py3 import Struct
from enum import Enum
import ast
from glean.schema.py.glean_schema_predicate import GleanSchemaPredicate , Just, InnerGleanSchemaPredicate
from glean.client.py3.angle_query import angle_for, R


from glean.schema.hackdependency.types import (
    inheritance,
    name,
)


class HackdependencyInheritance(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], parent: ast.Expr, child: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, parent, 'parent'), angle_for(__env, child, 'child')]))
    return f"hackdependency.inheritance.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", inheritance

  @staticmethod
  def angle_query(*, parent: Optional["Hackdependencyname"] = None, child: Optional["Hackdependencyname"] = None) -> "HackdependencyInheritance":
    raise Exception("this function can only be called from @angle_query")



class HackdependencyName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"hackdependency.name.1 { query_fields if query_fields else '_' }", name

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "HackdependencyName":
    raise Exception("this function can only be called from @angle_query")






