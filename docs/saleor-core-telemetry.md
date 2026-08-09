## Purpose

`saleor/core/telemetry` (`saleor/core/telemetry`) groups 10 source file(s) exposing 104 top-level declaration(s).

## Public surface

**`saleor/core/telemetry/__init__.py`**

- `load_object` (function) — [saleor/core/telemetry/__init__.py:23]
- `otel_configure_sdk` (function) — [saleor/core/telemetry/__init__.py:28]
- `initialize_telemetry` (function) — [saleor/core/telemetry/__init__.py:33]
- `get_task_context` (function) — [saleor/core/telemetry/__init__.py:58]

**`saleor/core/telemetry/metric.py`**

- `DuplicateMetricError` (class) — [saleor/core/telemetry/metric.py:23]
- `MetricType` (class) — [saleor/core/telemetry/metric.py:28]
- `get_instrument_method` (function) — [saleor/core/telemetry/metric.py:54]
- `Meter` (class) — [saleor/core/telemetry/metric.py:62]
- `create_metric` (function) — [saleor/core/telemetry/metric.py:114]
- `record` (function) — [saleor/core/telemetry/metric.py:148]
- `record_duration` (function) — [saleor/core/telemetry/metric.py:173]
- `MeterProxy` (class) — [saleor/core/telemetry/metric.py:188]
- `initialize` (function) — [saleor/core/telemetry/metric.py:200]
- `create_metric` (function) — [saleor/core/telemetry/metric.py:208]
- `record` (function) — [saleor/core/telemetry/metric.py:240]

**`saleor/core/telemetry/tests/__init__.py`**

- `TestTracer` (class) — [saleor/core/telemetry/tests/__init__.py:33]
- `inject_context` (function) — [saleor/core/telemetry/tests/__init__.py:39]
- `TestMeter` (class) — [saleor/core/telemetry/tests/__init__.py:44]

**`saleor/core/telemetry/tests/test_init.py`**

- `Invalid` (class) — [saleor/core/telemetry/tests/test_init.py:6]
- `test_initialize_telemetry_invalid_tracer_class` (function) — [saleor/core/telemetry/tests/test_init.py:10]
- `test_initialize_telemetry_invalid_meter_class` (function) — [saleor/core/telemetry/tests/test_init.py:20]

**`saleor/core/telemetry/tests/test_metric.py`**

- `test_get_instrument_method_add` (function) — [saleor/core/telemetry/tests/test_metric.py:19]
- `test_get_instrument_method_record` (function) — [saleor/core/telemetry/tests/test_metric.py:31]
- `test_meter_initialization` (function) — [saleor/core/telemetry/tests/test_metric.py:44]
- `test_meter_create_counter` (function) — [saleor/core/telemetry/tests/test_metric.py:57]
- `test_meter_create_up_down_counter` (function) — [saleor/core/telemetry/tests/test_metric.py:79]
- `test_meter_create_histogram` (function) — [saleor/core/telemetry/tests/test_metric.py:101]
- `test_meter_create_unsupported_metric_type` (function) — [saleor/core/telemetry/tests/test_metric.py:126]
- `test_meter_create_core_metric` (function) — [saleor/core/telemetry/tests/test_metric.py:138]
- `test_meter_create_service_metric` (function) — [saleor/core/telemetry/tests/test_metric.py:162]
- `test_create_duplicate_metric` (function) — [saleor/core/telemetry/tests/test_metric.py:186]
- `test_meter_record` (function) — [saleor/core/telemetry/tests/test_metric.py:205]
- `test_meter_record_with_different_unit` (function) — [saleor/core/telemetry/tests/test_metric.py:225]
- `test_meter_record_non_existent_metric` (function) — [saleor/core/telemetry/tests/test_metric.py:247]
- `test_meter_record_duration` (function) — [saleor/core/telemetry/tests/test_metric.py:258]
- `test_meter_proxy_initialize` (function) — [saleor/core/telemetry/tests/test_metric.py:274]
- `test_meter_proxy_create_metric_without_meter` (function) — [saleor/core/telemetry/tests/test_metric.py:311]
- `test_meter_proxy_create_duplicate_metric_without_meter` (function) — [saleor/core/telemetry/tests/test_metric.py:335]
- `test_meter_proxy_create_metric_with_meter` (function) — [saleor/core/telemetry/tests/test_metric.py:356]
- `test_meter_proxy_record_with_meter` (function) — [saleor/core/telemetry/tests/test_metric.py:384]
- `test_meter_create_histogram_with_explicit_bucket_boundaries` (function) — [saleor/core/telemetry/tests/test_metric.py:407]

**`saleor/core/telemetry/tests/test_trace.py`**

- `test_tracer_initialization` (function) — [saleor/core/telemetry/tests/test_trace.py:11]
- `test_tracer_start_as_current_span` (function) — [saleor/core/telemetry/tests/test_trace.py:25]
- `mock_get_tracer_func` (function) — [saleor/core/telemetry/tests/test_trace.py:38]
- `test_tracer_start_span` (function) — [saleor/core/telemetry/tests/test_trace.py:61]
- `mock_get_tracer_func` (function) — [saleor/core/telemetry/tests/test_trace.py:71]
- `test_tracer_get_current_span` (function) — [saleor/core/telemetry/tests/test_trace.py:92]
- `test_tracer_proxy_initialize` (function) — [saleor/core/telemetry/tests/test_trace.py:107]
- `test_tracer_proxy_start_as_current_span_with_tracer` (function) — [saleor/core/telemetry/tests/test_trace.py:123]
- `test_tracer_proxy_start_span_with_tracer` (function) — [saleor/core/telemetry/tests/test_trace.py:149]
- `test_tracer_proxy_get_current_span_with_tracer` (function) — [saleor/core/telemetry/tests/test_trace.py:175]
- `test_tracer_proxy_start_as_current_span_without_tracer` (function) — [saleor/core/telemetry/tests/test_trace.py:191]
- `test_tracer_proxy_start_span_without_tracer` (function) — [saleor/core/telemetry/tests/test_trace.py:201]
- `test_tracer_proxy_get_current_span_without_tracer` (function) — [saleor/core/telemetry/tests/test_trace.py:212]
- `test_span_set_attributes` (function) — [saleor/core/telemetry/tests/test_trace.py:223]
- `test_span_set_operation_name` (function) — [saleor/core/telemetry/tests/test_trace.py:241]
- `test_span_override_operation_name` (function) — [saleor/core/telemetry/tests/test_trace.py:256]

**`saleor/core/telemetry/tests/test_utils.py`**

- `test_scope_is_service` (function) — [saleor/core/telemetry/tests/test_utils.py:22]
- `test_convert_unit_same_unit` (function) — [saleor/core/telemetry/tests/test_utils.py:27]
- `test_convert_unit_supported_conversions` (function) — [saleor/core/telemetry/tests/test_utils.py:34]
- `test_convert_unit_unsupported_conversion` (function) — [saleor/core/telemetry/tests/test_utils.py:50]
- `test_convert_unit_unsupported_conversion_with_raising_disabled` (function) — [saleor/core/telemetry/tests/test_utils.py:55]
- `test_global_attributes` (function) — [saleor/core/telemetry/tests/test_utils.py:67]
- `test_enrich_with_global_attributes` (function) — [saleor/core/telemetry/tests/test_utils.py:91]
- `test_enrich_with_global_attributes_none` (function) — [saleor/core/telemetry/tests/test_utils.py:108]
- `test_enrich_span_with_global_attributes` (function) — [saleor/core/telemetry/tests/test_utils.py:120]
- `test_enrich_span_with_global_attributes_none` (function) — [saleor/core/telemetry/tests/test_utils.py:137]
- `test_telemetry_task_context_to_dict` (function) — [saleor/core/telemetry/tests/test_utils.py:150]
- `test_telemetry_task_context_to_dict_skip_link_to_invalid_span` (function) — [saleor/core/telemetry/tests/test_utils.py:175]
- `test_telemetry_task_context_to_dict_is_json_serializable` (function) — [saleor/core/telemetry/tests/test_utils.py:187]
- `test_telemetry_task_context_from_dict` (function) — [saleor/core/telemetry/tests/test_utils.py:226]
- `test_telemetry_task_context_from_dict_invalid` (function) — [saleor/core/telemetry/tests/test_utils.py:255]
- `test_telemetry_task_context_from_dict_empty` (function) — [saleor/core/telemetry/tests/test_utils.py:269]
- `test_telemetry_task_context_from_dict_skip_link_to_invalid_span` (function) — [saleor/core/telemetry/tests/test_utils.py:278]
- `test_task_with_telemetry_context_decorator` (function) — [saleor/core/telemetry/tests/test_utils.py:302]
- `test_task_with_telemetry_context_decorator_no_context` (function) — [saleor/core/telemetry/tests/test_utils.py:322]
- `test_task_with_telemetry_context_decorator_invalid_links_context` (function) — [saleor/core/telemetry/tests/test_utils.py:340]
- `test_task_with_telemetry_context_decorator_invalid_context` (function) — [saleor/core/telemetry/tests/test_utils.py:357]

**`saleor/core/telemetry/trace.py`**

- `Tracer` (class) — [saleor/core/telemetry/trace.py:24]
- `extract_context` (function) — [saleor/core/telemetry/trace.py:53]
- `start_as_current_span` (function) — [saleor/core/telemetry/trace.py:70]
- `start_span` (function) — [saleor/core/telemetry/trace.py:117]
- `get_current_span` (function) — [saleor/core/telemetry/trace.py:160]
- `inject_context` (function) — [saleor/core/telemetry/trace.py:164]
- `TracerProxy` (class) — [saleor/core/telemetry/trace.py:168]
- `initialize` (function) — [saleor/core/telemetry/trace.py:178]
- `extract_context` (function) — [saleor/core/telemetry/trace.py:184]
- `start_as_current_span` (function) — [saleor/core/telemetry/trace.py:194]
- `start_span` (function) — [saleor/core/telemetry/trace.py:225]
- `get_current_span` (function) — [saleor/core/telemetry/trace.py:252]
- `inject_context` (function) — [saleor/core/telemetry/trace.py:257]

**`saleor/core/telemetry/utils.py`**

- `Scope` (class) — [saleor/core/telemetry/utils.py:22]
- `is_service` (function) — [saleor/core/telemetry/utils.py:27]
- `Unit` (class) — [saleor/core/telemetry/utils.py:31]
- `convert_unit` (function) — [saleor/core/telemetry/utils.py:50]
- `set_global_attributes` (function) — [saleor/core/telemetry/utils.py:64]
- `get_global_attributes` (function) — [saleor/core/telemetry/utils.py:72]
- `enrich_with_global_attributes` (function) — [saleor/core/telemetry/utils.py:76]
- `enrich_span_with_global_attributes` (function) — [saleor/core/telemetry/utils.py:80]
- `TelemetryTaskContext` (class) — [saleor/core/telemetry/utils.py:87]
- `to_dict` (function) — [saleor/core/telemetry/utils.py:96]
- `from_dict` (function) — [saleor/core/telemetry/utils.py:116]
- `task_with_telemetry_context` (function) — [saleor/core/telemetry/utils.py:137]
- `wrapper` (function) — [saleor/core/telemetry/utils.py:146]

## How it works

The module's files, as provided to this run:

- `saleor/core/telemetry/trace.py` (260 lines)
- `saleor/core/telemetry/__init__.py` (78 lines)
- `saleor/core/telemetry/metric.py` (249 lines)
- `saleor/core/telemetry/saleor_attributes.py` (32 lines)
- `saleor/core/telemetry/tests/__init__.py` (46 lines)
- `saleor/core/telemetry/tests/test_init.py` (27 lines)
- `saleor/core/telemetry/tests/test_metric.py` (446 lines)
- `saleor/core/telemetry/tests/test_trace.py` (271 lines)
- `saleor/core/telemetry/tests/test_utils.py` (367 lines)
- `saleor/core/telemetry/utils.py` (161 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/csv/utils`, `saleor/core`, `saleor/plugins/openid_connect`
- Imported by: `saleor/webhook/transport/asynchronous`, `saleor/webhook/transport/synchronous`, `saleor/graphql/core/tests`, `saleor/graphql/tests`, `saleor/graphql`, `saleor/tests`

Internal dependencies named in the source:

- `....__version__`
- `....tests.utils.get_metric_data`
- `...initialize_telemetry`
- `...meter`
- `...saleor_attributes`
- `...tracer`
- `..metric.Meter`
- `..trace.Tracer`
- `..trace.TracerProxy`
- `..utils.Scope`
- `..utils.Unit`
- `.metric.DEFAULT_DURATION_BUCKETS`
- `.metric.Meter`
- `.metric.MeterProxy`
- `.metric.MetricType`
- `.saleor_attributes.OPERATION_NAME`
- `.trace.Link`
- `.trace.SpanKind`
- `.trace.Tracer`
- `.trace.TracerProxy`
- `.utils.Scope`
- `.utils.enrich_span_with_global_attributes`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `604d2287d716` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
