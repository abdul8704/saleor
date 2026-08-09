## Purpose

`saleor/core/db` (`saleor/core/db`) groups 9 source file(s) exposing 45 top-level declaration(s).

## Public surface

**`saleor/core/db/connection.py`**

- `UnsafeWriterAccessError` (class) — [saleor/core/db/connection.py:28]
- `allow_writer` (function) — [saleor/core/db/connection.py:33]
- `allow_writer_for_default_connection` (function) — [saleor/core/db/connection.py:58]
- `allow_writer_in_context` (function) — [saleor/core/db/connection.py:72]
- `restrict_writer_middleware` (function) — [saleor/core/db/connection.py:83]
- `middleware` (function) — [saleor/core/db/connection.py:92]
- `restrict_writer` (function) — [saleor/core/db/connection.py:100]
- `log_writer_usage_middleware` (function) — [saleor/core/db/connection.py:108]
- `middleware` (function) — [saleor/core/db/connection.py:116]
- `log_writer_usage` (function) — [saleor/core/db/connection.py:123]

**`saleor/core/db/expressions.py`**

- `PostgresJsonConcatenate` (class) — [saleor/core/db/expressions.py:5]
- `resolve_expression` (function) — [saleor/core/db/expressions.py:46]
- `as_postgresql` (function) — [saleor/core/db/expressions.py:76]

**`saleor/core/db/fields.py`**

- `SanitizedJSONField` (class) — [saleor/core/db/fields.py:12]
- `deconstruct` (function) — [saleor/core/db/fields.py:20]
- `get_db_prep_save` (function) — [saleor/core/db/fields.py:25]
- `NonDatabaseFieldBase` (class) — [saleor/core/db/fields.py:35]
- `contribute_to_class` (function) — [saleor/core/db/fields.py:76]
- `clean` (function) — [saleor/core/db/fields.py:82]
- `MoneyField` (class) — [saleor/core/db/fields.py:88]
- `get_default` (function) — [saleor/core/db/fields.py:128]
- `TaxedMoneyField` (class) — [saleor/core/db/fields.py:142]

**`saleor/core/db/filters.py`**

- `PostgresILike` (class) — [saleor/core/db/filters.py:4]
- `as_postgresql` (function) — [saleor/core/db/filters.py:7]

**`saleor/core/db/patch.py`**

- `patch_db` (function) — [saleor/core/db/patch.py:18]

**`saleor/core/db/tests/test_connection.py`**

- `test_allow_writer` (function) — [saleor/core/db/tests/test_connection.py:17]
- `test_allow_writer_yield_exception` (function) — [saleor/core/db/tests/test_connection.py:26]
- `example_function` (function) — [saleor/core/db/tests/test_connection.py:29]
- `test_allow_writer_in_context_writer` (function) — [saleor/core/db/tests/test_connection.py:42]
- `test_allow_writer_in_context_replica` (function) — [saleor/core/db/tests/test_connection.py:53]
- `test_restrict_writer_raises_error` (function) — [saleor/core/db/tests/test_connection.py:64]
- `test_restrict_writer_in_allow_writer` (function) — [saleor/core/db/tests/test_connection.py:72]
- `test_log_writer_usage` (function) — [saleor/core/db/tests/test_connection.py:80]

**`saleor/core/db/tests/test_postgres_json_concatenate.py`**

- `checkout_metadata_qs` (function) — [saleor/core/db/tests/test_postgres_json_concatenate.py:13]
- `test_save_concat_add_new_key` (function) — [saleor/core/db/tests/test_postgres_json_concatenate.py:17]
- `test_save_concat_update_key` (function) — [saleor/core/db/tests/test_postgres_json_concatenate.py:36]
- `test_save_concat_new_dict` (function) — [saleor/core/db/tests/test_postgres_json_concatenate.py:55]
- `test_save_concat_with_none_value` (function) — [saleor/core/db/tests/test_postgres_json_concatenate.py:74]
- `test_save_concat_add_multiple_new_key` (function) — [saleor/core/db/tests/test_postgres_json_concatenate.py:93]
- `test_raise_error_when_no_JSONField_output` (function) — [saleor/core/db/tests/test_postgres_json_concatenate.py:112]
- `test_raise_error_when_no_expression` (function) — [saleor/core/db/tests/test_postgres_json_concatenate.py:128]
- `test_multiple_updates` (function) — [saleor/core/db/tests/test_postgres_json_concatenate.py:142]
- `test_saving_same_value_no_affect` (function) — [saleor/core/db/tests/test_postgres_json_concatenate.py:168]
- `test_updating_existing_key_to_none` (function) — [saleor/core/db/tests/test_postgres_json_concatenate.py:187]
- `test_updating_with_empty_dict` (function) — [saleor/core/db/tests/test_postgres_json_concatenate.py:206]

## How it works

The module's files, as provided to this run:

- `saleor/core/db/expressions.py` (85 lines)
- `saleor/core/db/fields.py` (182 lines)
- `saleor/core/db/connection.py` (134 lines)
- `saleor/core/db/__init__.py` (1 lines)
- `saleor/core/db/filters.py` (11 lines)
- `saleor/core/db/patch.py` (32 lines)
- `saleor/core/db/tests/__init__.py` (1 lines)
- `saleor/core/db/tests/test_connection.py` (88 lines)
- `saleor/core/db/tests/test_postgres_json_concatenate.py` (222 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql/product/types`, `saleor/plugins/openid_connect`
- Imported by: `saleor/page/migrations`, `saleor/product/migrations`, `saleor/checkout/migrations`, `saleor/graphql/attribute/utils`, `saleor/graphql/page/mutations`, `saleor/graphql/product/bulk_mutations`, `saleor/order/migrations`, `saleor/warehouse`, `.semgrep`, `saleor/account`, `saleor/attribute/migrations`, `saleor/attribute/tests`, `saleor/csv`, `saleor/csv/tests`, `saleor/discount/migrations`, `saleor/giftcard`, `saleor/graphql`, `saleor/graphql/product/filters`, `saleor/graphql/product/mutations/product`, `saleor/graphql/product/mutations/product_type`, `saleor/order`, `saleor/schedulers`, `saleor/shipping/migrations`, `saleor/tax/migrations`, `saleor/webhook`

Internal dependencies named in the source:

- `....checkout.models.CheckoutMetadata`
- `....graphql.context.SaleorContext`
- `....tests.models.Book`
- `...graphql.core.context.SaleorContext`
- `...graphql.core.context.get_database_connection_name`
- `..expressions.PostgresJsonConcatenate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `11ebeda76dc3` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
