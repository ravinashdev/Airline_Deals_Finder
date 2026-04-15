from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[
        "config/settings.toml",
        "config/data_handler_class_api.toml",
        "config/flight_data_handler_class.toml",
        "config/flight_search_handler_class.toml",
        "config/notifications_handler_class.toml",
        "config/.secrets.toml"
    ],
    environments=True,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
