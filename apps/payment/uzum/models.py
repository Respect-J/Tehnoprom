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


@dataclass
class CalculateTariff:
    user_id: int
    products: list[NasiyaProduct]


@dataclass
class CreateOrder:
    user_id: int
    period: str
    callback: str
    products: list[NasiyaProduct]


@dataclass
class ConfirmContract:
    contract_id: int
