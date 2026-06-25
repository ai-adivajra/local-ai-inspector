from local_ai_inspector.domain.inspection import Inspection


def test_new_inspection_is_empty():
    inspection = Inspection()

    assert inspection.observations == []
    assert inspection.findings == []
    assert inspection.recommendations == []
