## Purpose

`saleor/page` (`saleor/page`) groups 7 source file(s) exposing 21 top-level declaration(s).

## Public surface

**`saleor/page/error_codes.py`**

- `PageErrorCode` (class) — [saleor/page/error_codes.py:4]

**`saleor/page/lock_objects.py`**

- `page_qs_select_for_update` (function) — [saleor/page/lock_objects.py:6]

**`saleor/page/models.py`**

- `PageQueryset` (class) — [saleor/page/models.py:18]
- `visible_to_user` (function) — [saleor/page/models.py:19]
- `Page` (class) — [saleor/page/models.py:28]
- `Meta` (class) — [saleor/page/models.py:41]
- `PageTranslation` (class) — [saleor/page/models.py:57]
- `Meta` (class) — [saleor/page/models.py:64]
- `get_translated_object_id` (function) — [saleor/page/models.py:81]
- `get_translated_keys` (function) — [saleor/page/models.py:84]
- `PageType` (class) — [saleor/page/models.py:95]
- `Meta` (class) — [saleor/page/models.py:99]

**`saleor/page/search.py`**

- `AttributeValueData` (class) — [saleor/page/search.py:24]
- `update_pages_search_vector` (function) — [saleor/page/search.py:31]
- `load_all_data` (function) — [saleor/page/search.py:86]
- `with_attributes` (function) — [saleor/page/search.py:92]
- `prepare_page_search_vector_value` (function) — [saleor/page/search.py:153]
- `generate_attributes_search_vector_value` (function) — [saleor/page/search.py:192]

**`saleor/page/tasks.py`**

- `mark_pages_search_vector_as_dirty` (function) — [saleor/page/tasks.py:16]
- `update_pages_search_vector_task` (function) — [saleor/page/tasks.py:29]

**`saleor/page/utils.py`**

- `mark_pages_search_vector_as_dirty_in_batches` (function) — [saleor/page/utils.py:7]

## How it works

The module's files, as provided to this run:

- `saleor/page/models.py` (107 lines)
- `saleor/page/__init__.py` (1 lines)
- `saleor/page/error_codes.py` (11 lines)
- `saleor/page/lock_objects.py` (7 lines)
- `saleor/page/search.py` (211 lines)
- `saleor/page/tasks.py` (38 lines)
- `saleor/page/utils.py` (11 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql/product/types`
- Imported by: `saleor/menu/migrations`

Internal dependencies named in the source:

- `..account.models.User`
- `..app.models.App`
- `..attribute.models.Attribute`
- `..attribute.models.AttributeValue`
- `..attribute.search.get_search_vectors_for_attribute_values`
- `..celeryconf.app`
- `..core.context.with_promise_context`
- `..core.db.connection.allow_writer`
- `..core.db.fields.SanitizedJSONField`
- `..core.editorjs.clean_editorjs`
- `..core.editorjs.editorjs_to_text`
- `..core.models.ModelWithMetadata`
- `..core.models.PublishableModel`
- `..core.models.PublishedQuerySet`
- `..core.postgres.FlatConcatSearchVector`
- `..core.postgres.NoValidationSearchVector`
- `..graphql.core.context.SaleorContext`
- `..graphql.page.dataloaders.PageTypeByIdLoader`
- `..permission.enums.PagePermissions`
- `..permission.enums.PageTypePermissions`
- `..seo.models.SeoModel`
- `..seo.models.SeoModelTranslationWithSlug`
- `.lock_objects.page_qs_select_for_update`
- `.models.Page`
- `.models.PageType`
- `.search.update_pages_search_vector`
- `.tasks.mark_pages_search_vector_as_dirty`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `8a26ea032aa7` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
