import os

from loguru import logger

ENV_VAR = "APP_ENV"

env = os.environ[ENV_VAR]
logger.success("{} - Hello, World!", env)
