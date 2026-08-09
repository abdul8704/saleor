## Purpose

`saleor/site` (`saleor/site`) groups 6 source file(s) exposing 24 top-level declaration(s).

## Public surface

**`saleor/site/__init__.py`**

- `PasswordLoginMode` (class) — [saleor/site/__init__.py:1]
- `GiftCardSettingsExpiryType` (class) — [saleor/site/__init__.py:22]
- `AccountConfirmMode` (class) — [saleor/site/__init__.py:32]
- `AnnouncementImportance` (class) — [saleor/site/__init__.py:56]

**`saleor/site/apps.py`**

- `SiteAppConfig` (class) — [saleor/site/apps.py:12]
- `setup_announcements` (function) — [saleor/site/apps.py:18]
- `ready` (function) — [saleor/site/apps.py:24]

**`saleor/site/context_processors.py`**

- `site` (function) — [saleor/site/context_processors.py:11]

**`saleor/site/error_codes.py`**

- `SiteErrorCode` (class) — [saleor/site/error_codes.py:4]
- `GiftCardSettingsErrorCode` (class) — [saleor/site/error_codes.py:9]
- `RefundSettingsErrorCode` (class) — [saleor/site/error_codes.py:15]
- `ReturnSettingsErrorCode` (class) — [saleor/site/error_codes.py:21]

**`saleor/site/models.py`**

- `email_sender_name_validators` (function) — [saleor/site/models.py:26]
- `SiteSettings` (class) — [saleor/site/models.py:38]
- `Meta` (class) — [saleor/site/models.py:165]
- `default_from_email` (function) — [saleor/site/models.py:172]
- `SiteSettingsTranslation` (class) — [saleor/site/models.py:193]
- `Meta` (class) — [saleor/site/models.py:200]
- `get_translated_object_id` (function) — [saleor/site/models.py:207]
- `get_translated_keys` (function) — [saleor/site/models.py:210]

**`saleor/site/patch_sites.py`**

- `new_get_current` (function) — [saleor/site/patch_sites.py:19]
- `new_clear_cache` (function) — [saleor/site/patch_sites.py:70]
- `new_get_by_natural_key` (function) — [saleor/site/patch_sites.py:76]
- `patch_contrib_sites` (function) — [saleor/site/patch_sites.py:80]

## How it works

The module's files, as provided to this run:

- `saleor/site/__init__.py` (71 lines)
- `saleor/site/apps.py` (25 lines)
- `saleor/site/context_processors.py` (16 lines)
- `saleor/site/error_codes.py` (25 lines)
- `saleor/site/models.py` (214 lines)
- `saleor/site/patch_sites.py` (83 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `..AccountConfirmMode`
- `..GiftCardSettingsExpiryType`
- `..PasswordLoginMode`
- `..core.TimePeriodType`
- `..core.models.ModelWithMetadata`
- `..core.units.WeightUnits`
- `..core.utils.translations.Translation`
- `..graphql.core.context.get_database_connection_name`
- `..graphql.shop.types.Announcement`
- `..permission.enums.SitePermissions`
- `.error_codes.SiteErrorCode`
- `.patch_sites.patch_contrib_sites`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `4c11e4c4edd6` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
