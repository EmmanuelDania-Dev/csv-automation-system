from app.processor import process_employee_files
from app.logger import setup_logger
from app.reporter import generate_report

def run_automation(dry_run: bool = False) -> dict:

    logger = setup_logger()

    logger.info("Automation pipeline started")

    if dry_run:
        logger.info("Pipeline running in DRY-RUN mode")

    results = process_employee_files(dry_run=dry_run)

    logger.info(
        f"Total files discovered: {results['total_files']}"
    )

    logger.info(
        f"Successfully processed: {len(results['successful_files'])}"
    )

    logger.info(
        f"Files skipped: {len(results['skipped_files'])}"
    )

    logger.info(
        f"Files failed: {len(results['failed_files'])}"
    )

    report_path = generate_report(results)

    logger.info(
        f"Processing report generated: {report_path}"
    )

    logger.info("Automation pipeline completed")

    return results
