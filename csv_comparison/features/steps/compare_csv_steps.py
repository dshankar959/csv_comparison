import csv
from behave import given, when, then


@given('I have two CSV files "{file1}" and "{file2}"')
def step_given_two_csv_files(context, file1, file2):
    context.file1 = file1
    context.file2 = file2


@when('I compare the CSV files')
def step_when_compare_csv_files(context):
    file1 = context.file1
    file2 = context.file2

    with open(file1, newline='') as f1, open(file2, newline='') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)

        rows1 = list(reader1)
        rows2 = list(reader2)

        # Print the rows for debugging
        print(f"File 1 rows: {rows1}")
        print(f"File 2 rows: {rows2}")

        # Save the comparison result in the context dictionary
        context.comparison = (rows1 == rows2, rows1, rows2)


@then('the CSV files should be identical')
def step_then_csv_files_should_be_identical(context):
    comparison, rows1, rows2 = context.comparison
    assert comparison, f"CSV files are not identical:\n{rows1}\n!=\n{rows2}"
    print(f"Comparison result: {comparison}")


@then('the CSV files should have differences')
def step_then_csv_files_should_have_differences(context):
    comparison, rows1, rows2 = context.comparison
    assert not comparison, f"CSV files are identical, but differences were expected:\n{rows1}\n==\n{rows2}"
    print(f"Comparison result: {comparison}")
