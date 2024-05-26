from dataclasses import dataclass
from enum import IntEnum


class UzumNasiyaStatus(IntEnum):
    NOT_FOUND = 0
    CARD_REQUIRED = 1
    WAITING_FOR_MODERATION = 2
    VERIFIED = 4
    MYID_VERIFICATION = 5
    VERIFICATION_DENIED = 8


@dataclass
class CheckStatus:
    phone: str


@dataclass
class NasiyaProduct:
    price: int
    amount: int
    product_id: int
    name: str = "Product"
    unit_id: int = 1
    category: str = "1"


@dataclass
class CalculateTariff:
    user_id: int
    products: list[NasiyaProduct]


@dataclass
class CreateOrder:
    user_id: int
    period: str
    products: list[NasiyaProduct]
    callback: str = ""


@dataclass
class ConfirmContract:
    contract_id: int
