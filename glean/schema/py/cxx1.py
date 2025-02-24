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
from glean.schema.py.pp1 import *
from glean.schema.py.src import *


from glean.schema.cxx1.types import (
    DeclInObjcContainer,
    IncludeTree,
    XRefIndirectTarget,
    DeclByName,
    DeclarationTargets,
    DeclarationLocationName,
    DeclarationScope,
    EnumDeclaration,
    FileXRefMap,
    ObjcContainerDeclaration,
    ObjcMethodDeclaration,
    MethodOverrides,
    FunctionDeclAttribute,
    ObjcInterfaceToImplementation,
    UsingDirective,
    Trace,
    ObjcPropertyImplementation,
    MethodOverridden,
    PPTrace,
    DeclFamilyOf,
    TargetUses,
    NamespaceDefinition,
    FunctionAttribute,
    FilePPUseTraceXRefs,
    TypeAliasDeclaration,
    USRToDeclaration,
    DefToBaseDecl,
    Name,
    FilePPUseXRefs,
    TranslationUnitIncludeTree,
    Enumerator,
    FunctionQName,
    TranslationUnitTrace,
    RecordDeclaration,
    FilePPTraceXRefs,
    NamespaceQName,
    DeclarationSrcRange,
    DeclarationLocation,
    ObjContainerIdName,
    FunctionDeclaration,
    Same,
    NamespaceDeclaration,
    DefnInRecord,
    ObjcPropertyDeclaration,
    DeclarationComment,
    DeclarationNameSpan,
    Declarations,
    DeclToFamily,
    DeclFamily,
    FunctionDeclarationNameString,
    EnumeratorInEnum,
    RecordDefinition,
    Type,
    RecordDerived,
    PPDefineLocation,
    ObjcImplements,
    ObjcSelector,
    ObjcMethodDefinition,
    DeclarationInTrace,
    PPEntityLocation,
    UsingDeclaration,
    QName,
    ObjcContainerDefinition,
    EnumDefinition,
    VariableDeclaration,
    DeclarationLocationNameSpan,
    ObjcContainerBase,
    DeclarationSources,
    TranslationUnitXRefs,
    ObjcPropertyIVar,
    ObjcContainerInheritance,
    FunctionDefinition,
    Signature,
    DeclInRecord,
    FileXRefs,
    Attribute,
    NamespaceDeclarationName,
    FunctionDeclarationName,
    FunctionName,
    Scope,
    ObjcPropertyKind,
    MethodSignature,
    ObjcIVar,
    Declaration,
    RefQualifier,
    GlobalVariableAttribute,
    ObjcCategoryId,
    Parameter,
    DeclKind,
    TypeAliasKind,
    ObjcContainerId,
    XRefVia,
    DeclIdent,
    GlobalVariable,
    GlobalVariableKind,
    Field,
    LocalVariableKind,
    PpEntity,
    LocalVariable,
    RecordBase,
    XRefTarget,
    MaybeIncludeTree,
    VariableKind,
    DefinitionEntity,
    FixedXRef,
    LocalVariableAttribute,
    PPEvent,
    Access,
    RecordKind,
    IncludeTrace,
)


class Cxx1DeclInObjcContainer(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, record: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, record, 'record')]))
    return f"cxx1.DeclInObjcContainer.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclInObjcContainer

  @staticmethod
  def angle_query(*, decl: Optional["Cxx1Declaration"] = None, record: Optional["Cxx1ObjcContainerDefinition"] = None) -> "Cxx1DeclInObjcContainer":
    raise Exception("this function can only be called from @angle_query")



class Cxx1IncludeTree(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], trace: ast.Expr, children: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, trace, 'trace'), angle_for(__env, children, 'children')]))
    return f"cxx1.IncludeTree.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", IncludeTree

  @staticmethod
  def angle_query(*, trace: Optional["Cxx1Trace"] = None, children: Optional[List["Cxx1MaybeIncludeTree"]] = None) -> "Cxx1IncludeTree":
    raise Exception("this function can only be called from @angle_query")



class Cxx1XRefIndirectTarget(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], via: ast.Expr, target: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, via, 'via'), angle_for(__env, target, 'target')]))
    return f"cxx1.XRefIndirectTarget.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", XRefIndirectTarget

  @staticmethod
  def angle_query(*, via: Optional["Cxx1XRefVia"] = None, target: Optional["Cxx1XRefTarget"] = None) -> "Cxx1XRefIndirectTarget":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclByName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name_lowercase: ast.Expr, kind: ast.Expr, ident: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name_lowercase, 'name_lowercase'), angle_for(__env, kind, 'kind'), angle_for(__env, ident, 'ident')]))
    return f"cxx1.DeclByName.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclByName

  @staticmethod
  def angle_query(*, name_lowercase: Optional[str] = None, kind: Optional["Cxx1DeclKind"] = None, ident: Optional["Cxx1DeclIdent"] = None) -> "Cxx1DeclByName":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclarationTargets(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], source: ast.Expr, targets: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, source, 'source'), angle_for(__env, targets, 'targets')]))
    return f"cxx1.DeclarationTargets.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationTargets

  @staticmethod
  def angle_query(*, source: Optional["Cxx1Declaration"] = None, targets: Optional[List["Cxx1Declaration"]] = None) -> "Cxx1DeclarationTargets":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclarationLocationName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, source: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, source, 'source'), angle_for(__env, name, 'name')]))
    return f"cxx1.DeclarationLocationName.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationLocationName

  @staticmethod
  def angle_query(*, decl: Optional["Cxx1Declaration"] = None, source: Optional["SrcRange"] = None, name: Optional[str] = None) -> "Cxx1DeclarationLocationName":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclarationScope(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, scope: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, scope, 'scope')]))
    return f"cxx1.DeclarationScope.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationScope

  @staticmethod
  def angle_query(*, decl: Optional["Cxx1Declaration"] = None, scope: Optional["Cxx1Scope"] = None) -> "Cxx1DeclarationScope":
    raise Exception("this function can only be called from @angle_query")



class Cxx1EnumDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, isScoped: ast.Expr, type: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, isScoped, 'isScoped'), angle_for(__env, type, 'type'), angle_for(__env, source, 'source')]))
    return f"cxx1.EnumDeclaration.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", EnumDeclaration

  @staticmethod
  def angle_query(*, name: Optional["Cxx1QName"] = None, isScoped: Optional[bool] = None, type: Optional[Union[Just["Cxx1Type"], Just[None]]] = None, source: Optional["SrcRange"] = None) -> "Cxx1EnumDeclaration":
    raise Exception("this function can only be called from @angle_query")



class Cxx1FileXRefMap(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, fixed: ast.Expr, variable: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, fixed, 'fixed'), angle_for(__env, variable, 'variable')]))
    return f"cxx1.FileXRefMap.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FileXRefMap

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, fixed: Optional[List["Cxx1FixedXRef"]] = None, variable: Optional[List["SrcByteSpans"]] = None) -> "Cxx1FileXRefMap":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjcContainerDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], id: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, id, 'id'), angle_for(__env, source, 'source')]))
    return f"cxx1.ObjcContainerDeclaration.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjcContainerDeclaration

  @staticmethod
  def angle_query(*, id: Optional["Cxx1ObjcContainerId"] = None, source: Optional["SrcRange"] = None) -> "Cxx1ObjcContainerDeclaration":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjcMethodDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], selector: ast.Expr, container: ast.Expr, signature: ast.Expr, isInstance: ast.Expr, isOptional: ast.Expr, isAccessor: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, selector, 'selector'), angle_for(__env, container, 'container'), angle_for(__env, signature, 'signature'), angle_for(__env, isInstance, 'isInstance'), angle_for(__env, isOptional, 'isOptional'), angle_for(__env, isAccessor, 'isAccessor'), angle_for(__env, source, 'source')]))
    return f"cxx1.ObjcMethodDeclaration.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjcMethodDeclaration

  @staticmethod
  def angle_query(*, selector: Optional["Cxx1ObjcSelector"] = None, container: Optional["Cxx1ObjcContainerId"] = None, signature: Optional["Cxx1Signature"] = None, isInstance: Optional[bool] = None, isOptional: Optional[bool] = None, isAccessor: Optional[bool] = None, source: Optional["SrcRange"] = None) -> "Cxx1ObjcMethodDeclaration":
    raise Exception("this function can only be called from @angle_query")



class Cxx1MethodOverrides(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], derived: ast.Expr, base: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, derived, 'derived'), angle_for(__env, base, 'base')]))
    return f"cxx1.MethodOverrides.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", MethodOverrides

  @staticmethod
  def angle_query(*, derived: Optional["Cxx1FunctionDeclaration"] = None, base: Optional["Cxx1FunctionDeclaration"] = None) -> "Cxx1MethodOverrides":
    raise Exception("this function can only be called from @angle_query")



class Cxx1FunctionDeclAttribute(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, attr: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, attr, 'attr')]))
    return f"cxx1.FunctionDeclAttribute.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FunctionDeclAttribute

  @staticmethod
  def angle_query(*, decl: Optional["Cxx1FunctionDeclaration"] = None, attr: Optional["Cxx1Attribute"] = None) -> "Cxx1FunctionDeclAttribute":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjcInterfaceToImplementation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], interface_: ast.Expr, implementation: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, interface_, 'interface_'), angle_for(__env, implementation, 'implementation')]))
    return f"cxx1.ObjcInterfaceToImplementation.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjcInterfaceToImplementation

  @staticmethod
  def angle_query(*, interface_: Optional["Cxx1ObjcContainerDeclaration"] = None, implementation: Optional["Cxx1ObjcContainerDeclaration"] = None) -> "Cxx1ObjcInterfaceToImplementation":
    raise Exception("this function can only be called from @angle_query")



class Cxx1UsingDirective(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, source, 'source')]))
    return f"cxx1.UsingDirective.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", UsingDirective

  @staticmethod
  def angle_query(*, name: Optional["Cxx1QName"] = None, source: Optional["SrcRange"] = None) -> "Cxx1UsingDirective":
    raise Exception("this function can only be called from @angle_query")



class Cxx1Trace(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, declarations: ast.Expr, preprocessor: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, declarations, 'declarations'), angle_for(__env, preprocessor, 'preprocessor')]))
    return f"cxx1.Trace.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Trace

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, declarations: Optional["Cxx1Declarations"] = None, preprocessor: Optional["Cxx1PPTrace"] = None) -> "Cxx1Trace":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjcPropertyImplementation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, kind: ast.Expr, ivar: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, kind, 'kind'), angle_for(__env, ivar, 'ivar'), angle_for(__env, source, 'source')]))
    return f"cxx1.ObjcPropertyImplementation.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjcPropertyImplementation

  @staticmethod
  def angle_query(*, declaration: Optional["Cxx1ObjcPropertyDeclaration"] = None, kind: Optional["Cxx1ObjcPropertyKind"] = None, ivar: Optional[Union[Just["Cxx1Name"], Just[None]]] = None, source: Optional["SrcRange"] = None) -> "Cxx1ObjcPropertyImplementation":
    raise Exception("this function can only be called from @angle_query")



class Cxx1MethodOverridden(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], base: ast.Expr, derived: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, base, 'base'), angle_for(__env, derived, 'derived')]))
    return f"cxx1.MethodOverridden.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", MethodOverridden

  @staticmethod
  def angle_query(*, base: Optional["Cxx1FunctionDeclaration"] = None, derived: Optional["Cxx1FunctionDeclaration"] = None) -> "Cxx1MethodOverridden":
    raise Exception("this function can only be called from @angle_query")



class Cxx1PPTrace(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, events: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, events, 'events')]))
    return f"cxx1.PPTrace.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PPTrace

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, events: Optional[List["Cxx1PPEvent"]] = None) -> "Cxx1PPTrace":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclFamilyOf(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, family: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, family, 'family')]))
    return f"cxx1.DeclFamilyOf.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclFamilyOf

  @staticmethod
  def angle_query(*, decl: Optional["Cxx1Declaration"] = None, family: Optional["Cxx1Declaration"] = None) -> "Cxx1DeclFamilyOf":
    raise Exception("this function can only be called from @angle_query")



class Cxx1TargetUses(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], target: ast.Expr, file: ast.Expr, uses: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, target, 'target'), angle_for(__env, file, 'file'), angle_for(__env, uses, 'uses')]))
    return f"cxx1.TargetUses.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TargetUses

  @staticmethod
  def angle_query(*, target: Optional["Cxx1XRefTarget"] = None, file: Optional["SrcFile"] = None, uses: Optional["SrcByteSpans"] = None) -> "Cxx1TargetUses":
    raise Exception("this function can only be called from @angle_query")



class Cxx1NamespaceDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, members: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, members, 'members')]))
    return f"cxx1.NamespaceDefinition.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", NamespaceDefinition

  @staticmethod
  def angle_query(*, declaration: Optional["Cxx1NamespaceDeclaration"] = None, members: Optional["Cxx1Declarations"] = None) -> "Cxx1NamespaceDefinition":
    raise Exception("this function can only be called from @angle_query")



class Cxx1FunctionAttribute(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], attr: ast.Expr, declaration: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, attr, 'attr'), angle_for(__env, declaration, 'declaration')]))
    return f"cxx1.FunctionAttribute.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FunctionAttribute

  @staticmethod
  def angle_query(*, attr: Optional["Cxx1Attribute"] = None, declaration: Optional["Cxx1FunctionDeclaration"] = None) -> "Cxx1FunctionAttribute":
    raise Exception("this function can only be called from @angle_query")



class Cxx1FilePPUseTraceXRefs(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, trace: ast.Expr, source: ast.Expr, define: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, trace, 'trace'), angle_for(__env, source, 'source'), angle_for(__env, define, 'define')]))
    return f"cxx1.FilePPUseTraceXRefs.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FilePPUseTraceXRefs

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, trace: Optional["Cxx1Trace"] = None, source: Optional["SrcRange"] = None, define: Optional["Pp1Define"] = None) -> "Cxx1FilePPUseTraceXRefs":
    raise Exception("this function can only be called from @angle_query")



class Cxx1TypeAliasDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, type: ast.Expr, kind: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, type, 'type'), angle_for(__env, kind, 'kind'), angle_for(__env, source, 'source')]))
    return f"cxx1.TypeAliasDeclaration.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TypeAliasDeclaration

  @staticmethod
  def angle_query(*, name: Optional["Cxx1QName"] = None, type: Optional["Cxx1Type"] = None, kind: Optional["Cxx1TypeAliasKind"] = None, source: Optional["SrcRange"] = None) -> "Cxx1TypeAliasDeclaration":
    raise Exception("this function can only be called from @angle_query")



class Cxx1USRToDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], hash: ast.Expr, declaration: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, hash, 'hash'), angle_for(__env, declaration, 'declaration')]))
    return f"cxx1.USRToDeclaration.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", USRToDeclaration

  @staticmethod
  def angle_query(*, hash: Optional["Cxx1USR"] = None, declaration: Optional["Cxx1Declaration"] = None) -> "Cxx1USRToDeclaration":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DefToBaseDecl(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], defn: ast.Expr, decl: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, defn, 'defn'), angle_for(__env, decl, 'decl')]))
    return f"cxx1.DefToBaseDecl.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DefToBaseDecl

  @staticmethod
  def angle_query(*, defn: Optional["Cxx1DefinitionEntity"] = None, decl: Optional["Cxx1Declaration"] = None) -> "Cxx1DefToBaseDecl":
    raise Exception("this function can only be called from @angle_query")



class Cxx1Name(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"cxx1.Name.5 { query_fields if query_fields else '_' }", Name

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "Cxx1Name":
    raise Exception("this function can only be called from @angle_query")



class Cxx1FilePPUseXRefs(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, source: ast.Expr, define: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, source, 'source'), angle_for(__env, define, 'define')]))
    return f"cxx1.FilePPUseXRefs.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FilePPUseXRefs

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, source: Optional["SrcRange"] = None, define: Optional["Pp1Define"] = None) -> "Cxx1FilePPUseXRefs":
    raise Exception("this function can only be called from @angle_query")



class Cxx1TranslationUnitIncludeTree(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], tunit: ast.Expr, tree: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, tunit, 'tunit'), angle_for(__env, tree, 'tree')]))
    return f"cxx1.TranslationUnitIncludeTree.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TranslationUnitIncludeTree

  @staticmethod
  def angle_query(*, tunit: Optional["BuckTranslationUnit"] = None, tree: Optional["Cxx1IncludeTree"] = None) -> "Cxx1TranslationUnitIncludeTree":
    raise Exception("this function can only be called from @angle_query")



class Cxx1Enumerator(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, enumeration: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, enumeration, 'enumeration'), angle_for(__env, source, 'source')]))
    return f"cxx1.Enumerator.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Enumerator

  @staticmethod
  def angle_query(*, name: Optional["Cxx1Name"] = None, enumeration: Optional["Cxx1EnumDeclaration"] = None, source: Optional["SrcRange"] = None) -> "Cxx1Enumerator":
    raise Exception("this function can only be called from @angle_query")



class Cxx1FunctionQName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, scope: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, scope, 'scope')]))
    return f"cxx1.FunctionQName.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FunctionQName

  @staticmethod
  def angle_query(*, name: Optional["Cxx1FunctionName"] = None, scope: Optional["Cxx1Scope"] = None) -> "Cxx1FunctionQName":
    raise Exception("this function can only be called from @angle_query")



class Cxx1TranslationUnitTrace(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], tunit: ast.Expr, trace: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, tunit, 'tunit'), angle_for(__env, trace, 'trace')]))
    return f"cxx1.TranslationUnitTrace.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TranslationUnitTrace

  @staticmethod
  def angle_query(*, tunit: Optional["BuckTranslationUnit"] = None, trace: Optional["Cxx1Trace"] = None) -> "Cxx1TranslationUnitTrace":
    raise Exception("this function can only be called from @angle_query")



class Cxx1RecordDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, kind: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, kind, 'kind'), angle_for(__env, source, 'source')]))
    return f"cxx1.RecordDeclaration.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", RecordDeclaration

  @staticmethod
  def angle_query(*, name: Optional["Cxx1QName"] = None, kind: Optional["Cxx1RecordKind"] = None, source: Optional["SrcRange"] = None) -> "Cxx1RecordDeclaration":
    raise Exception("this function can only be called from @angle_query")



class Cxx1FilePPTraceXRefs(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, trace: ast.Expr, source: ast.Expr, ppEntity: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, trace, 'trace'), angle_for(__env, source, 'source'), angle_for(__env, ppEntity, 'ppEntity')]))
    return f"cxx1.FilePPTraceXRefs.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FilePPTraceXRefs

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, trace: Optional["Cxx1Trace"] = None, source: Optional["SrcRange"] = None, ppEntity: Optional["Cxx1PpEntity"] = None) -> "Cxx1FilePPTraceXRefs":
    raise Exception("this function can only be called from @angle_query")



class Cxx1NamespaceQName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, parent: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, parent, 'parent')]))
    return f"cxx1.NamespaceQName.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", NamespaceQName

  @staticmethod
  def angle_query(*, name: Optional[Union[Just["Cxx1Name"], Just[None]]] = None, parent: Optional[Union[Just["Cxx1NamespaceQName"], Just[None]]] = None) -> "Cxx1NamespaceQName":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclarationSrcRange(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, source, 'source')]))
    return f"cxx1.DeclarationSrcRange.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationSrcRange

  @staticmethod
  def angle_query(*, decl: Optional["Cxx1Declaration"] = None, source: Optional["SrcRange"] = None) -> "Cxx1DeclarationSrcRange":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclarationLocation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, source: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, source, 'source'), angle_for(__env, name, 'name')]))
    return f"cxx1.DeclarationLocation.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationLocation

  @staticmethod
  def angle_query(*, decl: Optional["Cxx1Declaration"] = None, source: Optional["SrcRange"] = None, name: Optional["Cxx1Name"] = None) -> "Cxx1DeclarationLocation":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjContainerIdName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], id: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, id, 'id'), angle_for(__env, name, 'name')]))
    return f"cxx1.ObjContainerIdName.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjContainerIdName

  @staticmethod
  def angle_query(*, id: Optional["Cxx1ObjcContainerId"] = None, name: Optional["Cxx1Name"] = None) -> "Cxx1ObjContainerIdName":
    raise Exception("this function can only be called from @angle_query")



class Cxx1FunctionDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, signature: ast.Expr, method: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, signature, 'signature'), angle_for(__env, method, 'method'), angle_for(__env, source, 'source')]))
    return f"cxx1.FunctionDeclaration.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FunctionDeclaration

  @staticmethod
  def angle_query(*, name: Optional["Cxx1FunctionQName"] = None, signature: Optional["Cxx1Signature"] = None, method: Optional[Union[Just["Cxx1MethodSignature"], Just[None]]] = None, source: Optional["SrcRange"] = None) -> "Cxx1FunctionDeclaration":
    raise Exception("this function can only be called from @angle_query")



class Cxx1Same(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration1: ast.Expr, declaration2: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration1, 'declaration1'), angle_for(__env, declaration2, 'declaration2')]))
    return f"cxx1.Same.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Same

  @staticmethod
  def angle_query(*, declaration1: Optional["Cxx1Declaration"] = None, declaration2: Optional["Cxx1Declaration"] = None) -> "Cxx1Same":
    raise Exception("this function can only be called from @angle_query")



class Cxx1NamespaceDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, source, 'source')]))
    return f"cxx1.NamespaceDeclaration.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", NamespaceDeclaration

  @staticmethod
  def angle_query(*, name: Optional["Cxx1NamespaceQName"] = None, source: Optional["SrcRange"] = None) -> "Cxx1NamespaceDeclaration":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DefnInRecord(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], defn: ast.Expr, record: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, defn, 'defn'), angle_for(__env, record, 'record')]))
    return f"cxx1.DefnInRecord.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DefnInRecord

  @staticmethod
  def angle_query(*, defn: Optional["Cxx1DefinitionEntity"] = None, record: Optional["Cxx1RecordDefinition"] = None) -> "Cxx1DefnInRecord":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjcPropertyDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, container: ast.Expr, type: ast.Expr, isInstance: ast.Expr, isOptional: ast.Expr, isReadOnly: ast.Expr, isAtomic: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, container, 'container'), angle_for(__env, type, 'type'), angle_for(__env, isInstance, 'isInstance'), angle_for(__env, isOptional, 'isOptional'), angle_for(__env, isReadOnly, 'isReadOnly'), angle_for(__env, isAtomic, 'isAtomic'), angle_for(__env, source, 'source')]))
    return f"cxx1.ObjcPropertyDeclaration.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjcPropertyDeclaration

  @staticmethod
  def angle_query(*, name: Optional["Cxx1Name"] = None, container: Optional["Cxx1ObjcContainerId"] = None, type: Optional["Cxx1Type"] = None, isInstance: Optional[bool] = None, isOptional: Optional[bool] = None, isReadOnly: Optional[bool] = None, isAtomic: Optional[bool] = None, source: Optional["SrcRange"] = None) -> "Cxx1ObjcPropertyDeclaration":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclarationComment(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, file: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, file, 'file'), angle_for(__env, span, 'span')]))
    return f"cxx1.DeclarationComment.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationComment

  @staticmethod
  def angle_query(*, declaration: Optional["Cxx1Declaration"] = None, file: Optional["SrcFile"] = None, span: Optional["SrcByteSpan"] = None) -> "Cxx1DeclarationComment":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclarationNameSpan(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, file: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, file, 'file'), angle_for(__env, span, 'span')]))
    return f"cxx1.DeclarationNameSpan.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationNameSpan

  @staticmethod
  def angle_query(*, decl: Optional["Cxx1Declaration"] = None, file: Optional["SrcFile"] = None, span: Optional["SrcByteSpan"] = None) -> "Cxx1DeclarationNameSpan":
    raise Exception("this function can only be called from @angle_query")



class Cxx1Declarations(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"cxx1.Declarations.5 { query_fields if query_fields else '_' }", Declarations

  @staticmethod
  def angle_query(*, arg: Optional[List["Cxx1Declaration"]] = None) -> "Cxx1Declarations":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclToFamily(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, family: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, family, 'family')]))
    return f"cxx1.DeclToFamily.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclToFamily

  @staticmethod
  def angle_query(*, decl: Optional["Cxx1Declaration"] = None, family: Optional["Cxx1DeclFamily"] = None) -> "Cxx1DeclToFamily":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclFamily(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"cxx1.DeclFamily.5 { query_fields if query_fields else '_' }", DeclFamily

  @staticmethod
  def angle_query(*, arg: Optional[List["Cxx1Declaration"]] = None) -> "Cxx1DeclFamily":
    raise Exception("this function can only be called from @angle_query")



class Cxx1FunctionDeclarationNameString(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], fname: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, fname, 'fname'), angle_for(__env, name, 'name')]))
    return f"cxx1.FunctionDeclarationNameString.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FunctionDeclarationNameString

  @staticmethod
  def angle_query(*, fname: Optional["Cxx1FunctionName"] = None, name: Optional[str] = None) -> "Cxx1FunctionDeclarationNameString":
    raise Exception("this function can only be called from @angle_query")



class Cxx1EnumeratorInEnum(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], enumerator: ast.Expr, enum_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, enumerator, 'enumerator'), angle_for(__env, enum_, 'enum_')]))
    return f"cxx1.EnumeratorInEnum.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", EnumeratorInEnum

  @staticmethod
  def angle_query(*, enumerator: Optional["Cxx1Enumerator"] = None, enum_: Optional["Cxx1EnumDefinition"] = None) -> "Cxx1EnumeratorInEnum":
    raise Exception("this function can only be called from @angle_query")



class Cxx1RecordDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, bases: ast.Expr, members: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, bases, 'bases'), angle_for(__env, members, 'members')]))
    return f"cxx1.RecordDefinition.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", RecordDefinition

  @staticmethod
  def angle_query(*, declaration: Optional["Cxx1RecordDeclaration"] = None, bases: Optional[List["Cxx1RecordBase"]] = None, members: Optional["Cxx1Declarations"] = None) -> "Cxx1RecordDefinition":
    raise Exception("this function can only be called from @angle_query")



class Cxx1Type(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"cxx1.Type.5 { query_fields if query_fields else '_' }", Type

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "Cxx1Type":
    raise Exception("this function can only be called from @angle_query")



class Cxx1RecordDerived(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], base: ast.Expr, derived: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, base, 'base'), angle_for(__env, derived, 'derived')]))
    return f"cxx1.RecordDerived.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", RecordDerived

  @staticmethod
  def angle_query(*, base: Optional["Cxx1RecordDeclaration"] = None, derived: Optional["Cxx1RecordDeclaration"] = None) -> "Cxx1RecordDerived":
    raise Exception("this function can only be called from @angle_query")



class Cxx1PPDefineLocation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], define: ast.Expr, name: ast.Expr, file: ast.Expr, range: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, define, 'define'), angle_for(__env, name, 'name'), angle_for(__env, file, 'file'), angle_for(__env, range, 'range')]))
    return f"cxx1.PPDefineLocation.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PPDefineLocation

  @staticmethod
  def angle_query(*, define: Optional["Pp1Define"] = None, name: Optional[str] = None, file: Optional["SrcFile"] = None, range: Optional["SrcRange"] = None) -> "Cxx1PPDefineLocation":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjcImplements(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], implementation: ast.Expr, interface_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, implementation, 'implementation'), angle_for(__env, interface_, 'interface_')]))
    return f"cxx1.ObjcImplements.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjcImplements

  @staticmethod
  def angle_query(*, implementation: Optional["Cxx1ObjcContainerDeclaration"] = None, interface_: Optional["Cxx1ObjcContainerDeclaration"] = None) -> "Cxx1ObjcImplements":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjcSelector(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"cxx1.ObjcSelector.5 { query_fields if query_fields else '_' }", ObjcSelector

  @staticmethod
  def angle_query(*, arg: Optional[List[str]] = None) -> "Cxx1ObjcSelector":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjcMethodDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"cxx1.ObjcMethodDefinition.5 { query_fields if query_fields else '_' }", ObjcMethodDefinition

  @staticmethod
  def angle_query(*, arg: Optional["Cxx1ObjcMethodDeclaration"] = None) -> "Cxx1ObjcMethodDefinition":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclarationInTrace(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, trace: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, trace, 'trace')]))
    return f"cxx1.DeclarationInTrace.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationInTrace

  @staticmethod
  def angle_query(*, decl: Optional["Cxx1Declaration"] = None, trace: Optional["Cxx1Trace"] = None) -> "Cxx1DeclarationInTrace":
    raise Exception("this function can only be called from @angle_query")



class Cxx1PPEntityLocation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], entity: ast.Expr, name: ast.Expr, file: ast.Expr, range: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, entity, 'entity'), angle_for(__env, name, 'name'), angle_for(__env, file, 'file'), angle_for(__env, range, 'range')]))
    return f"cxx1.PPEntityLocation.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PPEntityLocation

  @staticmethod
  def angle_query(*, entity: Optional["Cxx1PpEntity"] = None, name: Optional[str] = None, file: Optional["SrcFile"] = None, range: Optional["SrcRange"] = None) -> "Cxx1PPEntityLocation":
    raise Exception("this function can only be called from @angle_query")



class Cxx1UsingDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, source, 'source')]))
    return f"cxx1.UsingDeclaration.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", UsingDeclaration

  @staticmethod
  def angle_query(*, name: Optional["Cxx1FunctionQName"] = None, source: Optional["SrcRange"] = None) -> "Cxx1UsingDeclaration":
    raise Exception("this function can only be called from @angle_query")



class Cxx1QName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, scope: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, scope, 'scope')]))
    return f"cxx1.QName.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", QName

  @staticmethod
  def angle_query(*, name: Optional["Cxx1Name"] = None, scope: Optional["Cxx1Scope"] = None) -> "Cxx1QName":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjcContainerDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, protocols: ast.Expr, members: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, protocols, 'protocols'), angle_for(__env, members, 'members')]))
    return f"cxx1.ObjcContainerDefinition.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjcContainerDefinition

  @staticmethod
  def angle_query(*, declaration: Optional["Cxx1ObjcContainerDeclaration"] = None, protocols: Optional[List["Cxx1ObjcContainerDeclaration"]] = None, members: Optional["Cxx1Declarations"] = None) -> "Cxx1ObjcContainerDefinition":
    raise Exception("this function can only be called from @angle_query")



class Cxx1EnumDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, enumerators: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, enumerators, 'enumerators')]))
    return f"cxx1.EnumDefinition.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", EnumDefinition

  @staticmethod
  def angle_query(*, declaration: Optional["Cxx1EnumDeclaration"] = None, enumerators: Optional[List["Cxx1Enumerator"]] = None) -> "Cxx1EnumDefinition":
    raise Exception("this function can only be called from @angle_query")



class Cxx1VariableDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, type: ast.Expr, kind: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, type, 'type'), angle_for(__env, kind, 'kind'), angle_for(__env, source, 'source')]))
    return f"cxx1.VariableDeclaration.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", VariableDeclaration

  @staticmethod
  def angle_query(*, name: Optional["Cxx1QName"] = None, type: Optional["Cxx1Type"] = None, kind: Optional["Cxx1VariableKind"] = None, source: Optional["SrcRange"] = None) -> "Cxx1VariableDeclaration":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclarationLocationNameSpan(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, source: ast.Expr, name: ast.Expr, file: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, source, 'source'), angle_for(__env, name, 'name'), angle_for(__env, file, 'file'), angle_for(__env, span, 'span')]))
    return f"cxx1.DeclarationLocationNameSpan.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationLocationNameSpan

  @staticmethod
  def angle_query(*, decl: Optional["Cxx1Declaration"] = None, source: Optional["SrcRange"] = None, name: Optional[str] = None, file: Optional["SrcFile"] = None, span: Optional["SrcByteSpan"] = None) -> "Cxx1DeclarationLocationNameSpan":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjcContainerBase(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, base: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, base, 'base')]))
    return f"cxx1.ObjcContainerBase.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjcContainerBase

  @staticmethod
  def angle_query(*, declaration: Optional["Cxx1ObjcContainerDeclaration"] = None, base: Optional["Cxx1ObjcContainerDeclaration"] = None) -> "Cxx1ObjcContainerBase":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclarationSources(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], target: ast.Expr, sources: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, target, 'target'), angle_for(__env, sources, 'sources')]))
    return f"cxx1.DeclarationSources.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationSources

  @staticmethod
  def angle_query(*, target: Optional["Cxx1Declaration"] = None, sources: Optional[List["Cxx1Declaration"]] = None) -> "Cxx1DeclarationSources":
    raise Exception("this function can only be called from @angle_query")



class Cxx1TranslationUnitXRefs(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], tunit: ast.Expr, xrefs: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, tunit, 'tunit'), angle_for(__env, xrefs, 'xrefs')]))
    return f"cxx1.TranslationUnitXRefs.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TranslationUnitXRefs

  @staticmethod
  def angle_query(*, tunit: Optional["BuckTranslationUnit"] = None, xrefs: Optional[List["Cxx1FileXRefs"]] = None) -> "Cxx1TranslationUnitXRefs":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjcPropertyIVar(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], property: ast.Expr, ivar: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, property, 'property'), angle_for(__env, ivar, 'ivar')]))
    return f"cxx1.ObjcPropertyIVar.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjcPropertyIVar

  @staticmethod
  def angle_query(*, property: Optional["Cxx1ObjcPropertyDeclaration"] = None, ivar: Optional["Cxx1VariableDeclaration"] = None) -> "Cxx1ObjcPropertyIVar":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjcContainerInheritance(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], base: ast.Expr, declaration: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, base, 'base'), angle_for(__env, declaration, 'declaration')]))
    return f"cxx1.ObjcContainerInheritance.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjcContainerInheritance

  @staticmethod
  def angle_query(*, base: Optional["Cxx1ObjcContainerDeclaration"] = None, declaration: Optional["Cxx1ObjcContainerDeclaration"] = None) -> "Cxx1ObjcContainerInheritance":
    raise Exception("this function can only be called from @angle_query")



class Cxx1FunctionDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, isInline: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, isInline, 'isInline')]))
    return f"cxx1.FunctionDefinition.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FunctionDefinition

  @staticmethod
  def angle_query(*, declaration: Optional["Cxx1FunctionDeclaration"] = None, isInline: Optional[bool] = None) -> "Cxx1FunctionDefinition":
    raise Exception("this function can only be called from @angle_query")



class Cxx1Signature(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], returns: ast.Expr, parameters: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, returns, 'returns'), angle_for(__env, parameters, 'parameters')]))
    return f"cxx1.Signature.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Signature

  @staticmethod
  def angle_query(*, returns: Optional["Cxx1Type"] = None, parameters: Optional[List["Cxx1Parameter"]] = None) -> "Cxx1Signature":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclInRecord(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, record: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, record, 'record')]))
    return f"cxx1.DeclInRecord.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclInRecord

  @staticmethod
  def angle_query(*, decl: Optional["Cxx1Declaration"] = None, record: Optional["Cxx1RecordDefinition"] = None) -> "Cxx1DeclInRecord":
    raise Exception("this function can only be called from @angle_query")



class Cxx1FileXRefs(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], xmap: ast.Expr, externals: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, xmap, 'xmap'), angle_for(__env, externals, 'externals')]))
    return f"cxx1.FileXRefs.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FileXRefs

  @staticmethod
  def angle_query(*, xmap: Optional["Cxx1FileXRefMap"] = None, externals: Optional[List["Cxx1XRefTarget"]] = None) -> "Cxx1FileXRefs":
    raise Exception("this function can only be called from @angle_query")



class Cxx1Attribute(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"cxx1.Attribute.5 { query_fields if query_fields else '_' }", Attribute

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "Cxx1Attribute":
    raise Exception("this function can only be called from @angle_query")



class Cxx1NamespaceDeclarationName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], qname: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, qname, 'qname'), angle_for(__env, name, 'name')]))
    return f"cxx1.NamespaceDeclarationName.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", NamespaceDeclarationName

  @staticmethod
  def angle_query(*, qname: Optional["Cxx1NamespaceQName"] = None, name: Optional["Cxx1Name"] = None) -> "Cxx1NamespaceDeclarationName":
    raise Exception("this function can only be called from @angle_query")



class Cxx1FunctionDeclarationName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], fname: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, fname, 'fname'), angle_for(__env, name, 'name')]))
    return f"cxx1.FunctionDeclarationName.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FunctionDeclarationName

  @staticmethod
  def angle_query(*, fname: Optional["Cxx1FunctionName"] = None, name: Optional["Cxx1Name"] = None) -> "Cxx1FunctionDeclarationName":
    raise Exception("this function can only be called from @angle_query")



class Cxx1FunctionName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, operator_: ast.Expr, literalOperator: ast.Expr, constructor: ast.Expr, destructor: ast.Expr, conversionOperator: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, operator_, 'operator_'), angle_for(__env, literalOperator, 'literalOperator'), angle_for(__env, constructor, 'constructor'), angle_for(__env, destructor, 'destructor'), angle_for(__env, conversionOperator, 'conversionOperator')]))
    return f"cxx1.FunctionName.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FunctionName

  @staticmethod
  def angle_query_name(*, name: Optional["Cxx1Name"] = None) -> "Cxx1FunctionName":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_operator_(*, operator_: Optional["Cxx1Operator"] = None) -> "Cxx1FunctionName":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_literalOperator(*, literalOperator: Optional["Cxx1LiteralOperator"] = None) -> "Cxx1FunctionName":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_constructor(*, constructor: Optional["BuiltinUnit"] = None) -> "Cxx1FunctionName":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_destructor(*, destructor: Optional["BuiltinUnit"] = None) -> "Cxx1FunctionName":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_conversionOperator(*, conversionOperator: Optional["Cxx1Type"] = None) -> "Cxx1FunctionName":
    raise Exception("this function can only be called from @angle_query")






class Cxx1Scope(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], global_: ast.Expr, namespace_: ast.Expr, recordWithAccess: ast.Expr, local: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, global_, 'global_'), angle_for(__env, namespace_, 'namespace_'), angle_for(__env, recordWithAccess, 'recordWithAccess'), angle_for(__env, local, 'local')]))
    return f"cxx1.Scope.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Scope

  @staticmethod
  def angle_query_global_(*, global_: Optional["BuiltinUnit"] = None) -> "Cxx1Scope":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_namespace_(*, namespace_: Optional["Cxx1NamespaceQName"] = None) -> "Cxx1Scope":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_recordWithAccess(*, recordWithAccess: Optional['Cxx1Scope_recordWithAccess'] = None) -> "Cxx1Scope":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_local(*, local: Optional["Cxx1FunctionQName"] = None) -> "Cxx1Scope":
    raise Exception("this function can only be called from @angle_query")


class Cxx1Scope_recordWithAccess(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], record: ast.Expr, access: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, record, 'record'), angle_for(__env, access, 'access')]))
    return f" { ('{ ' + query_fields + ' }') if query_fields else '_' }", Cxx1Scope_recordWithAccess

  @staticmethod
  def angle_query(*, record: Optional["Cxx1QName"] = None, access: Optional["Cxx1Access"] = None) -> "Cxx1Scope_recordWithAccess":
    raise Exception("this function can only be called from @angle_query")





class Cxx1ObjcPropertyKind(Enum):
  Synthesize = 0
  Dynamic = 1

class Cxx1MethodSignature(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], isVirtual: ast.Expr, isConst: ast.Expr, isVolatile: ast.Expr, refQualifier: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, isVirtual, 'isVirtual'), angle_for(__env, isConst, 'isConst'), angle_for(__env, isVolatile, 'isVolatile'), angle_for(__env, refQualifier, 'refQualifier')]))
    return f"cxx1.MethodSignature.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", MethodSignature

  @staticmethod
  def angle_query(*, isVirtual: Optional[bool] = None, isConst: Optional[bool] = None, isVolatile: Optional[bool] = None, refQualifier: Optional["Cxx1RefQualifier"] = None) -> "Cxx1MethodSignature":
    raise Exception("this function can only be called from @angle_query")



class Cxx1ObjcIVar(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], synthesize: ast.Expr, bitsize: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, synthesize, 'synthesize'), angle_for(__env, bitsize, 'bitsize')]))
    return f"cxx1.ObjcIVar.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjcIVar

  @staticmethod
  def angle_query(*, synthesize: Optional[bool] = None, bitsize: Optional[Union[Just[int], Just[None]]] = None) -> "Cxx1ObjcIVar":
    raise Exception("this function can only be called from @angle_query")



class Cxx1Declaration(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], namespace_: ast.Expr, usingDeclaration: ast.Expr, usingDirective: ast.Expr, record_: ast.Expr, enum_: ast.Expr, function_: ast.Expr, variable: ast.Expr, objcContainer: ast.Expr, objcMethod: ast.Expr, objcProperty: ast.Expr, typeAlias: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, namespace_, 'namespace_'), angle_for(__env, usingDeclaration, 'usingDeclaration'), angle_for(__env, usingDirective, 'usingDirective'), angle_for(__env, record_, 'record_'), angle_for(__env, enum_, 'enum_'), angle_for(__env, function_, 'function_'), angle_for(__env, variable, 'variable'), angle_for(__env, objcContainer, 'objcContainer'), angle_for(__env, objcMethod, 'objcMethod'), angle_for(__env, objcProperty, 'objcProperty'), angle_for(__env, typeAlias, 'typeAlias')]))
    return f"cxx1.Declaration.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Declaration

  @staticmethod
  def angle_query_namespace_(*, namespace_: Optional["Cxx1NamespaceDeclaration"] = None) -> "Cxx1Declaration":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_usingDeclaration(*, usingDeclaration: Optional["Cxx1UsingDeclaration"] = None) -> "Cxx1Declaration":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_usingDirective(*, usingDirective: Optional["Cxx1UsingDirective"] = None) -> "Cxx1Declaration":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_record_(*, record_: Optional["Cxx1RecordDeclaration"] = None) -> "Cxx1Declaration":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_enum_(*, enum_: Optional["Cxx1EnumDeclaration"] = None) -> "Cxx1Declaration":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_function_(*, function_: Optional["Cxx1FunctionDeclaration"] = None) -> "Cxx1Declaration":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_variable(*, variable: Optional["Cxx1VariableDeclaration"] = None) -> "Cxx1Declaration":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_objcContainer(*, objcContainer: Optional["Cxx1ObjcContainerDeclaration"] = None) -> "Cxx1Declaration":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_objcMethod(*, objcMethod: Optional["Cxx1ObjcMethodDeclaration"] = None) -> "Cxx1Declaration":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_objcProperty(*, objcProperty: Optional["Cxx1ObjcPropertyDeclaration"] = None) -> "Cxx1Declaration":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_typeAlias(*, typeAlias: Optional["Cxx1TypeAliasDeclaration"] = None) -> "Cxx1Declaration":
    raise Exception("this function can only be called from @angle_query")




class Cxx1RefQualifier(Enum):
  None_ = 0
  LValue = 1
  RValue = 2

class Cxx1GlobalVariableAttribute(Enum):
  Plain = 0
  Inline = 1
  Constexpr = 2

class Cxx1ObjcCategoryId(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], className: ast.Expr, categoryName: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, className, 'className'), angle_for(__env, categoryName, 'categoryName')]))
    return f"cxx1.ObjcCategoryId.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjcCategoryId

  @staticmethod
  def angle_query(*, className: Optional["Cxx1Name"] = None, categoryName: Optional["Cxx1Name"] = None) -> "Cxx1ObjcCategoryId":
    raise Exception("this function can only be called from @angle_query")



class Cxx1Parameter(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, type: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, type, 'type')]))
    return f"cxx1.Parameter.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Parameter

  @staticmethod
  def angle_query(*, name: Optional["Cxx1Name"] = None, type: Optional["Cxx1Type"] = None) -> "Cxx1Parameter":
    raise Exception("this function can only be called from @angle_query")



class Cxx1DeclKind(Enum):
  namespace_ = 0
  usingDeclaration = 1
  usingDirective = 2
  record_ = 3
  enum_ = 4
  enumerator = 5
  function_ = 6
  variable = 7
  objcContainer = 8
  objcMethod = 9
  objcProperty = 10
  typeAlias = 11
  macro = 12

class Cxx1TypeAliasKind(Enum):
  Typedef = 0
  Using = 1

class Cxx1ObjcContainerId(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], protocol: ast.Expr, interface_: ast.Expr, categoryInterface: ast.Expr, extensionInterface: ast.Expr, implementation: ast.Expr, categoryImplementation: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, protocol, 'protocol'), angle_for(__env, interface_, 'interface_'), angle_for(__env, categoryInterface, 'categoryInterface'), angle_for(__env, extensionInterface, 'extensionInterface'), angle_for(__env, implementation, 'implementation'), angle_for(__env, categoryImplementation, 'categoryImplementation')]))
    return f"cxx1.ObjcContainerId.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ObjcContainerId

  @staticmethod
  def angle_query_protocol(*, protocol: Optional["Cxx1Name"] = None) -> "Cxx1ObjcContainerId":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_interface_(*, interface_: Optional["Cxx1Name"] = None) -> "Cxx1ObjcContainerId":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_categoryInterface(*, categoryInterface: Optional["Cxx1ObjcCategoryId"] = None) -> "Cxx1ObjcContainerId":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_extensionInterface(*, extensionInterface: Optional["Cxx1Name"] = None) -> "Cxx1ObjcContainerId":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_implementation(*, implementation: Optional["Cxx1Name"] = None) -> "Cxx1ObjcContainerId":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_categoryImplementation(*, categoryImplementation: Optional["Cxx1ObjcCategoryId"] = None) -> "Cxx1ObjcContainerId":
    raise Exception("this function can only be called from @angle_query")




class Cxx1XRefVia(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], usingDeclaration: ast.Expr, usingDirective: ast.Expr, macro: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, usingDeclaration, 'usingDeclaration'), angle_for(__env, usingDirective, 'usingDirective'), angle_for(__env, macro, 'macro')]))
    return f"cxx1.XRefVia.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", XRefVia

  @staticmethod
  def angle_query_usingDeclaration(*, usingDeclaration: Optional["Cxx1UsingDeclaration"] = None) -> "Cxx1XRefVia":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_usingDirective(*, usingDirective: Optional["Cxx1UsingDirective"] = None) -> "Cxx1XRefVia":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_macro(*, macro: Optional["Pp1Use"] = None) -> "Cxx1XRefVia":
    raise Exception("this function can only be called from @angle_query")




class Cxx1DeclIdent(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, macro: ast.Expr, selector: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, macro, 'macro'), angle_for(__env, selector, 'selector')]))
    return f"cxx1.DeclIdent.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclIdent

  @staticmethod
  def angle_query_name(*, name: Optional["Cxx1Name"] = None) -> "Cxx1DeclIdent":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_macro(*, macro: Optional["Pp1Macro"] = None) -> "Cxx1DeclIdent":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_selector(*, selector: Optional["Cxx1ObjcSelector"] = None) -> "Cxx1DeclIdent":
    raise Exception("this function can only be called from @angle_query")




class Cxx1GlobalVariable(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], kind: ast.Expr, attribute: ast.Expr, definition: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, kind, 'kind'), angle_for(__env, attribute, 'attribute'), angle_for(__env, definition, 'definition')]))
    return f"cxx1.GlobalVariable.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", GlobalVariable

  @staticmethod
  def angle_query(*, kind: Optional["Cxx1GlobalVariableKind"] = None, attribute: Optional["Cxx1GlobalVariableAttribute"] = None, definition: Optional[bool] = None) -> "Cxx1GlobalVariable":
    raise Exception("this function can only be called from @angle_query")



class Cxx1GlobalVariableKind(Enum):
  SimpleVariable = 0
  StaticVariable = 1
  StaticMember = 2

class Cxx1Field(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], mutable_: ast.Expr, bitsize: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, mutable_, 'mutable_'), angle_for(__env, bitsize, 'bitsize')]))
    return f"cxx1.Field.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Field

  @staticmethod
  def angle_query(*, mutable_: Optional[bool] = None, bitsize: Optional[Union[Just[int], Just[None]]] = None) -> "Cxx1Field":
    raise Exception("this function can only be called from @angle_query")



class Cxx1LocalVariableKind(Enum):
  SimpleVariable = 0
  StaticVariable = 1
  Parameter = 2

class Cxx1PpEntity(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], define: ast.Expr, undef: ast.Expr, include_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, define, 'define'), angle_for(__env, undef, 'undef'), angle_for(__env, include_, 'include_')]))
    return f"cxx1.PpEntity.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PpEntity

  @staticmethod
  def angle_query_define(*, define: Optional["Pp1Define"] = None) -> "Cxx1PpEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_undef(*, undef: Optional["Pp1Undef"] = None) -> "Cxx1PpEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_include_(*, include_: Optional["SrcFile"] = None) -> "Cxx1PpEntity":
    raise Exception("this function can only be called from @angle_query")




class Cxx1LocalVariable(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], kind: ast.Expr, attribute: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, kind, 'kind'), angle_for(__env, attribute, 'attribute')]))
    return f"cxx1.LocalVariable.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", LocalVariable

  @staticmethod
  def angle_query(*, kind: Optional["Cxx1LocalVariableKind"] = None, attribute: Optional["Cxx1LocalVariableAttribute"] = None) -> "Cxx1LocalVariable":
    raise Exception("this function can only be called from @angle_query")



class Cxx1RecordBase(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], base: ast.Expr, access: ast.Expr, isVirtual: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, base, 'base'), angle_for(__env, access, 'access'), angle_for(__env, isVirtual, 'isVirtual')]))
    return f"cxx1.RecordBase.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", RecordBase

  @staticmethod
  def angle_query(*, base: Optional["Cxx1RecordDeclaration"] = None, access: Optional["Cxx1Access"] = None, isVirtual: Optional[bool] = None) -> "Cxx1RecordBase":
    raise Exception("this function can only be called from @angle_query")



class Cxx1XRefTarget(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, enumerator: ast.Expr, objcSelector: ast.Expr, unknown: ast.Expr, indirect: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, enumerator, 'enumerator'), angle_for(__env, objcSelector, 'objcSelector'), angle_for(__env, unknown, 'unknown'), angle_for(__env, indirect, 'indirect')]))
    return f"cxx1.XRefTarget.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", XRefTarget

  @staticmethod
  def angle_query_declaration(*, declaration: Optional["Cxx1Declaration"] = None) -> "Cxx1XRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_enumerator(*, enumerator: Optional["Cxx1Enumerator"] = None) -> "Cxx1XRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_objcSelector(*, objcSelector: Optional["Cxx1ObjcSelector"] = None) -> "Cxx1XRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_unknown(*, unknown: Optional["SrcLoc"] = None) -> "Cxx1XRefTarget":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_indirect(*, indirect: Optional["Cxx1XRefIndirectTarget"] = None) -> "Cxx1XRefTarget":
    raise Exception("this function can only be called from @angle_query")




class Cxx1MaybeIncludeTree(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], tree: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, tree, 'tree')]))
    return f"cxx1.MaybeIncludeTree.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", MaybeIncludeTree

  @staticmethod
  def angle_query(*, tree: Optional[Union[Just["Cxx1IncludeTree"], Just[None]]] = None) -> "Cxx1MaybeIncludeTree":
    raise Exception("this function can only be called from @angle_query")



class Cxx1VariableKind(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], global_: ast.Expr, local: ast.Expr, field: ast.Expr, ivar: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, global_, 'global_'), angle_for(__env, local, 'local'), angle_for(__env, field, 'field'), angle_for(__env, ivar, 'ivar')]))
    return f"cxx1.VariableKind.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", VariableKind

  @staticmethod
  def angle_query_global_(*, global_: Optional["Cxx1GlobalVariable"] = None) -> "Cxx1VariableKind":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_local(*, local: Optional["Cxx1LocalVariable"] = None) -> "Cxx1VariableKind":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_field(*, field: Optional["Cxx1Field"] = None) -> "Cxx1VariableKind":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_ivar(*, ivar: Optional["Cxx1ObjcIVar"] = None) -> "Cxx1VariableKind":
    raise Exception("this function can only be called from @angle_query")




class Cxx1DefinitionEntity(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], record_: ast.Expr, function_: ast.Expr, enum_: ast.Expr, objcMethod: ast.Expr, objcContainer: ast.Expr, variable: ast.Expr, namespace_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, record_, 'record_'), angle_for(__env, function_, 'function_'), angle_for(__env, enum_, 'enum_'), angle_for(__env, objcMethod, 'objcMethod'), angle_for(__env, objcContainer, 'objcContainer'), angle_for(__env, variable, 'variable'), angle_for(__env, namespace_, 'namespace_')]))
    return f"cxx1.DefinitionEntity.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DefinitionEntity

  @staticmethod
  def angle_query_record_(*, record_: Optional["Cxx1RecordDefinition"] = None) -> "Cxx1DefinitionEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_function_(*, function_: Optional["Cxx1FunctionDefinition"] = None) -> "Cxx1DefinitionEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_enum_(*, enum_: Optional["Cxx1EnumDefinition"] = None) -> "Cxx1DefinitionEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_objcMethod(*, objcMethod: Optional["Cxx1ObjcMethodDefinition"] = None) -> "Cxx1DefinitionEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_objcContainer(*, objcContainer: Optional["Cxx1ObjcContainerDefinition"] = None) -> "Cxx1DefinitionEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_variable(*, variable: Optional["Cxx1VariableDeclaration"] = None) -> "Cxx1DefinitionEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_namespace_(*, namespace_: Optional["Cxx1NamespaceDefinition"] = None) -> "Cxx1DefinitionEntity":
    raise Exception("this function can only be called from @angle_query")




class Cxx1FixedXRef(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], target: ast.Expr, ranges: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, target, 'target'), angle_for(__env, ranges, 'ranges')]))
    return f"cxx1.FixedXRef.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FixedXRef

  @staticmethod
  def angle_query(*, target: Optional["Cxx1XRefTarget"] = None, ranges: Optional["SrcByteSpans"] = None) -> "Cxx1FixedXRef":
    raise Exception("this function can only be called from @angle_query")



class Cxx1LocalVariableAttribute(Enum):
  Plain = 0
  Constexpr = 1

class Cxx1PPEvent(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], include_: ast.Expr, define: ast.Expr, undef: ast.Expr, use: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, include_, 'include_'), angle_for(__env, define, 'define'), angle_for(__env, undef, 'undef'), angle_for(__env, use, 'use')]))
    return f"cxx1.PPEvent.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", PPEvent

  @staticmethod
  def angle_query_include_(*, include_: Optional["Cxx1IncludeTrace"] = None) -> "Cxx1PPEvent":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_define(*, define: Optional["Pp1Define"] = None) -> "Cxx1PPEvent":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_undef(*, undef: Optional["Pp1Undef"] = None) -> "Cxx1PPEvent":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_use(*, use: Optional["Pp1Use"] = None) -> "Cxx1PPEvent":
    raise Exception("this function can only be called from @angle_query")




class Cxx1Access(Enum):
  Public = 0
  Protected = 1
  Private = 2

class Cxx1RecordKind(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], struct_: ast.Expr, class_: ast.Expr, union_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, struct_, 'struct_'), angle_for(__env, class_, 'class_'), angle_for(__env, union_, 'union_')]))
    return f"cxx1.RecordKind.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", RecordKind

  @staticmethod
  def angle_query_struct_(*, struct_: Optional["BuiltinUnit"] = None) -> "Cxx1RecordKind":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_class_(*, class_: Optional["BuiltinUnit"] = None) -> "Cxx1RecordKind":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_union_(*, union_: Optional["BuiltinUnit"] = None) -> "Cxx1RecordKind":
    raise Exception("this function can only be called from @angle_query")




class Cxx1IncludeTrace(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], include_: ast.Expr, trace: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, include_, 'include_'), angle_for(__env, trace, 'trace')]))
    return f"cxx1.IncludeTrace.5 { ('{ ' + query_fields + ' }') if query_fields else '_' }", IncludeTrace

  @staticmethod
  def angle_query(*, include_: Optional["Pp1Include"] = None, trace: Optional[Union[Just["Cxx1Trace"], Just[None]]] = None) -> "Cxx1IncludeTrace":
    raise Exception("this function can only be called from @angle_query")





Cxx1Operator = str

Cxx1LiteralOperator = str

Cxx1USR = str
