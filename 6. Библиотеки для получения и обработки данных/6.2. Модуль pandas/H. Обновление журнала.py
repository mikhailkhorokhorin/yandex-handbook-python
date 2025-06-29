from pandas import DataFrame


def update(journal: DataFrame) -> DataFrame:
    new_journal = journal.copy()
    for i in range(len(new_journal.loc[:, "name"])):
        new_journal.loc[:, "average"] = (
            new_journal["maths"]
            + new_journal["physics"]
            + new_journal["computer science"]
        ) / 3
    return new_journal.sort_values(
        by=["average", "name"], ascending=(False, True)
    )
