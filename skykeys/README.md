# SkyKeys – Meta-Preisvergleich (MVP)

Dieses Repository enthält das aktualisierte Projektgerüst für **SkyKeys**,
eine Meta-Preisvergleichsplattform für Game Keys. Das MVP ist nun auf ein
**Netlify**-basiertes Deployment ausgelegt: Das React-Frontend wird mit Vite
gebaut und als statische Seite ausgeliefert, während die Aggregations- und
Scraping-Logik in **Netlify Functions** portiert wird.

## Architekturüberblick

- **Frontend**: React (Vite) + TailwindCSS im norisk.gg-inspirierten Dark-Style
  (Neon-Akzente, Glas-Effekte, hochwertige Typografie).
- **Serverless Backend**: Netlify Functions (`/.netlify/functions/search`) als
  Ersatz für das ehemalige FastAPI-Backend. Adapter, Normalisierung,
  Deduplizierung und Caching werden nach Node.js/TypeScript überführt.
- **Scraping**: Playwright (Chromium) mit Stealth-Modus, zufälligen Delays,
  Backoff und Domain-Rate-Limits (Implementierung folgt in den Adaptern).
- **Konfiguration**: YAML-Dateien pro Quelle sowie `rates.json` für statische
  Wechselkurse, gebündelt unter `netlify/functions/config`.
- **Caching**: In-Memory-Cache mit 45-Minuten-TTL je Funktionsinstanz.
- **Deployment**: Netlify (`netlify.toml`) mit Build-Command `npm run build`,
  Publish-Ordner `dist` und Functions-Verzeichnis `netlify/functions`.

## Projektstruktur

```
skykeys/
  netlify.toml                       # Netlify Build & Redirect-Konfiguration
  package.json                       # Vite/Tailwind/React Setup & Scripts
  .env.example                       # Platzhalter für Netlify Environment Variablen
  frontend/
    index.html                       # Vite Entry (Root im Frontend-Ordner)
    vite.config.ts                   # Vite-Konfiguration (root=frontend, outDir=../dist)
    src/
      main.tsx                       # React Bootstrap (TODOs für App-Mounting)
      App.tsx                        # Komponenten-Skelett (Norisk.gg-Anmutung)
      components/                    # Navbar, Hero, SearchBar, BestDealCard, Filters,
                                     # OffersTable, OfferCard, Skeleton, Footer, FAQ, HowItWorks
      lib/api.ts                     # Fetch-Helfer für /.netlify/functions/search
      styles.css                     # Tailwind-Setup & Design-Tokens (TODO)
  netlify/
    functions/
      search.ts                      # Serverless Entry-Point (Caching, Aggregation, Fehlerreporting)
      core/                          # Normalisierung, Dedupe, Currency, Cache, Robots, Utils (TODO)
        cache.ts
        currency.ts
        dedupe.ts
        normalize.ts
        robots.ts
        utils.ts
      adapters/                      # 10 Source-Adapter (PlanetKey, GG.deals, etc.)
        planetkey.ts
        keysforsteam.ts
        ggdeals.ts
        cheapshark.ts
        isthereanydeal.ts
        gamivo.ts
        eneba.ts
        cdkeys.ts
        fanatical.ts
        greenmangaming.ts
      config/
        sources_enabled.yaml         # Feature-Flags für Adapteraktivierung
        rates.json                    # Statische EUR-Umrechnungskurse
        sources/*.yaml               # Selektoren & Scraping-Regeln (TODO)
```

## Einrichtung & lokale Entwicklung

1. **Node.js installieren** (>=18) und `npm install` im Projektroot ausführen.
   Dadurch werden Vite, React, Tailwind sowie Netlify-Funktionstypen verfügbar.
2. **Netlify CLI** optional installieren (`npm install -g netlify-cli`), um mit
   `netlify dev` Frontend und Functions gemeinsam zu testen.
3. **Environment Variablen** über `.env` bzw. Netlify Dashboard pflegen
   (Playwright-Credentials, Rate-Limits, Feature-Flags).
4. **Frontend-Entwicklung**: `npm run dev` startet Vite mit Proxy auf die
   Functions (`/.netlify/functions/search`).
5. **Build & Deploy**: `npm run build` erzeugt `dist/`. Netlify deployt dieses
   Verzeichnis und bundelt Functions aus `netlify/functions/`.

## Scraping-Richtlinien & robots.txt

- Vor jedem Crawl `robots.txt` respektieren. Die Helper unter
  `netlify/functions/core/robots.ts` sollen Regeln cachen und konfigurierbar
  machen.
- Pro Domain Rate-Limits und zufällige Delays nutzen (siehe TODOs in den
  Adapterdateien). Netlify Functions haben ein Zeitlimit von ca. 10s – passende
  Timeouts und parallele Ausführung mit Vorsicht planen.
- Fehlerhafte Quellen dürfen die Gesamtausgabe nicht blockieren. Stattdessen
  Fehler in `flags.errors` sammeln und `flags.partial_results` setzen.

## YAML-Selektoren pflegen

- Jede Datei unter `netlify/functions/config/sources/*.yaml` enthält Platzhalter
  für `search_url_template`, CSS-Selektoren, Pagination, `price.regex` usw.
- Dokumentiere Besonderheiten (Region-Locks, Gebührenhinweise) im `notes`-Feld.
- Nutze `sources_enabled.yaml`, um Quellen temporär zu deaktivieren (z. B.
  Wartung, Captcha-Schutz).

## Caching & Datenmodell (Serverless)

- Der frühere SQLite-Layer entfällt. Stattdessen legt `core/cache.ts` eine
  In-Memory-Map an, die pro Warm-Instance gültig ist.
- Normalisierung (`core/normalize.ts`) und Deduplizierung (`core/dedupe.ts`)
  spiegeln weiterhin das definierte Offer-Schema
  (`title`, `shop_domain`, `platform`, `price_total_eur`, …).

## Tests & Qualitätssicherung

- Unit-Tests werden künftig mit Jest/Vitest abgebildet (TODO: neue
  Testverzeichnisse anlegen).
- Für E2E-Smoke-Tests kann Netlify CLI Playwright-Aufrufe triggern (zeitliche
  Limits beachten).
- Logging erfolgt über `console.log` – Netlify stellt die Ausgaben im Dashboard
  bereit. Strukturierte Logs (JSON) erleichtern spätere Observability.

## Nächste Schritte

- Node.js-Portierung der bisherigen Python-Logik (Cache, Normalize, Dedupe).
- Playwright-Stealth-Setup als gemeinsam genutzes Modul implementieren.
- Tailwind Theme ausarbeiten (Cyan/Fuchsia-Gradienten, Glas-Effekte,
  Micro-Interactions).
- Tests & Linting (ESLint, Prettier) ergänzen, sobald produktiver Code entsteht.
