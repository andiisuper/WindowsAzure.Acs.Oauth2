#!/usr/bin/env python3
"""Send a HubSpot marketing email to a target list using Playwright.

Usage:
    python send_prospects.py --config config.json
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import dataclass
from pathlib import Path

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


@dataclass
class Config:
    email_url: str
    target_list_name: str
    user_data_dir: str = "./.hubspot-profile"
    headless: bool = False
    slow_mo_ms: int = 0
    timeout_ms: int = 45000
    screenshot_path: str = "./last-run.png"


def load_config(path: Path) -> Config:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    return Config(**data)


def send_email(config: Config) -> None:
    logging.info("Launching browser with persistent profile: %s", config.user_data_dir)

    with sync_playwright() as pw:
        browser = pw.chromium.launch_persistent_context(
            config.user_data_dir,
            headless=config.headless,
            slow_mo=config.slow_mo_ms,
        )

        try:
            page = browser.pages[0] if browser.pages else browser.new_page()
            page.set_default_timeout(config.timeout_ms)

            logging.info("Opening HubSpot email page")
            page.goto(config.email_url, wait_until="domcontentloaded")

            # Ensure we are logged in. If this fails, user must log in once manually.
            page.get_by_role("button", name="Send").wait_for()

            logging.info("Opening recipient side panel")
            page.get_by_role("button", name="Send to more").click()

            logging.info("Selecting target list: %s", config.target_list_name)
            list_row = page.locator("tr", has_text=config.target_list_name).first
            list_row.get_by_role("checkbox").check()

            logging.info("Submitting email send")
            page.get_by_role("button", name="Send", exact=True).click()

            page.wait_for_timeout(1500)
            page.screenshot(path=config.screenshot_path, full_page=True)
            logging.info("Saved evidence screenshot: %s", config.screenshot_path)
        except PlaywrightTimeoutError as exc:
            logging.error("UI element not found in time: %s", exc)
            page.screenshot(path=config.screenshot_path, full_page=True)
            logging.error("Saved failure screenshot: %s", config.screenshot_path)
            raise
        finally:
            browser.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config.json"),
        help="Path to JSON config file",
    )
    return parser.parse_args()


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    args = parse_args()

    if not args.config.exists():
        logging.error("Config file not found: %s", args.config)
        return 1

    try:
        config = load_config(args.config)
        send_email(config)
    except Exception:
        logging.exception("Run failed")
        return 1

    logging.info("Run completed successfully")
    return 0


if __name__ == "__main__":
    sys.exit(main())
