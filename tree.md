tre -a /Users/emreceng/sql-talk/
/Users/emreceng/sql-talk/sjw/
├── benchmark
│   ├── dbally_benchmark
│   │   ├── experiment_config
│   │   │   ├── iql
│   │   │   │   └── superhero.yaml
│   │   │   ├── config.yaml
│   │   │   ├── text2sql
│   │   │   │   └── superhero.yaml
│   │   │   └── e2e
│   │   │       └── superhero.yaml
│   │   ├── iql_benchmark.py
│   │   ├── config.py
│   │   ├── paths.py
│   │   ├── dataset
│   │   │   └── bird_dataset.py
│   │   ├── constants.py
│   │   ├── iql
│   │   │   ├── metrics.py
│   │   │   ├── method_call_visitor.py
│   │   │   └── iql_result.py
│   │   ├── __init__.py
│   │   ├── text2sql
│   │   │   ├── metrics.py
│   │   │   ├── text2sql_result.py
│   │   │   └── prompt_template.py
│   │   ├── e2e_benchmark.py
│   │   ├── utils.py
│   │   ├── evaluate.py
│   │   ├── views
│   │   │   └── superhero.py
│   │   └── text2sql_benchmark.py
│   ├── .DS_Store
│   └── tests
│       └── unit
│           ├── test_method_call_visitor.py
│           ├── test_iql_metrics.py
│           └── test_main_evaluate.py
├── docker
│   ├── tests
│   │   └── Dockerfile
│   └── precommit
│       └── Dockerfile
├── chroma
│   └── chroma.sqlite3
├── .DS_Store
├── mkdocs.yml
├── LICENSE
├── CHANGELOG.md
├── dist
│   └── dbally-0.5.0-py3.12.egg
├── pyproject.toml
├── tests
│   ├── unit
│   │   ├── test_nl_responder.py
│   │   ├── test_view_selector.py
│   │   ├── iql
│   │   │   ├── test_iql_parser.py
│   │   │   ├── test_type_validators.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── test_iql_parser.cpython-312-pytest-8.3.1.pyc
│   │   │       ├── test_type_validators.cpython-312-pytest-8.3.1.pyc
│   │   │       └── __init__.cpython-312.pyc
│   │   ├── similarity
│   │   │   ├── test_chroma.py
│   │   │   ├── sample_module
│   │   │   │   ├── __init__.py
│   │   │   │   ├── empty_submodule.py
│   │   │   │   └── submodule.py
│   │   │   └── __pycache__
│   │   │       └── test_chroma.cpython-312-pytest-8.3.1.pyc
│   │   ├── __init__.py
│   │   ├── test_collection.py
│   │   ├── __pycache__
│   │   │   ├── test_iql_format.cpython-312-pytest-8.3.1.pyc
│   │   │   ├── test_assistants_adapters.cpython-312-pytest-8.3.1.pyc
│   │   │   ├── test_prompt_builder.cpython-312-pytest-8.3.1.pyc
│   │   │   ├── test_fewshot.cpython-312-pytest-8.3.1.pyc
│   │   │   ├── test_view_selector.cpython-312-pytest-8.3.1.pyc
│   │   │   ├── test_iql_generator.cpython-312-pytest-8.3.1.pyc
│   │   │   ├── mocks.cpython-312.pyc
│   │   │   ├── test_collection.cpython-312-pytest-8.3.1.pyc
│   │   │   ├── test_nl_responder.cpython-312-pytest-8.3.1.pyc
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── test_fallback_collection.cpython-312-pytest-8.3.1.pyc
│   │   ├── codegen
│   │   │   ├── test_generator.py
│   │   │   └── __pycache__
│   │   │       └── test_generator.cpython-312-pytest-8.3.1.pyc
│   │   ├── test_iql_generator.py
│   │   ├── test_assistants_adapters.py
│   │   ├── audit
│   │   │   ├── __init__.py
│   │   │   ├── event_handlers
│   │   │   │   ├── __init__.py
│   │   │   │   ├── __pycache__
│   │   │   │   │   ├── test_otel_event_handler.cpython-312-pytest-8.3.1.pyc
│   │   │   │   │   └── __init__.cpython-312.pyc
│   │   │   │   └── test_otel_event_handler.py
│   │   │   └── __pycache__
│   │   │       └── __init__.cpython-312.pyc
│   │   ├── test_iql_format.py
│   │   ├── test_fallback_collection.py
│   │   ├── views
│   │   │   ├── test_sqlalchemy_base.py
│   │   │   ├── __init__.py
│   │   │   ├── text2sql
│   │   │   │   ├── __init__.py
│   │   │   │   ├── __pycache__
│   │   │   │   │   ├── test_view.cpython-312-pytest-8.3.1.pyc
│   │   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   │   └── test_autodiscovery.cpython-312-pytest-8.3.1.pyc
│   │   │   │   ├── test_view.py
│   │   │   │   └── test_autodiscovery.py
│   │   │   ├── __pycache__
│   │   │   │   ├── test_methods_base.cpython-312-pytest-8.3.1.pyc
│   │   │   │   ├── test_pandas_base.cpython-312-pytest-8.3.1.pyc
│   │   │   │   ├── test_sqlalchemy_base.cpython-312-pytest-8.3.1.pyc
│   │   │   │   └── __init__.cpython-312.pyc
│   │   │   ├── test_pandas_base.py
│   │   │   └── test_methods_base.py
│   │   ├── test_prompt_builder.py
│   │   ├── test_fewshot.py
│   │   └── mocks.py
│   ├── integration
│   │   ├── test_index_with_chroma.py
│   │   ├── __pycache__
│   │   │   ├── test_llm_options.cpython-312-pytest-8.3.1.pyc
│   │   │   └── test_index_with_chroma.cpython-312-pytest-8.3.1.pyc
│   │   └── test_llm_options.py
│   ├── __init__.py
│   └── __pycache__
│       └── __init__.cpython-312.pyc
├── MANIFEST.in
├── docs
│   ├── about
│   │   ├── changelog.md
│   │   ├── contact.md
│   │   ├── roadmap.md
│   │   └── contributing.md
│   ├── quickstart
│   │   ├── quickstart2.md
│   │   ├── quickstart3.md
│   │   ├── quickstart2_code.py
│   │   ├── quickstart3_code.py
│   │   ├── quickstart_code.py
│   │   └── index.md
│   ├── how-to
│   │   ├── visualize_views.md
│   │   ├── use_elastic_store.md
│   │   ├── create_custom_event_handler.md
│   │   ├── use_chromadb_store.md
│   │   ├── use_elasticsearch_store_code.py
│   │   ├── log_runs_to_langsmith.md
│   │   ├── use_elastic_vector_store_code.py
│   │   ├── use_custom_similarity_store.md
│   │   ├── trace_runs_with_otel.md
│   │   ├── openai_assistants_integration.md
│   │   ├── llms
│   │   │   ├── litellm.md
│   │   │   ├── custom.md
│   │   │   └── local.md
│   │   ├── use_custom_similarity_fetcher.md
│   │   ├── views
│   │   │   ├── few-shots.md
│   │   │   ├── custom_views_code.py
│   │   │   ├── text-to-sql.md
│   │   │   ├── sql.md
│   │   │   ├── pandas.md
│   │   │   ├── custom.md
│   │   │   └── pandas_views_code.py
│   │   └── update_similarity_indexes.md
│   ├── tutorials.md
│   ├── index.md
│   ├── concepts
│   │   ├── collections.md
│   │   ├── views.md
│   │   ├── similarity_indexes.md
│   │   ├── nl_responder.md
│   │   ├── iql.md
│   │   ├── freeform_views.md
│   │   └── structured_views.md
│   ├── tutorials
│   │   ├── db-ally_tutorial.ipynb
│   │   ├── LangGraphXdbally.ipynb
│   │   └── dbally-assistants-api.ipynb
│   ├── assets
│   │   ├── event_handler_example.png
│   │   ├── guide_dog_lg.png
│   │   ├── otel_handler_jeager.png
│   │   └── guide_dog_sm.png
│   ├── reference
│   │   ├── collection.md
│   │   ├── embeddings
│   │   │   ├── litellm.md
│   │   │   └── index.md
│   │   ├── iql
│   │   │   ├── iql_generator.md
│   │   │   └── index.md
│   │   ├── similarity
│   │   │   ├── similarity_fetcher
│   │   │   │   ├── sqlalchemy.md
│   │   │   │   ├── index.md
│   │   │   │   └── sqlalchemy_simple.md
│   │   │   ├── similarity_store
│   │   │   │   ├── elastic.md
│   │   │   │   ├── chroma.md
│   │   │   │   ├── index.md
│   │   │   │   └── faiss.md
│   │   │   └── index.md
│   │   ├── view_selection
│   │   │   ├── llm_view_selector.md
│   │   │   └── index.md
│   │   ├── prompt.md
│   │   ├── event_handlers
│   │   │   ├── langsmith_handler.md
│   │   │   ├── cli_handler.md
│   │   │   ├── index.md
│   │   │   └── otel_handler.md
│   │   ├── nl_responder.md
│   │   ├── index.md
│   │   ├── llms
│   │   │   ├── litellm.md
│   │   │   ├── index.md
│   │   │   └── local.md
│   │   └── views
│   │       ├── structured.md
│   │       ├── text-to-sql.md
│   │       ├── index.md
│   │       ├── databases.md
│   │       └── dataframe.md
│   └── stylesheets
│       └── extra.css
├── setup.py
├── setup_dev_env.sh
├── requirements-dev.txt
├── example.py
├── examples
│   ├── visualize_fallback_code.py
│   ├── freeform.py
│   ├── __init__.py
│   ├── recruiting.py
│   ├── visualize_views_code.py
│   └── recruiting
│       ├── db.py
│       ├── candidate_view_with_similarity_store.py
│       ├── candidates_freeform.py
│       ├── __init__.py
│       ├── cypher_text2sql_view.py
│       ├── data
│       │   ├── offers.csv
│       │   ├── candidates.db
│       │   ├── application.csv
│       │   └── recruiting.csv
│       └── views.py
├── check_licenses.sh
├── setup.cfg
├── tree.md
├── build
│   ├── bdist.macosx-14.0-arm64
│   └── lib
│       ├── dbally_cli
│       │   ├── __init__.py
│       │   ├── text2sql.py
│       │   └── main.py
│       ├── dbally
│       │   ├── _types.py
│       │   ├── collection
│       │   │   ├── results.py
│       │   │   ├── __init__.py
│       │   │   ├── collection.py
│       │   │   └── exceptions.py
│       │   ├── embeddings
│       │   │   ├── __init__.py
│       │   │   ├── litellm.py
│       │   │   ├── exceptions.py
│       │   │   └── base.py
│       │   ├── _main.py
│       │   ├── assistants
│       │   │   ├── __init__.py
│       │   │   ├── openai.py
│       │   │   └── base.py
│       │   ├── iql
│       │   │   ├── _processor.py
│       │   │   ├── _query.py
│       │   │   ├── __init__.py
│       │   │   ├── _type_validators.py
│       │   │   ├── syntax.py
│       │   │   └── _exceptions.py
│       │   ├── similarity
│       │   │   ├── store.py
│       │   │   ├── elasticsearch_store.py
│       │   │   ├── index.py
│       │   │   ├── chroma_store.py
│       │   │   ├── __init__.py
│       │   │   ├── faiss_store.py
│       │   │   ├── sqlalchemy_base.py
│       │   │   ├── fetcher.py
│       │   │   └── elastic_vector_search.py
│       │   ├── view_selection
│       │   │   ├── __init__.py
│       │   │   ├── random_view_selector.py
│       │   │   ├── prompt.py
│       │   │   ├── llm_view_selector.py
│       │   │   └── base.py
│       │   ├── __init__.py
│       │   ├── __version__.py
│       │   ├── gradio
│       │   │   ├── gradio_interface.py
│       │   │   └── __init__.py
│       │   ├── audit
│       │   │   ├── events.py
│       │   │   ├── __init__.py
│       │   │   ├── event_handlers
│       │   │   │   ├── otel_event_handler.py
│       │   │   │   ├── cli_event_handler.py
│       │   │   │   ├── buffer_event_handler.py
│       │   │   │   ├── langsmith_event_handler.py
│       │   │   │   ├── __init__.py
│       │   │   │   └── base.py
│       │   │   ├── spans.py
│       │   │   └── event_tracker.py
│       │   ├── nl_responder
│       │   │   ├── __init__.py
│       │   │   ├── prompts.py
│       │   │   └── nl_responder.py
│       │   ├── prompt
│       │   │   ├── elements.py
│       │   │   ├── __init__.py
│       │   │   └── template.py
│       │   ├── py.typed
│       │   ├── exceptions.py
│       │   ├── llms
│       │   │   ├── clients
│       │   │   │   ├── local.py
│       │   │   │   ├── __init__.py
│       │   │   │   ├── litellm.py
│       │   │   │   ├── exceptions.py
│       │   │   │   └── base.py
│       │   │   ├── local.py
│       │   │   ├── __init__.py
│       │   │   ├── litellm.py
│       │   │   └── base.py
│       │   ├── views
│       │   │   ├── methods_base.py
│       │   │   ├── exposed_functions.py
│       │   │   ├── __init__.py
│       │   │   ├── structured.py
│       │   │   ├── freeform
│       │   │   │   ├── __init__.py
│       │   │   │   └── text2sql
│       │   │   │       ├── config.py
│       │   │   │       ├── __init__.py
│       │   │   │       ├── view.py
│       │   │   │       ├── exceptions.py
│       │   │   │       └── prompt.py
│       │   │   ├── pandas_base.py
│       │   │   ├── base.py
│       │   │   ├── sqlalchemy_base.py
│       │   │   └── decorators.py
│       │   └── iql_generator
│       │       ├── __init__.py
│       │       ├── iql_generator.py
│       │       └── prompt.py
│       └── dbally_codegen
│           ├── __init__.py
│           ├── generator.py
│           └── autodiscovery.py
├── data
│   └── candidates.db
└── src
    ├── dbally_cli
    │   ├── __init__.py
    │   ├── text2sql.py
    │   └── main.py
    ├── dbally.egg-info
    │   ├── PKG-INFO
    │   ├── not-zip-safe
    │   ├── SOURCES.txt
    │   ├── entry_points.txt
    │   ├── requires.txt
    │   ├── top_level.txt
    │   └── dependency_links.txt
    ├── py.typed
    ├── dbally
    │   ├── _types.py
    │   ├── collection
    │   │   ├── results.py
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── exceptions.cpython-312.pyc
    │   │   │   ├── collection.cpython-312.pyc
    │   │   │   ├── results.cpython-312.pyc
    │   │   │   └── __init__.cpython-312.pyc
    │   │   ├── collection.py
    │   │   └── exceptions.py
    │   ├── embeddings
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── litellm.cpython-312.pyc
    │   │   │   ├── base.cpython-312.pyc
    │   │   │   ├── exceptions.cpython-312.pyc
    │   │   │   └── __init__.cpython-312.pyc
    │   │   ├── litellm.py
    │   │   ├── exceptions.py
    │   │   └── base.py
    │   ├── _main.py
    │   ├── assistants
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── base.cpython-312.pyc
    │   │   │   ├── openai.cpython-312.pyc
    │   │   │   └── __init__.cpython-312.pyc
    │   │   ├── openai.py
    │   │   └── base.py
    │   ├── iql
    │   │   ├── _processor.py
    │   │   ├── _query.py
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── _query.cpython-312.pyc
    │   │   │   ├── _processor.cpython-312.pyc
    │   │   │   ├── _exceptions.cpython-312.pyc
    │   │   │   ├── syntax.cpython-312.pyc
    │   │   │   ├── _type_validators.cpython-312.pyc
    │   │   │   └── __init__.cpython-312.pyc
    │   │   ├── _type_validators.py
    │   │   ├── syntax.py
    │   │   └── _exceptions.py
    │   ├── similarity
    │   │   ├── store.py
    │   │   ├── elasticsearch_store.py
    │   │   ├── index.py
    │   │   ├── chroma_store.py
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── chroma_store.cpython-312.pyc
    │   │   │   ├── elasticsearch_store.cpython-312.pyc
    │   │   │   ├── sqlalchemy_base.cpython-312.pyc
    │   │   │   ├── elastic_vector_search.cpython-312.pyc
    │   │   │   ├── index.cpython-312.pyc
    │   │   │   ├── store.cpython-312.pyc
    │   │   │   ├── faiss_store.cpython-312.pyc
    │   │   │   ├── __init__.cpython-312.pyc
    │   │   │   └── fetcher.cpython-312.pyc
    │   │   ├── faiss_store.py
    │   │   ├── sqlalchemy_base.py
    │   │   ├── fetcher.py
    │   │   └── elastic_vector_search.py
    │   ├── view_selection
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── base.cpython-312.pyc
    │   │   │   ├── prompt.cpython-312.pyc
    │   │   │   ├── llm_view_selector.cpython-312.pyc
    │   │   │   └── __init__.cpython-312.pyc
    │   │   ├── random_view_selector.py
    │   │   ├── prompt.py
    │   │   ├── llm_view_selector.py
    │   │   └── base.py
    │   ├── __init__.py
    │   ├── __version__.py
    │   ├── __pycache__
    │   │   ├── __version__.cpython-312.pyc
    │   │   ├── _main.cpython-312.pyc
    │   │   ├── _types.cpython-312.pyc
    │   │   ├── exceptions.cpython-312.pyc
    │   │   └── __init__.cpython-312.pyc
    │   ├── gradio
    │   │   ├── gradio_interface.py
    │   │   └── __init__.py
    │   ├── audit
    │   │   ├── events.py
    │   │   ├── __init__.py
    │   │   ├── event_handlers
    │   │   │   ├── otel_event_handler.py
    │   │   │   ├── cli_event_handler.py
    │   │   │   ├── buffer_event_handler.py
    │   │   │   ├── langsmith_event_handler.py
    │   │   │   ├── __init__.py
    │   │   │   ├── __pycache__
    │   │   │   │   ├── otel_event_handler.cpython-312.pyc
    │   │   │   │   ├── buffer_event_handler.cpython-312.pyc
    │   │   │   │   ├── base.cpython-312.pyc
    │   │   │   │   ├── cli_event_handler.cpython-312.pyc
    │   │   │   │   ├── langsmith_event_handler.cpython-312.pyc
    │   │   │   │   └── __init__.cpython-312.pyc
    │   │   │   └── base.py
    │   │   ├── spans.py
    │   │   ├── __pycache__
    │   │   │   ├── event_tracker.cpython-312.pyc
    │   │   │   ├── spans.cpython-312.pyc
    │   │   │   ├── events.cpython-312.pyc
    │   │   │   └── __init__.cpython-312.pyc
    │   │   └── event_tracker.py
    │   ├── nl_responder
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── nl_responder.cpython-312.pyc
    │   │   │   ├── prompts.cpython-312.pyc
    │   │   │   └── __init__.cpython-312.pyc
    │   │   ├── prompts.py
    │   │   └── nl_responder.py
    │   ├── prompt
    │   │   ├── elements.py
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── elements.cpython-312.pyc
    │   │   │   ├── template.cpython-312.pyc
    │   │   │   └── __init__.cpython-312.pyc
    │   │   └── template.py
    │   ├── py.typed
    │   ├── exceptions.py
    │   ├── llms
    │   │   ├── clients
    │   │   │   ├── local.py
    │   │   │   ├── __init__.py
    │   │   │   ├── __pycache__
    │   │   │   │   ├── litellm.cpython-312.pyc
    │   │   │   │   ├── base.cpython-312.pyc
    │   │   │   │   ├── exceptions.cpython-312.pyc
    │   │   │   │   └── __init__.cpython-312.pyc
    │   │   │   ├── litellm.py
    │   │   │   ├── exceptions.py
    │   │   │   └── base.py
    │   │   ├── local.py
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── litellm.cpython-312.pyc
    │   │   │   ├── base.cpython-312.pyc
    │   │   │   └── __init__.cpython-312.pyc
    │   │   ├── litellm.py
    │   │   └── base.py
    │   ├── views
    │   │   ├── methods_base.py
    │   │   ├── exposed_functions.py
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── pandas_base.cpython-312.pyc
    │   │   │   ├── base.cpython-312.pyc
    │   │   │   ├── exposed_functions.cpython-312.pyc
    │   │   │   ├── structured.cpython-312.pyc
    │   │   │   ├── methods_base.cpython-312.pyc
    │   │   │   ├── sqlalchemy_base.cpython-312.pyc
    │   │   │   ├── decorators.cpython-312.pyc
    │   │   │   └── __init__.cpython-312.pyc
    │   │   ├── structured.py
    │   │   ├── freeform
    │   │   │   ├── __init__.py
    │   │   │   ├── text2sql
    │   │   │   │   ├── config.py
    │   │   │   │   ├── __init__.py
    │   │   │   │   ├── __pycache__
    │   │   │   │   │   ├── config.cpython-312.pyc
    │   │   │   │   │   ├── prompt.cpython-312.pyc
    │   │   │   │   │   ├── view.cpython-312.pyc
    │   │   │   │   │   ├── exceptions.cpython-312.pyc
    │   │   │   │   │   └── __init__.cpython-312.pyc
    │   │   │   │   ├── view.py
    │   │   │   │   ├── exceptions.py
    │   │   │   │   └── prompt.py
    │   │   │   └── __pycache__
    │   │   │       └── __init__.cpython-312.pyc
    │   │   ├── pandas_base.py
    │   │   ├── base.py
    │   │   ├── sqlalchemy_base.py
    │   │   └── decorators.py
    │   └── iql_generator
    │       ├── __init__.py
    │       ├── __pycache__
    │       │   ├── prompt.cpython-312.pyc
    │       │   ├── __init__.cpython-312.pyc
    │       │   └── iql_generator.cpython-312.pyc
    │       ├── iql_generator.py
    │       └── prompt.py
    └── dbally_codegen
        ├── __init__.py
        ├── __pycache__
        │   ├── generator.cpython-312.pyc
        │   ├── autodiscovery.cpython-312.pyc
        │   └── __init__.cpython-312.pyc
        ├── generator.py
        └── autodiscovery.py