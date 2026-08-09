## Purpose

`saleor/core/cleaners` (`saleor/core/cleaners`) groups 5 source file(s) exposing 15 top-level declaration(s).

## Public surface

**`saleor/core/cleaners/html.py`**

- `HtmlCleanerSettings` (class) — [saleor/core/cleaners/html.py:11]
- `reload` (function) — [saleor/core/cleaners/html.py:34]
- `parse` (function) — [saleor/core/cleaners/html.py:58]

**`saleor/core/cleaners/tests/test_urls.py`**

- `test_clean_url_tel_scheme_valid` (function) — [saleor/core/cleaners/tests/test_urls.py:31]
- `test_clean_url_tel_scheme_invalid` (function) — [saleor/core/cleaners/tests/test_urls.py:48]
- `test_clean_url_mailto_scheme_valid` (function) — [saleor/core/cleaners/tests/test_urls.py:102]
- `test_clean_url_mailto_scheme_invalid_urls` (function) — [saleor/core/cleaners/tests/test_urls.py:125]

**`saleor/core/cleaners/urls.py`**

- `UrlCleaner` (class) — [saleor/core/cleaners/urls.py:10]
- `URLCleanerError` (class) — [saleor/core/cleaners/urls.py:14]
- `InvalidHostname` (class) — [saleor/core/cleaners/urls.py:18]
- `InvalidURL` (class) — [saleor/core/cleaners/urls.py:22]
- `InvalidUsage` (class) — [saleor/core/cleaners/urls.py:26]
- `normalize_host` (function) — [saleor/core/cleaners/urls.py:30]
- `clean_tel` (function) — [saleor/core/cleaners/urls.py:61]
- `clean_mailto` (function) — [saleor/core/cleaners/urls.py:75]

## How it works

The module's files, as provided to this run:

- `saleor/core/cleaners/html.py` (59 lines)
- `saleor/core/cleaners/__init__.py` (15 lines)
- `saleor/core/cleaners/tests/__init__.py` (1 lines)
- `saleor/core/cleaners/tests/test_urls.py` (129 lines)
- `saleor/core/cleaners/urls.py` (145 lines)

## Interactions

- Imports from: `saleor/plugins/openid_connect`
- Imported by: `saleor/attribute/migrations`, `saleor/core/editorjs`, `saleor/graphql/product/tests/mutations`

Internal dependencies named in the source:

- `...clean_mailto`
- `...clean_tel`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `f390706b868d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
