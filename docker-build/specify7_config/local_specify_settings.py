# The webapp server piggybacks on the thick client.
# Set the path to a thick client installation.
THICK_CLIENT_LOCATION = '/usr/local/specify6/'

# Set the database name to the MySQL database you
# want to access.
DATABASE_NAME = 'specify'

# Database hostname or IP
DATABASE_HOST = 'mariadb'
DATABASE_PORT = '3306'

# The master user login. Use the same values as
# you did setting up the thick client.
MASTER_NAME = 'root'
MASTER_PASSWORD = 'root'

# Select the schema localization language.
SCHEMA_LANGUAGE = 'en'

# The Specify web attachment server URL.
WEB_ATTACHMENT_URL = 'http://localhost:8081/web_asset_store.xml'

# The Specify web attachment server key.
WEB_ATTACHMENT_KEY = ''

# The collection name to use with the web attachment server.
WEB_ATTACHMENT_COLLECTION = 'main'

# Set to true if the asset server requires auth token to get files.
WEB_ATTACHMENT_REQUIRES_KEY_FOR_GET = False

# Report runner service
REPORT_RUNNER_HOST = ''
REPORT_RUNNER_PORT = ''

# To allow anonymous use, set ANONYMOUS_USER to a Specify username
# to use for anonymous access.
ANONYMOUS_USER = None

# For exception logging using Sentry (https://github.com/getsentry/sentry).
RAVEN_CONFIG = None

# Support login mechanism.
ALLOW_SUPPORT_LOGIN = False
SUPPORT_LOGIN_TTL = 300

# Usage stats are transmitted to the following address.
# Set to None to disable.
STATS_URL = None

# Workbench uploader log directory.
# Must exist and be writeable by the web server process.
WB_UPLOAD_LOG_DIR = "/usr/local/specify_wb_upload/"

# Asynchronously generated exports are placed in
# the following directory. This includes query result
# exports and Darwin Core archives.
DEPOSITORY_DIR = '/var/www/html/specify/specify_depository'

# Old notifications are deleted after this many days.
# If DEPOSITORY_DIR is being cleaned out with a
# scheduled job, this interval should be shorter
# than the cleanout time, so that notifications
# are not left that refer to deleted exports.
NOTIFICATION_TTL_DAYS = 7
