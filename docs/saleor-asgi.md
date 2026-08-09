## Purpose

`saleor/asgi` (`saleor/asgi`) groups 15 source file(s) exposing 51 top-level declaration(s).

## Public surface

**`saleor/asgi/__init__.py`**

- `preload_app` (function) — [saleor/asgi/__init__.py:23]

**`saleor/asgi/asgi_handler.py`**

- `get_asgi_application` (function) — [saleor/asgi/asgi_handler.py:47]
- `PatchedASGIHandler` (class) — [saleor/asgi/asgi_handler.py:52]
- `handle` (function) — [saleor/asgi/asgi_handler.py:53]
- `process_request` (function) — [saleor/asgi/asgi_handler.py:73]

**`saleor/asgi/cors_handler.py`**

- `cors_handler` (function) — [saleor/asgi/cors_handler.py:15]
- `cors_wrapper` (function) — [saleor/asgi/cors_handler.py:16]
- `send_with_origin` (function) — [saleor/asgi/cors_handler.py:69]

**`saleor/asgi/gzip_compression.py`**

- `gzip_compression` (function) — [saleor/asgi/gzip_compression.py:32]
- `gzip_compression_wrapper` (function) — [saleor/asgi/gzip_compression.py:35]
- `send_compressed` (function) — [saleor/asgi/gzip_compression.py:59]

**`saleor/asgi/health_check.py`**

- `health_check` (function) — [saleor/asgi/health_check.py:11]
- `health_check_wrapper` (function) — [saleor/asgi/health_check.py:12]

**`saleor/asgi/telemetry.py`**

- `get_hostname` (function) — [saleor/asgi/telemetry.py:11]
- `telemetry_middleware` (function) — [saleor/asgi/telemetry.py:19]
- `telemetry_wrapper` (function) — [saleor/asgi/telemetry.py:20]

**`saleor/asgi/tests/asgi_test_utils.py`**

- `DummyASGIApplication` (class) — [saleor/asgi/tests/asgi_test_utils.py:5]
- `create_asgi_scope_websocket_proto` (function) — [saleor/asgi/tests/asgi_test_utils.py:17]

**`saleor/asgi/tests/conftest.py`**

- `asgi_app` (function) — [saleor/asgi/tests/conftest.py:13]
- `fake_app` (function) — [saleor/asgi/tests/conftest.py:14]
- `large_asgi_app` (function) — [saleor/asgi/tests/conftest.py:33]
- `fake_app` (function) — [saleor/asgi/tests/conftest.py:34]

**`saleor/asgi/tests/test_cors.py`**

- `build_scope` (function) — [saleor/asgi/tests/test_cors.py:18]
- `run_app` (function) — [saleor/asgi/tests/test_cors.py:39]
- `send` (function) — [saleor/asgi/tests/test_cors.py:42]
- `receive` (function) — [saleor/asgi/tests/test_cors.py:45]
- `test_access_control_header_preflight` (function) — [saleor/asgi/tests/test_cors.py:52]
- `test_access_control_header_simple` (function) — [saleor/asgi/tests/test_cors.py:78]
- `test_access_control_allowed_origins` (function) — [saleor/asgi/tests/test_cors.py:112]
- `test_access_control_disallowed_origins` (function) — [saleor/asgi/tests/test_cors.py:136]

**`saleor/asgi/tests/test_gzip.py`**

- `build_scope` (function) — [saleor/asgi/tests/test_gzip.py:15]
- `run_app` (function) — [saleor/asgi/tests/test_gzip.py:37]
- `send` (function) — [saleor/asgi/tests/test_gzip.py:40]
- `receive` (function) — [saleor/asgi/tests/test_gzip.py:43]
- `test_no_compression` (function) — [saleor/asgi/tests/test_gzip.py:50]
- `test_with_supported_compression` (function) — [saleor/asgi/tests/test_gzip.py:70]
- `test_response_content_length_includes_random_filename` (function) — [saleor/asgi/tests/test_gzip.py:99]
- `test_response_content_length_is_random` (function) — [saleor/asgi/tests/test_gzip.py:161]

**`saleor/asgi/tests/test_healthcheck.py`**

- `test_non_http_requests_forwarded_to_next_wrapper` (function) — [saleor/asgi/tests/test_healthcheck.py:10]

**`saleor/asgi/tests/test_telemetry.py`**

- `test_get_hostname_with_http_request` (function) — [saleor/asgi/tests/test_telemetry.py:21]
- `test_get_hostname_with_non_http_request` (function) — [saleor/asgi/tests/test_telemetry.py:29]
- `test_get_hostname_with_no_host_header` (function) — [saleor/asgi/tests/test_telemetry.py:45]
- `test_telemetry_middleware` (function) — [saleor/asgi/tests/test_telemetry.py:63]

**`saleor/asgi/tests/test_usage_telemetry.py`**

- `test_get_usage_telemetry` (function) — [saleor/asgi/tests/test_usage_telemetry.py:8]
- `test_get_usage_telemetry_checks_reported_at` (function) — [saleor/asgi/tests/test_usage_telemetry.py:52]

**`saleor/asgi/usage_telemetry.py`**

- `send_usage_telemetry_task` (function) — [saleor/asgi/usage_telemetry.py:28]
- `get_usage_telemetry` (function) — [saleor/asgi/usage_telemetry.py:49]
- `send_usage_telemetry` (function) — [saleor/asgi/usage_telemetry.py:170]
- `update_usage_telemetry_reported_at` (function) — [saleor/asgi/usage_telemetry.py:194]
- `usage_telemetry_middleware` (function) — [saleor/asgi/usage_telemetry.py:205]
- `wrapper` (function) — [saleor/asgi/usage_telemetry.py:213]

## How it works

The module's files, as provided to this run:

- `saleor/asgi/tests/asgi_test_utils.py` (36 lines)
- `saleor/asgi/__init__.py` (47 lines)
- `saleor/asgi/asgi_handler.py` (126 lines)
- `saleor/asgi/cors_handler.py` (111 lines)
- `saleor/asgi/gzip_compression.py` (165 lines)
- `saleor/asgi/health_check.py` (30 lines)
- `saleor/asgi/telemetry.py` (28 lines)
- `saleor/asgi/tests/__init__.py` (1 lines)
- `saleor/asgi/tests/conftest.py` (54 lines)
- `saleor/asgi/tests/test_cors.py` (146 lines)
- `saleor/asgi/tests/test_gzip.py` (207 lines)
- `saleor/asgi/tests/test_healthcheck.py` (46 lines)
- `saleor/asgi/tests/test_telemetry.py` (90 lines)
- `saleor/asgi/tests/test_usage_telemetry.py` (63 lines)
- `saleor/asgi/usage_telemetry.py` (234 lines)

## Interactions

- Imports from: `saleor/app`, `saleor`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...__version__`
- `...asgi.telemetry.get_hostname`
- `...asgi.telemetry.telemetry_middleware`
- `...core.telemetry.saleor_attributes.SALEOR_ENVIRONMENT_DOMAIN`
- `..attribute.AttributeEntityType`
- `..attribute.AttributeInputType`
- `..attribute.AttributeType`
- `..core.http_client.HTTPClient`
- `..core.telemetry.initialize_telemetry`
- `..core.telemetry.saleor_attributes`
- `..core.telemetry.set_global_attributes`
- `..cors_handler.cors_handler`
- `..gzip_compression.gzip_compression`
- `..usage_telemetry.get_usage_telemetry`
- `.asgi_handler.get_asgi_application`
- `.cors_handler.cors_handler`
- `.gzip_compression.gzip_compression`
- `.health_check.health_check`
- `.telemetry.telemetry_middleware`
- `.usage_telemetry.usage_telemetry_middleware`
- `saleor.asgi.health_check`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `bb7fc09f56c7` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
