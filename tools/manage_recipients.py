import argparse
import json
import os
import sys

RECIPIENTS_FILE = os.path.join(os.path.dirname(__file__), "..", "recipients.json")


def load():
    if not os.path.exists(RECIPIENTS_FILE):
        return []
    with open(RECIPIENTS_FILE, "r") as f:
        return json.load(f)


def save(recipients):
    with open(RECIPIENTS_FILE, "w") as f:
        json.dump(recipients, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Manage newsletter recipients")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", action="store_true", help="List all recipients")
    group.add_argument("--add", metavar="EMAIL", help="Add a recipient")
    group.add_argument("--remove", metavar="EMAIL", help="Remove a recipient")
    group.add_argument("--export", action="store_true", help="Print comma-separated recipient list")
    args = parser.parse_args()

    recipients = load()

    if args.list:
        if not recipients:
            print("No recipients.")
        else:
            for r in recipients:
                print(r)

    elif args.add:
        email = args.add.strip().lower()
        if email in recipients:
            print(f"Already in list: {email}")
        else:
            recipients.append(email)
            save(recipients)
            print(f"Added: {email} ({len(recipients)} total)")

    elif args.remove:
        email = args.remove.strip().lower()
        if email not in recipients:
            print(f"Not found: {email}", file=sys.stderr)
            sys.exit(1)
        recipients.remove(email)
        save(recipients)
        print(f"Removed: {email} ({len(recipients)} remaining)")

    elif args.export:
        if not recipients:
            print("ERROR: Recipient list is empty. Add recipients first.", file=sys.stderr)
            sys.exit(1)
        print(",".join(recipients))


if __name__ == "__main__":
    main()
