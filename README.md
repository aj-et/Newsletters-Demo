# Toast@ Newsletter System

An AI-powered newsletter generator that researches topics, writes branded HTML emails, creates infographics, and delivers a Gmail draft — ready for you to send.

---

## What This Is

You give Claude a topic. It does the rest.

Behind the scenes, it searches the web for relevant information, writes a fully formatted HTML email in the Toast@ brand style, generates a custom infographic, and creates a Gmail draft addressed to your recipient list. You review it, then hit Send. No design work, no HTML wrangling, no copy-pasting from research tabs.

The system is built to be reliable. Each run follows the same documented process, uses the same tools, and produces consistent output — not because the AI is consistent, but because the deterministic parts (rendering HTML, converting images, managing recipients) are handled by Python scripts that behave the same way every time.

---

## How It Works — The WAT Framework

This project is organized around three layers: **Workflows**, **Agents**, and **Tools**.

**Workflows** live in the `workflows/` folder as plain Markdown files. They're step-by-step instructions — like an SOP you'd give a new team member — that define what to do, which tools to use, what the output should look like, and how to handle things that go wrong. The `send_newsletter.md` workflow is the main one you'll use.

**Agents** are Claude Code itself. When you ask it to send a newsletter, it reads the relevant workflow, decides what to do at each step, and calls the right tools. The agent handles all the reasoning: interpreting the brief, structuring the content, deciding what the infographic should show, recovering from errors.

**Tools** live in the `tools/` folder as Python scripts. They do the deterministic work: inlining CSS so Gmail renders the email correctly, converting SVG infographics to PNG, adding or removing people from the recipient list. These scripts are called by the agent but can also be run directly from the terminal.

The reason for this split is reliability. If the AI tried to handle every step itself — including things like HTML rendering and image conversion — small errors would compound. By handing execution off to scripts that always behave the same way, the agent stays focused on what it's actually good at: reading, writing, and making decisions.

---

## Project Structure

```
Newsletters Demo/
├── workflows/               # Step-by-step instructions for the agent
│   └── send_newsletter.md   # The main newsletter workflow
├── tools/                   # Python scripts for execution
│   ├── manage_recipients.py # Add/remove/list newsletter recipients
│   ├── render_newsletter.py # Inline CSS and validate HTML for email
│   └── svg_to_png.py        # Convert SVG infographics to PNG
├── brand_assets/            # Toast@ brand images (logo, guidelines)
├── .tmp/                    # Temporary files generated during a run (gitignored)
├── recipients.json          # Your current recipient list
├── .env                     # API keys — never commit this
├── CLAUDE.md                # Agent instructions (how the agent should behave)
└── README.md                # This file
```

---

## Prerequisites

Before you can run the system, you need a few things set up.

**Python packages** — Install these once:

```bash
pip install premailer
pip install cairosvg
```

If `cairosvg` doesn't work on your machine, Playwright is the fallback:

```bash
pip install playwright
python -m playwright install chromium
```

**Claude Code** — You need the Claude Code CLI installed and connected to your Google account. The system uses two Google integrations:
- **Gmail MCP** — to create draft emails
- **Google Drive MCP** — to host infographic images

If these aren't connected yet, set them up through the Claude Code settings before running your first newsletter.

**Environment variables** — Create a `.env` file in the project root with the following:

```
ANTHROPIC_API_KEY=your_key_here
IMGBB_API_KEY=your_key_here   # Optional — only needed if Google Drive upload fails
```

**Google OAuth** — When you first use the Gmail or Drive integrations, you'll be prompted to authorize access. This creates `credentials.json` and `token.json` in the project root. Both are gitignored — don't move or delete them.

---

## Getting Started

1. Clone or download this repository and open the folder in Claude Code.

2. Create your `.env` file with your `ANTHROPIC_API_KEY` (see above).

3. Install the Python dependencies listed in the Prerequisites section.

4. Add yourself as a recipient so you receive test drafts:

   ```bash
   python tools/manage_recipients.py --add you@example.com
   ```

5. Open Claude Code in this folder and say:

   > "Send a newsletter about [your topic]"

   Claude will take it from there.

---

## Sending a Newsletter

Here's what happens when you kick off a newsletter run:

1. **Brand check** — The agent reads the brand guidelines from `brand_assets/` to extract the correct colors, tone, and visual style for Toast@.

2. **Research** — It runs several web searches to gather information on your topic: core explanations, recent developments, interesting angles, and data points worth highlighting.

3. **Planning** — It decides on a subject line, preview text, the two or three content sections, and what the infographic should show.

4. **Infographic** — It generates an SVG graphic (a comparison table, stat card, or bar chart) using only Toast@ brand colors, then converts it to PNG using `tools/svg_to_png.py` and uploads it to Google Drive for hosting.

5. **Writing the email** — It writes a table-based HTML email (required for email client compatibility), with inline CSS, a header, content sections, the infographic, and a footer.

6. **Rendering** — It runs the HTML through `tools/render_newsletter.py`, which inlines any remaining CSS and checks that the file is under Gmail's 102KB size limit.

7. **Test draft** — It creates a Gmail draft addressed to you with a `[TEST]` prefix in the subject line. You review it. If something looks off, tell Claude what to fix.

8. **Final draft** — Once you confirm the test looks good, it creates the final draft addressed to all recipients in `recipients.json`. You hit Send.

The final HTML is also saved to `.tmp/newsletter_final.html` as an archive.

---

## Managing Recipients

Use `manage_recipients.py` directly from the terminal to maintain your list:

```bash
# See who's on the list
python tools/manage_recipients.py --list

# Add someone
python tools/manage_recipients.py --add name@example.com

# Remove someone
python tools/manage_recipients.py --remove name@example.com
```

The list is stored in `recipients.json`. The agent reads this file automatically when creating the final draft.

---

## Customizing and Extending

**Change the newsletter format or tone** — Edit `workflows/send_newsletter.md`. This file controls everything about how newsletters are produced: the structure, the writing style, the infographic rules, the HTML template. It's written in plain language and is meant to be edited.

**Add a new capability** — Create a Python script in `tools/` and a new workflow in `workflows/` that tells the agent when and how to use it. Follow the same pattern as the existing tools: accept arguments from the command line, print results to stdout, exit with a non-zero code on failure.

**Add a new workflow** — Create a new `.md` file in `workflows/` following the same structure as `send_newsletter.md` (Objective, Inputs, Steps, Outputs, Edge Cases). Then tell the agent about it in conversation.

---

## Credentials and Security

The following files are gitignored and should never be committed:

- `.env` — contains your API keys
- `credentials.json` — Google OAuth client credentials
- `token.json` — your Google OAuth access token
- `.tmp/` — temporary output files

If you're sharing this repo, make sure none of these files are present before pushing. The `.gitignore` is already configured to exclude them, but it's worth double-checking.
