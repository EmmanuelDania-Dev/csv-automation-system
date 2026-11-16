# Python Automation & Analytics Pipeline

**Week 8 Project | AI Native Python Developer Internship at FlexiSAF**

A Python-based automation pipeline for processing employee CSV files. The project automates CSV discovery, data validation, cleaning, processing, and reporting while maintaining detailed logs of pipeline activities.

This project was developed as part of my Week 8 internship assignment at FlexiSAF, demonstrating practical application of Python automation, Pandas, data quality checks, error handling, and automated reporting.

## Project Overview

This project was developed to automate the processing of employee datasets using Python and Pandas.

Instead of manually inspecting and cleaning CSV files, the pipeline automatically discovers incoming files, validates their structure and contents, cleans valid employee data, and exports the processed datasets.

It also generates processing reports and maintains logs to make the entire workflow traceable.

## Features

- **CSV File Discovery:** Automatically discovers CSV files in the incoming directory.
- **CSV Reading with Retry:** Retries failed file-reading operations up to a configurable number of attempts.
- **Data Validation:** Checks datasets for empty files, invalid structures, and missing required columns.
- **Employee Data Validation:** Performs additional validation specific to employee records.
- **Data Cleaning:** Removes duplicate records, handles missing values, and converts data into appropriate data types.
- **Automated Processing:** Processes valid CSV files and saves cleaned datasets.
- **Dry-Run Mode:** Simulates the processing workflow without saving processed files.
- **Error Handling:** Handles file-reading and data-processing errors without unnecessarily interrupting the pipeline.
- **Logging:** Records processing activities, warnings, errors, and successful operations.
- **Report Generation:** Generates timestamped reports summarising pipeline execution.

## Technologies Used

- Python
- Pandas
- Logging
- pathlib
- Time

## Project Structure

```text
automation-system/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── processor.py
│   ├── automation.py
│   ├── reporter.py
│   └── logger.py
│
├── data/
│   ├── incoming/
│   ├── processed/
│   └── reports/
│
├── logs/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How the Pipeline Works

The automation pipeline follows these steps:

1. **File Discovery:** Searches the incoming directory for CSV files.
2. **File Reading:** Reads each CSV file using a retry mechanism to handle temporary file-reading failures.
3. **General Validation:** Checks whether the dataset is valid and contains records.
4. **Employee Validation:** Checks for the required employee columns.
5. **Data Cleaning:** Removes duplicate records, handles missing age values, and ensures appropriate data types.
6. **File Export:** Saves successfully processed datasets into the processed directory.
7. **Logging:** Records successful operations, validation warnings, and processing errors.
8. **Report Generation:** Creates a processing report containing execution details and file-processing results.

## Required Employee Dataset Columns

The pipeline expects employee CSV files to contain the following columns:

| Column | Description |
|---|---|
| employee_name | Employee's name |
| age | Employee's age |
| department | Employee's department |
| salary | Employee's salary |

## Data Cleaning Operations

The cleaning process includes:

- Removing duplicate records.
- Identifying and handling missing age values.
- Filling missing age values using the median age.
- Converting age values to the appropriate integer data type.
- Checking the cleaned dataset for remaining missing values and duplicates.

The original incoming CSV files are preserved. Cleaned datasets are exported separately.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/EmmanuelDania-Dev
```

### 2. Navigate into the project directory

```bash
cd automation-system
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Place your CSV files inside:

```text
data/incoming/
```

Run the automation pipeline from the project root directory:

```bash
python main.py
```

The pipeline will automatically discover and process the available CSV files.

## Dry-Run Mode

The pipeline supports dry-run mode, which allows the processing workflow to be executed without saving processed CSV files.

This is useful for checking the pipeline's behaviour before performing actual file exports.

The dry-run functionality is controlled through the `dry_run` parameter.

## Output Directories

The pipeline generates three main categories of output:

**1. Processed Data**

```text
data/processed/
```

Contains successfully cleaned and processed CSV files.

**2. Processing Reports**

```text
data/reports/
```

Contains timestamped reports summarising each pipeline execution.

**3. Application Logs**

```text
logs/
```

Contains execution logs, including successful operations, validation warnings, and errors.

## Error Handling and Reliability

The pipeline includes error-handling mechanisms designed to improve reliability:

- Retries failed CSV-reading operations before giving up.
- Handles empty CSV files and parsing errors.
- Records invalid datasets as skipped files.
- Records unrecoverable processing errors as failed files.
- Continues processing other files when an individual file encounters a handled error.

## Key Learning Outcomes

Building this project provided practical experience with:

- Python automation and file handling.
- Pandas for data processing and cleaning.
- Data validation and quality checks.
- Exception handling and retry mechanisms.
- Modular Python application architecture.
- Logging and application monitoring.
- Generating automated processing reports.
- Designing reusable and maintainable data-processing functions.

## Demo Recording

This is a demo video of the project running successfully:
https://drive.google.com/file/d/1rZM_ZKBGqXa3ESEitEfnzIItr9ZjeW5d/view?usp=sharing

## Author

**Emmanuel Dania**

GitHub: https://github.com/EmmanuelDania-Dev