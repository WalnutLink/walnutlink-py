# -*- coding: utf-8 -*-
"""WalnutLink AI — ask why a China A-share number moved.

Zero dependencies on purpose: `pip install walnutlink` and it runs. Every
MCP server that requires you to also install an HTTP client is a server
half the agents will never get to.

    >>> from walnutlink import Desk
    >>> d = Desk()
    >>> d.search("毛利率")["matched"]
    >>> d.ask("海康威视单季毛利率下季度会继续降吗")["queue_id"]

The desk does not serve quotes. Price, pct change, PE, market cap and
limit-up reason are refused with an explanation, not a number. That is a
positioning decision, not a gap.
"""

from .client import Desk, DeskError, Answer, Edge, Note

__version__ = "0.1.0"
__all__ = ["Desk", "DeskError", "Answer", "Edge", "Note"]
