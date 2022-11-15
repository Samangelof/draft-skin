from . import get_env_variable



ALLOWED_HOSTS = []

ROOT_URLCONF = 'settings.urls'

DROP_DEBUG = get_env_variable("DEBUG")

SECRET_KEY = get_env_variable("SECRET_KEY")
ADMIN_SITE_URL = get_env_variable("ADMIN_SITE_URL")





NAME_DATEBASE = get_env_variable('NAME_DATEBASE')
USER_DATEBASE = get_env_variable('USER_DATEBASE')
PASSWORD_DATEBASE = get_env_variable('PASSWORD_DATEBASE')
HOST_DATEBASE = get_env_variable('HOST_DATEBASE')
PORT_DATEBASE = get_env_variable('PORT_DATEBASE')