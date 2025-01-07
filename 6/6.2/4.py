# Акция
from pandas import DataFrame, Series


def cheque(price_list: Series, **kwargs) -> DataFrame:
    products = sorted(kwargs)
    product_dict = {
        "product": products,
        "price": [price_list[i] for i in products],
        "number": [kwargs[i] for i in products]}
    product_dict["cost"] = [price_list[i] * product_dict["number"][index] for index, i in enumerate(products)]
    return DataFrame(product_dict)


def discount(cheque: DataFrame) -> DataFrame:
    new_cheque = cheque.copy()
    for i in range(len(new_cheque.loc[:, "cost"])):
        new_cheque.loc[i, "cost"] /= 1 + (cheque.loc[:, "number"][i] > 2)
    return new_cheque
