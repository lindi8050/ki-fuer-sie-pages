import os
from dotenv import load_dotenv
from browser_use_sdk.v2 import BrowserUse

load_dotenv()

client = BrowserUse()  # liest BROWSER_USE_API_KEY aus .env


def run_task(task: str, start_url: str | None = None) -> str | None:
    """Führt einen Browser-Task aus und gibt das Ergebnis zurück."""
    result = client.run(task, start_url=start_url)
    return result.output


if __name__ == "__main__":
    # Guthaben prüfen
    account = client.billing.account()
    print(f"Guthaben: ${account.total_credits_balance_usd}")

    # Beispiel-Task
    output = run_task("Öffne google.com und gib den Titel der Seite zurück.")
    print(f"Ergebnis: {output}")
