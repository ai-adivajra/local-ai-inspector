from local_ai_inspector.collectors.cpu import CPUCollector


def test_cpu_collector_returns_observations():
    collector = CPUCollector()

    observations = collector.collect()

    assert len(observations) >= 4
