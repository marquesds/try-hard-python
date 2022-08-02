"""
Adapter:
    Allows objects with incompatible interfaces to collaborate.

See: https://refactoring.guru/design-patterns/adapter
"""
import csv
import json
from io import StringIO
from typing import Protocol


class Report(Protocol):
    def generate_report(self) -> str:
        ...


class AccountingReport:
    def generate_report(self) -> str:
        """
        Generates report in csv format
        """
        return "transaction_id,transaction_type,value\n" "1,CREDIT,1000\n" "2,DEBIT,800\n"


class JsonAdapter:
    def __init__(self, adaptee: Report):
        self.adaptee = adaptee

    def generate_report(self) -> str:
        csv_report = self.adaptee.generate_report()
        return self._convert_to_json(csv_report)

    def _convert_to_json(self, report: str) -> str:
        buffer = StringIO(report)
        reader = csv.DictReader(buffer, delimiter=",")
        results = []
        for row in reader:
            results.append(row)
        return json.dumps(results)
