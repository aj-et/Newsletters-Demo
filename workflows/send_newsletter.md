# Workflow: Send Newsletter

## Objective
Research a topic, produce a branded Toast@ HTML newsletter with one SVG infographic, and create a Gmail draft for review and sending.

## Inputs
| Input | Required | Notes |
|---|---|---|
| Topic | Yes | Plain language — "AI in restaurants", "the history of sourdough", anything |
| Tone override | No | Default: warm, minimal, retro-techy (per Toast brand) |
| Recipient override | No | Send to specific email instead of full list |

---

## Steps

### 1. Read Brand Guidelines
- Load `brand_assets/toast-brand-guidelines.jpg` and `brand_assets/Hashbrown.jpg` using vision
- Extract and hold in context:
  - **Colors**: Brown `#B5732A`, Amber `#E8A33D`, Cream `#FAF6EE`, Sand `#F0DCB4`, Charcoal `#1F2230`
  - **Fonts**: Headers: General Sans / Satoshi (fallback: Georgia, serif). Body: Inter (fallback: Arial, sans-serif). Accent: JetBrains Mono (fallback: monospace)
  - **Tone**: Warm, curious, minimal, nostalgic, retro-techy. Like a smart friend who reads a lot.
  - **Logo**: "TOAST@" as plain text in the header — the @ is part of the wordmark

### 2. Research the Topic
- Run 3–5 WebSearch queries covering:
  1. Core explanation / definition
  2. Recent developments or news
  3. One interesting angle, counterintuitive fact, or surprising stat
  4. One concrete number, data point, or real-world example
- Synthesize findings into 3–5 key points. Do NOT dump raw search results into the newsletter.

### 3. Plan the Newsletter Structure
Before writing HTML, decide:
- **Subject line**: 6–9 words, curiosity-driven. Format: `TOAST@ | [hook]`. Optional: one emoji at the start.
- **Preview text**: 85–100 characters that expand on the subject without repeating it
- **Sections** (pick 2–3 from: explainer, key stat, timeline, counterintuitive angle, real-world example, what it means for you)
- **Infographic concept**: What will the graphic visualize? (comparison table, stat callout, simple bar chart, timeline, process diagram)

### 4. Generate Infographic SVG
Write a self-contained SVG file saved to `.tmp/infographic.svg`:
- Use only Toast brand colors (`#B5732A`, `#E8A33D`, `#FAF6EE`, `#F0DCB4`, `#1F2230`, white)
- No external font URLs — use `font-family: Georgia, serif` or `font-family: Arial, sans-serif`
- Dimensions: `width="560" height="280"` (2:1 ratio fits email width)
- Keep it simple: a 2–3 column comparison, a large typographic stat card, or a horizontal bar chart
- Every text element needs `font-family` set explicitly (SVG does not inherit CSS fonts)

### 5. Convert SVG to PNG
```
python tools/svg_to_png.py --input .tmp/infographic.svg --output .tmp/infographic.png --width 560
```
- Confirm exit code 0 and reported output path
- If it fails, fall back: replace the infographic with a pure-CSS styled table in the HTML (no image needed)

### 6. Upload PNG to Google Drive
- Use `mcp__claude_ai_Google_Drive__authenticate` if not already authenticated
- Upload `.tmp/infographic.png` via Google Drive MCP
- Set sharing to "anyone with link can view"
- **Critical**: Construct the direct image URL as: `https://drive.google.com/uc?export=view&id=FILE_ID`
  - Do NOT use the default share link (`drive.google.com/file/d/FILE_ID/view`) — it does not work as `<img src>`
  - Extract FILE_ID from the uploaded file's metadata

### 7. Write the HTML Newsletter
Produce a complete HTML email saved to `.tmp/newsletter_draft.html`. Requirements:

**Layout rules (email clients are not browsers):**
- Table-based layout only — no CSS Grid, no Flexbox
- Max width: 600px, centered with `margin: 0 auto`
- All CSS must be inline (the next step will handle this, but avoid complex selectors)
- No JavaScript, no `<link>` stylesheets, no external fonts
- All images need explicit `width` and `alt` attributes

**Structure:**
```
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Subject Line]</title>
  <style>
    /* Write CSS here — render_newsletter.py will inline it */
    body { margin: 0; padding: 0; background: #FAF6EE; font-family: Arial, sans-serif; }
    /* etc. */
  </style>
</head>
<body>

  <!-- PREVIEW TEXT: Controls inbox preview snippet. Must be immediately after <body>. -->
  <div style="display:none;max-height:0;overflow:hidden;font-size:1px;color:#FAF6EE;">
    [Preview text here — 85-100 chars]&#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847;
  </div>

  <!-- WRAPPER -->
  <table width="100%" cellpadding="0" cellspacing="0">
    <tr><td align="center" style="background:#FAF6EE;padding:20px 0;">

      <!-- NEWSLETTER CONTAINER -->
      <table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;">

        <!-- HEADER -->
        <tr><td style="background:#B5732A;padding:24px 32px;text-align:center;">
          <span style="font-family:Georgia,serif;font-size:28px;color:#FAF6EE;letter-spacing:2px;">TOAST@</span>
        </td></tr>

        <!-- HERO -->
        <tr><td style="background:#1F2230;padding:40px 32px;">
          <h1 style="font-family:Georgia,serif;color:#FAF6EE;font-size:32px;margin:0 0 16px;">
            [Headline]
          </h1>
          <p style="font-family:Arial,sans-serif;color:#F0DCB4;font-size:16px;line-height:1.6;margin:0;">
            [2–3 sentence intro]
          </p>
        </td></tr>

        <!-- CONTENT SECTIONS (repeat as needed) -->
        <tr><td style="background:#FAF6EE;padding:32px;">
          <h2 style="font-family:Georgia,serif;color:#B5732A;font-size:20px;margin:0 0 12px;">
            [Section Title]
          </h2>
          <p style="font-family:Arial,sans-serif;color:#1F2230;font-size:15px;line-height:1.7;margin:0;">
            [Content]
          </p>
        </td></tr>

        <!-- INFOGRAPHIC -->
        <tr><td style="background:#F0DCB4;padding:24px 32px;text-align:center;">
          <img src="[DRIVE_URL]" width="536" alt="[Infographic description]"
               style="display:block;margin:0 auto;border:0;">
        </td></tr>

        <!-- FOOTER -->
        <tr><td style="background:#1F2230;padding:24px 32px;text-align:center;">
          <p style="font-family:Arial,sans-serif;color:#F0DCB4;font-size:12px;line-height:1.6;margin:0;">
            You're receiving this because you subscribed to TOAST@.<br>
            To unsubscribe, reply with "unsubscribe".
          </p>
        </td></tr>

      </table>
    </td></tr>
  </table>

</body>
</html>
```

### 8. Inline CSS and Validate
```
python tools/render_newsletter.py --input .tmp/newsletter_draft.html --output .tmp/newsletter_final.html
```
- If size > 102KB: remove one content section, save the draft again, re-run
- If size warning (90–102KB): note it but proceed
- Read `.tmp/newsletter_final.html` to confirm it looks correct

### 9. Test Send (Always Do This First)
- Get the final HTML from `.tmp/newsletter_final.html`
- Call `mcp__claude_ai_Gmail__create_draft` with:
  - `to`: `tumbokon.aaronjulius@gmail.com` (test address only)
  - `subject`: `[TEST] ` + the subject line
  - `htmlBody`: full HTML content
- Tell the user: "Test draft created in Gmail. Subject: [subject]. Please open Gmail, check how it looks, and confirm before I create the full draft."
- **Wait for explicit confirmation before proceeding.**

### 10. Create Final Draft
After test confirmation:
- Run `python tools/manage_recipients.py --export` to get the recipient list
- If recipient override was specified, use that address instead
- If list is empty: stop and ask user to add recipients first
- Call `mcp__claude_ai_Gmail__create_draft` with:
  - `to`: recipient list
  - `subject`: subject line (no [TEST] prefix)
  - `htmlBody`: full HTML content
- Report: "Draft created. Subject: [subject]. Recipients: [count]. Open Gmail to review and send."

---

## Outputs
| Output | Location | Notes |
|---|---|---|
| Gmail draft | Gmail inbox (Drafts) | User opens Gmail and sends manually |
| Newsletter HTML | `.tmp/newsletter_final.html` | Keep as archive |
| Infographic PNG | `.tmp/infographic.png` | Keep for reference |

---

## Edge Cases

| Situation | Resolution |
|---|---|
| SVG conversion fails | Replace infographic with a pure-CSS styled `<table>` using brand colors. No image needed. |
| Google Drive upload fails | Try ImgBB API as fallback (add `IMGBB_API_KEY` to `.env`, POST to `https://api.imgbb.com/1/upload`) |
| Newsletter > 102KB after inlining | Remove one content section. Re-save draft. Re-run render_newsletter.py. |
| Recipient list empty | Stop. Tell user: `python tools/manage_recipients.py --add email@example.com` |
| Drive image doesn't display in email | Verify URL uses `uc?export=view&id=FILE_ID` format, not the default share link |
| User wants to edit before sending | Tell them the draft is in Gmail — they can edit there and send manually. Or describe the change and Claude regenerates that section. |

---

## Notes & Gotchas

- **Gmail clips at 102KB** — silently. The email shows a "View entire message" link. `render_newsletter.py` prevents this.
- **Gmail strips `<style>` tags** — CSS must be inline. `render_newsletter.py` handles this via premailer.
- **SVG is stripped by Gmail and Outlook** — always convert to PNG first.
- **Google Drive share URL ≠ image URL** — must construct `uc?export=view&id=FILE_ID` manually.
- **Preview text** — the `&#847;` characters after the preview text are zero-width non-breaking spaces. They pad the hidden div so Gmail doesn't pull body text into the preview.
- **No send tool in Gmail MCP** — the workflow creates a draft. User must send from Gmail. This is intentional — it's the human review step.
