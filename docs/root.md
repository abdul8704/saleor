## Purpose

`(root)` (`(root)`) groups 23 source file(s) exposing 25 top-level declaration(s).

## Public surface

**`AGENTS.md`**

- `test_something` (function) — [AGENTS.md:118]
- `test_authorization` (function) — [AGENTS.md:218]
- `my_model_qs_select_for_update` (function) — [AGENTS.md:368]
- `foo` (function) — [AGENTS.md:529]
- `foo` (function) — [AGENTS.md:538]

**`CLAUDE.md`**

- `test_something` (function) — [CLAUDE.md:118]
- `test_authorization` (function) — [CLAUDE.md:218]
- `my_model_qs_select_for_update` (function) — [CLAUDE.md:368]
- `foo` (function) — [CLAUDE.md:529]
- `foo` (function) — [CLAUDE.md:538]

**`conftest.py`**

- `django_db_setup` (function) — [conftest.py:56]
- `Custom` (class) — [conftest.py:72]

**`CONTRIBUTING.md`**

- `test_apps_for_federation_query_count` (function) — [CONTRIBUTING.md:279]
- `AppError` (class) — [CONTRIBUTING.md:469]
- `AppSortField` (class) — [CONTRIBUTING.md:483]
- `description` (function) — [CONTRIBUTING.md:488]
- `AppSortingInput` (class) — [CONTRIBUTING.md:495]
- `Meta` (class) — [CONTRIBUTING.md:496]
- `AppFilterInput` (class) — [CONTRIBUTING.md:530]
- `Meta` (class) — [CONTRIBUTING.md:531]
- `AppFilter` (class) — [CONTRIBUTING.md:535]
- `Meta` (class) — [CONTRIBUTING.md:540]
- `AppCountableConnection` (class) — [CONTRIBUTING.md:548]
- `Meta` (class) — [CONTRIBUTING.md:549]
- `AppQueries` (class) — [CONTRIBUTING.md:558]

## How it works

The module's files, as provided to this run:

- `.devcontainer/devcontainer.json` (41 lines)
- `.github/dependabot.yml` (19 lines)
- `.github/DISCUSSION_TEMPLATE/RFC.yml` (82 lines)
- `.github/graphql-inspector.yaml` (11 lines)
- `.github/ISSUE_TEMPLATE/bug_report.yaml` (49 lines)
- `.github/ISSUE_TEMPLATE/config.yml` (5 lines)
- `.github/ISSUE_TEMPLATE/feature_request.yaml` (118 lines)
- `.github/PULL_REQUEST_TEMPLATE.md` (32 lines)
- `.github/stale.yml` (60 lines)
- `.pre-commit-config.yaml` (79 lines)
- `.release-it.json` (43 lines)
- `AGENTS.md` (612 lines)
- `CHANGELOG.md` (66 lines)
- `CLAUDE.md` (612 lines)
- `conftest.py` (89 lines)
- `CONTRIBUTING.md` (680 lines)
- `deployment/elasticbeanstalk/Dockerrun.aws.json` (12 lines)
- `manage.py` (10 lines)
- `SECURITY.md` (55 lines)
- `socket.yml` (18 lines)
- `templates/graphql/playground.html` (37 lines)
- `templates/home/index.html` (215 lines)
- `templates/price.html` (23 lines)

## Interactions

- Imports from: `saleor/tests`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `saleor.core.tracing.traced_atomic_transaction`
- `saleor.core.utils.events.call_event`
- `saleor.tests.utils.prepare_test_db_connections`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `b61828396ea0` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
