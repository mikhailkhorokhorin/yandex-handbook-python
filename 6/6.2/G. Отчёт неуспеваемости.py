from pandas import DataFrame


def need_to_work_better(journal: DataFrame) -> DataFrame:
    new_journal = journal.copy()
    return new_journal[
        (new_journal["maths"] < 3)
        | (new_journal["physics"] < 3)
        | (new_journal["computer science"] < 3)
    ]
