#
from __future__ import annotations

from dataclasses import dataclass

from .models import Order


@dataclass
class RequestCtx:
    remote_ip: str
    order: Order
