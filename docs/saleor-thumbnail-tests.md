## Purpose

`saleor/thumbnail/tests` (`saleor/thumbnail/tests`) groups 6 source file(s) exposing 61 top-level declaration(s).

## Public surface

**`saleor/thumbnail/tests/fixtures/thumbnail.py`**

- `thumbnail_product_media` (function) — [saleor/thumbnail/tests/fixtures/thumbnail.py:7]
- `thumbnail_category` (function) — [saleor/thumbnail/tests/fixtures/thumbnail.py:16]
- `thumbnail_collection` (function) — [saleor/thumbnail/tests/fixtures/thumbnail.py:25]
- `thumbnail_user` (function) — [saleor/thumbnail/tests/fixtures/thumbnail.py:34]

**`saleor/thumbnail/tests/test_utils.py`**

- `test_get_thumbnail_size` (function) — [saleor/thumbnail/tests/test_utils.py:25]
- `test_prepare_thumbnail_file_name` (function) — [saleor/thumbnail/tests/test_utils.py:47]
- `test_prepare_image_proxy_url` (function) — [saleor/thumbnail/tests/test_utils.py:58]
- `test_get_image_or_proxy_url_proxy_url_returned` (function) — [saleor/thumbnail/tests/test_utils.py:72]
- `test_get_image_or_proxy_url_thumbnail_url_returned` (function) — [saleor/thumbnail/tests/test_utils.py:85]
- `test_processed_image_preprocess_method_called` (function) — [saleor/thumbnail/tests/test_utils.py:104]
- `test_processed_image_preprocess_with_exif_corrupted` (function) — [saleor/thumbnail/tests/test_utils.py:122]
- `test_get_filename_from_url_unique` (function) — [saleor/thumbnail/tests/test_utils.py:141]
- `test_get_filename_from_url_with_long_name_is_trimmed` (function) — [saleor/thumbnail/tests/test_utils.py:156]
- `test_get_filename_from_url_with_short_name_is_not_trimmed` (function) — [saleor/thumbnail/tests/test_utils.py:173]
- `test_get_filename_from_url_with_query_params` (function) — [saleor/thumbnail/tests/test_utils.py:191]
- `test_get_filename_from_url_with_query_params_path` (function) — [saleor/thumbnail/tests/test_utils.py:205]
- `test_get_filename_from_url_without_extension` (function) — [saleor/thumbnail/tests/test_utils.py:227]

**`saleor/thumbnail/tests/test_validators.py`**

- `image_factory` (function) — [saleor/thumbnail/tests/test_validators.py:18]
- `factory` (function) — [saleor/thumbnail/tests/test_validators.py:19]
- `test_validate_image_format` (function) — [saleor/thumbnail/tests/test_validators.py:27]
- `test_validate_image_format_when_not_allowed` (function) — [saleor/thumbnail/tests/test_validators.py:31]
- `test_validate_image_exif` (function) — [saleor/thumbnail/tests/test_validators.py:38]
- `test_validate_image_size` (function) — [saleor/thumbnail/tests/test_validators.py:46]
- `test_validate_image_size_with_invalid_image` (function) — [saleor/thumbnail/tests/test_validators.py:59]
- `test_validate_icon_image` (function) — [saleor/thumbnail/tests/test_validators.py:69]
- `test_validate_icon_image_with_invalid_image` (function) — [saleor/thumbnail/tests/test_validators.py:75]

**`saleor/thumbnail/tests/test_views.py`**

- `test_handle_thumbnail_view_with_format` (function) — [saleor/thumbnail/tests/test_views.py:11]
- `test_handle_thumbnail_view_for_category` (function) — [saleor/thumbnail/tests/test_views.py:31]
- `test_handle_thumbnail_view_for_collection` (function) — [saleor/thumbnail/tests/test_views.py:50]
- `test_handle_thumbnail_view_for_user` (function) — [saleor/thumbnail/tests/test_views.py:69]
- `test_handle_thumbnail_view_for_product_media` (function) — [saleor/thumbnail/tests/test_views.py:93]
- `test_handle_thumbnail_view_for_category_thumbnail_already_exist` (function) — [saleor/thumbnail/tests/test_views.py:116]
- `test_handle_thumbnail_view_for_collection_thumbnail_already_exist` (function) — [saleor/thumbnail/tests/test_views.py:134]
- `test_handle_thumbnail_view_for_user_thumbnail_already_exist` (function) — [saleor/thumbnail/tests/test_views.py:152]
- `test_handle_thumbnail_view_for_product_media_thumbnail_already_exist` (function) — [saleor/thumbnail/tests/test_views.py:170]
- `test_handle_thumbnail_view_no_image` (function) — [saleor/thumbnail/tests/test_views.py:191]
- `test_handle_thumbnail_view_for_product_media_image_type_with_external_url_but_no_image` (function) — [saleor/thumbnail/tests/test_views.py:203]
- `test_handle_thumbnail_view_invalid_object_type` (function) — [saleor/thumbnail/tests/test_views.py:223]
- `test_handle_thumbnail_view_invalid_format` (function) — [saleor/thumbnail/tests/test_views.py:235]
- `test_handle_icon_thumbnail_view_invalid_format` (function) — [saleor/thumbnail/tests/test_views.py:247]
- `test_handle_thumbnail_view_invalid_instance_id` (function) — [saleor/thumbnail/tests/test_views.py:258]
- `test_handle_thumbnail_view_object_does_not_exists` (function) — [saleor/thumbnail/tests/test_views.py:270]
- `test_handle_thumbnail_view_invalid_image_mime_type` (function) — [saleor/thumbnail/tests/test_views.py:283]
- `test_handle_thumbnail_view_image_does_not_exist` (function) — [saleor/thumbnail/tests/test_views.py:303]
- `test_handle_icon_thumbnail_view_with_format` (function) — [saleor/thumbnail/tests/test_views.py:324]
- `test_handle_thumbnail_view_for_app_logo_default` (function) — [saleor/thumbnail/tests/test_views.py:353]
- `test_handle_thumbnail_view_for_app_logo_default_thumbnail_exist` (function) — [saleor/thumbnail/tests/test_views.py:377]
- `test_handle_thumbnail_view_for_app_installation_logo_default` (function) — [saleor/thumbnail/tests/test_views.py:395]
- `test_handle_thumbnail_view_for_app_installation_logo_default_thumbnail_exist` (function) — [saleor/thumbnail/tests/test_views.py:419]
- `test_handle_original_image_for_category` (function) — [saleor/thumbnail/tests/test_views.py:439]
- `test_handle_original_image_for_collection` (function) — [saleor/thumbnail/tests/test_views.py:453]
- `test_handle_original_image_for_user` (function) — [saleor/thumbnail/tests/test_views.py:467]
- `test_handle_original_image_for_product_media` (function) — [saleor/thumbnail/tests/test_views.py:484]
- `test_handle_original_image_for_app` (function) — [saleor/thumbnail/tests/test_views.py:497]
- `test_handle_original_image_for_app_installation` (function) — [saleor/thumbnail/tests/test_views.py:512]
- `test_handle_original_image_invalid_instance_id` (function) — [saleor/thumbnail/tests/test_views.py:529]
- `test_handle_original_image_invalid_object_type` (function) — [saleor/thumbnail/tests/test_views.py:540]
- `test_handle_original_image_object_does_not_exist` (function) — [saleor/thumbnail/tests/test_views.py:551]
- `test_handle_original_image_no_image` (function) — [saleor/thumbnail/tests/test_views.py:562]
- `test_handle_original_image_for_product_media_without_image` (function) — [saleor/thumbnail/tests/test_views.py:574]
- `test_handle_original_image_for_product_media_image_type_with_external_url_but_no_image` (function) — [saleor/thumbnail/tests/test_views.py:586]

## How it works

The module's files, as provided to this run:

- `saleor/thumbnail/tests/__init__.py` (1 lines)
- `saleor/thumbnail/tests/fixtures/__init__.py` (1 lines)
- `saleor/thumbnail/tests/fixtures/thumbnail.py` (40 lines)
- `saleor/thumbnail/tests/test_utils.py` (228 lines)
- `saleor/thumbnail/tests/test_validators.py` (79 lines)
- `saleor/thumbnail/tests/test_views.py` (602 lines)

## Interactions

- Imports from: `saleor/thumbnail`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...FILE_NAME_MAX_LENGTH`
- `...IconThumbnailFormat`
- `...MIN_ICON_SIZE`
- `...ThumbnailFormat`
- `...models.Thumbnail`
- `...product.ProductMediaTypes`
- `..models.Thumbnail`
- `.thumbnail.*  # noqa: F403`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `ae0b89c18ed7` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
