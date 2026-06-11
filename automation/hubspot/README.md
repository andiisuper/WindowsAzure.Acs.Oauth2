# HubSpot daily send automation (Windows + Python Playwright)

This folder contains a starter script to send a HubSpot marketing email to a target contact list.

## What this solves

- Uses **Python + Playwright** instead of pixel-based mouse clicking.
- Supports a **persistent browser profile** so HubSpot login can be reused.
- Can be scheduled with **Windows Task Scheduler** at 8:00 AM every day.

## 1) Install

```powershell
cd automation/hubspot
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m playwright install chromium
```

## 2) Configure

```powershell
copy config.example.json config.json
```

Edit `config.json`:
- `email_url`: full URL to your HubSpot email edit/send page.
- `target_list_name`: list label to check (example: `New Prospect`).
- `user_data_dir`: folder for persistent browser profile.

## 3) First-time login warm-up

Run once manually so HubSpot auth/session cookies are saved:

```powershell
python send_prospects.py --config config.json
```

If asked, log into HubSpot in the opened Chromium window.

## 4) Schedule 8:00 AM daily

Create a file `run_hubspot_send.ps1`:

```powershell
Set-Location "C:\path\to\repo\automation\hubspot"
.\.venv\Scripts\Activate.ps1
python .\send_prospects.py --config .\config.json
```

Then register a scheduled task:

```powershell
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File C:\path\to\repo\automation\hubspot\run_hubspot_send.ps1"
$trigger = New-ScheduledTaskTrigger -Daily -At 8:00AM
Register-ScheduledTask -TaskName "HubSpot Daily Prospect Send" -Action $action -Trigger $trigger -Description "Send HubSpot campaign to prospects daily"
```

> For UI-driven browser automation, run the task with a user account that stays logged in.

## Notes

- UI labels in HubSpot can vary. If elements are not found, update selectors in `send_prospects.py`.
- Prefer HubSpot-native scheduling/workflows for maximum reliability and compliance.
