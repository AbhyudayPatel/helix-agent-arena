──────────────────────────────── Overall Stats ────────────────────────────────
Num Passed Tests : 1
Num Failed Tests : 1
Num Total  Tests : 2
─────────────────────────────────── Passes ────────────────────────────────────
>> Passed Requirement
Assert no model changes
──────────────────────────────────── Fails ────────────────────────────────────
>> Failed Requirement
assert answers match.
```python
with test(
    """
    assert answers match.
    """
):
    ground_truth_song_titles = ground_truth_answer.split(",")
    predicted_song_titles = predicted_answer.split(",")
    test.case(
```
----------
AssertionError:
['crimson veil', 'fire and ice', 'haunted memories', 'mysteries of the silent
sea']
==
['fire and ice', 'haunted memories', 'mysteries of the silent sea', 'shadows of
the past']

In left but not right:
['crimson veil']

In right but not left:
['shadows of the past']

Original values:
['Mysteries of the Silent Sea', 'Crimson Veil', 'Haunted Memories', 'Fire and
Ice']
==
['Mysteries of the Silent Sea', ' Haunted Memories', ' Fire and Ice', ' Shadows
of the Past']