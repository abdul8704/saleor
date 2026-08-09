## Purpose

`saleor/core/editorjs` (`saleor/core/editorjs`) groups 9 source file(s) exposing 71 top-level declaration(s).

## Public surface

**`saleor/core/editorjs/converters.py`**

- `parse_editorjs` (function) — [saleor/core/editorjs/converters.py:13]
- `clean_editorjs` (function) — [saleor/core/editorjs/converters.py:38]
- `clean_editorjs` (function) — [saleor/core/editorjs/converters.py:40]
- `clean_editorjs` (function) — [saleor/core/editorjs/converters.py:43]
- `editorjs_to_text` (function) — [saleor/core/editorjs/converters.py:62]

**`saleor/core/editorjs/models.py`**

- `StrictBaseModel` (class) — [saleor/core/editorjs/models.py:42]
- `SizeDataModel` (class) — [saleor/core/editorjs/models.py:55]
- `EditorJSBlock` (class) — [saleor/core/editorjs/models.py:62]
- `to_text` (function) — [saleor/core/editorjs/models.py:65]
- `EditorJSParagraphDataModel` (class) — [saleor/core/editorjs/models.py:70]
- `EditorJSHeaderDataModel` (class) — [saleor/core/editorjs/models.py:85]
- `EditorJSQuoteDataModel` (class) — [saleor/core/editorjs/models.py:102]
- `EditorJSEmbedDataModel` (class) — [saleor/core/editorjs/models.py:119]
- `ImageFileModel` (class) — [saleor/core/editorjs/models.py:136]
- `EditorJSImageDataModel` (class) — [saleor/core/editorjs/models.py:145]
- `EditorJSTableDataModel` (class) — [saleor/core/editorjs/models.py:172]
- `EditorJSNestedListItemModel` (class) — [saleor/core/editorjs/models.py:195]
- `EditorJSListDataModel` (class) — [saleor/core/editorjs/models.py:224]
- `to_text` (function) — [saleor/core/editorjs/models.py:243]
- `EditorJSParagraphBlockModel` (class) — [saleor/core/editorjs/models.py:281]
- `to_text` (function) — [saleor/core/editorjs/models.py:298]
- `EditorJSHeaderBlockModel` (class) — [saleor/core/editorjs/models.py:302]
- `to_text` (function) — [saleor/core/editorjs/models.py:320]
- `EditorJSListBlockModel` (class) — [saleor/core/editorjs/models.py:324]
- `to_text` (function) — [saleor/core/editorjs/models.py:344]
- `EditorJSQuoteBlockModel` (class) — [saleor/core/editorjs/models.py:363]
- `to_text` (function) — [saleor/core/editorjs/models.py:381]
- `EditorJSEmbedBlockModel` (class) — [saleor/core/editorjs/models.py:385]
- `to_text` (function) — [saleor/core/editorjs/models.py:403]
- `EditorJSImageBlockModel` (class) — [saleor/core/editorjs/models.py:412]
- `to_text` (function) — [saleor/core/editorjs/models.py:439]
- `EditorJSTableBlockModel` (class) — [saleor/core/editorjs/models.py:451]
- `to_text` (function) — [saleor/core/editorjs/models.py:475]
- `EditorJSDocumentModel` (class) — [saleor/core/editorjs/models.py:499]

**`saleor/core/editorjs/tests/conftest.py`**

- `no_link_rel` (function) — [saleor/core/editorjs/tests/conftest.py:6]
- `assert_pydantic_errors` (function) — [saleor/core/editorjs/tests/conftest.py:15]

**`saleor/core/editorjs/tests/test_editorjs.py`**

- `assert_paragraph_cleaned` (function) — [saleor/core/editorjs/tests/test_editorjs.py:33]
- `cleaner_settings` (function) — [saleor/core/editorjs/tests/test_editorjs.py:44]
- `test_clean_url` (function) — [saleor/core/editorjs/tests/test_editorjs.py:79]
- `test_clean_url_error_handling` (function) — [saleor/core/editorjs/tests/test_editorjs.py:100]
- `test_clean_text_data_block` (function) — [saleor/core/editorjs/tests/test_editorjs.py:181]
- `test_clean_text_data_block_allow_custom_attributes` (function) — [saleor/core/editorjs/tests/test_editorjs.py:208]
- `test_clean_text_data_block_allow_custom_attribute_values` (function) — [saleor/core/editorjs/tests/test_editorjs.py:269]
- `test_clean_editor_js` (function) — [saleor/core/editorjs/tests/test_editorjs.py:318]
- `test_clean_editor_js_no_blocks` (function) — [saleor/core/editorjs/tests/test_editorjs.py:345]
- `test_clean_editor_js_invalid_url` (function) — [saleor/core/editorjs/tests/test_editorjs.py:355]
- `test_clean_editor_js_for_list` (function) — [saleor/core/editorjs/tests/test_editorjs.py:382]
- `test_clean_editor_js_for_list_invalid_url` (function) — [saleor/core/editorjs/tests/test_editorjs.py:429]
- `test_clean_editor_js_for_complex_description` (function) — [saleor/core/editorjs/tests/test_editorjs.py:472]
- `test_clean_editor_js_for_malicious_value` (function) — [saleor/core/editorjs/tests/test_editorjs.py:569]
- `test_clean_editor_js_image_invalid_url` (function) — [saleor/core/editorjs/tests/test_editorjs.py:595]
- `test_clean_editor_js_image_disallowed_scheme` (function) — [saleor/core/editorjs/tests/test_editorjs.py:611]
- `test_clean_editorjs_image_can_put_extras` (function) — [saleor/core/editorjs/tests/test_editorjs.py:627]
- `test_clean_editorjs_legacy` (function) — [saleor/core/editorjs/tests/test_editorjs.py:729]
- `test_clean_editorjs_legacy_works_for_valid_inputs` (function) — [saleor/core/editorjs/tests/test_editorjs.py:817]
- `test_clean_editorjs_legacy_rejects_invalid` (function) — [saleor/core/editorjs/tests/test_editorjs.py:874]
- `test_cleans_editorjs_nested_lists` (function) — [saleor/core/editorjs/tests/test_editorjs.py:1050]
- `test_clean_editorjs_rejects_invalid_nested_lists` (function) — [saleor/core/editorjs/tests/test_editorjs.py:1173]
- `test_clean_editorjs_rejects_too_deep_nested_list` (function) — [saleor/core/editorjs/tests/test_editorjs.py:1191]
- `test_heading_level_cleaned` (function) — [saleor/core/editorjs/tests/test_editorjs.py:1228]
- `test_cleans_size_caption_blocks` (function) — [saleor/core/editorjs/tests/test_editorjs.py:1283]
- `test_cleans_all_editor_js_blocks` (function) — [saleor/core/editorjs/tests/test_editorjs.py:1413]
- `test_converts_exceptions_to_django` (function) — [saleor/core/editorjs/tests/test_editorjs.py:1432]
- `test_clean_editorjs_table` (function) — [saleor/core/editorjs/tests/test_editorjs.py:1442]
- `test_clean_editorjs_table_cleans_cell_content` (function) — [saleor/core/editorjs/tests/test_editorjs.py:1473]
- `test_clean_editorjs_table_cleans_cell_url` (function) — [saleor/core/editorjs/tests/test_editorjs.py:1494]
- `test_clean_editorjs_table_drops_extra_fields` (function) — [saleor/core/editorjs/tests/test_editorjs.py:1515]
- `test_editorjs_to_text_table` (function) — [saleor/core/editorjs/tests/test_editorjs.py:1539]

**`saleor/core/editorjs/tests/test_lists.py`**

- `test_legacy_lists_to_text` (function) — [saleor/core/editorjs/tests/test_lists.py:16]
- `test_nested_lists_to_text` (function) — [saleor/core/editorjs/tests/test_lists.py:91]

**`saleor/core/editorjs/utils.py`**

- `maybe_to_int` (function) — [saleor/core/editorjs/utils.py:4]

## How it works

The module's files, as provided to this run:

- `saleor/core/editorjs/__init__.py` (3 lines)
- `saleor/core/editorjs/cleaners.py` (113 lines)
- `saleor/core/editorjs/converters.py` (91 lines)
- `saleor/core/editorjs/models.py` (513 lines)
- `saleor/core/editorjs/tests/__init__.py` (1 lines)
- `saleor/core/editorjs/tests/conftest.py` (22 lines)
- `saleor/core/editorjs/tests/test_editorjs.py` (1560 lines)
- `saleor/core/editorjs/tests/test_lists.py` (97 lines)
- `saleor/core/editorjs/utils.py` (18 lines)

## Interactions

- Imports from: `saleor/core/cleaners`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...clean_editorjs`
- `...cleaners.html.HtmlCleanerSettings`
- `...editorjs.editorjs_to_text`
- `...editorjs_to_text`
- `..cleaners.URLCleanerError`
- `..cleaners.URL_SCHEME_CLEANERS`
- `..cleaners._clean_url_value`
- `.conftest.assert_pydantic_errors`
- `.converters.clean_editorjs`
- `.converters.editorjs_to_text`
- `.converters.parse_editorjs`
- `.models.EditorJSDocumentModel`
- `.utils.maybe_to_int`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `d2bef48cf193` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
