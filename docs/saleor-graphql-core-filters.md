## Purpose

`saleor/graphql/core/filters` (`saleor/graphql/core/filters`) groups 6 source file(s) exposing 77 top-level declaration(s).

## Public surface

**`saleor/graphql/core/filters/filter_input.py`**

- `GraphQLFilterSetMixin` (class) — [saleor/graphql/core/filters/filter_input.py:23]
- `get_filterset_class` (function) — [saleor/graphql/core/filters/filter_input.py:29]
- `FilterInputObjectType` (class) — [saleor/graphql/core/filters/filter_input.py:37]
- `get_filtering_args_from_filterset` (function) — [saleor/graphql/core/filters/filter_input.py:66]
- `ChannelFilterInputObjectType` (class) — [saleor/graphql/core/filters/filter_input.py:93]
- `Meta` (class) — [saleor/graphql/core/filters/filter_input.py:102]

**`saleor/graphql/core/filters/filters.py`**

- `DefaultMultipleChoiceField` (class) — [saleor/graphql/core/filters/filters.py:12]
- `to_python` (function) — [saleor/graphql/core/filters/filters.py:15]
- `validate` (function) — [saleor/graphql/core/filters/filters.py:22]
- `EnumFilter` (class) — [saleor/graphql/core/filters/filters.py:33]
- `ListObjectTypeFilter` (class) — [saleor/graphql/core/filters/filters.py:47]
- `ObjectTypeFilter` (class) — [saleor/graphql/core/filters/filters.py:55]
- `DefaultOperationField` (class) — [saleor/graphql/core/filters/filters.py:61]
- `validate` (function) — [saleor/graphql/core/filters/filters.py:62]
- `OperationObjectTypeFilter` (class) — [saleor/graphql/core/filters/filters.py:68]
- `MetadataFilter` (class) — [saleor/graphql/core/filters/filters.py:76]
- `MetadataFilterBase` (class) — [saleor/graphql/core/filters/filters.py:81]
- `Meta` (class) — [saleor/graphql/core/filters/filters.py:84]
- `filter_created_at` (function) — [saleor/graphql/core/filters/filters.py:88]
- `filter_updated_at` (function) — [saleor/graphql/core/filters/filters.py:92]
- `filter_status` (function) — [saleor/graphql/core/filters/filters.py:96]
- `BaseJobFilter` (class) — [saleor/graphql/core/filters/filters.py:102]

**`saleor/graphql/core/filters/shared_filters.py`**

- `GlobalIDFormField` (class) — [saleor/graphql/core/filters/shared_filters.py:7]
- `clean` (function) — [saleor/graphql/core/filters/shared_filters.py:10]
- `GlobalIDFilter` (class) — [saleor/graphql/core/filters/shared_filters.py:28]
- `filter` (function) — [saleor/graphql/core/filters/shared_filters.py:31]
- `GlobalIDMultipleChoiceField` (class) — [saleor/graphql/core/filters/shared_filters.py:39]
- `to_python` (function) — [saleor/graphql/core/filters/shared_filters.py:45]
- `valid_value` (function) — [saleor/graphql/core/filters/shared_filters.py:48]
- `GlobalIDMultipleChoiceFilter` (class) — [saleor/graphql/core/filters/shared_filters.py:54]
- `filter` (function) — [saleor/graphql/core/filters/shared_filters.py:57]
- `filter_metadata` (function) — [saleor/graphql/core/filters/shared_filters.py:62]

**`saleor/graphql/core/filters/where_filters.py`**

- `WhereFilterSet` (class) — [saleor/graphql/core/filters/where_filters.py:23]
- `filter_queryset` (function) — [saleor/graphql/core/filters/where_filters.py:29]
- `WhereFilter` (class) — [saleor/graphql/core/filters/where_filters.py:51]
- `method` (function) — [saleor/graphql/core/filters/where_filters.py:53]
- `method` (function) — [saleor/graphql/core/filters/where_filters.py:59]
- `filter` (function) — [saleor/graphql/core/filters/where_filters.py:70]
- `WhereFilterMethod` (class) — [saleor/graphql/core/filters/where_filters.py:78]
- `ObjectTypeWhereFilter` (class) — [saleor/graphql/core/filters/where_filters.py:84]
- `OperationObjectTypeWhereFilter` (class) — [saleor/graphql/core/filters/where_filters.py:90]
- `ListObjectTypeWhereFilter` (class) — [saleor/graphql/core/filters/where_filters.py:98]
- `BooleanWhereFilter` (class) — [saleor/graphql/core/filters/where_filters.py:106]
- `CharWhereFilter` (class) — [saleor/graphql/core/filters/where_filters.py:110]
- `EnumWhereFilter` (class) — [saleor/graphql/core/filters/where_filters.py:114]
- `GlobalIDMultipleChoiceWhereFilter` (class) — [saleor/graphql/core/filters/where_filters.py:128]
- `filter` (function) — [saleor/graphql/core/filters/where_filters.py:131]
- `GlobalIDWhereFilter` (class) — [saleor/graphql/core/filters/where_filters.py:136]
- `filter` (function) — [saleor/graphql/core/filters/where_filters.py:139]
- `MetadataWhereFilterBase` (class) — [saleor/graphql/core/filters/where_filters.py:147]
- `Meta` (class) — [saleor/graphql/core/filters/where_filters.py:150]
- `filter_where_metadata` (function) — [saleor/graphql/core/filters/where_filters.py:154]
- `MetadataWhereBase` (class) — [saleor/graphql/core/filters/where_filters.py:178]

**`saleor/graphql/core/filters/where_input.py`**

- `WhereInputObjectType` (class) — [saleor/graphql/core/filters/where_input.py:14]
- `Meta` (class) — [saleor/graphql/core/filters/where_input.py:24]
- `FilterInputDescriptions` (class) — [saleor/graphql/core/filters/where_input.py:54]
- `StringFilterInput` (class) — [saleor/graphql/core/filters/where_input.py:63]
- `Meta` (class) — [saleor/graphql/core/filters/where_input.py:71]
- `IntFilterInput` (class) — [saleor/graphql/core/filters/where_input.py:75]
- `Meta` (class) — [saleor/graphql/core/filters/where_input.py:82]
- `DecimalFilterInput` (class) — [saleor/graphql/core/filters/where_input.py:86]
- `Meta` (class) — [saleor/graphql/core/filters/where_input.py:93]
- `DateFilterInput` (class) — [saleor/graphql/core/filters/where_input.py:97]
- `Meta` (class) — [saleor/graphql/core/filters/where_input.py:104]
- `DateTimeFilterInput` (class) — [saleor/graphql/core/filters/where_input.py:108]
- `Meta` (class) — [saleor/graphql/core/filters/where_input.py:119]
- `GlobalIDFilterInput` (class) — [saleor/graphql/core/filters/where_input.py:123]
- `Meta` (class) — [saleor/graphql/core/filters/where_input.py:131]
- `UUIDFilterInput` (class) — [saleor/graphql/core/filters/where_input.py:135]
- `Meta` (class) — [saleor/graphql/core/filters/where_input.py:143]
- `PriceFilterInput` (class) — [saleor/graphql/core/filters/where_input.py:147]
- `MetadataValueFilterInput` (class) — [saleor/graphql/core/filters/where_input.py:156]
- `Meta` (class) — [saleor/graphql/core/filters/where_input.py:162]
- `MetadataFilterInput` (class) — [saleor/graphql/core/filters/where_input.py:166]
- `Meta` (class) — [saleor/graphql/core/filters/where_input.py:176]
- `ContainsFilterInput` (class) — [saleor/graphql/core/filters/where_input.py:189]
- `Meta` (class) — [saleor/graphql/core/filters/where_input.py:201]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/core/filters/__init__.py` (77 lines)
- `saleor/graphql/core/filters/filter_input.py` (103 lines)
- `saleor/graphql/core/filters/filters.py` (109 lines)
- `saleor/graphql/core/filters/shared_filters.py` (70 lines)
- `saleor/graphql/core/filters/where_filters.py` (183 lines)
- `saleor/graphql/core/filters/where_input.py` (204 lines)

## Interactions

- Imports from: `saleor/account`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...utils.filters.filter_range_field`
- `..descriptions.DEPRECATED_IN_3X_INPUT`
- `..enums.JobStatusEnum`
- `..scalars.Date`
- `..scalars.DateTime`
- `..scalars.Decimal`
- `..scalars.UUID`
- `..types.DateTimeRangeInput`
- `..types.NonNullList`
- `..types.base.BaseInputObjectType`
- `..types.converter.convert_form_field`
- `.filter_input.FilterInputObjectType`
- `.shared_filters.GlobalIDFilter`
- `.shared_filters.GlobalIDMultipleChoiceFilter`
- `.shared_filters.filter_metadata`
- `.where_input.MetadataFilterInput`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `ae623dbd120d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
