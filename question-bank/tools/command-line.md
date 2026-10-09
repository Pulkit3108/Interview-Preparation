# Command-Line Utilities

Small command-line tasks commonly used in operational interviews.

[Back to the question-bank index](../README.md)

## How can you retrieve a web page from the command line?

**Answer**

Use an HTTP client and enable failure reporting when appropriate:

```bash
curl --fail --show-error --location https://example.com/
wget --quiet --output-document=- https://example.com/
```

In PowerShell, use `Invoke-WebRequest -Uri https://example.com/`. For an API, `Invoke-RestMethod`
usually provides more convenient structured-data handling.

Avoid disabling TLS verification. Add authentication headers only through an appropriate secret
source, and do not place credentials directly in shell history or a committed script.

## Which Unix command displays the newest lines in a log file?

**Answer**

`tail` prints the end of a file:

```bash
tail -n 20 /path/to/application.log
```

Use `tail -f` to follow appended lines, or `tail -F` when the file may be rotated and recreated. For
systemd-managed services, `journalctl -u service-name -n 20` reads recent service entries from the
journal.

## What is a cron job?

**Answer**

Cron schedules commands on Unix-like systems from a crontab expression containing minute, hour, day
of month, month, and day of week. Jobs run in a minimal non-interactive environment, so use absolute
paths, set required environment explicitly, prevent unsafe overlap, capture output, and make the job
idempotent. Time zones, daylight-saving changes, missed runs, retries, and distributed singleton
execution require deliberate handling; a workflow scheduler may be more appropriate for critical
jobs.
