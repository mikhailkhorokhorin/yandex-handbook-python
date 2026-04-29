import datetime as _dt
import itertools as _it
from dataclasses import dataclass, field
from enum import Enum

DEFAULT_CARD_INFO_FIELDS = [
    "card_id",
    "user_id",
    "phone",
    "bank_name",
    "bank_bic",
    "acc_id",
    "pan",
    "payment_system",
    "currency",
    "status",
    "issue_date",
    "expiry_date",
    "balance",
    "cashback_balance",
    "user_cards",
]
DEFAULT_ACCOUNT_BALANCE = 0.00
DEFAULT_CASHBACK_BALANCE = 0.00
DEFAULT_CASHBACK_TRANSACTION = 0.00
CARD_CURRENCY = "RUB"
DEFAULT_PAYMENT_SYSTEM = "MIR"

ACCOUNT_TYPE_CODE = "40817"
ACCOUNT_BRANCH = "0000"
ACCOUNT_CURRENCY = "810"

EMPTY_PAN = "0000000000000000"

BIN_BY_SYSTEM = {
    "MIR": "220400",
    "VISA": "400000",
    "MASTERCARD": "510000",
}

TRANSACTION_HISTORY_HEADER = [
    "timestamp,type,from_card,to_card,amount,mcc,cashback,description"
]
DEPOSIT_DESCRIPTION = "{amount:.2f}₽ → карта #{card_id}"
TRANSFER_DESCRIPTION = "{amount:.2f}₽: карта #{from_card} → карта #{to_card}"
PAY_DESCRIPTION = "{amount:.2f}₽ (MCC: {mcc}) с карты #{card_id}"
BALANCE_DESCRIPTION = "Баланс: {balance:.2f}₽"

ISSUE_DATE_START = _dt.date(2022, 1, 1)
ISSUE_DATE_GENERATOR = (ISSUE_DATE_START + _dt.timedelta(days=i) for i in _it.count())
EXPIRY_YEARS = 4

TIMESTAMP_START = _dt.datetime(2022, 1, 1, 9, 0, 0)


def timestamp_generator():
    for i in _it.count():
        base_date = TIMESTAMP_START + _dt.timedelta(days=i)
        hour = 9 + (i * 3) % 10
        minute = (i * 7) % 60
        second = (i * 11) % 60
        yield base_date.replace(hour=hour % 24, minute=minute, second=second)


TIMESTAMP_GENERATOR = timestamp_generator()


def next_timestamp_after(issue_date: _dt.date) -> _dt.datetime:
    while True:
        ts = next(TIMESTAMP_GENERATOR)
        if ts.date() > issue_date:
            return ts


class CardStatus(Enum):
    ACTIVE = "Active"
    CLOSED = "Closed"
    BLOCKED = "Blocked"


CARD_STATUS = CardStatus.ACTIVE


class TransactionType(Enum):
    DEPOSIT = "deposit"
    TRANSFER = "transfer"
    PAY = "pay"
    INTEREST = "interest"


@dataclass
class Transaction:
    from_card: int | None
    to_card: int | None
    amount: float
    type: TransactionType
    mcc: str | None
    description: str
    timestamp: _dt.datetime
    cashback: float = DEFAULT_CASHBACK_TRANSACTION


@dataclass
class User:
    last_name: str
    first_name: str
    pin: str
    phone: str
    user_id: int

    accounts: list = field(default_factory=list)
    cards: list = field(default_factory=list)

    def change_pin(self, old_pin: str, new_pin: str):
        if self.pin == old_pin:
            self.pin = new_pin


@dataclass
class Account:
    owner: "User"
    acc_id: str
    balance: float = DEFAULT_ACCOUNT_BALANCE
    cashback_balance: float = DEFAULT_CASHBACK_BALANCE


class Card:
    def __init__(
        self,
        account,
        card_id,
        payment_system=DEFAULT_PAYMENT_SYSTEM,
        pan=EMPTY_PAN,
        issue_date=None,
        expiry_date=None,
        currency=CARD_CURRENCY,
        status=CARD_STATUS,
        bank=None,
    ):
        self.account = account
        self.card_id = card_id
        self.payment_system = payment_system
        self.pan = pan
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.currency = currency
        self.status = status
        self.bank = bank

        if self.issue_date is None:
            self.issue_date = next(ISSUE_DATE_GENERATOR)
        if self.expiry_date is None and self.issue_date is not None:
            self.expiry_date = _dt.date(
                self.issue_date.year + EXPIRY_YEARS,
                self.issue_date.month,
                self.issue_date.day,
            )

    def get_card_info(self, fields: list = None):
        user = self.account.owner
        data = {
            "bank_name": f"Банк:          {self.bank.name}",
            "bank_bic": f"БИК банка:     {self.bank.bic}",
            "card_id": f"Карта #{self.card_id}",
            "user_id": f"Пользователь:  {user.user_id} — {user.last_name} {user.first_name}",
            "phone": f"Телефон:       {user.phone}",
            "pan": f"PAN:           {self.pan}",
            "acc_id": f"Счёт:          {self.account.acc_id}",
            "payment_system": f"Плат. система: {self.payment_system}",
            "currency": f"Валюта:        {self.currency}",
            "status": f"Статус:        {self.status.value}",
            "issue_date": f"Выпуск:        {self.issue_date}",
            "expiry_date": f"Срок:          {self.expiry_date}",
            "user_cards": f"Карты пользователя: {[c.pan for c in user.cards]}",
            "cashback_balance": f"Кешбэк:        {self.account.cashback_balance:.2f}₽",
            "balance": f"Баланс:        {self.account.balance:.2f}₽",
        }
        if fields is None:
            fields = DEFAULT_CARD_INFO_FIELDS
        return (
            "\n".join([data[field] for field in fields if field in data])
            + "\n"
            + "-" * 50
        )

    def get_balance(self):
        return BALANCE_DESCRIPTION.format(balance=self.account.balance)

    def deposit(self, amount: float):
        self.account.balance += amount
        self.bank.transaction_log.append(
            Transaction(
                from_card=None,
                to_card=self.card_id,
                amount=amount,
                type=TransactionType.DEPOSIT,
                mcc=None,
                cashback=DEFAULT_CASHBACK_TRANSACTION,
                description=DEPOSIT_DESCRIPTION.format(
                    amount=amount, card_id=self.card_id
                ),
                timestamp=next_timestamp_after(self.issue_date),
            )
        )

    def transfer(self, to_card, amount: float):
        self.account.balance -= amount
        to_card.account.balance += amount
        latest_issue = max(self.issue_date, to_card.issue_date)
        self.bank.transaction_log.append(
            Transaction(
                from_card=self.card_id,
                to_card=to_card.card_id,
                amount=amount,
                type=TransactionType.TRANSFER,
                mcc=None,
                cashback=DEFAULT_CASHBACK_TRANSACTION,
                description=TRANSFER_DESCRIPTION.format(
                    amount=amount,
                    from_card=self.card_id,
                    to_card=to_card.card_id,
                ),
                timestamp=next_timestamp_after(latest_issue),
            )
        )

    def pay(self, amount: float, mcc: str):
        self.account.balance -= amount
        self.bank.transaction_log.append(
            Transaction(
                from_card=self.card_id,
                to_card=None,
                amount=amount,
                type=TransactionType.PAY,
                mcc=mcc,
                cashback=DEFAULT_CASHBACK_TRANSACTION,
                description=PAY_DESCRIPTION.format(
                    amount=amount, mcc=mcc, card_id=self.card_id
                ),
                timestamp=next_timestamp_after(self.issue_date),
            )
        )

    def get_transaction_history(self):
        rows = list(TRANSACTION_HISTORY_HEADER)
        sorted_transactions = sorted(
            self.bank.transaction_log, key=lambda x: x.timestamp
        )
        for tx in sorted_transactions:
            if tx.from_card == self.card_id or tx.to_card == self.card_id:
                dt_str = tx.timestamp.strftime("%Y-%m-%d %H:%M:%S")
                from_card = tx.from_card if tx.from_card is not None else ""
                to_card = tx.to_card if tx.to_card is not None else ""
                if tx.from_card == self.card_id:
                    sign = "-"
                elif tx.to_card == self.card_id:
                    sign = "+"
                else:
                    sign = ""
                amount_str = f"{sign}{tx.amount:.2f}₽"
                mcc_str = tx.mcc if tx.mcc else ""
                tx_type = tx.type.value
                cashback_str = f"{getattr(tx, 'cashback', 0):.2f}₽"
                rows.append(
                    f"{dt_str},{tx_type},{from_card},{to_card},{amount_str},{mcc_str},{cashback_str},{tx.description}"
                )
        return rows

    def close(self):
        self.status = CardStatus.CLOSED

    def __repr__(self):
        return (
            f"Card(card_id={self.card_id}, pan={self.pan}, account={self.account}, "
            f"status={self.status}, issue_date={self.issue_date}, expiry_date={self.expiry_date})"
        )


@dataclass
class Bank:
    name: str
    bic: str

    _user_seq: int = field(default_factory=lambda: _it.count(1), init=False)
    _account_seq: int = field(default_factory=lambda: _it.count(1), init=False)
    _card_seq: int = field(default_factory=lambda: _it.count(1), init=False)
    _pan_seq: int = field(default_factory=lambda: _it.count(1), init=False)

    customers: dict = field(default_factory=dict)
    accounts: dict = field(default_factory=dict)
    cards: dict = field(default_factory=dict)
    transaction_log: list = field(default_factory=list)

    def _next_account_number(self):
        prefix_left = ACCOUNT_TYPE_CODE + ACCOUNT_CURRENCY
        prefix_right = ACCOUNT_BRANCH
        bic_tail = self.bic[-3:]
        serial = f"{next(self._account_seq):07d}"
        for control_digit in range(10):
            candidate_account_number = (
                prefix_left + str(control_digit) + prefix_right + serial
            )
            digits = [int(d) for d in bic_tail + candidate_account_number]
            weights = [7, 1, 3] * 8
            weighted = [a * b for a, b in zip(digits, weights[:23])]
            control_sum = sum(x % 10 for x in weighted)
            if control_sum % 10 == 0:
                return candidate_account_number

    def _generate_pan(self, system):
        bin_code = BIN_BY_SYSTEM.get(
            system.upper(), BIN_BY_SYSTEM[DEFAULT_PAYMENT_SYSTEM]
        )
        seq = f"{next(self._pan_seq):09d}"
        partial = bin_code + seq
        check = self._luhn(partial)
        return partial + str(check)

    def _luhn(self, number15):
        digits = [int(d) for d in number15[::-1]]
        for i in range(1, len(digits), 2):
            doubled = digits[i] * 2
            digits[i] = doubled - 9 if doubled > 9 else doubled
        return (10 - sum(digits) % 10) % 10

    def apply_for_card(
        self,
        last_name,
        first_name,
        pin,
        phone,
        payment_system=DEFAULT_PAYMENT_SYSTEM,
        card_class: type = Card,
        **kwargs,
    ):
        user = next(
            (
                user
                for user in self.customers.values()
                if user.last_name == last_name
                and user.first_name == first_name
                and user.phone == phone
            ),
            None,
        )
        if not user:
            user_id = next(self._user_seq)
            user = User(last_name, first_name, pin, phone, user_id)
            self.customers[user_id] = user

        acc_id = self._next_account_number()
        acc = Account(owner=user, acc_id=acc_id)
        self.accounts[acc_id] = acc
        user.accounts.append(acc)

        card_id = next(self._card_seq)
        pan = self._generate_pan(payment_system)
        issue_date = next(ISSUE_DATE_GENERATOR)

        card = card_class(
            account=acc,
            card_id=card_id,
            payment_system=payment_system,
            pan=pan,
            issue_date=issue_date,
            currency=CARD_CURRENCY,
            status=CARD_STATUS,
            bank=self,
            **kwargs,
        )

        self.cards[card_id] = card
        user.cards.append(card)
        return card

    def get_global_history(self) -> list:
        rows = list(TRANSACTION_HISTORY_HEADER)
        for tx in sorted(self.transaction_log, key=lambda x: x.timestamp):
            dt_str = tx.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            tx_type = tx.type.value
            from_card = tx.from_card if tx.from_card is not None else ""
            to_card = tx.to_card if tx.to_card is not None else ""
            amount_str = f"{tx.amount:.2f}₽"
            cashback_str = f"{getattr(tx, 'cashback', 0):.2f}₽"
            mcc_str = tx.mcc if tx.mcc else ""
            rows.append(
                f"{dt_str},{tx_type},{from_card},{to_card},{amount_str},{mcc_str},{cashback_str},{tx.description}"
            )
        return rows
