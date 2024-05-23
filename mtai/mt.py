"""Entry point defined here."""

from mtai.base import MTAIBase
from mtai.tags import Tag


class MT(MTAIBase):
    """MT Class used across defined."""

    def __init__(self, *args, **kwargs):
        """Initialize mtai with secret key."""
        MTAIBase.__init__(self, *args, **kwargs)

        self.tags = Tag