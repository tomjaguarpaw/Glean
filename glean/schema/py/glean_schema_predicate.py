# @generated
# To regenerate this file run fbcode//glean/schema/gen/sync
from typing import Generic, Optional, TypeVar
from thrift.py3.types import Struct

# Pyre expects a Fact to be bound to a Struct in GleanClient. For our API, we expect a GleanSchemaPredicate as the result. To meet both conditions, GleanSchemaPredicate extends a Struct.
class GleanSchemaPredicate(Struct):
  @staticmethod
  def angle_query(*, arg: str) -> "GleanSchemaPredicate":
    raise Exception("this function can only be called from @angle_query")

class InnerGleanSchemaPredicate:
  @staticmethod
  def angle_query(*, arg: str) -> "InnerGleanSchemaPredicate":
    raise Exception("this function can only be called as a parameter of a GleanSchemaPredicate")

T = TypeVar("T")

class Just(Generic[T]):
  just: T = None
  def __init__(self, just: T = None) -> None:
    self.just = just
  def get(self) -> Optional[T]:
    return self.just

