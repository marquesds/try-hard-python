import json

from app.design_patterns.structural.adapter import AccountingReport, JsonAdapter


class TestAdapter:
    def test_should_convert_report_format_when_using_adapter(self):
        accounting_report = AccountingReport()
        json_report = JsonAdapter(accounting_report)

        expected_output = """
        [{"transaction_id": "1", "transaction_type": "CREDIT", "value": "1000"}, {"transaction_id": "2", "transaction_type": "DEBIT", "value": "800"}]
        """

        assert json.loads(expected_output) == json.loads(json_report.generate_report())
