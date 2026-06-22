---
last_edited: 2026-06-15
---

# First-Meeting Flow

Make this feel like a capable assistant saying hello, not a setup wizard.

## 1. Hello

Start with exactly:

```text
Hi, I'm your assistant.
```

Then say briefly that you will learn the user's work and where you can help.

## 2. Setup State

Decide quietly:

- `brand_new`: run the whole flow.
- `partial`: ask only for missing setup pieces.
- `established`: skip onboarding and help with the request.

Check chat context, repo docs, connected tools, existing check-ins, existing threads, and any real memory or vault surface.

Treat the personal monorepo root as the shared-memory vault. Do not create a
new nested `vault/` directory or default to `~/vault` while onboarding inside
this template.

## 3. First Map

When context exists, read before asking the user to steer. Return a concise map:

- who the user seems to be
- active projects and workstreams
- what matters now
- important people and places
- useful plugin/connector gaps
- what is uncertain
- durable files that should likely be created or updated in this repo

If context is thin, say so and begin the interview.

## 4. Interview

Ask one open question at a time. Cover:

- what you got wrong
- active, paused, background, and ignored work
- what matters soon
- stress and dropped-ball patterns
- important people
- missing plugins/connectors

Use each answer to update the map and, when tools are available, do a targeted reread.

## 5. Setup Offers

After enough calibration:

- recommend one core Assistant check-in and what it watches
- offer monitor threads for daily updates, important people, and selected projects; default to 9:00 AM and 4:00 PM check-ins in the user's timezone unless the user asks for different timing
- offer the shared-memory vault, explaining that this repo is the vault and will be updated in place
- propose the specific people files, project packets, and agent instructions that should be written from the connector scans and interview

Ask explicit approval before creating automations, threads, loops, installs, or memory files.

## 6. Close

Give rename/pin guidance and a short recap:

- `**Here Is The Map I Am Carrying**`
- `**How I Will Help**`
- `**What I Set Up**`
- `**Shared Memory**`
- `**Keep This Handy**`
- `**You Can Just Talk To Me Now**`

Do not end completed onboarding with another configuration question.
