import argparse
import os
import sys


def convert_cairosvg(svg_path, png_path, width=None):
    try:
        import cairosvg
    except (ImportError, OSError):
        return False, "cairosvg not available (Cairo native library missing)"

    try:
        kwargs = {"write_to": png_path}
        if width:
            kwargs["output_width"] = width
        cairosvg.svg2png(url=svg_path, **kwargs)
        return True, None
    except Exception as e:
        return False, str(e)


def convert_playwright(svg_path, png_path, width=None):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False, "playwright not installed"

    try:
        abs_svg = os.path.abspath(svg_path).replace("\\", "/")

        # Wrap SVG in a minimal HTML page so we can control viewport precisely
        with open(svg_path, "r", encoding="utf-8") as f:
            svg_content = f.read()

        html = f"""<!DOCTYPE html>
<html><head><style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: transparent; }}
  svg {{ display: block; }}
</style></head><body>{svg_content}</body></html>"""

        html_path = abs_svg.replace(".svg", "_tmp_render.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            w = width or 560
            page.set_viewport_size({"width": w, "height": w})
            page.goto(f"file:///{html_path}")
            svg_el = page.query_selector("svg")
            if svg_el:
                svg_el.screenshot(path=png_path)
            else:
                page.screenshot(path=png_path, full_page=True)
            browser.close()

        os.remove(html_path)
        return True, None
    except Exception as e:
        return False, str(e)


def main():
    parser = argparse.ArgumentParser(description="Convert SVG to PNG for email embedding")
    parser.add_argument("--input", required=True, help="Path to input SVG file")
    parser.add_argument("--output", required=True, help="Path to output PNG file")
    parser.add_argument("--width", type=int, default=560, help="Output width in pixels (default: 560)")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"ERROR: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)

    ok, err = convert_cairosvg(args.input, args.output, args.width)
    if not ok:
        print(f"cairosvg failed ({err}), trying playwright...", file=sys.stderr)
        ok, err = convert_playwright(args.input, args.output, args.width)

    if not ok:
        print(f"ERROR: Both converters failed. Last error: {err}", file=sys.stderr)
        print("Install cairosvg: pip install cairosvg", file=sys.stderr)
        print("Or install playwright: pip install playwright && playwright install chromium", file=sys.stderr)
        sys.exit(1)

    size_kb = os.path.getsize(args.output) / 1024
    print(f"Output: {args.output}")
    print(f"Size:   {size_kb:.1f} KB")


if __name__ == "__main__":
    main()
