# 5.5. Разработка бэкенда банковского приложения
### A. Оформление заявки на выпуск карты
```python
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


ISSUE_DATE_START = _dt.date(2022, 1, 1)
ISSUE_DATE_GENERATOR = (ISSUE_DATE_START + _dt.timedelta(days=i) for i in _it.count())
EXPIRY_YEARS = 4


class CardStatus(Enum):
    ACTIVE = "Active"
    CLOSED = "Closed"
    BLOCKED = "Blocked"


CARD_STATUS = CardStatus.ACTIVE


@dataclass
class User:
    last_name: str
    first_name: str
    pin: str
    phone: str
    user_id: int

    accounts: list = field(default_factory=list)
    cards: list = field(default_factory=list)


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
                if user.first_name == first_name
                and user.last_name == last_name
                and user.phone == phone
            ),
            None,
        )
        if not user:
            user_id = next(self._user_seq)
            user = User(last_name, first_name, pin, phone, user_id)
            self.customers[user_id] = user

        acc_id = self._next_account_number()
        account = Account(user, acc_id)
        self.accounts[acc_id] = account
        user.accounts.append(account)

        card_id = next(self._card_seq)
        pan = self._generate_pan(payment_system)
        iss_dt = next(ISSUE_DATE_GENERATOR)

        card = card_class(
            account=account,
            card_id=card_id,
            payment_system=payment_system,
            pan=pan,
            issue_date=iss_dt,
            currency=CARD_CURRENCY,
            status=CARD_STATUS,
            bank=self,
            **kwargs,
        )

        self.cards[card_id] = card
        user.cards.append(card)
        return card
```
### B. Использование банковской карты и ведение журнала операций
```python
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
```
### C. Запускаем новые типы банковских карт
```python
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
CB_DEBIT_PAY_DESCRIPTION = (
    "{amount:.2f}₽ (MCC: {mcc}) с карты #{card_id} (кешбэк {cashback_amount:.2f}₽)"
)
SAVING_INTEREST_DESCRIPTION = (
    "Начислены проценты {interest:.2f}₽ по накопительной карте #{card_id}"
)

DEBIT_DEFAULT_CASHBACK_RATE = 0.03
SAVING_CARD_DEFAULT_INTEREST = 0.015

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
    """
    Возвращает ближайший timestamp из генератора, который позже issue_date.
    """
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
        balance = self.account.balance
        return BALANCE_DESCRIPTION.format(balance=balance)

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
        for tx in self.bank.transaction_log:
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


class SimpleDebitCard(Card):
    pass


class CashbackDebitCard(Card):
    def __init__(self, *, cashback_rate: float = DEBIT_DEFAULT_CASHBACK_RATE, **kwargs):
        super().__init__(**kwargs)
        self.cashback_rate = cashback_rate

    def pay(self, amount: float, mcc: str):
        self.account.balance -= amount
        cashback_amount = round(float(amount * self.cashback_rate), 2)
        self.account.cashback_balance += cashback_amount

        self.bank.transaction_log.append(
            Transaction(
                from_card=self.card_id,
                to_card=None,
                amount=amount,
                type=TransactionType.PAY,
                mcc=mcc,
                cashback=cashback_amount,
                description=CB_DEBIT_PAY_DESCRIPTION.format(
                    amount=amount,
                    mcc=mcc,
                    card_id=self.card_id,
                    cashback_amount=cashback_amount,
                ),
                timestamp=next_timestamp_after(self.issue_date),
            )
        )


class SavingCard(Card):
    def __init__(
        self, *, interest_rate: float = SAVING_CARD_DEFAULT_INTEREST, **kwargs
    ):
        super().__init__(**kwargs)
        self.interest_rate = interest_rate

    def accrue_interest(self):
        interest = round(self.account.balance * self.interest_rate, 2)
        self.account.balance += interest

        self.bank.transaction_log.append(
            Transaction(
                from_card=None,
                to_card=self.card_id,
                amount=interest,
                cashback=DEFAULT_CASHBACK_TRANSACTION,
                type=TransactionType.INTEREST,
                mcc=None,
                description=SAVING_INTEREST_DESCRIPTION.format(
                    interest=interest, card_id=self.card_id
                ),
                timestamp=next_timestamp_after(self.issue_date),
            )
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

    def issue_simple_debit_card(
        self, last_name, first_name, pin, phone, payment_system, **kwargs
    ):
        return self.apply_for_card(
            last_name,
            first_name,
            pin,
            phone,
            payment_system,
            card_class=SimpleDebitCard,
            **kwargs,
        )

    def issue_cashback_debit_card(
        self, last_name, first_name, pin, phone, payment_system, **kwargs
    ):
        return self.apply_for_card(
            last_name,
            first_name,
            pin,
            phone,
            payment_system,
            card_class=CashbackDebitCard,
            **kwargs,
        )

    def issue_saving_card(
        self, last_name, first_name, pin, phone, payment_system, **kwargs
    ):
        return self.apply_for_card(
            last_name,
            first_name,
            pin,
            phone,
            payment_system,
            card_class=SavingCard,
            **kwargs,
        )

    def get_global_history(self) -> list:
        rows = list(TRANSACTION_HISTORY_HEADER)
        for tx in self.transaction_log:
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
```
### D. Обработка исключений
```python
import datetime as _dt
import itertools as _it
import re
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
CB_DEBIT_PAY_DESCRIPTION = (
    "{amount:.2f}₽ (MCC: {mcc}) с карты #{card_id} (кешбэк {cashback_amount:.2f}₽)"
)
SAVING_INTEREST_DESCRIPTION = (
    "Начислены проценты {interest:.2f}₽ по накопительной карте #{card_id}"
)

FORBIDDEN_MCC = {"7995", "4829", "6051"}

DEBIT_DEFAULT_CASHBACK_RATE = 0.03
DEPOSIT_LIMIT = 1_000_000.00
TRANSFER_LIMIT = 500_000.00
PAY_LIMIT = 500_000.00
MAX_CASHBACK_RATE = 0.10
MAX_SAVING_INTEREST_RATE = 0.3

SAVING_CARD_DEFAULT_INTEREST = 0.015

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


class BankError(Exception):
    pass


class ValidationError(BankError):
    PIN_MISMATCH = "Введенный ПИН-код не соответствует текущему"
    PIN_INVALID = "ПИН-код должен быть строкой из 4 символов"
    PIN_FORMAT_INVALID = "ПИН-код должен состоять только из цифр"
    NAME_INVALID = (
        "Имя и фамилия должны быть на русском, без использования специальных символов"
    )
    AMOUNT_NEGATIVE = "Сумма должна быть положительной"
    DEPOSIT_AMOUNT_NEGATIVE = "Сумма пополнений должна быть положительной"
    CASHBACK_NEGATIVE = "Процент кешбэка на покупки должен быть положительным"
    INTEREST_NEGATIVE = "Ставка по счету должна быть положительной"
    PAY_AMOUNT_NEGATIVE = "Сумма покупки должна быть положительной"
    INVALID_MCC = "Неверный код категории продавца (MCC)"
    PAYMENT_SYSTEM_NOT_SUPPORTED = (
        "Платежная система {payment_system} не поддерживается банком"
    )


class NotFoundError(BankError):
    RECIPIENT_NOT_FOUND = "Ошибка номером карты. Такой карты не существует."


class AccessError(BankError):
    CARD_CLOSED = "Карта закрыта или заблокирована. Невозможно провести операцию."
    ACCOUNT_NOT_LINKED = "Карта не привязана к счёту"
    BANK_NOT_LINKED = "Карта не привязана к банку"
    RECIPIENT_ACCOUNT_NOT_LINKED = "Карта получателя не привязана к счёту"
    RECIPIENT_CARD_CLOSED = (
        "Карта получателя закрыта или заблокирована. Невозможно провести операцию."
    )


class BusinessRuleError(BankError):
    DEPOSIT_LIMIT_EXCEEDED = (
        "Превышен лимит депозита. Карта заблокирована до выяснения причин."
    )
    TRANSFER_LIMIT_EXCEEDED = (
        "Подозрение на мошенническую операцию. Карта заблокирована до выяснения причин."
    )
    CASHBACK_LIMIT = "Процент кешбэка завышен, возможна техническая ошибка. Карта заблокирована до выяснения причин."
    TRANSFER_TO_SELF = "Нельзя пересылать деньги самому себе"
    USER_CONFLICT = "Пользователь с таким телефоном уже зарегистрирован"
    TOO_MANY_DEBIT_CARDS = "У пользователя уже есть пять дебетовых карт"
    MCC_FORBIDDEN = "Оплата отклонена. Покупки по {mcc} запрещены банком"
    PURCHASE_LIMIT_EXCEEDED = (
        "Сумма оплаты превышает лимит. Операция заблокирована до выяснения причин."
    )
    PAYMENT_NOT_ALLOWED_FOR_SAVING = "С накопительного счёта нельзя списывать покупки"
    SAVING_RATE_TOO_HIGH = (
        "Ставка накопления завышена, возможна техническая ошибка. "
        "Карта заблокирована до выяснения причины."
    )


class InsufficientFundsError(BankError):
    INSUFFICIENT_FUNDS_FOR_PAYMENT = "Недостаточно денег для оплаты."
    INSUFFICIENT_FUNDS_FOR_TRANSFER = "Недостаточно денег для осуществления перевода."


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
        for pin_value in [old_pin, new_pin]:
            if not (isinstance(pin_value, str) and len(pin_value) == 4):
                raise ValidationError(ValidationError.PIN_INVALID)
            if not pin_value.isdigit():
                raise ValidationError(ValidationError.PIN_FORMAT_INVALID)
        if self.pin != old_pin:
            raise ValidationError(ValidationError.PIN_MISMATCH)
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
        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)
        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)

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
        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)
        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)
        balance = self.account.balance
        return BALANCE_DESCRIPTION.format(balance=balance)

    def deposit(self, amount: float):

        if amount <= 0:
            raise ValidationError(ValidationError.DEPOSIT_AMOUNT_NEGATIVE)
        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)
        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)
        if amount > DEPOSIT_LIMIT:
            self.status = CardStatus.BLOCKED
            raise BusinessRuleError(BusinessRuleError.DEPOSIT_LIMIT_EXCEEDED)

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
        if amount <= 0:
            raise ValidationError(ValidationError.AMOUNT_NEGATIVE)

        if to_card is None:
            raise NotFoundError(NotFoundError.RECIPIENT_NOT_FOUND)

        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)

        if not to_card.account:
            raise AccessError(AccessError.RECIPIENT_ACCOUNT_NOT_LINKED)

        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)

        if to_card.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.RECIPIENT_CARD_CLOSED)

        if self.card_id == to_card.card_id:
            raise BusinessRuleError(BusinessRuleError.TRANSFER_TO_SELF)

        if amount > TRANSFER_LIMIT:
            self.status = CardStatus.BLOCKED
            raise BusinessRuleError(BusinessRuleError.TRANSFER_LIMIT_EXCEEDED)

        if self.account.balance < amount:
            raise InsufficientFundsError(
                InsufficientFundsError.INSUFFICIENT_FUNDS_FOR_TRANSFER
            )

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
        if amount <= 0:
            raise ValidationError(ValidationError.PAY_AMOUNT_NEGATIVE)

        if not (isinstance(mcc, str) and mcc.isdigit() and len(mcc) == 4):
            raise ValidationError(ValidationError.INVALID_MCC)

        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)

        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)

        if mcc in FORBIDDEN_MCC:
            raise BusinessRuleError(BusinessRuleError.MCC_FORBIDDEN.format(mcc=mcc))

        if amount > PAY_LIMIT:
            self.status = CardStatus.BLOCKED
            raise BusinessRuleError(BusinessRuleError.PURCHASE_LIMIT_EXCEEDED)

        if self.account.balance < amount:
            raise InsufficientFundsError(
                InsufficientFundsError.INSUFFICIENT_FUNDS_FOR_PAYMENT
            )

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
        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)

        if not self.bank:
            raise AccessError(AccessError.BANK_NOT_LINKED)

        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)

        rows = list(TRANSACTION_HISTORY_HEADER)
        for tx in self.bank.transaction_log:
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


class SimpleDebitCard(Card):
    pass


class CashbackDebitCard(Card):
    def __init__(self, *, cashback_rate: float = DEBIT_DEFAULT_CASHBACK_RATE, **kwargs):
        super().__init__(**kwargs)
        self.cashback_rate = cashback_rate

    def pay(self, amount: float, mcc: str):
        if amount <= 0:
            raise ValidationError(ValidationError.PAY_AMOUNT_NEGATIVE)

        if not (isinstance(mcc, str) and mcc.isdigit() and len(mcc) == 4):
            raise ValidationError(ValidationError.INVALID_MCC)

        if self.cashback_rate < 0:
            raise ValidationError(ValidationError.CASHBACK_NEGATIVE)

        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)

        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)

        if self.cashback_rate >= MAX_CASHBACK_RATE:
            self.status = CardStatus.BLOCKED
            raise BusinessRuleError(BusinessRuleError.CASHBACK_LIMIT)

        if mcc in FORBIDDEN_MCC:
            raise BusinessRuleError(BusinessRuleError.MCC_FORBIDDEN.format(mcc=mcc))

        if amount > PAY_LIMIT:
            self.status = CardStatus.BLOCKED
            raise BusinessRuleError(BusinessRuleError.PURCHASE_LIMIT_EXCEEDED)

        if self.account.balance < amount:
            raise InsufficientFundsError(
                InsufficientFundsError.INSUFFICIENT_FUNDS_FOR_PAYMENT
            )

        self.account.balance -= amount
        cashback_amount = round(float(amount * self.cashback_rate), 2)
        self.account.cashback_balance += cashback_amount

        self.bank.transaction_log.append(
            Transaction(
                from_card=self.card_id,
                to_card=None,
                amount=amount,
                type=TransactionType.PAY,
                mcc=mcc,
                cashback=cashback_amount,
                description=CB_DEBIT_PAY_DESCRIPTION.format(
                    amount=amount,
                    mcc=mcc,
                    card_id=self.card_id,
                    cashback_amount=cashback_amount,
                ),
                timestamp=next_timestamp_after(self.issue_date),
            )
        )


class SavingCard(Card):
    def __init__(
        self, *, interest_rate: float = SAVING_CARD_DEFAULT_INTEREST, **kwargs
    ):
        super().__init__(**kwargs)
        self.interest_rate = interest_rate

    def pay(self, amount: float, mcc: str):
        raise BusinessRuleError(BusinessRuleError.PAYMENT_NOT_ALLOWED_FOR_SAVING)

    def accrue_interest(self):
        if self.interest_rate < 0:
            raise ValidationError(ValidationError.INTEREST_NEGATIVE)

        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)

        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)

        if self.interest_rate >= MAX_SAVING_INTEREST_RATE:
            self.status = CardStatus.BLOCKED
            raise BusinessRuleError(BusinessRuleError.SAVING_RATE_TOO_HIGH)

        if self.account.balance >= 0:
            interest = round(self.account.balance * self.interest_rate, 2)
            self.account.balance += interest

            self.bank.transaction_log.append(
                Transaction(
                    from_card=None,
                    to_card=self.card_id,
                    amount=interest,
                    cashback=DEFAULT_CASHBACK_TRANSACTION,
                    type=TransactionType.INTEREST,
                    mcc=None,
                    description=SAVING_INTEREST_DESCRIPTION.format(
                        interest=interest, card_id=self.card_id
                    ),
                    timestamp=next_timestamp_after(self.issue_date),
                )
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
        if not (isinstance(pin, str) and pin.isdigit() and len(pin) == 4):
            if not (isinstance(pin, str) and pin.isdigit()):
                raise ValidationError(ValidationError.PIN_FORMAT_INVALID)
            else:
                raise ValidationError(ValidationError.PIN_INVALID)

        name_pattern = r"^[А-ЯЁа-яё]+(?:[ -][А-ЯЁа-яё]+)*$"
        if not re.fullmatch(name_pattern, last_name) or not re.fullmatch(
            name_pattern, first_name
        ):
            raise ValidationError(ValidationError.NAME_INVALID)

        allowed_systems = set(BIN_BY_SYSTEM.keys())
        if payment_system.upper() not in allowed_systems:
            raise ValidationError(
                ValidationError.PAYMENT_SYSTEM_NOT_SUPPORTED.format(
                    payment_system=payment_system
                )
            )

        for existing_user in self.customers.values():
            if existing_user.phone == phone:
                if (
                    existing_user.last_name != last_name
                    or existing_user.first_name != first_name
                ):
                    raise BusinessRuleError(BusinessRuleError.USER_CONFLICT)

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
        if user and issubclass(card_class, (SimpleDebitCard, CashbackDebitCard)):
            debit_cards_count = sum(
                1
                for c in user.cards
                if isinstance(c, (SimpleDebitCard, CashbackDebitCard))
                and c.status not in [CardStatus.CLOSED, CardStatus.BLOCKED]
            )
            if debit_cards_count >= 5:
                raise BusinessRuleError(BusinessRuleError.TOO_MANY_DEBIT_CARDS)

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

    def issue_simple_debit_card(
        self, last_name, first_name, pin, phone, payment_system, **kwargs
    ):
        return self.apply_for_card(
            last_name,
            first_name,
            pin,
            phone,
            payment_system,
            card_class=SimpleDebitCard,
            **kwargs,
        )

    def issue_cashback_debit_card(
        self, last_name, first_name, pin, phone, payment_system, **kwargs
    ):
        return self.apply_for_card(
            last_name,
            first_name,
            pin,
            phone,
            payment_system,
            card_class=CashbackDebitCard,
            **kwargs,
        )

    def issue_saving_card(
        self, last_name, first_name, pin, phone, payment_system, **kwargs
    ):
        return self.apply_for_card(
            last_name,
            first_name,
            pin,
            phone,
            payment_system,
            card_class=SavingCard,
            **kwargs,
        )

    def get_global_history(self) -> list:
        rows = list(TRANSACTION_HISTORY_HEADER)
        for tx in self.transaction_log:
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
```
### E. Сбор всех ошибок и поддержка работы программы
```python
import datetime as _dt
import itertools as _it
import re
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
CB_DEBIT_PAY_DESCRIPTION = (
    "{amount:.2f}₽ (MCC: {mcc}) с карты #{card_id} (кешбэк {cashback_amount:.2f}₽)"
)
SAVING_INTEREST_DESCRIPTION = (
    "Начислены проценты {interest:.2f}₽ по накопительной карте #{card_id}"
)

FORBIDDEN_MCC = {"7995", "4829", "6051"}

DEBIT_DEFAULT_CASHBACK_RATE = 0.03
DEPOSIT_LIMIT = 1_000_000.00
TRANSFER_LIMIT = 500_000.00
PAY_LIMIT = 500_000.00
MAX_CASHBACK_RATE = 0.10  # 10%
MAX_SAVING_INTEREST_RATE = 0.3

SAVING_CARD_DEFAULT_INTEREST = 0.015

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


class BankError(Exception):
    pass


class ValidationError(BankError):
    PIN_MISMATCH = "Введенный ПИН-код не соответствует текущему"
    PIN_INVALID = "ПИН-код должен быть строкой из 4 символов"
    PIN_FORMAT_INVALID = "ПИН-код должен состоять только из цифр"
    NAME_INVALID = (
        "Имя и фамилия должны быть на русском, без использования специальных символов"
    )
    AMOUNT_NEGATIVE = "Сумма должна быть положительной"
    DEPOSIT_AMOUNT_NEGATIVE = "Сумма пополнений должна быть положительной"
    CASHBACK_NEGATIVE = "Процент кешбэка на покупки должен быть положительным"
    INTEREST_NEGATIVE = "Ставка по счету должна быть положительной"
    PAY_AMOUNT_NEGATIVE = "Сумма покупки должна быть положительной"
    INVALID_MCC = "Неверный код категории продавца (MCC)"
    PAYMENT_SYSTEM_NOT_SUPPORTED = (
        "Платежная система {payment_system} не поддерживается банком"
    )


class NotFoundError(BankError):
    RECIPIENT_NOT_FOUND = "Ошибка номером карты. Такой карты не существует."


class AccessError(BankError):
    CARD_CLOSED = "Карта закрыта или заблокирована. Невозможно провести операцию."
    ACCOUNT_NOT_LINKED = "Карта не привязана к счёту"
    BANK_NOT_LINKED = "Карта не привязана к банку"
    RECIPIENT_ACCOUNT_NOT_LINKED = "Карта получателя не привязана к счёту"
    RECIPIENT_CARD_CLOSED = (
        "Карта получателя закрыта или заблокирована. Невозможно провести операцию."
    )


class BusinessRuleError(BankError):
    DEPOSIT_LIMIT_EXCEEDED = (
        "Превышен лимит депозита. Карта заблокирована до выяснения причин."
    )
    TRANSFER_LIMIT_EXCEEDED = (
        "Подозрение на мошенническую операцию. Карта заблокирована до выяснения причин."
    )
    CASHBACK_LIMIT = "Процент кешбэка завышен, возможна техническая ошибка. Карта заблокирована до выяснения причин."
    TRANSFER_TO_SELF = "Нельзя пересылать деньги самому себе"
    USER_CONFLICT = "Пользователь с таким телефоном уже зарегистрирован"
    TOO_MANY_DEBIT_CARDS = "У пользователя уже есть пять дебетовых карт"
    MCC_FORBIDDEN = "Оплата отклонена. Покупки по {mcc} запрещены банком"
    PURCHASE_LIMIT_EXCEEDED = (
        "Сумма оплаты превышает лимит. Операция заблокирована до выяснения причин."
    )
    PAYMENT_NOT_ALLOWED_FOR_SAVING = "С накопительного счёта нельзя списывать покупки"
    SAVING_RATE_TOO_HIGH = (
        "Ставка накопления завышена, возможна техническая ошибка. "
        "Карта заблокирована до выяснения причины."
    )


class InsufficientFundsError(BankError):
    INSUFFICIENT_FUNDS_FOR_PAYMENT = "Недостаточно денег для оплаты."
    INSUFFICIENT_FUNDS_FOR_TRANSFER = "Недостаточно денег для осуществления перевода."


error_log = []


def catch_errors_and_log_method(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except BankError as e:
            error_text = str(e)
            error_log.append(error_text)
            print(f"{error_text}")

    return wrapper


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

    @catch_errors_and_log_method
    def change_pin(self, old_pin: str, new_pin: str):
        for pin_value in [old_pin, new_pin]:
            if not (isinstance(pin_value, str) and len(pin_value) == 4):
                raise ValidationError(ValidationError.PIN_INVALID)
            if not pin_value.isdigit():
                raise ValidationError(ValidationError.PIN_FORMAT_INVALID)
        if self.pin != old_pin:
            raise ValidationError(ValidationError.PIN_MISMATCH)
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

    @catch_errors_and_log_method
    def get_card_info(self, fields: list = None):
        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)
        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)

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

    @catch_errors_and_log_method
    def get_balance(self):
        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)
        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)
        balance = self.account.balance
        return BALANCE_DESCRIPTION.format(balance=balance)

    @catch_errors_and_log_method
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValidationError(ValidationError.DEPOSIT_AMOUNT_NEGATIVE)
        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)
        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)
        if amount > DEPOSIT_LIMIT:
            self.status = CardStatus.BLOCKED
            raise BusinessRuleError(BusinessRuleError.DEPOSIT_LIMIT_EXCEEDED)

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

    @catch_errors_and_log_method
    def transfer(self, to_card, amount: float):
        if amount <= 0:
            raise ValidationError(ValidationError.AMOUNT_NEGATIVE)
        if to_card is None:
            raise NotFoundError(NotFoundError.RECIPIENT_NOT_FOUND)
        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)
        if not to_card.account:
            raise AccessError(AccessError.RECIPIENT_ACCOUNT_NOT_LINKED)
        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)
        if to_card.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.RECIPIENT_CARD_CLOSED)
        if self.card_id == to_card.card_id:
            raise BusinessRuleError(BusinessRuleError.TRANSFER_TO_SELF)
        if amount > TRANSFER_LIMIT:
            self.status = CardStatus.BLOCKED
            raise BusinessRuleError(BusinessRuleError.TRANSFER_LIMIT_EXCEEDED)
        if self.account.balance < amount:
            raise InsufficientFundsError(
                InsufficientFundsError.INSUFFICIENT_FUNDS_FOR_TRANSFER
            )

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

    @catch_errors_and_log_method
    def pay(self, amount: float, mcc: str):
        if amount <= 0:
            raise ValidationError(ValidationError.PAY_AMOUNT_NEGATIVE)
        if not (isinstance(mcc, str) and mcc.isdigit() and len(mcc) == 4):
            raise ValidationError(ValidationError.INVALID_MCC)
        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)
        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)
        if mcc in FORBIDDEN_MCC:
            raise BusinessRuleError(BusinessRuleError.MCC_FORBIDDEN.format(mcc=mcc))
        if amount > PAY_LIMIT:
            self.status = CardStatus.BLOCKED
            raise BusinessRuleError(BusinessRuleError.PURCHASE_LIMIT_EXCEEDED)
        if self.account.balance < amount:
            raise InsufficientFundsError(
                InsufficientFundsError.INSUFFICIENT_FUNDS_FOR_PAYMENT
            )

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

    @catch_errors_and_log_method
    def get_transaction_history(self):
        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)
        if not self.bank:
            raise AccessError(AccessError.BANK_NOT_LINKED)
        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)

        rows = list(TRANSACTION_HISTORY_HEADER)
        for tx in self.bank.transaction_log:
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


class SimpleDebitCard(Card):
    pass


class CashbackDebitCard(Card):
    def __init__(self, *, cashback_rate: float = DEBIT_DEFAULT_CASHBACK_RATE, **kwargs):
        super().__init__(**kwargs)
        self.cashback_rate = cashback_rate

    @catch_errors_and_log_method
    def pay(self, amount: float, mcc: str):
        if amount <= 0:
            raise ValidationError(ValidationError.PAY_AMOUNT_NEGATIVE)
        if not (isinstance(mcc, str) and mcc.isdigit() and len(mcc) == 4):
            raise ValidationError(ValidationError.INVALID_MCC)
        if self.cashback_rate < 0:
            raise ValidationError(ValidationError.CASHBACK_NEGATIVE)
        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)
        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)
        if self.cashback_rate >= MAX_CASHBACK_RATE:
            self.status = CardStatus.BLOCKED
            raise BusinessRuleError(BusinessRuleError.CASHBACK_LIMIT)
        if mcc in FORBIDDEN_MCC:
            raise BusinessRuleError(BusinessRuleError.MCC_FORBIDDEN.format(mcc=mcc))
        if amount > PAY_LIMIT:
            self.status = CardStatus.BLOCKED
            raise BusinessRuleError(BusinessRuleError.PURCHASE_LIMIT_EXCEEDED)
        if self.account.balance < amount:
            raise InsufficientFundsError(
                InsufficientFundsError.INSUFFICIENT_FUNDS_FOR_PAYMENT
            )

        self.account.balance -= amount
        cashback_amount = round(float(amount * self.cashback_rate), 2)
        self.account.cashback_balance += cashback_amount

        self.bank.transaction_log.append(
            Transaction(
                from_card=self.card_id,
                to_card=None,
                amount=amount,
                type=TransactionType.PAY,
                mcc=mcc,
                cashback=cashback_amount,
                description=CB_DEBIT_PAY_DESCRIPTION.format(
                    amount=amount,
                    mcc=mcc,
                    card_id=self.card_id,
                    cashback_amount=cashback_amount,
                ),
                timestamp=next_timestamp_after(self.issue_date),
            )
        )


class SavingCard(Card):
    def __init__(
        self, *, interest_rate: float = SAVING_CARD_DEFAULT_INTEREST, **kwargs
    ):
        super().__init__(**kwargs)
        self.interest_rate = interest_rate

    @catch_errors_and_log_method
    def pay(self, amount: float, mcc: str):
        raise BusinessRuleError(BusinessRuleError.PAYMENT_NOT_ALLOWED_FOR_SAVING)

    @catch_errors_and_log_method
    def accrue_interest(self):
        if self.interest_rate < 0:
            raise ValidationError(ValidationError.INTEREST_NEGATIVE)
        if not self.account:
            raise AccessError(AccessError.ACCOUNT_NOT_LINKED)
        if self.status in [CardStatus.CLOSED, CardStatus.BLOCKED]:
            raise AccessError(AccessError.CARD_CLOSED)
        if self.interest_rate >= MAX_SAVING_INTEREST_RATE:
            self.status = CardStatus.BLOCKED
            raise BusinessRuleError(BusinessRuleError.SAVING_RATE_TOO_HIGH)

        if self.account.balance >= 0:
            interest = round(self.account.balance * self.interest_rate, 2)
            self.account.balance += interest

            self.bank.transaction_log.append(
                Transaction(
                    from_card=None,
                    to_card=self.card_id,
                    amount=interest,
                    cashback=DEFAULT_CASHBACK_TRANSACTION,
                    type=TransactionType.INTEREST,
                    mcc=None,
                    description=SAVING_INTEREST_DESCRIPTION.format(
                        interest=interest, card_id=self.card_id
                    ),
                    timestamp=next_timestamp_after(self.issue_date),
                )
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

    @catch_errors_and_log_method
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
        if not (isinstance(pin, str) and pin.isdigit() and len(pin) == 4):
            if not (isinstance(pin, str) and pin.isdigit()):
                raise ValidationError(ValidationError.PIN_FORMAT_INVALID)
            else:
                raise ValidationError(ValidationError.PIN_INVALID)

        name_pattern = r"^[А-ЯЁа-яё]+(?:[ -][А-ЯЁа-яё]+)*$"
        if not re.fullmatch(name_pattern, last_name) or not re.fullmatch(
            name_pattern, first_name
        ):
            raise ValidationError(ValidationError.NAME_INVALID)

        allowed_systems = set(BIN_BY_SYSTEM.keys())
        if payment_system.upper() not in allowed_systems:
            raise ValidationError(
                ValidationError.PAYMENT_SYSTEM_NOT_SUPPORTED.format(
                    payment_system=payment_system
                )
            )

        for existing_user in self.customers.values():
            if existing_user.phone == phone:
                if (
                    existing_user.last_name != last_name
                    or existing_user.first_name != first_name
                ):
                    raise BusinessRuleError(BusinessRuleError.USER_CONFLICT)

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
        if user and issubclass(card_class, (SimpleDebitCard, CashbackDebitCard)):
            debit_cards_count = sum(
                1
                for c in user.cards
                if isinstance(c, (SimpleDebitCard, CashbackDebitCard))
                and c.status not in [CardStatus.CLOSED, CardStatus.BLOCKED]
            )
            if debit_cards_count >= 5:
                raise BusinessRuleError(BusinessRuleError.TOO_MANY_DEBIT_CARDS)

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

    def issue_simple_debit_card(
        self, last_name, first_name, pin, phone, payment_system, **kwargs
    ):
        return self.apply_for_card(
            last_name,
            first_name,
            pin,
            phone,
            payment_system,
            card_class=SimpleDebitCard,
            **kwargs,
        )

    def issue_cashback_debit_card(
        self, last_name, first_name, pin, phone, payment_system, **kwargs
    ):
        return self.apply_for_card(
            last_name,
            first_name,
            pin,
            phone,
            payment_system,
            card_class=CashbackDebitCard,
            **kwargs,
        )

    def issue_saving_card(
        self, last_name, first_name, pin, phone, payment_system, **kwargs
    ):
        return self.apply_for_card(
            last_name,
            first_name,
            pin,
            phone,
            payment_system,
            card_class=SavingCard,
            **kwargs,
        )

    def get_global_history(self) -> list:
        rows = list(TRANSACTION_HISTORY_HEADER)
        for tx in self.transaction_log:
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
```
