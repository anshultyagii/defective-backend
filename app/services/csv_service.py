import csv
import io

from app.schemas.screening import ScreeningRequest


class CSVService:

    REQUIRED_COLUMNS = [
        "component_id",
        "lot_id",
        "value_0h",
        "value_24h",
        "value_96h"
    ]

    def parse_csv(self, file_content: bytes):

        # Decode uploaded CSV
        try:
            text = file_content.decode("utf-8")
        except UnicodeDecodeError:
            raise ValueError(
                "CSV file must be UTF-8 encoded."
            )

        # Read CSV
        reader = csv.DictReader(
            io.StringIO(text)
        )

        # Check headers
        if reader.fieldnames is None:
            raise ValueError(
                "CSV file does not contain headers."
            )

        missing_columns = [
            column
            for column in self.REQUIRED_COLUMNS
            if column not in reader.fieldnames
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

        components = []

        for row_number, row in enumerate(
            reader,
            start=2
        ):

            try:

                component = ScreeningRequest(
                    component_id=row["component_id"],
                    lot_id=row["lot_id"],
                    value_0h=float(row["value_0h"]),
                    value_24h=float(row["value_24h"]),
                    value_96h=float(row["value_96h"])
                )

                components.append(component)

            except Exception as error:

                raise ValueError(
                    f"Invalid data at CSV row "
                    f"{row_number}: {error}"
                )

        if not components:
            raise ValueError(
                "CSV file contains no component records."
            )

        return components
