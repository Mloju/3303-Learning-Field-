"""Small, reusable CSV analysis example built with pandas.

Run this module directly to analyse the Seaborn Iris dataset, or import its
functions to analyse another CSV/DataFrame.
"""

from __future__ import annotations

from pathlib import Path
from typing import TypeAlias

import pandas as pd


DEFAULT_DATASET = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
DataSource: TypeAlias = str | Path


class DataAnalysisError(Exception):
    """Raised when input data cannot be loaded or does not meet requirements."""


def load_csv(source: DataSource) -> pd.DataFrame:
    """Load a CSV from a local path or URL.

    Args:
        source: Path or HTTP(S) URL of the CSV file.

    Raises:
        DataAnalysisError: If pandas cannot read the CSV.
    """
    try:
        return pd.read_csv(source)
    except (OSError, ValueError, UnicodeDecodeError) as error:
        raise DataAnalysisError(f"Could not load CSV from {source!s}: {error}") from error


def require_columns(data: pd.DataFrame, *columns: str) -> None:
    """Validate that every requested column exists in *data*."""
    missing_columns = sorted(set(columns) - set(data.columns))
    if missing_columns:
        available = ", ".join(map(str, data.columns))
        missing = ", ".join(missing_columns)
        raise DataAnalysisError(
            f"Missing required column(s): {missing}. Available columns: {available}"
        )


def column_mean(data: pd.DataFrame, column: str) -> float:
    """Return the mean of a numeric column after validating its presence."""
    require_columns(data, column)
    try:
        return float(data[column].mean())
    except TypeError as error:
        raise DataAnalysisError(f"Column '{column}' must contain numeric values.") from error


def column_maximum(data: pd.DataFrame, column: str) -> float:
    """Return the maximum of a numeric column after validating its presence."""
    require_columns(data, column)
    try:
        return float(data[column].max())
    except TypeError as error:
        raise DataAnalysisError(f"Column '{column}' must contain numeric values.") from error


def filter_by_value(data: pd.DataFrame, column: str, value: object) -> pd.DataFrame:
    """Return rows whose *column* exactly matches *value*."""
    require_columns(data, column)
    return data.loc[data[column] == value].copy()


def analyse_iris(source: DataSource = DEFAULT_DATASET) -> tuple[float, float, pd.DataFrame]:
    """Load Iris data and return its requested summary values and setosa rows."""
    data = load_csv(source)
    average_sepal_length = column_mean(data, "sepal_length")
    maximum_petal_width = column_maximum(data, "petal_width")
    setosa_rows = filter_by_value(data, "species", "setosa")
    return average_sepal_length, maximum_petal_width, setosa_rows


def main() -> None:
    """Run the classroom Iris analysis and print a concise report."""
    try:
        average, maximum, setosa_rows = analyse_iris()
    except DataAnalysisError as error:
        print(f"Analysis failed: {error}")
        return

    print(f"Average sepal length: {average}")
    print(f"Max petal width: {maximum}")
    print("First five setosa rows:")
    print(setosa_rows.head())


if __name__ == "__main__":
    main()
