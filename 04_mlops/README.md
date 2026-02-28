```

04_mlops/
├── README.md
│
├── 01_model_persistence/
│   ├── README.md
│   ├── 01_pickle_and_joblib.ipynb
│   ├── 02_onnx_basics.ipynb
│   └── models/                          # saved model artifacts (.pkl, .joblib, .onnx)
│
├── 02_api_development/
│   ├── README.md
│   ├── 01_fastapi_fundamentals.ipynb
│   ├── 02_serving_a_model_with_fastapi.ipynb
│   ├── 03_request_validation_with_pydantic.ipynb
│   └── app/                             # example working API project
│       ├── main.py
│       ├── schemas.py
│       └── model_loader.py
│
├── 03_containerization/
│   ├── README.md
│   ├── 01_docker_fundamentals.ipynb
│   ├── 02_dockerizing_an_ml_api.ipynb
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── 04_cloud_deployment/
│   ├── README.md
│   ├── 01_deployment_options_overview.ipynb
│   ├── 02_deploying_to_a_cloud_platform.ipynb
│   └── 03_ci_cd_basics_with_github_actions.ipynb
│
├── 05_interactive_dashboards/
│   ├── README.md
│   ├── 01_streamlit_fundamentals.ipynb
│   └── 02_building_an_ml_dashboard.ipynb
│
└── 06_monitoring_and_maintenance/
    ├── README.md
    ├── 01_logging_and_error_handling.ipynb
    ├── 02_data_and_model_drift_concepts.ipynb
    └── 03_model_retraining_strategies.ipynb

```