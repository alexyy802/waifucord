"""
waifucord
~~~~~~~~~~~~~~~~~~~

A basic wrapper for the Discord API.

:copyright: (c) 2021-present waifucord
:license: MIT, see LICENSE for more details.

"""

__title__ = "senpai"
__author__ = "waifucord"
__license__ = "MIT"
__copyright__ = "Copyright 2021-present waifucord"
__version__ = "2.5.5"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import NamedTuple, Literal

from .bunny import *
from .appinfo import *
from .user import *
from .emoji import *
from .partial_emoji import *
from .activity import *
from .channel import *
from .guild import *
from .flags import *
from .member import *
from .message import *
from .asset import *
from .errors import *
from .permissions import *
from .role import *
from .file import *
from .colour import *
from .integrations import *
from .invite import *
from .template import *
from .widget import *
from .object import *
from .reaction import *
from . import utils, opus, abc, ui
from .enums import *
from .embeds import *
from .mentions import *
from .shard import *
from .player import *
from .webhooker import *
from .voice_bunny import *
from .audit_logs import *
from .raw_models import *
from .team import *
from .sticker import *
from .stage_instance import *
from .interactions import *
from .components import *
from .threads import *


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=2, minor=0, micro=0, releaselevel="candidate", serial=0
)

logging.getLogger(__name__).addHandler(logging.NullHandler())
