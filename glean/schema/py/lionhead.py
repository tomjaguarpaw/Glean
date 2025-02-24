# @generated
# To regenerate this file run fbcode//glean/schema/gen/sync
from typing import Optional, Tuple, Union, List, Dict, TypeVar
from thrift.py3 import Struct
from enum import Enum
import ast
from glean.schema.py.glean_schema_predicate import GleanSchemaPredicate , Just, InnerGleanSchemaPredicate
from glean.client.py3.angle_query import angle_for, R
from glean.schema.py.testinfra import *


from glean.schema.lionhead.types import (
    CoveredHarness,
    FbId,
)


class LionheadCoveredHarness(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], harnessId: ast.Expr, root: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, harnessId, 'harnessId'), angle_for(__env, root, 'root')]))
    return f"lionhead.CoveredHarness.1 { ('{ ' + query_fields + ' }') if query_fields else '_' }", CoveredHarness

  @staticmethod
  def angle_query(*, harnessId: Optional["LionheadFbId"] = None, root: Optional["TestinfraCoveredFolder"] = None) -> "LionheadCoveredHarness":
    raise Exception("this function can only be called from @angle_query")



class LionheadFbId(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"lionhead.FbId.1 { query_fields if query_fields else '_' }", FbId

  @staticmethod
  def angle_query(*, arg: Optional[int] = None) -> "LionheadFbId":
    raise Exception("this function can only be called from @angle_query")






