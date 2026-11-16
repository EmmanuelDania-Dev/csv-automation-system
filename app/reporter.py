from datetime import datetime
from pathlib import Path

from app.config import REPORTS_DIR


now = datetime.now()

def generate_report(results: dict) -> Path:

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = now.strftime("%Y%m%d_%H%M%S")

    report_path = REPORTS_DIR / f"processing_report_{timestamp}.txt"


    lines = [
        "EMPLOYEE DATA PROCESSING REPORT",
        "=" * 40,
        "",
        f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"Total files discovered: {results['total_files']}",
        f"Successfully processed: {len(results['successful_files'])}",
        f"Files skipped: {len(results['skipped_files'])}",
        f"Files failed: {len(results['failed_files'])}",
        "",
        "SUCCESSFUL FILES",
        "=" * 40,
    ]

    if results["successful_files"]:
        for filename in results["successful_files"]:
            lines.append(f"- {filename}")
    else:
        lines.append("No files processed successfully")

    lines.extend([
        "",
        "SKIPPED FILES",
        "=" * 40,
    ])

    if results["skipped_files"]:
        for filename, errors in results["skipped_files"].items():
            lines.append(f"- {filename}")

            for error in errors:
                lines.append(f" Reason: {error}")

    else:
        lines.append("No files were skipped")

    lines.extend([
        "",
        "FAILED FILES",
        "=" * 40,
    ])

    if results["failed_files"]:
        for filename, errors in results["failed_files"].items():
            lines.append(f"- {filename}")

            for error in errors:
                lines.append(f"  Error: {error}")
    else:
        lines.append("No files failed.")

    lines.extend([
        "",
        "=" * 40,
        "END OF REPORT",
    ])

    report_path.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    return report_path
