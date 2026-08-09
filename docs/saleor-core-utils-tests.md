## Purpose

`saleor/core/utils/tests` (`saleor/core/utils/tests`) groups 9 source file(s) exposing 24 top-level declaration(s).

## Public surface

**`saleor/core/utils/tests/test_cache.py`**

- `test_capacity` (function) — [saleor/core/utils/tests/test_cache.py:4]
- `test_persistence` (function) — [saleor/core/utils/tests/test_cache.py:19]
- `test_eviction_order` (function) — [saleor/core/utils/tests/test_cache.py:31]

**`saleor/core/utils/tests/test_events.py`**

- `test_call_event_triggers_provided_method` (function) — [saleor/core/utils/tests/test_events.py:9]

**`saleor/core/utils/tests/test_metadata_manager.py`**

- `test_metadata_is_valid_true` (function) — [saleor/core/utils/tests/test_metadata_manager.py:14]
- `test_metadata_is_valid_false` (function) — [saleor/core/utils/tests/test_metadata_manager.py:33]

**`saleor/core/utils/tests/test_serializer.py`**

- `test_custom_json_encoder_dumps_money_objects` (function) — [saleor/core/utils/tests/test_serializer.py:9]
- `test_custom_json_encoder_dumps_weight_objects` (function) — [saleor/core/utils/tests/test_serializer.py:24]

**`saleor/core/utils/tests/test_text.py`**

- `test_safe_truncate` (function) — [saleor/core/utils/tests/test_text.py:4]
- `test_safe_truncate_with_combining_characters` (function) — [saleor/core/utils/tests/test_text.py:12]

**`saleor/core/utils/tests/test_update_mutation_manager.py`**

- `test_instance_tracker` (function) — [saleor/core/utils/tests/test_update_mutation_manager.py:5]
- `test_instance_tracker_no_instance_on_init` (function) — [saleor/core/utils/tests/test_update_mutation_manager.py:18]
- `test_instance_tracker_no_instance_on_init_and_on_get_modified_fields` (function) — [saleor/core/utils/tests/test_update_mutation_manager.py:31]
- `test_instance_tracker_remove_instance` (function) — [saleor/core/utils/tests/test_update_mutation_manager.py:43]
- `test_instance_tracker_foreign_relation` (function) — [saleor/core/utils/tests/test_update_mutation_manager.py:56]
- `test_instance_tracker_foreign_relation_new_instance` (function) — [saleor/core/utils/tests/test_update_mutation_manager.py:80]

**`saleor/core/utils/tests/test_url.py`**

- `test_prepare_url` (function) — [saleor/core/utils/tests/test_url.py:10]
- `test_prepare_url_with_existing_query` (function) — [saleor/core/utils/tests/test_url.py:17]
- `test_get_default_storage_root_url` (function) — [saleor/core/utils/tests/test_url.py:24]
- `test_sanitize_url_for_logging` (function) — [saleor/core/utils/tests/test_url.py:52]

**`saleor/core/utils/tests/test_validators.py`**

- `test_is_image_mimetype_valid_mimetype` (function) — [saleor/core/utils/tests/test_validators.py:6]
- `test_is_image_mimetype_invalid_mimetype` (function) — [saleor/core/utils/tests/test_validators.py:17]
- `test_is_valid_image_content_type` (function) — [saleor/core/utils/tests/test_validators.py:46]
- `test_get_mime_type` (function) — [saleor/core/utils/tests/test_validators.py:67]

## How it works

The module's files, as provided to this run:

- `saleor/core/utils/tests/__init__.py` (1 lines)
- `saleor/core/utils/tests/test_cache.py` (44 lines)
- `saleor/core/utils/tests/test_events.py` (26 lines)
- `saleor/core/utils/tests/test_metadata_manager.py` (38 lines)
- `saleor/core/utils/tests/test_serializer.py` (33 lines)
- `saleor/core/utils/tests/test_text.py` (16 lines)
- `saleor/core/utils/tests/test_update_mutation_manager.py` (102 lines)
- `saleor/core/utils/tests/test_url.py` (53 lines)
- `saleor/core/utils/tests/test_validators.py` (68 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....order.OrderStatus`
- `...taxes.zero_money`
- `..cache.CacheDict`
- `..events.call_event`
- `..json_serializer.CustomJsonEncoder`
- `..metadata_manager.metadata_is_valid`
- `..text.safe_truncate`
- `..update_mutation_manager.InstanceTracker`
- `..url.get_default_storage_root_url`
- `..url.prepare_url`
- `..url.sanitize_url_for_logging`
- `..validators.get_mime_type`
- `..validators.is_image_mimetype`
- `..validators.is_valid_image_content_type`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `833408bdd27f` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
