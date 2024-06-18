# CSV Comparison Framework

This project provides a simple BDD framework for comparing CSV files using the Behave library in Python.
It contains scenarios to verify if two CSV files are identical or different.

## Directory Structure

csv_comparison/
│
├── features/
│ ├── compare_csv.feature
│ └── steps/
│ └── compare_csv_steps.py
├── data/
│ ├── identical1.csv
│ ├── identical2.csv
│ ├── different1.csv
│ └── different2.csv
└── behave.ini

## Prerequisites

- Python 3.x
- `pip` package installer

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/csv_comparison.git
    cd csv_comparison
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install behave
    ```

## Usage

### Preparing the Test Data

Ensure the following CSV files are present in the `data/` directory:

**Identical CSV Files:**

`data/identical1.csv`:

`data/identical2.csv` (identical to `identical1.csv`):

**Different CSV Files:**

`data/different1.csv`:

`data/different2.csv` (different from `different1.csv`):

### Running the Tests

Execute the following command to run the Behave tests:

```sh
behave

Expected Output:
If the CSV files are correctly set up, the output should indicate that the scenarios passed or failed based on the comparisons:

qa@PC-0051 csv_comparison $ behave
Feature: Compare CSV files # features/compare_csv.feature:1

  Scenario: CSV files should be identical                                      # features/compare_csv.feature:3
    Given I have two CSV files "data/identical1.csv" and "data/identical2.csv" # features/steps/compare_csv_steps.py:5 0.000s
    When I compare the CSV files                                               # features/steps/compare_csv_steps.py:11 0.001s
    Then the CSV files should be identical                                     # features/steps/compare_csv_steps.py:31 0.000s

  Scenario: CSV files should have differences                                  # features/compare_csv.feature:8
    Given I have two CSV files "data/different1.csv" and "data/different2.csv" # features/steps/compare_csv_steps.py:5 0.000s
    When I compare the CSV files                                               # features/steps/compare_csv_steps.py:11 0.001s
    Then the CSV files should have differences                                 # features/steps/compare_csv_steps.py:38 0.000s

1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.002s

Project Structure:
features/compare_csv.feature: Contains the BDD scenarios for comparing CSV files.
features/steps/compare_csv_steps.py: Implements the step definitions for the scenarios.
data/: Directory containing the CSV files used in the tests.
behave.ini: Configuration file for Behave (optional).

# Additional scenarios can be covered as follows

When comparing CSV files, there are several additional scenarios that can be tested to ensure comprehensive coverage. Here are some examples:

Identical CSV Files with Different Orders:
Ensure that the comparison detects differences if the rows are in different orders, assuming order matters.
CSV Files with Different Headers:

Verify that differences are detected if the headers (first row) are different.
CSV Files with Different Number of Rows:

Ensure that the comparison detects differences if one file has more or fewer rows than the other.
CSV Files with Different Number of Columns:

Verify that differences are detected if the number of columns (fields) in the rows are different.
CSV Files with Extra Whitespace:

Ensure that differences are detected if there are extra spaces or tabs within the cells.
Empty CSV Files:

Verify the behavior when one or both CSV files are empty.
CSV Files with Missing Values:

Ensure that differences are detected if there are missing values in some rows.
CSV Files with Special Characters:

Verify that differences are detected correctly if special characters or different encodings are used.
