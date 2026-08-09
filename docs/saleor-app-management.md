## Purpose

`saleor/app/management` (`saleor/app/management`) groups 6 source file(s) exposing 12 top-level declaration(s).

## Public surface

**`saleor/app/management/commands/app_delete_all.py`**

- `Command` (class) — [saleor/app/management/commands/app_delete_all.py:11]
- `add_arguments` (function) — [saleor/app/management/commands/app_delete_all.py:17]
- `handle` (function) — [saleor/app/management/commands/app_delete_all.py:25]

**`saleor/app/management/commands/create_app.py`**

- `Command` (class) — [saleor/app/management/commands/create_app.py:18]
- `add_arguments` (function) — [saleor/app/management/commands/create_app.py:21]
- `send_app_data` (function) — [saleor/app/management/commands/create_app.py:60]
- `handle` (function) — [saleor/app/management/commands/create_app.py:81]

**`saleor/app/management/commands/install_app.py`**

- `Command` (class) — [saleor/app/management/commands/install_app.py:16]
- `add_arguments` (function) — [saleor/app/management/commands/install_app.py:19]
- `validate_manifest_url` (function) — [saleor/app/management/commands/install_app.py:34]
- `handle` (function) — [saleor/app/management/commands/install_app.py:43]

**`saleor/app/management/commands/utils.py`**

- `clean_permissions` (function) — [saleor/app/management/commands/utils.py:10]

## How it works

The module's files, as provided to this run:

- `saleor/app/management/__init__.py` (1 lines)
- `saleor/app/management/commands/__init__.py` (1 lines)
- `saleor/app/management/commands/app_delete_all.py` (42 lines)
- `saleor/app/management/commands/create_app.py` (103 lines)
- `saleor/app/management/commands/install_app.py` (82 lines)
- `saleor/app/management/commands/utils.py` (28 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....schema_version`
- `....app.headers.AppHeaders`
- `....app.headers.DeprecatedAppHeaders`
- `....app.models.App`
- `....app.validators.AppURLValidator`
- `....core.JobStatus`
- `....core.http_client.HTTPClient`
- `....core.utils.build_absolute_uri`
- `....core.utils.get_domain`
- `....plugins.manager.get_plugins_manager`
- `...actions.delete_app`
- `...installation_utils.fetch_manifest`
- `...installation_utils.install_app`
- `...models.App`
- `...models.AppInstallation`
- `.utils.clean_permissions`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `e92f045595e4` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
