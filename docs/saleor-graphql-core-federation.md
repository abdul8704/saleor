## Purpose

`saleor/graphql/core/federation` (`saleor/graphql/core/federation`) groups 7 source file(s) exposing 18 top-level declaration(s).

## Public surface

**`saleor/graphql/core/federation/entities.py`**

- `federated_entity` (function) — [saleor/graphql/core/federation/entities.py:11]
- `federate_entity` (function) — [saleor/graphql/core/federation/entities.py:12]

**`saleor/graphql/core/federation/resolvers.py`**

- `resolve_id_or_error` (function) — [saleor/graphql/core/federation/resolvers.py:10]
- `resolve_federation_references` (function) — [saleor/graphql/core/federation/resolvers.py:30]

**`saleor/graphql/core/federation/schema.py`**

- `serialize` (function) — [saleor/graphql/core/federation/schema.py:27]
- `parse_literal` (function) — [saleor/graphql/core/federation/schema.py:31]
- `parse_value` (function) — [saleor/graphql/core/federation/schema.py:35]
- `Meta` (class) — [saleor/graphql/core/federation/schema.py:42]
- `build_federated_schema` (function) — [saleor/graphql/core/federation/schema.py:52]
- `create_entity_type_resolver` (function) — [saleor/graphql/core/federation/schema.py:89]
- `resolve_entity_type` (function) — [saleor/graphql/core/federation/schema.py:92]
- `resolve_entities` (function) — [saleor/graphql/core/federation/schema.py:111]
- `create_service_sdl_resolver` (function) — [saleor/graphql/core/federation/schema.py:167]
- `resolve_service_sdl` (function) — [saleor/graphql/core/federation/schema.py:199]

**`saleor/graphql/core/federation/tests/test_resolvers.py`**

- `test_resolve_federation_references` (function) — [saleor/graphql/core/federation/tests/test_resolvers.py:57]

**`saleor/graphql/core/federation/tests/test_schema.py`**

- `test_resolve_entities_handles_errors_invalid_input` (function) — [saleor/graphql/core/federation/tests/test_schema.py:99]
- `test_resolve_entities_can_only_provide_fields` (function) — [saleor/graphql/core/federation/tests/test_schema.py:117]
- `test_resolve_entity_should_return_object_when_found` (function) — [saleor/graphql/core/federation/tests/test_schema.py:140]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/core/federation/__init__.py` (4 lines)
- `saleor/graphql/core/federation/entities.py` (29 lines)
- `saleor/graphql/core/federation/resolvers.py` (35 lines)
- `saleor/graphql/core/federation/schema.py` (202 lines)
- `saleor/graphql/core/federation/tests/__init__.py` (1 lines)
- `saleor/graphql/core/federation/tests/test_resolvers.py` (70 lines)
- `saleor/graphql/core/federation/tests/test_schema.py` (159 lines)

## Interactions

- Imports from: `saleor/graphql`, `saleor/graphql/product/types`, `saleor/graphql/core`, `saleor/graphql/order`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...ResolveInfo`
- `...schema_printer.print_schema`
- `..context.BaseContext`
- `..utils.from_global_id_or_error`
- `.entities.federated_entities`
- `.entities.federated_entity`
- `.resolvers.resolve_federation_references`
- `saleor.graphql.order.types.Order`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `e9b2c9202185` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
