from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[
        "config/settings.toml",
        "config/sheety.toml",
        "config/twillio.toml",
        "config/serp.toml",
        "config/.secrets.toml"
    ],
    environments=True,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
