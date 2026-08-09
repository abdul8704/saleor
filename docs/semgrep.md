## Purpose

`.semgrep` (`.semgrep`) groups 15 source file(s) exposing 46 top-level declaration(s).

## Public surface

**`.semgrep/best-practice/add-index-concurrently.py`**

- `Migration` (class) — [.semgrep/best-practice/add-index-concurrently.py:5]

**`.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py`**

- `migration_task_without_queue_set` (function) — [.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py:9]
- `migration_task_without_queue_set_and_more_decorators` (function) — [.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py:16]
- `migration_task_with_no_args` (function) — [.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py:22]
- `migration_task_with_arg` (function) — [.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py:28]
- `migration_task_with_args_and_kwargs` (function) — [.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py:34]
- `migration_task_with_queue_set_to_raw_value` (function) — [.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py:42]
- `migration_task_with_args_kwargs_and_queue_set_to_raw_value` (function) — [.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py:48]
- `migration_task_with_queue_set` (function) — [.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py:54]
- `migration_task_with_queue_set_and_more_decorators` (function) — [.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py:61]
- `migration_task_with_kwargs_and_queue_set_first` (function) — [.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py:67]
- `migration_task_with_kwargs_and_queue_set_last` (function) — [.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py:73]
- `migration_task_with_kwargs_and_queue_set_in_the_middle` (function) — [.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py:79]
- `migration_task_with_multiline_kwargs_and_queue` (function) — [.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py:85]

**`.semgrep/correctness/celery/task-logger-without-suffix.py`**

- `same_name_using___name__` (function) — [.semgrep/correctness/celery/task-logger-without-suffix.py:4]
- `same_name_with_celery_first` (function) — [.semgrep/correctness/celery/task-logger-without-suffix.py:10]
- `different_name_get_task_logger` (function) — [.semgrep/correctness/celery/task-logger-without-suffix.py:17]
- `different_name_logging_getlogger` (function) — [.semgrep/correctness/celery/task-logger-without-suffix.py:22]
- `same_name_hardcoded` (function) — [.semgrep/correctness/celery/task-logger-without-suffix.py:28]
- `same_name_without_variables` (function) — [.semgrep/correctness/celery/task-logger-without-suffix.py:34]

**`.semgrep/correctness/django/django-migration-wrong-app-config.py`**

- `wrong_app_config` (function) — [.semgrep/correctness/django/django-migration-wrong-app-config.py:6]
- `on_migrations_complete` (function) — [.semgrep/correctness/django/django-migration-wrong-app-config.py:7]
- `correct_app_config` (function) — [.semgrep/correctness/django/django-migration-wrong-app-config.py:15]
- `on_migrations_complete` (function) — [.semgrep/correctness/django/django-migration-wrong-app-config.py:16]
- `wrong_app_config_multiline` (function) — [.semgrep/correctness/django/django-migration-wrong-app-config.py:24]
- `on_migrations_complete` (function) — [.semgrep/correctness/django/django-migration-wrong-app-config.py:25]
- `correct_app_config_multiline` (function) — [.semgrep/correctness/django/django-migration-wrong-app-config.py:35]
- `on_migrations_complete` (function) — [.semgrep/correctness/django/django-migration-wrong-app-config.py:36]
- `Migration` (class) — [.semgrep/correctness/django/django-migration-wrong-app-config.py:46]

**`.semgrep/correctness/django/django-migration-wrong-app-config.yaml`**

- `Migration` (class) — [.semgrep/correctness/django/django-migration-wrong-app-config.yaml:27]
- `Migration` (class) — [.semgrep/correctness/django/django-migration-wrong-app-config.yaml:36]

**`.semgrep/correctness/django/django-no-default-token-generator.py`**

- `test_using_default_token_generator` (function) — [.semgrep/correctness/django/django-no-default-token-generator.py:1]
- `test_using_token_generator_class` (function) — [.semgrep/correctness/django/django-no-default-token-generator.py:6]
- `test_ok_not_using_django_builtin_default_token_generator` (function) — [.semgrep/correctness/django/django-no-default-token-generator.py:10]

**`.semgrep/security/logging/exception-object-in-logger-extra.py`**

- `test_log_info_exception` (function) — [.semgrep/security/logging/exception-object-in-logger-extra.py:2]
- `test_log_catch_multiple_exceptions` (function) — [.semgrep/security/logging/exception-object-in-logger-extra.py:10]
- `test_log_middle_of_statement` (function) — [.semgrep/security/logging/exception-object-in-logger-extra.py:29]
- `test_log_info_exception` (function) — [.semgrep/security/logging/exception-object-in-logger-extra.py:39]
- `test_log_multiple_extra` (function) — [.semgrep/security/logging/exception-object-in-logger-extra.py:47]
- `test_log_exception_trailing_arguments_case1` (function) — [.semgrep/security/logging/exception-object-in-logger-extra.py:55]
- `test_log_exception_trailing_arguments_case2` (function) — [.semgrep/security/logging/exception-object-in-logger-extra.py:65]
- `test_log_exception_with_finally_block` (function) — [.semgrep/security/logging/exception-object-in-logger-extra.py:74]
- `test_log_exception_with_else_block` (function) — [.semgrep/security/logging/exception-object-in-logger-extra.py:84]
- `test_log_exception_with_finally_else_block` (function) — [.semgrep/security/logging/exception-object-in-logger-extra.py:94]
- `test_not_logging_exception` (function) — [.semgrep/security/logging/exception-object-in-logger-extra.py:106]
- `test_not_logging_exception` (function) — [.semgrep/security/logging/exception-object-in-logger-extra.py:115]

## How it works

The module's files, as provided to this run:

- `.semgrep/best-practice/add-index-concurrently.py` (20 lines)
- `.semgrep/best-practice/add-index-concurrently.yaml` (13 lines)
- `.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.py` (86 lines)
- `.semgrep/correctness/celery/celery-migration-task-missing-dedicated-queue.yaml` (26 lines)
- `.semgrep/correctness/celery/task-logger-without-suffix.py` (38 lines)
- `.semgrep/correctness/celery/task-logger-without-suffix.yaml` (22 lines)
- `.semgrep/correctness/django/django-migration-wrong-app-config.py` (54 lines)
- `.semgrep/correctness/django/django-migration-wrong-app-config.yaml` (44 lines)
- `.semgrep/correctness/django/django-no-default-token-generator.py` (12 lines)
- `.semgrep/correctness/django/django-no-default-token-generator.yaml` (25 lines)
- `.semgrep/security/logging/exception-object-in-logger-extra.py` (120 lines)
- `.semgrep/security/logging/exception-object-in-logger-extra.yaml` (66 lines)
- `.semgrep/security/requests/no-use-requests-lib.fixed.py` (86 lines)
- `.semgrep/security/requests/no-use-requests-lib.py` (86 lines)
- `.semgrep/security/requests/no-use-requests-lib.yaml` (43 lines)

## Interactions

- Imports from: `saleor/core`, `saleor`, `saleor/core/db`, `saleor/attribute/tests`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `saleor.celeryconf.app`
- `saleor.core.db.connection.allow_writer`
- `saleor.core.tokens.token_generator`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `77dd7734dca2` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
