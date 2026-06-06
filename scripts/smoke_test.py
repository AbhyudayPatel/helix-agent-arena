"""Smoke test: prove the AppWorld stack runs end-to-end on this machine.

Run: .venv\\Scripts\\python.exe scripts\\smoke_test.py
"""
import sys

from appworld import AppWorld, load_task_ids


def main() -> int:
    for split in ("train", "dev", "test_normal", "test_challenge"):
        try:
            ids = load_task_ids(split)
            print(f"[split] {split:15s} -> {len(ids)} tasks")
        except Exception as e:  # noqa: BLE001
            print(f"[split] {split:15s} -> ERROR {e}")

    ids = load_task_ids("train")
    tid = ids[0]
    print(f"\n[task] using train[0] = {tid}")

    with AppWorld(task_id=tid, experiment_name="helix_smoke", timeout_seconds=None) as world:
        print("[instruction]", world.task.instruction)
        sup = world.task.supervisor
        print("[supervisor]", sup.first_name, sup.last_name, "|", sup.email, "|", sup.phone_number)
        print("[allowed_apps]", world.task.allowed_apps)

        out = world.execute("print(apis.api_docs.show_app_descriptions())")
        print("\n[execute show_app_descriptions] ->\n", out[:600])

        out = world.execute("print(apis.supervisor.show_account_passwords())")
        print("\n[execute show_account_passwords] ->\n", out[:400])

        out = world.execute(
            "print(apis.api_docs.show_api_descriptions(app_name='supervisor'))"
        )
        print("\n[execute show_api_descriptions(supervisor)] ->\n", out[:600])

        tracker = world.evaluate()
        print("\n[evaluate.to_dict()] ->", tracker.to_dict(stats_only=True))
        print("[evaluate.success] ->", tracker.success)

    print("\nSMOKE TEST OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
