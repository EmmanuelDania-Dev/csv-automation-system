from pathlib import Path
import pandas as pd
from typing import Any
import time

from app.logger import setup_logger
from app.config import INCOMING_DIR, PROCESSED_DIR

def find_csv_files() -> list[Path]:

    csv_files = list(INCOMING_DIR.glob("*.csv"))

    return csv_files

def read_csv_file(filepath: Path) -> pd.DataFrame:

    df = pd.read_csv(filepath)

    return df 


def validate_dataframe(df: pd.DataFrame) -> list[str]:
    errors = []

    if df.empty:
        errors.append("The CSV file contains no records.")

    if df.columns.duplicated().any():
        errors.append("The CSV file contains duplicate column names.")

    return errors

def clean_employee_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()

    cleaned_df = cleaned_df.drop_duplicates()

    cleaned_df["age"] = pd.to_numeric(
        cleaned_df["age"],
        errors="coerce"
    )

    median_age = cleaned_df["age"].median()

    if pd.isna(median_age):
        raise ValueError("Cannot fill missing ages because no valid age exist.")

    cleaned_df["age"] = cleaned_df["age"].fillna(median_age)

    cleaned_df["age"] = cleaned_df["age"].astype(int)

    return cleaned_df

def save_processed_file(
    file_path: Path,
    df: pd.DataFrame,
) -> Path:

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    output_path = PROCESSED_DIR / file_path.name

    df.to_csv(output_path, index=False)

    return output_path

def validate_employee_dataframe(df: pd.DataFrame) -> list[str]:
    required_columns = [
        "employee_name",
        "age",
        "department",
        "salary"
    ]

    errors = []

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        errors.append(
            f"Missing required employee columns: {', '.join(missing_columns)}"
        )

    return errors


import time


def read_csv_with_retry(
    filepath: Path,
    max_attempts: int = 3,
    delay: int = 2
) -> pd.DataFrame:

    logger = setup_logger()

    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    for attempt in range(1, max_attempts + 1):
        try:
            return read_csv_file(filepath)

        except OSError as error:
            logger.warning(
                f"Attempt {attempt}/{max_attempts} failed "
                f"for {filepath.name}: {error}"
            )

            if attempt == max_attempts:
                raise

            time.sleep(delay)

    raise RuntimeError("CSV reading failed unexpectedly")



def process_employee_files(dry_run: bool = False) -> dict[str, Any]:

    csv_files = find_csv_files()

    processed_data = {}
    successful_files = []
    skipped_files = {}
    failed_files = {}

    logger = setup_logger()

    for file_path in csv_files:
        try:
            df = read_csv_with_retry(file_path)

            validation_errors = validate_dataframe(df)

            if validation_errors:
                logger.warning(
                    f"Validation failed for {file_path.name}"
                )

                for error in validation_errors:
                    logger.warning(error)

                skipped_files[file_path.name] = validation_errors
                continue

            employee_errors = validate_employee_dataframe(df)

            if employee_errors:
                logger.warning(
                    f"Employee validation failed for {file_path.name}"
                )

                for error in employee_errors:
                    logger.warning(error)

                skipped_files[file_path.name] = employee_errors
                continue

            cleaned_df = clean_employee_data(df)

            if dry_run:
                logger.info(
                    f"Dry run: {file_path.name} would be processed successfully"
                )

            else:
                save_processed_file(file_path, cleaned_df)

                logger.info(
                    f"Successfully processed {file_path.name}"
                )

            processed_data[file_path.name] = cleaned_df
            successful_files.append(file_path.name)

        except (
            pd.errors.EmptyDataError,
            pd.errors.ParserError,
            UnicodeDecodeError,
            ValueError,
            OSError
        ) as error:

            logger.error(
                f"Failed to process {file_path.name}: {error}"
            )

            failed_files[file_path.name] = [str(error)]

    return {
        "total_files": len(csv_files),
        "dry_run": dry_run,
        "processed_data": processed_data,
        "successful_files": successful_files,
        "skipped_files": skipped_files,
        "failed_files": failed_files
    }
