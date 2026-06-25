from local_ai_inspector.collectors.memory import MemoryCollector


def test_memory_collector():

    collector = MemoryCollector()

    observations = collector.collect()

    keys = {o.key for o in observations}

    assert "installed" in keys
    assert "available" in keys
