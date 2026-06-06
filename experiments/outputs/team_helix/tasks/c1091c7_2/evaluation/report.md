──────────────────────────────── Overall Stats ────────────────────────────────
Num Passed Tests : 2
Num Failed Tests : 2
Num Total  Tests : 4
─────────────────────────────────── Passes ────────────────────────────────────
>> Passed Requirement
assert model changes match phone.Alarm.
>> Passed Requirement
obtain updated, removed phone.Alarm records using models.changed_records,
and assert 0 alarms were added or removed.
──────────────────────────────────── Fails ────────────────────────────────────
>> Failed Requirement
assert answers match.
```python
with test(
    """
    assert answers match.
    """
):
    test.answer(predicted_answer, ground_truth_answer)
```
----------
AssertionError:
'no meeting cancellations found in emails, but all meeting alarms have been
disabled.'
==
'null'
>> Failed Requirement
assert set of updated alarm ids match exactly to
private_data.to_disable_alarm_ids (ignore order).
```python
with test(
    """
    assert set of updated alarm ids match exactly to
private_data.to_disable_alarm_ids (ignore order).
    """
):
```
----------
AssertionError:  {606} == {744, 745, 746, 743}

In left but not right:
[606]

In right but not left:
[744, 745, 746, 743]