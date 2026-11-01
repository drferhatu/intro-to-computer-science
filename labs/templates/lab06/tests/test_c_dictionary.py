"""Part C"""
import re
from conftest import run, need_valgrind, ROOT


def stats(out):
    return {k: int(v) for k, v in re.findall(r"WORDS (MISSPELLED|IN DICTIONARY|IN TEXT):\s+(\d+)", out)}


def test_speller_small_dictionary(speller):
    """speller + dictionary.c on dictionaries/small: 30 words loaded, 23 words in cat.txt, 1 misspelling (purrs)"""
    out, code, _ = run(speller, "", ("dictionaries/small", "texts/cat.txt"))
    assert code == 0, f"speller exited with {code}: {out[:300]!r}"
    s = stats(out)
    assert s.get("IN DICTIONARY") == 30, f"size() should be 30, got {s}"
    assert s.get("IN TEXT") == 23 and s.get("MISSPELLED") == 1 and "purrs" in out, f"got {s}; misspelled list:\n{out[:300]}"


def test_speller_case_insensitive_and_typos(speller):
    """check() ignores case: 'Caterpillar' is correct; typos.txt has exactly the 6 typos"""
    out, _, _ = run(speller, "", ("dictionaries/small", "texts/typos.txt"))
    miss = [l for l in out.split("MISSPELLED WORDS")[1].split("WORDS MISSPELLED")[0].split("\n") if l.strip()]
    assert "Caterpillar" not in miss and "Cat" not in miss, f"case-insensitive check failed: {miss}"
    assert {"quikc", "jumpd", "teh", "Helo", "computre", "sceince"} <= set(miss), f"missing typos: {miss}"
    # words that are simply not in the small dictionary also count as misspelled; nothing else should
    assert set(miss) <= {"quikc", "brown", "fox", "jumpd", "over", "teh", "lazy", "Helo", "computre", "sceince", "fun"}, f"unexpected: {miss}"


def test_speller_large_dictionary(speller):
    """load/check/size work on the large dictionary within 60 seconds"""
    n = sum(1 for _ in open(ROOT / "dictionaries" / "large", encoding="utf-8", errors="ignore"))
    out, code, _ = run(speller, "", ("dictionaries/large", "texts/lecture.txt"), timeout=60)
    s = stats(out)
    assert code == 0 and s.get("IN DICTIONARY") == n, f"size() should be {n}, got {s}"
    assert s.get("MISSPELLED") == 0, f"every word of lecture.txt is in the dictionary; got {s}"


def test_speller_valgrind_clean(speller):
    """unload() frees everything: valgrind reports no leaks and no invalid accesses (small dictionary)"""
    need_valgrind()
    out, code, rep = run(speller, "", ("dictionaries/small", "texts/cat.txt"), valgrind=True, timeout=120)
    assert code != 99 and "Invalid" not in rep, f"memory errors:\n{rep[:600]}"
    assert "definitely lost" not in rep, f"leak (unload incomplete?):\n{rep[:600]}"
