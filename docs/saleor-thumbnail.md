## Purpose

`saleor/thumbnail` (`saleor/thumbnail`) groups 7 source file(s) exposing 34 top-level declaration(s).

## Public surface

**`saleor/thumbnail/__init__.py`**

- `ThumbnailFormat` (class) — [saleor/thumbnail/__init__.py:9]
- `IconThumbnailFormat` (class) — [saleor/thumbnail/__init__.py:52]

**`saleor/thumbnail/apps.py`**

- `ThumbnailAppConfig` (class) — [saleor/thumbnail/apps.py:5]
- `ready` (function) — [saleor/thumbnail/apps.py:8]

**`saleor/thumbnail/models.py`**

- `validate_thumbnail_size` (function) — [saleor/thumbnail/models.py:10]
- `Thumbnail` (class) — [saleor/thumbnail/models.py:18]

**`saleor/thumbnail/signals.py`**

- `delete_thumbnail_image` (function) — [saleor/thumbnail/signals.py:4]

**`saleor/thumbnail/utils.py`**

- `get_image_or_proxy_url` (function) — [saleor/thumbnail/utils.py:29]
- `prepare_image_proxy_url` (function) — [saleor/thumbnail/utils.py:44]
- `get_original_image_proxy_url` (function) — [saleor/thumbnail/utils.py:54]
- `get_thumbnail_size` (function) — [saleor/thumbnail/utils.py:64]
- `get_thumbnail_format` (function) — [saleor/thumbnail/utils.py:76]
- `get_icon_thumbnail_format` (function) — [saleor/thumbnail/utils.py:88]
- `prepare_thumbnail_file_name` (function) — [saleor/thumbnail/utils.py:95]
- `ProcessedImage` (class) — [saleor/thumbnail/utils.py:101]
- `create_thumbnail` (function) — [saleor/thumbnail/utils.py:130]
- `retrieve_image` (function) — [saleor/thumbnail/utils.py:139]
- `get_image_metadata_from_file` (function) — [saleor/thumbnail/utils.py:148]
- `preprocess` (function) — [saleor/thumbnail/utils.py:163]
- `preprocess_AVIF` (function) — [saleor/thumbnail/utils.py:216]
- `preprocess_GIF` (function) — [saleor/thumbnail/utils.py:225]
- `preprocess_JPEG` (function) — [saleor/thumbnail/utils.py:233]
- `preprocess_WEBP` (function) — [saleor/thumbnail/utils.py:240]
- `process_image` (function) — [saleor/thumbnail/utils.py:250]
- `ProcessedIconImage` (class) — [saleor/thumbnail/utils.py:264]
- `get_filename_from_url` (function) — [saleor/thumbnail/utils.py:268]
- `is_product_media_image_pending` (function) — [saleor/thumbnail/utils.py:280]

**`saleor/thumbnail/validators.py`**

- `validate_image_format` (function) — [saleor/thumbnail/validators.py:14]
- `validate_image_exif` (function) — [saleor/thumbnail/validators.py:25]
- `validate_image_size` (function) — [saleor/thumbnail/validators.py:36]
- `validate_icon_image` (function) — [saleor/thumbnail/validators.py:54]

**`saleor/thumbnail/views.py`**

- `ModelData` (class) — [saleor/thumbnail/views.py:36]
- `handle_thumbnail` (function) — [saleor/thumbnail/views.py:58]
- `handle_original_image` (function) — [saleor/thumbnail/views.py:153]

## How it works

The module's files, as provided to this run:

- `saleor/thumbnail/__init__.py` (64 lines)
- `saleor/thumbnail/models.py` (57 lines)
- `saleor/thumbnail/apps.py` (16 lines)
- `saleor/thumbnail/signals.py` (6 lines)
- `saleor/thumbnail/utils.py` (286 lines)
- `saleor/thumbnail/validators.py` (72 lines)
- `saleor/thumbnail/views.py` (183 lines)

## Interactions

- Imports from: `saleor/webhook`, `saleor/graphql/product/types`, `saleor/graphql`, `saleor/core`
- Imported by: `saleor/thumbnail/tests`, `saleor/thumbnail/migrations`

Internal dependencies named in the source:

- `..ALLOWED_ICON_THUMBNAIL_FORMATS`
- `..ALLOWED_THUMBNAIL_FORMATS`
- `..THUMBNAIL_SIZES`
- `..ThumbnailFormat`
- `..account.models.User`
- `..app.models.App`
- `..app.models.AppInstallation`
- `..core.db.connection.allow_writer`
- `..core.tasks.delete_from_storage_task`
- `..core.utils.events.call_event`
- `..graphql.core.utils.from_global_id_or_error`
- `..plugins.manager.get_plugins_manager`
- `..product.ProductMediaTypes`
- `..product.models.Category`
- `..product.models.Collection`
- `..product.models.ProductMedia`
- `..thumbnail.models.Thumbnail`
- `.models.Thumbnail`
- `.signals.delete_thumbnail_image`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `17d82622027e` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
