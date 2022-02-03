# Include apiv2 endpoints
from .api.apiv2.endpoints.leaderboard import leaderboard
from .api.apiv2.endpoints.teams import teams
from .api.apiv2.endpoints.news import news

# Include bootstrap items
from .api.info.bootstrap.items.car import car
from .api.info.bootstrap.items.loot import loot

# Include bootstrap misc items
from .api.info.bootstrap.misc.challenges import challenges
from .api.info.bootstrap.misc.top import top

# Include entire bootstrap
from .api.info.bootstrap.bootstrap import bootstrap

# Include user information
from .api.info.user import user

# Allow user to access the nitrotype api directly
from .api.apiv2.api import api
