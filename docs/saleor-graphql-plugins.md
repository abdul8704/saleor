## Purpose

`saleor/graphql/plugins` (`saleor/graphql/plugins`) groups 15 source file(s) exposing 77 top-level declaration(s).

## Public surface

**`saleor/graphql/plugins/dataloaders.py`**

- `EmailTemplatesByPluginConfigurationLoader` (class) — [saleor/graphql/plugins/dataloaders.py:14]
- `batch_load` (function) — [saleor/graphql/plugins/dataloaders.py:19]
- `PluginManagerByRequestorDataloader` (class) — [saleor/graphql/plugins/dataloaders.py:31]
- `batch_load` (function) — [saleor/graphql/plugins/dataloaders.py:34]
- `AnonymousPluginManagerLoader` (class) — [saleor/graphql/plugins/dataloaders.py:39]
- `batch_load` (function) — [saleor/graphql/plugins/dataloaders.py:42]
- `plugin_manager_promise` (function) — [saleor/graphql/plugins/dataloaders.py:50]
- `get_plugin_manager_promise` (function) — [saleor/graphql/plugins/dataloaders.py:58]
- `plugin_manager_promise_callback` (function) — [saleor/graphql/plugins/dataloaders.py:63]

**`saleor/graphql/plugins/enums.py`**

- `PluginConfigurationType` (class) — [saleor/graphql/plugins/enums.py:11]

**`saleor/graphql/plugins/filters.py`**

- `filter_plugin_status_in_channels` (function) — [saleor/graphql/plugins/filters.py:10]
- `filter_plugin_by_type` (function) — [saleor/graphql/plugins/filters.py:35]
- `filter_plugin_search` (function) — [saleor/graphql/plugins/filters.py:43]
- `PluginStatusInChannelsInput` (class) — [saleor/graphql/plugins/filters.py:57]
- `PluginFilterInput` (class) — [saleor/graphql/plugins/filters.py:62]

**`saleor/graphql/plugins/mutations.py`**

- `ConfigurationItemInput` (class) — [saleor/graphql/plugins/mutations.py:16]
- `PluginUpdateInput` (class) — [saleor/graphql/plugins/mutations.py:23]
- `PluginUpdate` (class) — [saleor/graphql/plugins/mutations.py:34]
- `Arguments` (class) — [saleor/graphql/plugins/mutations.py:37]
- `Meta` (class) — [saleor/graphql/plugins/mutations.py:48]
- `clean_input` (function) — [saleor/graphql/plugins/mutations.py:55]
- `perform_mutation` (function) — [saleor/graphql/plugins/mutations.py:97]

**`saleor/graphql/plugins/resolvers.py`**

- `hide_private_configuration_fields` (function) — [saleor/graphql/plugins/resolvers.py:15]
- `aggregate_plugins_configuration` (function) — [saleor/graphql/plugins/resolvers.py:40]
- `resolve_plugin` (function) — [saleor/graphql/plugins/resolvers.py:57]
- `resolve_plugins` (function) — [saleor/graphql/plugins/resolvers.py:72]

**`saleor/graphql/plugins/schema.py`**

- `PluginsQueries` (class) — [saleor/graphql/plugins/schema.py:17]
- `resolve_plugin` (function) — [saleor/graphql/plugins/schema.py:42]
- `resolve_plugins` (function) — [saleor/graphql/plugins/schema.py:48]
- `PluginsMutations` (class) — [saleor/graphql/plugins/schema.py:56]

**`saleor/graphql/plugins/sorters.py`**

- `sort_active_key` (function) — [saleor/graphql/plugins/sorters.py:8]
- `sort_plugins` (function) — [saleor/graphql/plugins/sorters.py:20]
- `PluginSortField` (class) — [saleor/graphql/plugins/sorters.py:40]
- `description` (function) — [saleor/graphql/plugins/sorters.py:45]
- `PluginSortingInput` (class) — [saleor/graphql/plugins/sorters.py:56]
- `Meta` (class) — [saleor/graphql/plugins/sorters.py:57]

**`saleor/graphql/plugins/tests/conftest.py`**

- `staff_api_client_can_manage_plugins` (function) — [saleor/graphql/plugins/tests/conftest.py:5]

**`saleor/graphql/plugins/tests/queries/test_plugin.py`**

- `test_query_plugin_hides_secret_fields` (function) — [saleor/graphql/plugins/tests/queries/test_plugin.py:58]
- `test_query_plugin_hides_secret_fields_for_channel_configurations` (function) — [saleor/graphql/plugins/tests/queries/test_plugin.py:109]
- `test_query_plugin_configuration` (function) — [saleor/graphql/plugins/tests/queries/test_plugin.py:158]
- `test_query_plugin_configuration_for_channel_configurations` (function) — [saleor/graphql/plugins/tests/queries/test_plugin.py:180]
- `test_query_plugin_configuration_for_multiple_channels` (function) — [saleor/graphql/plugins/tests/queries/test_plugin.py:208]
- `test_query_plugin_configuration_for_invalid_plugin_name` (function) — [saleor/graphql/plugins/tests/queries/test_plugin.py:232]
- `test_query_plugin_configuration_as_customer_user` (function) — [saleor/graphql/plugins/tests/queries/test_plugin.py:242]
- `test_cannot_retrieve_hidden_plugin` (function) — [saleor/graphql/plugins/tests/queries/test_plugin.py:253]
- `test_cannot_retrieve_hidden_multichannel_plugin` (function) — [saleor/graphql/plugins/tests/queries/test_plugin.py:272]

**`saleor/graphql/plugins/tests/queries/test_plugins.py`**

- `test_query_plugin_configurations` (function) — [saleor/graphql/plugins/tests/queries/test_plugins.py:51]
- `test_query_plugin_configurations_for_channel_configurations` (function) — [saleor/graphql/plugins/tests/queries/test_plugins.py:91]
- `test_query_plugins_hides_secret_fields` (function) — [saleor/graphql/plugins/tests/queries/test_plugins.py:156]
- `test_query_plugins_hides_secret_fields_for_channel_configurations` (function) — [saleor/graphql/plugins/tests/queries/test_plugins.py:219]
- `test_query_plugin_configurations_as_customer_user` (function) — [saleor/graphql/plugins/tests/queries/test_plugins.py:273]
- `test_plugins_query_with_filter` (function) — [saleor/graphql/plugins/tests/queries/test_plugins.py:296]
- `test_query_plugins_with_sort` (function) — [saleor/graphql/plugins/tests/queries/test_plugins.py:370]
- `test_cannot_retrieve_hidden_plugins` (function) — [saleor/graphql/plugins/tests/queries/test_plugins.py:389]

**`saleor/graphql/plugins/tests/test_mutation_plugin_update.py`**

- `test_plugin_configuration_update` (function) — [saleor/graphql/plugins/tests/test_mutation_plugin_update.py:78]
- `test_plugin_configuration_update_value_not_given` (function) — [saleor/graphql/plugins/tests/test_mutation_plugin_update.py:119]
- `test_plugin_configuration_update_for_channel_configurations` (function) — [saleor/graphql/plugins/tests/test_mutation_plugin_update.py:170]
- `test_plugin_configuration_update_channel_slug_required` (function) — [saleor/graphql/plugins/tests/test_mutation_plugin_update.py:211]
- `test_plugin_configuration_update_unneeded_channel_slug` (function) — [saleor/graphql/plugins/tests/test_mutation_plugin_update.py:239]
- `test_plugin_configuration_update_containing_invalid_plugin_id` (function) — [saleor/graphql/plugins/tests/test_mutation_plugin_update.py:265]
- `test_plugin_update_saves_boolean_as_boolean` (function) — [saleor/graphql/plugins/tests/test_mutation_plugin_update.py:284]
- `test_plugin_configuration_update_as_customer_user` (function) — [saleor/graphql/plugins/tests/test_mutation_plugin_update.py:306]
- `test_cannot_update_configuration_of_hidden_plugin` (function) — [saleor/graphql/plugins/tests/test_mutation_plugin_update.py:322]
- `test_cannot_update_configuration_of_hidden_multichannel_plugin` (function) — [saleor/graphql/plugins/tests/test_mutation_plugin_update.py:364]

**`saleor/graphql/plugins/types.py`**

- `ConfigurationItem` (class) — [saleor/graphql/plugins/types.py:15]
- `Meta` (class) — [saleor/graphql/plugins/types.py:22]
- `PluginConfiguration` (class) — [saleor/graphql/plugins/types.py:26]
- `Meta` (class) — [saleor/graphql/plugins/types.py:38]
- `resolve_configuration` (function) — [saleor/graphql/plugins/types.py:42]
- `Plugin` (class) — [saleor/graphql/plugins/types.py:46]
- `Meta` (class) — [saleor/graphql/plugins/types.py:62]
- `resolve_name` (function) — [saleor/graphql/plugins/types.py:66]
- `resolve_description` (function) — [saleor/graphql/plugins/types.py:70]
- `resolve_global_configuration` (function) — [saleor/graphql/plugins/types.py:74]
- `resolve_channel_configurations` (function) — [saleor/graphql/plugins/types.py:78]
- `PluginCountableConnection` (class) — [saleor/graphql/plugins/types.py:82]
- `Meta` (class) — [saleor/graphql/plugins/types.py:83]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/plugins/__init__.py` (1 lines)
- `saleor/graphql/plugins/dataloaders.py` (70 lines)
- `saleor/graphql/plugins/enums.py` (13 lines)
- `saleor/graphql/plugins/filters.py` (65 lines)
- `saleor/graphql/plugins/mutations.py` (107 lines)
- `saleor/graphql/plugins/resolvers.py` (117 lines)
- `saleor/graphql/plugins/schema.py` (57 lines)
- `saleor/graphql/plugins/sorters.py` (59 lines)
- `saleor/graphql/plugins/tests/__init__.py` (1 lines)
- `saleor/graphql/plugins/tests/conftest.py` (7 lines)
- `saleor/graphql/plugins/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/plugins/tests/queries/test_plugin.py` (290 lines)
- `saleor/graphql/plugins/tests/queries/test_plugins.py` (429 lines)
- `saleor/graphql/plugins/tests/test_mutation_plugin_update.py` (407 lines)
- `saleor/graphql/plugins/types.py` (84 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....plugins.base_plugin.ConfigurationTypeField`
- `.....plugins.manager.get_plugins_manager`
- `.....plugins.tests.sample_plugins.ChannelPluginSample`
- `.....plugins.tests.sample_plugins.PluginSample`
- `....plugins.error_codes.PluginErrorCode`
- `....plugins.manager.get_plugins_manager`
- `....plugins.models.PluginConfiguration`
- `....plugins.tests.sample_plugins.ChannelPluginSample`
- `....plugins.tests.sample_plugins.PluginSample`
- `....plugins.tests.utils.get_config_value`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...core.middleware.Requestor`
- `...graphql.core.enums.to_enum`
- `...permission.enums.PluginsPermissions`
- `...plugins.base_plugin.BasePlugin`
- `...plugins.base_plugin.ConfigurationTypeField`
- `...plugins.error_codes.PluginErrorCode`
- `...plugins.manager.PluginsManager`
- `...plugins.manager.get_plugins_manager`
- `...plugins.models.EmailTemplate`
- `...tests.utils.assert_no_permission`
- `...tests.utils.get_graphql_content`
- `..app.dataloaders.get_app_promise`
- `..channel.types.Channel`
- `..core.ResolveInfo`
- `..core.SaleorContext`
- `..core.connection.CountableConnection`
- `..core.connection.create_connection_slice`
- `..core.context.get_database_connection_name`
- `..core.dataloaders.DataLoader`
- `..core.enums.OrderDirection`
- `..core.fields.ConnectionField`
- `..core.fields.PermissionsField`
- `..core.mutations.BaseMutation`
- `..core.tracing.traced_resolver`
- `..core.types.NonNullList`
- `..core.types.PluginError`
- `..core.types.SortInputObjectType`
- `..utils.get_nodes`
- `.dataloaders.get_plugin_manager_promise`
- `.dataloaders.plugin_manager_promise_callback`
- `.enums.ConfigurationTypeFieldEnum`
- `.enums.PluginConfigurationType`
- `.filters.PluginFilterInput`
- `.mutations.PluginUpdate`
- `.resolvers.resolve_plugin`
- `.resolvers.resolve_plugins`
- `.sorters.PluginSortingInput`
- `.sorters.sort_plugins`
- `.types.Plugin`
- `.types.PluginCountableConnection`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `8cc7b6299039` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
