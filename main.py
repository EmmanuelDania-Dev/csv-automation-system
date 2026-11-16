
import argparse

from app.automation import run_automation


def main() -> None:

    parser = argparse.ArgumentParser(
        description="Employee Data Automation Pipeline"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run the pipeline without saving processed CSV files"
    )

    args = parser.parse_args()

    results = run_automation(dry_run=args.dry_run)

    print("\nAutomation Results")
    print("------------------")

    print(f"Total files discovered: {results['total_files']}")

    print(
        f"Successfully processed: "
        f"{len(results['successful_files'])}"
    )

    print(
        f"Files skipped: {len(results['skipped_files'])}"
    )

    print(
        f"Files failed: {len(results['failed_files'])}"
    )


if __name__ == "__main__":
    main()
