from attendance import group_name, limit, status, failed_terms
 
 
def test_names():
    assert group_name(3, "Fall") == "DBE301"
    assert group_name(5, "Spring") == "DBE502"
 
 
def test_limits_match_regulation():
    assert [limit(l, "Fall") for l in (5, 4, 3, 2, 1)] == [30, 40, 40, 40, 50]
    assert [limit(l, "Spring") for l in (5, 4, 3, 2, 1)] == [20, 40, 40, 50, 60]
 
 
def test_exact_limit_is_not_exceeded():
    assert not status(3, "Fall", 40).exceeded
    assert status(3, "Fall", 41).exceeded
 
 
def test_percent_like_mockup():
    s = status(1, "Fall", 12)
    assert (s.remaining, s.remaining_percent) == (38, 76)
 
 
def test_failing_either_term_fails():
    assert failed_terms({"Fall": (3, 10), "Spring": (3, 10)}) == []
    assert failed_terms({"Fall": (5, 31), "Spring": (5, 0)}) == ["Fall"]
    assert failed_terms({"Fall": (1, 0), "Spring": (5, 21)}) == ["Spring"]
