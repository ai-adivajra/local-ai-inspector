from local_ai_inspector.collectors.system import SystemCollector


def test_system_collector():

    collector = SystemCollector()

    observations = collector.collect()

    keys = {o.key for o in observations}

    assert "hostname" in keys
    assert "kernel" in keys
