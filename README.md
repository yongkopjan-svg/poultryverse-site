# Poultryverse — Farm Console

A local dashboard + daily logbook for a layer farm, built from the phone app's
backup export (`poultryverse_backup_YYYY-MM-DD.json`). Everything runs on this
machine — no internet needed at any point.

## Start it (every time you want to record)

```
cd poultryverse-site
python server.py
```

Then open **http://localhost:8621** in the browser (Chrome recommended).

You can also double-click `index.html` without the server — you'll see the
data read-only.

## Where the records live

| File | Role |
|------|------|
| `data.json` | the original phone backup — **never modified, byte-for-byte** |
| `data.js`   | the same backup wrapped as `window.__DATA__` (lets the site run without a server) |
| `farm-live.json` | your real, ever-changing records — written on every save |

Daily loop (20 seconds): open the console → **☀ Morning round** → eggs collected,
broken, deaths, feed used → Save. Everything else updates itself.

## What's inside the console (v1.4 — 10 tabs)

- **Today** — feed countdown, loan due dates, lay status, backup-stale alert,
  "nothing logged yet" nudge, data-checks card (duplicate sweep + silent days)
- **Grow** — lay curve vs ISA Brown reference, break-even runway, profit ladder,
  flock vitality, restock rhythm + feed price trend, batch-3 planning
- **Money** — cash-flow calendar, where money went, money-flow drum, payback bar,
  loan cards; deep explanations live on Notes as tiles + links
- **Birds & health** — bird count walks itself with every mortality entry,
  health tape timeline
- **Eggs** — lay % (7-day vs breed reference), eggs/day, broken share,
  crates/month projection, production-percent chart, week-by-week table,
  where-every-egg-went, egg log, buyer book
- **Feed** — store level, days of cover at the ISA guide's weekly burn rate,
  restock history, price trend, feed-audit vs the official guide
- **Vaccine log** — schedule vs reality, lateness chips, "log its bill" on done
  vaccines
- **Alerts** — app alert history
- **Full ledger** — loans with repaid-so-far, reminders, phone-backup import,
  print report, download/reset
- **Notes** — the deep write-ups: plain-words glossary, payback math, feed era
  story, week-by-week guide, bird losses, buyer plan, loan rules, counting rules
- Full **dark mode** (🌙 toggle, remembered on this machine)

## House rules

- Editing egg records keeps the money log in step (one income row per egg sale).
- Deleting an egg record deletes its linked money row.
- `resetAll` (Full ledger) restores everything from the untouched seed backup.
- Download `farm-live.json` regularly — it is also your phone-import copy.

Now doesn't break. Type carefully, count the birds every day.
