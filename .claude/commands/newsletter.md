# /newsletter

Generate a TOAST@ branded HTML newsletter on the given topic, create a Gmail test draft, and wait for approval before sending to the full list.

**Usage:** `/newsletter <topic>`  
**Example:** `/newsletter sourdough fermentation science`

---

## Brand Colors (memorize these)
- Brown: `#B5732A` — headers, section titles, primary CTAs
- Amber: `#E8A33D` — accents, dark-bg section titles
- Cream: `#FAF6EE` — page background, light-bg text
- Sand: `#F0DCB4` — infographic background, secondary sections
- Charcoal: `#1F2230` — hero background, footer, dark-bg sections

## Brand Fonts
- Headers: `Georgia, serif`
- Body: `Arial, sans-serif`
- Accent/labels: `monospace`

---

## Steps

### 1. Research the Topic
Run 3–5 WebSearch queries:
1. Core explanation / what it is
2. Recent news or developments
3. One counterintuitive fact or surprising angle
4. One concrete number, stat, or real-world example

Synthesize into 3–5 key points. Do NOT dump raw results into the newsletter.

### 2. Plan Structure
Before writing HTML, decide:
- **Subject line**: `TOAST@ | [6–9 word hook]`
- **Preview text**: 85–100 chars that expand on the subject
- **Sections**: pick 2–3 content sections (explainer, key stat, timeline, counterintuitive angle, real-world example, what it means for you)
- **Infographic concept**: what 3 stats or data points will the CSS card row show?

### 3. Write the Newsletter HTML

Save to `.tmp/newsletter_draft.html`. Use this exact layout — do not deviate from the structure or brand colors:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TOAST@ | [Subject]</title>
</head>
<body style="margin:0; padding:0; background:#FAF6EE; font-family:Arial, sans-serif">

  <!-- PREVIEW TEXT -->
  <div style="display:none;max-height:0;overflow:hidden;font-size:1px;color:#FAF6EE;">
    [85-100 char preview text]͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏ ͏
  </div>

  <!-- OUTER WRAPPER -->
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>
      <td align="center" style="background:#FAF6EE;padding:24px 0;">

        <!-- NEWSLETTER CONTAINER -->
        <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;">

          <!-- HEADER -->
          <tr>
            <td style="background:#B5732A;padding:22px 32px;text-align:center;">
              <span style="font-family:Georgia,serif;font-size:26px;color:#FAF6EE;letter-spacing:3px;font-weight:bold;">TOAST@</span>
              <br>
              <span style="font-family:monospace;font-size:11px;color:#F0DCB4;letter-spacing:1px;">a daily byte of the internet</span>
            </td>
          </tr>

          <!-- HERO (dark bg) -->
          <tr>
            <td style="background:#1F2230;padding:44px 36px 40px;">
              <p style="font-family:monospace; font-size:11px; line-height:1.75; margin:0 0 14px; color:#E8A33D; letter-spacing:2px">ISSUE #[NNN] · [MONTH YEAR]</p>
              <h1 style="font-family:Georgia, serif; color:#FAF6EE; font-size:30px; margin:0 0 20px; line-height:1.25">[Headline]</h1>
              <p style="font-family:Arial, sans-serif; font-size:15px; line-height:1.75; margin:0; color:#F0DCB4">
                [2–3 sentence intro that sets up why this topic matters right now]
              </p>
            </td>
          </tr>

          <!-- SECTION 1 (light bg) -->
          <tr>
            <td style="background:#FAF6EE;padding:36px 36px 28px;">
              <h2 style="font-family:Georgia, serif; font-size:19px; margin:0 0 14px; color:#B5732A">[Section Title]</h2>
              <p style="font-family:Arial, sans-serif; font-size:15px; line-height:1.75; margin:0 0 14px; color:#1F2230">
                [Content paragraph]
              </p>
              <p style="font-family:Arial, sans-serif; font-size:15px; line-height:1.75; margin:0; color:#1F2230">
                [Content paragraph]
              </p>
            </td>
          </tr>

          <!-- SECTION 2 (dark bg) -->
          <tr>
            <td style="background:#1F2230;padding:36px;">
              <h2 style="font-family:Georgia, serif; font-size:19px; margin:0 0 14px; color:#E8A33D">[Section Title]</h2>
              <p style="font-family:Arial, sans-serif; font-size:15px; line-height:1.75; margin:0 0 14px; color:#F0DCB4">
                [Content paragraph]
              </p>
              <p style="font-family:Arial, sans-serif; font-size:15px; line-height:1.75; margin:0; color:#F0DCB4">
                [Content paragraph]
              </p>
            </td>
          </tr>

          <!-- INFOGRAPHIC: CSS STAT CARDS (3 columns) -->
          <!-- Always use this pattern — no image needed, pure CSS, email-safe -->
          <tr>
            <td style="background:#F0DCB4;padding:28px 36px;">
              <p style="font-family:Georgia, serif; font-size:13px; line-height:1.75; margin:0 0 16px; color:#1F2230; text-align:center; letter-spacing:2px; font-weight:bold">BY THE NUMBERS · [MONTH YEAR]</p>
              <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <!-- Card 1: Brown bg -->
                  <td width="33%" style="padding:0 6px 0 0;vertical-align:top;">
                    <div style="background:#B5732A;padding:20px 12px;text-align:center;border-radius:6px;">
                      <p style="font-family:Georgia, serif; font-size:28px; line-height:1.75; margin:0 0 6px; color:#FAF6EE; font-weight:bold">[BIG STAT]</p>
                      <div style="border-top:1px solid #E8A33D;margin:0 0 10px;"></div>
                      <p style="font-family:Arial, sans-serif; font-size:11px; line-height:1.5; margin:0 0 8px; color:#FAF6EE">[Stat label]</p>
                      <p style="font-family:Arial, sans-serif; font-size:10px; line-height:1.5; margin:0; color:#F0DCB4">[Supporting detail]</p>
                    </div>
                  </td>
                  <!-- Card 2: Charcoal bg -->
                  <td width="33%" style="padding:0 3px;vertical-align:top;">
                    <div style="background:#1F2230;padding:20px 12px;text-align:center;border-radius:6px;">
                      <p style="font-family:Georgia, serif; font-size:28px; line-height:1.75; margin:0 0 6px; color:#E8A33D; font-weight:bold">[BIG STAT]</p>
                      <div style="border-top:1px solid #B5732A;margin:0 0 10px;"></div>
                      <p style="font-family:Arial, sans-serif; font-size:11px; line-height:1.5; margin:0 0 8px; color:#FAF6EE">[Stat label]</p>
                      <p style="font-family:Arial, sans-serif; font-size:10px; line-height:1.5; margin:0; color:#F0DCB4">[Supporting detail]</p>
                    </div>
                  </td>
                  <!-- Card 3: Amber bg -->
                  <td width="33%" style="padding:0 0 0 6px;vertical-align:top;">
                    <div style="background:#E8A33D;padding:20px 12px;text-align:center;border-radius:6px;">
                      <p style="font-family:Georgia, serif; font-size:28px; line-height:1.75; margin:0 0 6px; color:#1F2230; font-weight:bold">[BIG STAT]</p>
                      <div style="border-top:1px solid #B5732A;margin:0 0 10px;"></div>
                      <p style="font-family:Arial, sans-serif; font-size:11px; line-height:1.5; margin:0 0 8px; color:#1F2230">[Stat label]</p>
                      <p style="font-family:Arial, sans-serif; font-size:10px; line-height:1.5; margin:0; color:#1F2230">[Supporting detail]</p>
                    </div>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- SECTION 3 (light bg) — optional, remove if content is short -->
          <tr>
            <td style="background:#FAF6EE;padding:36px 36px 28px;">
              <h2 style="font-family:Georgia, serif; font-size:19px; margin:0 0 14px; color:#B5732A">[Section Title]</h2>
              <p style="font-family:Arial, sans-serif; font-size:15px; line-height:1.75; margin:0; color:#1F2230">
                [Content]
              </p>
            </td>
          </tr>

          <!-- ONE MORE THING (sand bg, smaller — always last content section) -->
          <tr>
            <td style="background:#F0DCB4;padding:28px 36px;">
              <h2 style="font-family:Georgia, serif; font-size:17px; margin:0 0 12px; color:#1F2230">One More Thing</h2>
              <p style="font-family:Arial, sans-serif; font-size:14px; line-height:1.75; margin:0; color:#1F2230">
                [One surprising, counterintuitive, or delightful fact related to the topic. 2–3 sentences max.]
              </p>
            </td>
          </tr>

          <!-- DIVIDER -->
          <tr>
            <td style="background:#FAF6EE;padding:0 36px;">
              <div style="border-top:1px solid #F0DCB4;"></div>
            </td>
          </tr>

          <!-- FOOTER -->
          <tr>
            <td style="background:#1F2230;padding:28px 36px;text-align:center;">
              <p style="font-family:Georgia, serif; font-size:16px; line-height:1.75; margin:0 0 6px; color:#E8A33D; letter-spacing:2px">TOAST@</p>
              <p style="font-family:Arial, sans-serif; font-size:12px; line-height:1.7; margin:0; color:#F0DCB4">
                You're receiving this because you subscribed to TOAST@.<br>
                To unsubscribe, reply with "unsubscribe".
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>

</body>
</html>
```

### 4. Inline CSS and Validate
```
python tools/render_newsletter.py --input .tmp/newsletter_draft.html --output .tmp/newsletter_final.html
```
- If size > 102KB: remove one section, re-save draft, re-run
- If 90–102KB: note it but proceed

### 5. Create Test Draft in Gmail
- Read `.tmp/newsletter_final.html`
- Call `mcp__claude_ai_Gmail__create_draft`:
  - `to`: `tumbokon.aaronjulius@gmail.com`
  - `subject`: `[TEST] ` + subject line
  - `htmlBody`: full HTML from the file
- Tell user: "Test draft created. Subject: [subject]. Open Gmail, check how it looks, and confirm before I send to the full list."
- **Stop and wait for explicit confirmation.**

### 6. Create Final Draft (after approval)
```
python tools/manage_recipients.py --export
```
- If list is empty: stop and tell user to add recipients first
- Call `mcp__claude_ai_Gmail__create_draft`:
  - `to`: recipient list
  - `subject`: subject line (no [TEST] prefix)
  - `htmlBody`: full HTML
- Report: "Draft created. Subject: [subject]. Recipients: [count]. Open Gmail to send."

---

## Layout Rules (non-negotiable for email clients)
- Table-based layout only — no Grid, no Flexbox
- All CSS must be inline (render_newsletter.py handles this)
- No JavaScript, no `<link>` stylesheets, no external fonts
- All images need explicit `width` and `alt`
- Gmail clips at 102KB — render_newsletter.py enforces this

## Infographic Rule
Always use the pure-CSS 3-column stat card pattern above. No SVG, no external images needed. The CSS cards are email-safe and render identically across all clients.

## Section Alternation Pattern
- Hero: always dark (`#1F2230`)
- Alternate light (`#FAF6EE`) and dark (`#1F2230`) for content sections
- Infographic: always sand (`#F0DCB4`)
- "One More Thing": always sand (`#F0DCB4`)
- Footer: always dark (`#1F2230`)
