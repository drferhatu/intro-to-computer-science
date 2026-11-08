"""Part C"""
import re
from conftest import run, ROOT


def stats(out):
    return {k: int(v) for k, v in re.findall(r"WORDS (MISSPELLED|IN DICTIONARY|IN TEXT):\s+(\d+)", out)}


def test_speller_small_dictionary():
    """speller.py + dictionary.py on dictionaries/small: 30 words loaded, 23 words in cat.txt, 1 misspelling (purrs)"""
    out, code = run("speller.py", "", ("dictionaries/small", "texts/cat.txt"))
    assert code == 0, f"speller exited with {code}: {out[:300]!r}"
    s = stats(out)
    assert s.get("IN DICTIONARY") == 30, f"size() should be 30, got {s}"
    assert s.get("IN TEXT") == 23 and s.get("MISSPELLED") == 1 and "purrs" in out, f"got {s}; misspelled list:\n{out[:300]}"


def test_speller_case_insensitive_and_typos():
    """check() ignores case: 'Caterpillar' is correct; typos.txt has exactly the 6 typos"""
    out, _ = run("speller.py", "", ("dictionaries/small", "texts/typos.txt"))
    miss = [l for l in out.split("MISSPELLED WORDS")[1].split("WORDS MISSPELLED")[0].split("\n") if l.strip()]
    assert "Caterpillar" not in miss and "Cat" not in miss, f"case-insensitive check failed: {miss}"
    assert {"quikc", "jumpd", "teh", "Helo", "computre", "sceince"} <= set(miss), f"missing typos: {miss}"
    assert set(miss) <= {"quikc", "brown", "fox", "jumpd", "over", "teh", "lazy", "Helo", "computre", "sceince", "fun"}, f"unexpected: {miss}"


def test_speller_large_dictionary():
    """load/check/size work on the large dictionary within 60 seconds, and load() returns False for a missing file"""
    n = sum(1 for _ in open(ROOT / "dictionaries" / "large", encoding="utf-8", errors="ignore"))
    out, code = run("speller.py", "", ("dictionaries/large", "texts/lecture.txt"), timeout=60)
    s = stats(out)
    assert code == 0 and s.get("IN DICTIONARY") == n, f"size() should be {n}, got {s}"
    assert s.get("MISSPELLED") == 0, f"every word of lecture.txt is in the dictionary; got {s}"
    out, code = run("speller.py", "", ("dictionaries/nothing", "texts/cat.txt"))
    assert code == 1 and "Could not load" in out, f"load() of a missing file should return False; got {code}, {out[:100]!r}"
