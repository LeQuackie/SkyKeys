# SkyKeys – Meta-Preisvergleich (MVP)

Dieses Repository enthält das Projektgerüst für **SkyKeys**, eine
asynchrone Meta-Preisvergleichsplattform für Game Keys. Das Ziel ist,
über zehn etablierte Vergleichsseiten hinweg Angebote zu scrapen,
normalisieren und deduplizieren, sodass Nutzer:innen stets das günstigste
Angebot finden – präsentiert in einem norisk.gg-inspirierten UI.

## Architekturüberblick

- **Backend**: FastAPI (async) mit modularer Adapterstruktur für jede
  Quelle, Normalisierung und Caching (SQLite mit 45 Minuten TTL).
- **Scraping**: Playwright (Chromium) mit Stealth-Setup, zufälligen
  Delays, Backoff und per-Domain-Rate-Limit.
- **Konfiguration**: YAML-Dateien für Selektoren je Quelle sowie
  `config/rates.json` für feste Wechselkurse.
- **Frontend**: React (Vite) + TailwindCSS, inspiriert von norisk.gg –
  dunkler Premium-Look, Neon-Akzente, Glas-Effekte.
- **Deployment**: Dockerfiles für Backend und Frontend sowie
  `docker-compose` für lokales Orchestrieren.

## Projektstruktur

```
skykeys/
  backend/
    main.py                          # FastAPI-Einstiegspunkt (TODOs für Routen, Middleware, Lifespan)
    core/                            # Normalisierung, Dedupe, Currency, Cache, Robots, Utils
      normalize.py
      dedupe.py
      currency.py
      cache.py
      robots.py
      utils.py
    adapters/                        # Adapter je Quelle (10 Stück + Base)
      base.py
      planetkey.py
      keys_for_steam.py
      ggdeals.py
      cheapshark.py
      isthereanydeal.py
      cdkeys.py
      eneba.py
      fanatical.py
      gamivo.py
      greenmangaming.py
  config/
    sources_enabled.yaml             # Reihenfolge & Aktivierung der Quellen
    sources/*.yaml                   # Selektoren & Rate-Limits je Quelle (Platzhalter)
    rates.json                       # Statische EUR-Umrechnungskurse
  frontend/
    index.html
    src/
      main.tsx
      App.tsx
      components/                    # Navbar, Hero, SearchBar, BestDealCard, Filters, OffersTable, OfferCard, Skeleton, Footer, HowItWorks, FAQ
      lib/api.ts
      styles.css                     # Tailwind/Tokens-Platzhalter
  tests/
    test_normalize.py
    test_dedupe.py
    test_parsers.py
  scripts/
    add_source.py
    smoke_test.sh
  .env.example
  docker-compose.yml
  Dockerfile.backend
  Dockerfile.frontend
  Makefile
```

## Einrichtung & lokale Entwicklung

1. **Playwright-Abhängigkeiten installieren**: Chromium + Stealth-Patches
   vorbereiten. Siehe künftige Dockerfiles oder manuelle Installation via
   `playwright install --with-deps`.
2. **Python-Umgebung**: Virtuelle Umgebung erstellen, FastAPI, Playwright
   und SQLite-Driver installieren (abhängige Versionen folgen in Pip-/Poetry-Dateien).
3. **Frontend**: Node.js (>=18) installieren, `npm install` im
   `frontend`-Verzeichnis ausführen, Tailwind konfigurieren.
4. **Umgebungsvariablen**: `.env` auf Basis von `.env.example`
   anpassen (Playwright-Timeouts, Rate-Limits, Pfade für SQLite etc.).
5. **Docker**: Alternativ `docker-compose` verwenden (Services müssen in
   der Compose-Datei ergänzt werden).

## Scraping-Richtlinien & robots.txt

- **robots.txt beachten**: Der Adapter muss vor jedem Crawl prüfen, ob
  der jeweilige Pfad für den SkyKeys User-Agent erlaubt ist.
- **Rate-Limits respektieren**: Per Quelle in der YAML definiert
  (`requests_per_minute`, zufällige Delays). Diese Limits sind strikt
  einzuhalten.
- **Backoff & Fehlerhandling**: Bei HTTP-/Timeout-Fehlern exponentielles
  Backoff verwenden, aber das Gesamtergebnis dennoch liefern. Fehler pro
  Quelle in `flags.errors` melden.

## YAML-Selektoren anpassen

- Jede Datei unter `config/sources/*.yaml` enthält Platzhalter für
  Selektoren (`TODO-CSS-SELECTOR`).
- Fülle `metadata`, `search`, `selectors`, `price_parsing` und `flags`
  mit realen Werten, sobald die DOM-Struktur analysiert wurde.
- Halte das Limit `max_items` konservativ, um Performance und
  Anti-Bot-Maßnahmen nicht zu gefährden.
- Dokumentiere Besonderheiten (z. B. Gebühren, Regionen) im `notes`-Feld.

## Datenmodell & Caching

- `offers`-Tabelle speichert normalisierte Resultate inklusive TTL.
- `scrape_logs` protokolliert Dauer, Status und Fehlergründe pro Quelle.
- Cache-Regel: gleiche Suche innerhalb von 45 Minuten liefert gespeichertes
  Ergebnis, ansonsten erneute Scrape-Runde.

## Tests & Qualitätssicherung

- **Unit-Tests**: `tests/test_normalize.py`, `tests/test_dedupe.py`,
  `tests/test_parsers.py` – derzeit Platzhalter, sollen Mock-HTML und
  synthetische Daten nutzen.
- **Smoke-Test**: `scripts/smoke_test.sh` vorbereitet für künftige
  E2E-Läufe mit Playwright.
- **Makefile**: geplanter Einstieg für `make up`, `make test`, `make fmt`.

## Design-Richtlinien (Frontend)

- Dark Theme (#0b0d12) mit subtilen Gradients.
- Neon-Akzente (Cyan/Fuchsia) für Buttons, Badges, Fokus-Stati.
- Glassmorphism: halbtransparente Karten (`backdrop-blur`, feine
  1px-Border), sanfte Schatten, runde Ecken (`rounded-2xl`).
- Mikro-Interaktionen: 150–250 ms Transitions, Hover-Glows, Fokus-Ringe.
- Responsives Layout: mobile Cards, Tablet 2-Spalten, Desktop großzügige
  Abstände. Filters ggf. als Drawer.
- A11y: ausreichende Kontraste, ARIA-Labels, Tastaturnavigation.

## Nächste Schritte

- FastAPI-Routen implementieren (`/search`, `/health`).
- Adapterlogik aufbauen, YAML-Selektoren konkretisieren.
- SQLite-Schema entwerfen, Migrationsstrategie festlegen.
- React-Komponenten mit Tailwind umsetzen und API anbinden.
- Tests schreiben, CI/CD-Pipeline aufsetzen.

Viel Erfolg beim Ausbau von SkyKeys! 🚀
