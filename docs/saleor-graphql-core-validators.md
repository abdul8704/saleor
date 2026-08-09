## Purpose

`saleor/graphql/core/validators` (`saleor/graphql/core/validators`) groups 8 source file(s) exposing 45 top-level declaration(s).

## Public surface

**`saleor/graphql/core/validators/__init__.py`**

- `validate_query` (function) — [saleor/graphql/core/validators/__init__.py:26]
- `validate_one_of_args_is_in_mutation` (function) — [saleor/graphql/core/validators/__init__.py:52]
- `validate_one_of_args_is_in_query` (function) — [saleor/graphql/core/validators/__init__.py:59]
- `validate_price_precision` (function) — [saleor/graphql/core/validators/__init__.py:90]
- `validate_decimal_max_value` (function) — [saleor/graphql/core/validators/__init__.py:120]
- `get_not_available_variants_in_channel` (function) — [saleor/graphql/core/validators/__init__.py:130]
- `validate_variants_available_in_channel` (function) — [saleor/graphql/core/validators/__init__.py:152]
- `validate_end_is_after_start` (function) — [saleor/graphql/core/validators/__init__.py:177]
- `validate_slug_and_generate_if_needed` (function) — [saleor/graphql/core/validators/__init__.py:188]
- `validate_slug_value` (function) — [saleor/graphql/core/validators/__init__.py:210]
- `clean_seo_fields` (function) — [saleor/graphql/core/validators/__init__.py:219]
- `validate_required_string_field` (function) — [saleor/graphql/core/validators/__init__.py:231]
- `validate_if_int_or_uuid` (function) — [saleor/graphql/core/validators/__init__.py:242]
- `validate_limit_of_list_input` (function) — [saleor/graphql/core/validators/__init__.py:252]

**`saleor/graphql/core/validators/alias_count_limit_rule.py`**

- `AliasCountLimitRule` (class) — [saleor/graphql/core/validators/alias_count_limit_rule.py:15]
- `enter_Field` (function) — [saleor/graphql/core/validators/alias_count_limit_rule.py:23]
- `leave_Document` (function) — [saleor/graphql/core/validators/alias_count_limit_rule.py:27]

**`saleor/graphql/core/validators/file.py`**

- `validate_upload_file` (function) — [saleor/graphql/core/validators/file.py:19]
- `detect_mime_type` (function) — [saleor/graphql/core/validators/file.py:82]
- `is_supported_image_mimetype` (function) — [saleor/graphql/core/validators/file.py:90]
- `clean_image_file` (function) — [saleor/graphql/core/validators/file.py:97]

**`saleor/graphql/core/validators/mutation_count_limit_rule.py`**

- `MutationCountLimitRule` (class) — [saleor/graphql/core/validators/mutation_count_limit_rule.py:15]
- `enter_OperationDefinition` (function) — [saleor/graphql/core/validators/mutation_count_limit_rule.py:23]
- `leave_Document` (function) — [saleor/graphql/core/validators/mutation_count_limit_rule.py:27]

**`saleor/graphql/core/validators/query_cost.py`**

- `CostValidator` (class) — [saleor/graphql/core/validators/query_cost.py:34]
- `compute_node_cost` (function) — [saleor/graphql/core/validators/query_cost.py:62]
- `update_empty_args_with_default` (function) — [saleor/graphql/core/validators/query_cost.py:161]
- `enter_operation_definition` (function) — [saleor/graphql/core/validators/query_cost.py:172]
- `leave_operation_definition` (function) — [saleor/graphql/core/validators/query_cost.py:193]
- `compute_cost` (function) — [saleor/graphql/core/validators/query_cost.py:197]
- `get_args_from_cost_map` (function) — [saleor/graphql/core/validators/query_cost.py:207]
- `get_multipliers_from_string` (function) — [saleor/graphql/core/validators/query_cost.py:221]
- `get_cost_exceeded_error` (function) — [saleor/graphql/core/validators/query_cost.py:238]
- `enter` (function) — [saleor/graphql/core/validators/query_cost.py:249]
- `leave` (function) — [saleor/graphql/core/validators/query_cost.py:260]
- `validate_cost_map` (function) — [saleor/graphql/core/validators/query_cost.py:272]
- `report_error` (function) — [saleor/graphql/core/validators/query_cost.py:299]
- `cost_analysis_message` (function) — [saleor/graphql/core/validators/query_cost.py:303]
- `QueryCostError` (class) — [saleor/graphql/core/validators/query_cost.py:309]
- `cost_validator` (function) — [saleor/graphql/core/validators/query_cost.py:313]
- `validate_query_cost` (function) — [saleor/graphql/core/validators/query_cost.py:330]

**`saleor/graphql/core/validators/tests/test_alias_count_limit.py`**

- `test_limits_number_of_aliases` (function) — [saleor/graphql/core/validators/tests/test_alias_count_limit.py:64]
- `test_metric_recorded` (function) — [saleor/graphql/core/validators/tests/test_alias_count_limit.py:120]

**`saleor/graphql/core/validators/tests/test_mutation_count_limit.py`**

- `test_limits_number_of_aliases` (function) — [saleor/graphql/core/validators/tests/test_mutation_count_limit.py:61]
- `test_metric_recorded` (function) — [saleor/graphql/core/validators/tests/test_mutation_count_limit.py:129]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/core/validators/__init__.py` (261 lines)
- `saleor/graphql/core/validators/alias_count_limit_rule.py` (39 lines)
- `saleor/graphql/core/validators/file.py` (202 lines)
- `saleor/graphql/core/validators/mutation_count_limit_rule.py` (40 lines)
- `saleor/graphql/core/validators/query_cost.py` (349 lines)
- `saleor/graphql/core/validators/tests/__init__.py` (1 lines)
- `saleor/graphql/core/validators/tests/test_alias_count_limit.py` (141 lines)
- `saleor/graphql/core/validators/tests/test_mutation_count_limit.py` (155 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql`, `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....core.telemetry.Scope`
- `.....core.telemetry.Unit`
- `.....tests.utils.get_metric_data`
- `....api.backend`
- `....api.schema`
- `....core.utils.generate_unique_slug`
- `....metrics.METRIC_GRAPHQL_ALIAS_COUNT`
- `....metrics.METRIC_GRAPHQL_MUTATION_COUNT`
- `....product.models.ProductVariantChannelListing`
- `....thumbnail.MIME_TYPE_TO_PIL_IDENTIFIER`
- `....thumbnail.utils.ProcessedImage`
- `....views.GraphQLView`
- `...metrics.record_graphql_alias_count`
- `...metrics.record_graphql_mutation_count`
- `..utils.add_hash_to_file_name`
- `.alias_count_limit_rule.AliasCountLimitRule`
- `.mutation_count_limit_rule.MutationCountLimitRule`
- `.query_cost.cost_validator`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `8d9c11ebd314` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
