import argparse
import os
import re
import sys

try:
    import premailer
except ImportError:
    print("ERROR: premailer not installed. Run: pip install premailer", file=sys.stderr)
    sys.exit(1)

WARN_BYTES = 90_000
MAX_BYTES = 102_000


def strip_forbidden_tags(html):
    html = re.sub(r"<script\b[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<link\b[^>]*rel=["\']stylesheet["\'][^>]*/?\s*>', "", html, flags=re.IGNORECASE)
    return html


def main():
    parser = argparse.ArgumentParser(description="Inline CSS and validate newsletter HTML for email")
    parser.add_argument("--input", required=True, help="Path to raw HTML file")
    parser.add_argument("--output", required=True, help="Path to save email-ready HTML")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"ERROR: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    with open(args.input, "r", encoding="utf-8") as f:
        raw_html = f.read()

    cleaned = strip_forbidden_tags(raw_html)

    try:
        inlined = premailer.transform(
            cleaned,
            remove_classes=False,
            strip_important=False,
        )
    except Exception as e:
        print(f"ERROR: CSS inlining failed: {e}", file=sys.stderr)
        sys.exit(1)

    size_bytes = len(inlined.encode("utf-8"))
    size_kb = size_bytes / 1024

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(inlined)

    print(f"Output: {args.output}")
    print(f"Size:   {size_kb:.1f} KB ({size_bytes:,} bytes)")

    if size_bytes > MAX_BYTES:
        print(f"ERROR: Exceeds Gmail 102KB limit ({size_kb:.1f} KB). Trim content and re-run.", file=sys.stderr)
        sys.exit(1)
    elif size_bytes > WARN_BYTES:
        print(f"WARNING: Approaching Gmail 102KB limit ({size_kb:.1f} KB). Consider trimming.")
    else:
        print("OK: Within Gmail size limits.")


if __name__ == "__main__":
    main()
