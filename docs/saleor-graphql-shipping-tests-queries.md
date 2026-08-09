## Purpose

`saleor/graphql/shipping/tests/queries` (`saleor/graphql/shipping/tests/queries`) groups 4 source file(s) exposing 14 top-level declaration(s).

## Public surface

**`saleor/graphql/shipping/tests/queries/test_shipping_zone.py`**

- `test_shipping_zone_query` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zone.py:57]
- `test_shipping_zone_query_weights_returned_in_default_unit` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zone.py:90]
- `test_staff_query_shipping_zone_by_invalid_id` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zone.py:142]
- `test_staff_query_shipping_zone_object_given_id_does_not_exists` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zone.py:163]
- `test_shipping_method_tax_class_query_by_app` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zone.py:194]
- `test_shipping_method_tax_class_query_by_staff` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zone.py:212]
- `test_query_channels_when_channel_deleted_during_load` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zone.py:241]
- `delete_channel` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zone.py:249]

**`saleor/graphql/shipping/tests/queries/test_shipping_zones_filtering.py`**

- `test_query_shipping_zone_search_by_name` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zones_filtering.py:30]
- `test_query_shipping_zone_search_by_channels` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zones_filtering.py:51]
- `test_query_shipping_zone_search_by_channels_no_matter_of_input` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zones_filtering.py:77]

**`saleor/graphql/shipping/tests/queries/test_shipping_zones.py`**

- `test_shipping_zones_query` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zones.py:37]
- `test_shipping_methods_query_with_channel` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zones.py:60]
- `test_shipping_methods_query` (function) — [saleor/graphql/shipping/tests/queries/test_shipping_zones.py:87]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/shipping/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/shipping/tests/queries/test_shipping_zone.py` (267 lines)
- `saleor/graphql/shipping/tests/queries/test_shipping_zones_filtering.py` (104 lines)
- `saleor/graphql/shipping/tests/queries/test_shipping_zones.py` (109 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....channel.models.Channel`
- `.....core.db.connection.allow_writer`
- `.....core.units.WeightUnits`
- `.....tests.race_condition`
- `....shipping.resolvers.resolve_price_range`
- `....tests.utils.get_graphql_content`
- `....tests.utils.get_graphql_content_from_response`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `b9df6fdbc57a` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
