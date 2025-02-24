# @generated
# To regenerate this file run fbcode//glean/schema/gen/sync
from typing import Optional, Tuple, Union, List, Dict, TypeVar
from thrift.py3 import Struct
from enum import Enum
import ast
from glean.schema.py.glean_schema_predicate import GleanSchemaPredicate , Just, InnerGleanSchemaPredicate
from glean.client.py3.angle_query import angle_for, R
from glean.schema.py.src import *


from glean.schema.flow.types import (
    FlowTypeEntityImportUses,
    TypeExport,
    ImportDeclaration,
    DeclarationLocation,
    DeclarationInfo,
    FileDeclaration,
    ModuleTypeExport,
    LocalDeclarationReference,
    FlowTypeImportXRef,
    Name,
    SearchByModule,
    Range,
    Declaration,
    DeclarationUses,
    SourceOfTypeExport,
    FlowCompatibleExport,
    FlowEntityUsesAll,
    NameLowerCase,
    SearchByFileModule,
    Module,
    FlowSameModule,
    FlowModuleNamespaceXRef,
    Documentation,
    SearchByName,
    StringToFileModule,
    FlowExportLocation,
    FlowXRefDeclInfo,
    SearchTypeByModuleExport,
    FlowEntityImportUses,
    Export,
    TypeImportDeclaration,
    FlowImportXRef,
    ModuleExport,
    MemberDeclarationInfo,
    TypeDeclarationInfo,
    FileXRef,
    SourceOfExport,
    MemberDeclaration,
    Type,
    FileOfStringModule,
    TypeDeclaration,
    DeclarationNameSpan,
    MemberDeclarationReference,
    FlowTypeExportLocation,
    TypeDeclarationReference,
    SomeDeclaration,
    SomeEntity,
    XRef,
)


class FlowFlowTypeEntityImportUses(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], target: ast.Expr, local: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, target, 'target'), angle_for(__env, local, 'local')]))
    return f"flow.FlowTypeEntityImportUses.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowTypeEntityImportUses

  @staticmethod
  def angle_query(*, target: Optional["FlowSomeEntity"] = None, local: Optional["FlowTypeDeclaration"] = None) -> "FlowFlowTypeEntityImportUses":
    raise Exception("this function can only be called from @angle_query")



class FlowTypeExport(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], named: ast.Expr, star: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, named, 'named'), angle_for(__env, star, 'star')]))
    return f"flow.TypeExport.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TypeExport

  @staticmethod
  def angle_query_named(*, named: Optional["FlowName"] = None) -> "FlowTypeExport":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_star(*, star: Optional["FlowModule"] = None) -> "FlowTypeExport":
    raise Exception("this function can only be called from @angle_query")




class FlowImportDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, import_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, import_, 'import_')]))
    return f"flow.ImportDeclaration.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ImportDeclaration

  @staticmethod
  def angle_query(*, declaration: Optional["FlowDeclaration"] = None, import_: Optional['FlowImportDeclaration_import_'] = None) -> "FlowImportDeclaration":
    raise Exception("this function can only be called from @angle_query")

class FlowImportDeclaration_import_(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], moduleExport: ast.Expr, moduleNamespace: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, moduleExport, 'moduleExport'), angle_for(__env, moduleNamespace, 'moduleNamespace')]))
    return f" { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowImportDeclaration_import_

  @staticmethod
  def angle_query_moduleExport(*, moduleExport: Optional["FlowModuleExport"] = None) -> "FlowImportDeclaration_import_":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_moduleNamespace(*, moduleNamespace: Optional["FlowModule"] = None) -> "FlowImportDeclaration_import_":
    raise Exception("this function can only be called from @angle_query")






class FlowDeclarationLocation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, file: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, file, 'file'), angle_for(__env, span, 'span')]))
    return f"flow.DeclarationLocation.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationLocation

  @staticmethod
  def angle_query(*, decl: Optional["FlowSomeDeclaration"] = None, file: Optional["SrcFile"] = None, span: Optional["SrcByteSpan"] = None) -> "FlowDeclarationLocation":
    raise Exception("this function can only be called from @angle_query")



class FlowDeclarationInfo(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, type: ast.Expr, documentation: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, type, 'type'), angle_for(__env, documentation, 'documentation')]))
    return f"flow.DeclarationInfo.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationInfo

  @staticmethod
  def angle_query(*, declaration: Optional["FlowDeclaration"] = None, type: Optional["FlowType"] = None, documentation: Optional[Union[Just["FlowDocumentation"], Just[None]]] = None) -> "FlowDeclarationInfo":
    raise Exception("this function can only be called from @angle_query")



class FlowFileDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, declaration: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, declaration, 'declaration')]))
    return f"flow.FileDeclaration.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FileDeclaration

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, declaration: Optional["FlowSomeDeclaration"] = None) -> "FlowFileDeclaration":
    raise Exception("this function can only be called from @angle_query")



class FlowModuleTypeExport(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], module: ast.Expr, typeExport: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, module, 'module'), angle_for(__env, typeExport, 'typeExport')]))
    return f"flow.ModuleTypeExport.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ModuleTypeExport

  @staticmethod
  def angle_query(*, module: Optional["FlowModule"] = None, typeExport: Optional["FlowTypeExport"] = None) -> "FlowModuleTypeExport":
    raise Exception("this function can only be called from @angle_query")



class FlowLocalDeclarationReference(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, loc: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, loc, 'loc')]))
    return f"flow.LocalDeclarationReference.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", LocalDeclarationReference

  @staticmethod
  def angle_query(*, declaration: Optional["FlowDeclaration"] = None, loc: Optional["FlowRange"] = None) -> "FlowLocalDeclarationReference":
    raise Exception("this function can only be called from @angle_query")



class FlowFlowTypeImportXRef(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], local: ast.Expr, entity: ast.Expr, targetFile: ast.Expr, targetSpan: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, local, 'local'), angle_for(__env, entity, 'entity'), angle_for(__env, targetFile, 'targetFile'), angle_for(__env, targetSpan, 'targetSpan')]))
    return f"flow.FlowTypeImportXRef.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowTypeImportXRef

  @staticmethod
  def angle_query(*, local: Optional["FlowTypeDeclaration"] = None, entity: Optional["FlowSomeEntity"] = None, targetFile: Optional["SrcFile"] = None, targetSpan: Optional["SrcByteSpan"] = None) -> "FlowFlowTypeImportXRef":
    raise Exception("this function can only be called from @angle_query")



class FlowName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"flow.Name.3 { query_fields if query_fields else '_' }", Name

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "FlowName":
    raise Exception("this function can only be called from @angle_query")



class FlowSearchByModule(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], string_: ast.Expr, name: ast.Expr, decl: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, string_, 'string_'), angle_for(__env, name, 'name'), angle_for(__env, decl, 'decl')]))
    return f"flow.SearchByModule.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", SearchByModule

  @staticmethod
  def angle_query(*, string_: Optional[str] = None, name: Optional["FlowName"] = None, decl: Optional["FlowSomeDeclaration"] = None) -> "FlowSearchByModule":
    raise Exception("this function can only be called from @angle_query")



class FlowRange(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], module: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, module, 'module'), angle_for(__env, span, 'span')]))
    return f"flow.Range.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Range

  @staticmethod
  def angle_query(*, module: Optional["FlowModule"] = None, span: Optional["SrcByteSpan"] = None) -> "FlowRange":
    raise Exception("this function can only be called from @angle_query")



class FlowDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, loc: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, loc, 'loc')]))
    return f"flow.Declaration.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Declaration

  @staticmethod
  def angle_query(*, name: Optional["FlowName"] = None, loc: Optional["FlowRange"] = None) -> "FlowDeclaration":
    raise Exception("this function can only be called from @angle_query")



class FlowDeclarationUses(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], target: ast.Expr, file: ast.Expr, use: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, target, 'target'), angle_for(__env, file, 'file'), angle_for(__env, use, 'use')]))
    return f"flow.DeclarationUses.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationUses

  @staticmethod
  def angle_query(*, target: Optional["FlowSomeDeclaration"] = None, file: Optional["SrcFile"] = None, use: Optional["SrcByteSpan"] = None) -> "FlowDeclarationUses":
    raise Exception("this function can only be called from @angle_query")



class FlowSourceOfTypeExport(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], moduleTypeExport: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, moduleTypeExport, 'moduleTypeExport'), angle_for(__env, source, 'source')]))
    return f"flow.SourceOfTypeExport.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", SourceOfTypeExport

  @staticmethod
  def angle_query(*, moduleTypeExport: Optional["FlowModuleTypeExport"] = None, source: Optional['FlowSourceOfTypeExport_source'] = None) -> "FlowSourceOfTypeExport":
    raise Exception("this function can only be called from @angle_query")

class FlowSourceOfTypeExport_source(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], typeDeclaration: ast.Expr, moduleTypeExport: ast.Expr, moduleNamespace: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, typeDeclaration, 'typeDeclaration'), angle_for(__env, moduleTypeExport, 'moduleTypeExport'), angle_for(__env, moduleNamespace, 'moduleNamespace')]))
    return f" { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowSourceOfTypeExport_source

  @staticmethod
  def angle_query_typeDeclaration(*, typeDeclaration: Optional["FlowTypeDeclaration"] = None) -> "FlowSourceOfTypeExport_source":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_moduleTypeExport(*, moduleTypeExport: Optional["FlowModuleTypeExport"] = None) -> "FlowSourceOfTypeExport_source":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_moduleNamespace(*, moduleNamespace: Optional["FlowModule"] = None) -> "FlowSourceOfTypeExport_source":
    raise Exception("this function can only be called from @angle_query")






class FlowFlowCompatibleExport(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], left: ast.Expr, right: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, left, 'left'), angle_for(__env, right, 'right')]))
    return f"flow.FlowCompatibleExport.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowCompatibleExport

  @staticmethod
  def angle_query(*, left: Optional["FlowExport"] = None, right: Optional["FlowExport"] = None) -> "FlowFlowCompatibleExport":
    raise Exception("this function can only be called from @angle_query")



class FlowFlowEntityUsesAll(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], target: ast.Expr, file: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, target, 'target'), angle_for(__env, file, 'file'), angle_for(__env, span, 'span')]))
    return f"flow.FlowEntityUsesAll.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowEntityUsesAll

  @staticmethod
  def angle_query(*, target: Optional["FlowSomeEntity"] = None, file: Optional["SrcFile"] = None, span: Optional["SrcByteSpan"] = None) -> "FlowFlowEntityUsesAll":
    raise Exception("this function can only be called from @angle_query")



class FlowNameLowerCase(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], nameLowerCase: ast.Expr, name: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, nameLowerCase, 'nameLowerCase'), angle_for(__env, name, 'name')]))
    return f"flow.NameLowerCase.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", NameLowerCase

  @staticmethod
  def angle_query(*, nameLowerCase: Optional[str] = None, name: Optional["FlowName"] = None) -> "FlowNameLowerCase":
    raise Exception("this function can only be called from @angle_query")



class FlowSearchByFileModule(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, name: ast.Expr, decl: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, name, 'name'), angle_for(__env, decl, 'decl')]))
    return f"flow.SearchByFileModule.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", SearchByFileModule

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, name: Optional["FlowName"] = None, decl: Optional["FlowSomeDeclaration"] = None) -> "FlowSearchByFileModule":
    raise Exception("this function can only be called from @angle_query")



class FlowModule(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, builtin: ast.Expr, lib: ast.Expr, noSource: ast.Expr, string_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, builtin, 'builtin'), angle_for(__env, lib, 'lib'), angle_for(__env, noSource, 'noSource'), angle_for(__env, string_, 'string_')]))
    return f"flow.Module.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Module

  @staticmethod
  def angle_query_file(*, file: Optional["SrcFile"] = None) -> "FlowModule":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_builtin(*, builtin: Optional['FlowModule_builtin'] = None) -> "FlowModule":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_lib(*, lib: Optional[str] = None) -> "FlowModule":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_noSource(*, noSource: Optional['FlowModule_noSource'] = None) -> "FlowModule":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_string_(*, string_: Optional[str] = None) -> "FlowModule":
    raise Exception("this function can only be called from @angle_query")


FlowModule_builtin = Tuple[()]

FlowModule_noSource = Tuple[()]



class FlowFlowSameModule(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], left: ast.Expr, right: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, left, 'left'), angle_for(__env, right, 'right')]))
    return f"flow.FlowSameModule.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowSameModule

  @staticmethod
  def angle_query(*, left: Optional["FlowModule"] = None, right: Optional["FlowModule"] = None) -> "FlowFlowSameModule":
    raise Exception("this function can only be called from @angle_query")



class FlowFlowModuleNamespaceXRef(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], local: ast.Expr, entity: ast.Expr, file: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, local, 'local'), angle_for(__env, entity, 'entity'), angle_for(__env, file, 'file')]))
    return f"flow.FlowModuleNamespaceXRef.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowModuleNamespaceXRef

  @staticmethod
  def angle_query(*, local: Optional["FlowDeclaration"] = None, entity: Optional["FlowSomeEntity"] = None, file: Optional["SrcFile"] = None) -> "FlowFlowModuleNamespaceXRef":
    raise Exception("this function can only be called from @angle_query")



class FlowDocumentation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"flow.Documentation.3 { query_fields if query_fields else '_' }", Documentation

  @staticmethod
  def angle_query(*, arg: Optional["FlowRange"] = None) -> "FlowDocumentation":
    raise Exception("this function can only be called from @angle_query")



class FlowSearchByName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, decl: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, decl, 'decl')]))
    return f"flow.SearchByName.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", SearchByName

  @staticmethod
  def angle_query(*, name: Optional["FlowName"] = None, decl: Optional["FlowSomeDeclaration"] = None) -> "FlowSearchByName":
    raise Exception("this function can only be called from @angle_query")



class FlowStringToFileModule(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], string_: ast.Expr, file: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, string_, 'string_'), angle_for(__env, file, 'file')]))
    return f"flow.StringToFileModule.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", StringToFileModule

  @staticmethod
  def angle_query(*, string_: Optional[str] = None, file: Optional["SrcFile"] = None) -> "FlowStringToFileModule":
    raise Exception("this function can only be called from @angle_query")



class FlowFlowExportLocation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], module: ast.Expr, export_: ast.Expr, entity: ast.Expr, file: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, module, 'module'), angle_for(__env, export_, 'export_'), angle_for(__env, entity, 'entity'), angle_for(__env, file, 'file'), angle_for(__env, span, 'span')]))
    return f"flow.FlowExportLocation.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowExportLocation

  @staticmethod
  def angle_query(*, module: Optional["FlowModule"] = None, export_: Optional["FlowExport"] = None, entity: Optional["FlowSomeEntity"] = None, file: Optional["SrcFile"] = None, span: Optional["SrcByteSpan"] = None) -> "FlowFlowExportLocation":
    raise Exception("this function can only be called from @angle_query")



class FlowFlowXRefDeclInfo(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], ref: ast.Expr, srcLoc: ast.Expr, name: ast.Expr, targetLoc: ast.Expr, entity: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, ref, 'ref'), angle_for(__env, srcLoc, 'srcLoc'), angle_for(__env, name, 'name'), angle_for(__env, targetLoc, 'targetLoc'), angle_for(__env, entity, 'entity')]))
    return f"flow.FlowXRefDeclInfo.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowXRefDeclInfo

  @staticmethod
  def angle_query(*, ref: Optional["FlowXRef"] = None, srcLoc: Optional["FlowRange"] = None, name: Optional["FlowName"] = None, targetLoc: Optional["FlowRange"] = None, entity: Optional["FlowSomeDeclaration"] = None) -> "FlowFlowXRefDeclInfo":
    raise Exception("this function can only be called from @angle_query")



class FlowSearchTypeByModuleExport(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], string_: ast.Expr, name: ast.Expr, decl: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, string_, 'string_'), angle_for(__env, name, 'name'), angle_for(__env, decl, 'decl')]))
    return f"flow.SearchTypeByModuleExport.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", SearchTypeByModuleExport

  @staticmethod
  def angle_query(*, string_: Optional[str] = None, name: Optional["FlowName"] = None, decl: Optional["FlowSomeDeclaration"] = None) -> "FlowSearchTypeByModuleExport":
    raise Exception("this function can only be called from @angle_query")



class FlowFlowEntityImportUses(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], target: ast.Expr, local: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, target, 'target'), angle_for(__env, local, 'local')]))
    return f"flow.FlowEntityImportUses.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowEntityImportUses

  @staticmethod
  def angle_query(*, target: Optional["FlowSomeEntity"] = None, local: Optional["FlowDeclaration"] = None) -> "FlowFlowEntityImportUses":
    raise Exception("this function can only be called from @angle_query")



class FlowExport(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], commonJS: ast.Expr, commonJSMember: ast.Expr, named: ast.Expr, default_: ast.Expr, star: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, commonJS, 'commonJS'), angle_for(__env, commonJSMember, 'commonJSMember'), angle_for(__env, named, 'named'), angle_for(__env, default_, 'default_'), angle_for(__env, star, 'star')]))
    return f"flow.Export.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", Export

  @staticmethod
  def angle_query_commonJS(*, commonJS: Optional['FlowExport_commonJS'] = None) -> "FlowExport":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_commonJSMember(*, commonJSMember: Optional["FlowName"] = None) -> "FlowExport":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_named(*, named: Optional["FlowName"] = None) -> "FlowExport":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_default_(*, default_: Optional['FlowExport_default_'] = None) -> "FlowExport":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_star(*, star: Optional["FlowModule"] = None) -> "FlowExport":
    raise Exception("this function can only be called from @angle_query")


FlowExport_commonJS = Tuple[()]

FlowExport_default_ = Tuple[()]



class FlowTypeImportDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], typeDeclaration: ast.Expr, import_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, typeDeclaration, 'typeDeclaration'), angle_for(__env, import_, 'import_')]))
    return f"flow.TypeImportDeclaration.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TypeImportDeclaration

  @staticmethod
  def angle_query(*, typeDeclaration: Optional["FlowTypeDeclaration"] = None, import_: Optional['FlowTypeImportDeclaration_import_'] = None) -> "FlowTypeImportDeclaration":
    raise Exception("this function can only be called from @angle_query")

class FlowTypeImportDeclaration_import_(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], type: ast.Expr, typeof_: ast.Expr, moduleTypeof: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, type, 'type'), angle_for(__env, typeof_, 'typeof_'), angle_for(__env, moduleTypeof, 'moduleTypeof')]))
    return f" { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowTypeImportDeclaration_import_

  @staticmethod
  def angle_query_type(*, type: Optional["FlowModuleTypeExport"] = None) -> "FlowTypeImportDeclaration_import_":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_typeof_(*, typeof_: Optional["FlowModuleExport"] = None) -> "FlowTypeImportDeclaration_import_":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_moduleTypeof(*, moduleTypeof: Optional["FlowModule"] = None) -> "FlowTypeImportDeclaration_import_":
    raise Exception("this function can only be called from @angle_query")






class FlowFlowImportXRef(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], local: ast.Expr, entity: ast.Expr, targetFile: ast.Expr, targetSpan: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, local, 'local'), angle_for(__env, entity, 'entity'), angle_for(__env, targetFile, 'targetFile'), angle_for(__env, targetSpan, 'targetSpan')]))
    return f"flow.FlowImportXRef.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowImportXRef

  @staticmethod
  def angle_query(*, local: Optional["FlowDeclaration"] = None, entity: Optional["FlowSomeEntity"] = None, targetFile: Optional["SrcFile"] = None, targetSpan: Optional["SrcByteSpan"] = None) -> "FlowFlowImportXRef":
    raise Exception("this function can only be called from @angle_query")



class FlowModuleExport(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], module: ast.Expr, export_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, module, 'module'), angle_for(__env, export_, 'export_')]))
    return f"flow.ModuleExport.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", ModuleExport

  @staticmethod
  def angle_query(*, module: Optional["FlowModule"] = None, export_: Optional["FlowExport"] = None) -> "FlowModuleExport":
    raise Exception("this function can only be called from @angle_query")



class FlowMemberDeclarationInfo(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], memberDeclaration: ast.Expr, type: ast.Expr, documentation: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, memberDeclaration, 'memberDeclaration'), angle_for(__env, type, 'type'), angle_for(__env, documentation, 'documentation')]))
    return f"flow.MemberDeclarationInfo.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", MemberDeclarationInfo

  @staticmethod
  def angle_query(*, memberDeclaration: Optional["FlowMemberDeclaration"] = None, type: Optional["FlowType"] = None, documentation: Optional[Union[Just["FlowDocumentation"], Just[None]]] = None) -> "FlowMemberDeclarationInfo":
    raise Exception("this function can only be called from @angle_query")



class FlowTypeDeclarationInfo(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], typeDeclaration: ast.Expr, type: ast.Expr, documentation: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, typeDeclaration, 'typeDeclaration'), angle_for(__env, type, 'type'), angle_for(__env, documentation, 'documentation')]))
    return f"flow.TypeDeclarationInfo.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TypeDeclarationInfo

  @staticmethod
  def angle_query(*, typeDeclaration: Optional["FlowTypeDeclaration"] = None, type: Optional["FlowType"] = None, documentation: Optional[Union[Just["FlowDocumentation"], Just[None]]] = None) -> "FlowTypeDeclarationInfo":
    raise Exception("this function can only be called from @angle_query")



class FlowFileXRef(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, ref: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, ref, 'ref')]))
    return f"flow.FileXRef.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FileXRef

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, ref: Optional["FlowXRef"] = None) -> "FlowFileXRef":
    raise Exception("this function can only be called from @angle_query")



class FlowSourceOfExport(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], moduleExport: ast.Expr, source: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, moduleExport, 'moduleExport'), angle_for(__env, source, 'source')]))
    return f"flow.SourceOfExport.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", SourceOfExport

  @staticmethod
  def angle_query(*, moduleExport: Optional["FlowModuleExport"] = None, source: Optional['FlowSourceOfExport_source'] = None) -> "FlowSourceOfExport":
    raise Exception("this function can only be called from @angle_query")

class FlowSourceOfExport_source(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], declaration: ast.Expr, memberDeclaration: ast.Expr, moduleExport: ast.Expr, moduleNamespace: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, declaration, 'declaration'), angle_for(__env, memberDeclaration, 'memberDeclaration'), angle_for(__env, moduleExport, 'moduleExport'), angle_for(__env, moduleNamespace, 'moduleNamespace')]))
    return f" { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowSourceOfExport_source

  @staticmethod
  def angle_query_declaration(*, declaration: Optional["FlowDeclaration"] = None) -> "FlowSourceOfExport_source":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_memberDeclaration(*, memberDeclaration: Optional["FlowMemberDeclaration"] = None) -> "FlowSourceOfExport_source":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_moduleExport(*, moduleExport: Optional["FlowModuleExport"] = None) -> "FlowSourceOfExport_source":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_moduleNamespace(*, moduleNamespace: Optional["FlowModule"] = None) -> "FlowSourceOfExport_source":
    raise Exception("this function can only be called from @angle_query")






class FlowMemberDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, loc: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, loc, 'loc')]))
    return f"flow.MemberDeclaration.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", MemberDeclaration

  @staticmethod
  def angle_query(*, name: Optional["FlowName"] = None, loc: Optional["FlowRange"] = None) -> "FlowMemberDeclaration":
    raise Exception("this function can only be called from @angle_query")



class FlowType(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], arg: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  angle_for(__env, arg, None)
    return f"flow.Type.3 { query_fields if query_fields else '_' }", Type

  @staticmethod
  def angle_query(*, arg: Optional[str] = None) -> "FlowType":
    raise Exception("this function can only be called from @angle_query")



class FlowFileOfStringModule(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], file: ast.Expr, string_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, file, 'file'), angle_for(__env, string_, 'string_')]))
    return f"flow.FileOfStringModule.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FileOfStringModule

  @staticmethod
  def angle_query(*, file: Optional["SrcFile"] = None, string_: Optional[str] = None) -> "FlowFileOfStringModule":
    raise Exception("this function can only be called from @angle_query")



class FlowTypeDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], name: ast.Expr, loc: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, name, 'name'), angle_for(__env, loc, 'loc')]))
    return f"flow.TypeDeclaration.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TypeDeclaration

  @staticmethod
  def angle_query(*, name: Optional["FlowName"] = None, loc: Optional["FlowRange"] = None) -> "FlowTypeDeclaration":
    raise Exception("this function can only be called from @angle_query")



class FlowDeclarationNameSpan(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, name: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, name, 'name'), angle_for(__env, span, 'span')]))
    return f"flow.DeclarationNameSpan.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", DeclarationNameSpan

  @staticmethod
  def angle_query(*, decl: Optional["FlowSomeDeclaration"] = None, name: Optional["FlowName"] = None, span: Optional["SrcByteSpan"] = None) -> "FlowDeclarationNameSpan":
    raise Exception("this function can only be called from @angle_query")



class FlowMemberDeclarationReference(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], memberDeclaration: ast.Expr, loc: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, memberDeclaration, 'memberDeclaration'), angle_for(__env, loc, 'loc')]))
    return f"flow.MemberDeclarationReference.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", MemberDeclarationReference

  @staticmethod
  def angle_query(*, memberDeclaration: Optional["FlowMemberDeclaration"] = None, loc: Optional["FlowRange"] = None) -> "FlowMemberDeclarationReference":
    raise Exception("this function can only be called from @angle_query")



class FlowFlowTypeExportLocation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], moduleTypeExport: ast.Expr, entity: ast.Expr, file: ast.Expr, span: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, moduleTypeExport, 'moduleTypeExport'), angle_for(__env, entity, 'entity'), angle_for(__env, file, 'file'), angle_for(__env, span, 'span')]))
    return f"flow.FlowTypeExportLocation.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", FlowTypeExportLocation

  @staticmethod
  def angle_query(*, moduleTypeExport: Optional["FlowModuleTypeExport"] = None, entity: Optional["FlowSomeEntity"] = None, file: Optional["SrcFile"] = None, span: Optional["SrcByteSpan"] = None) -> "FlowFlowTypeExportLocation":
    raise Exception("this function can only be called from @angle_query")



class FlowTypeDeclarationReference(GleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], typeDeclaration: ast.Expr, loc: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, typeDeclaration, 'typeDeclaration'), angle_for(__env, loc, 'loc')]))
    return f"flow.TypeDeclarationReference.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", TypeDeclarationReference

  @staticmethod
  def angle_query(*, typeDeclaration: Optional["FlowTypeDeclaration"] = None, loc: Optional["FlowRange"] = None) -> "FlowTypeDeclarationReference":
    raise Exception("this function can only be called from @angle_query")





class FlowSomeDeclaration(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], localDecl: ast.Expr, memberDecl: ast.Expr, typeDecl: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, localDecl, 'localDecl'), angle_for(__env, memberDecl, 'memberDecl'), angle_for(__env, typeDecl, 'typeDecl')]))
    return f"flow.SomeDeclaration.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", SomeDeclaration

  @staticmethod
  def angle_query_localDecl(*, localDecl: Optional["FlowDeclaration"] = None) -> "FlowSomeDeclaration":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_memberDecl(*, memberDecl: Optional["FlowMemberDeclaration"] = None) -> "FlowSomeDeclaration":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_typeDecl(*, typeDecl: Optional["FlowTypeDeclaration"] = None) -> "FlowSomeDeclaration":
    raise Exception("this function can only be called from @angle_query")




class FlowSomeEntity(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], decl: ast.Expr, module_: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, decl, 'decl'), angle_for(__env, module_, 'module_')]))
    return f"flow.SomeEntity.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", SomeEntity

  @staticmethod
  def angle_query_decl(*, decl: Optional["FlowSomeDeclaration"] = None) -> "FlowSomeEntity":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_module_(*, module_: Optional["FlowModule"] = None) -> "FlowSomeEntity":
    raise Exception("this function can only be called from @angle_query")




class FlowXRef(InnerGleanSchemaPredicate):
  @staticmethod
  def build_angle(__env: Dict[str, R], localRef: ast.Expr, memberRef: ast.Expr, typeRef: ast.Expr) -> Tuple[str, Struct]:
    query_fields =  ', '.join(filter(lambda x: x != '', [angle_for(__env, localRef, 'localRef'), angle_for(__env, memberRef, 'memberRef'), angle_for(__env, typeRef, 'typeRef')]))
    return f"flow.XRef.3 { ('{ ' + query_fields + ' }') if query_fields else '_' }", XRef

  @staticmethod
  def angle_query_localRef(*, localRef: Optional["FlowLocalDeclarationReference"] = None) -> "FlowXRef":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_memberRef(*, memberRef: Optional["FlowMemberDeclarationReference"] = None) -> "FlowXRef":
    raise Exception("this function can only be called from @angle_query")

  @staticmethod
  def angle_query_typeRef(*, typeRef: Optional["FlowTypeDeclarationReference"] = None) -> "FlowXRef":
    raise Exception("this function can only be called from @angle_query")





