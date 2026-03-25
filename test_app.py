from app import get_system_stats

def test_stats_keys():
    stats = get_system_stats()
    assert "cpu" in stats
    assert "memory" in stats

def test_stats_values():
    stats = get_system_stats()
    assert 0 <= stats["cpu"] <= 100
    assert 0 <= stats["memory"] <= 100
