# KI für Sie — Homepage Design Guidelines

## Projekt-Übersicht
Dieses Repo enthält Demo-Homepages für lokale Schweizer Klein- und Mittelunternehmen.
Jede Seite ist ein einzelnes HTML-File mit Inline-CSS und Inline-JS.

---

## Prompt-Template für neue Homepages

Verwende dieses Template als Basis-Prompt für jede neue Seite:

```
Erstelle eine professionelle, visuell einzigartige Single-Page-Website für [BUSINESS NAME],
[BRANCHE] in [ORT/KANTON].

PFLICHT-ANFORDERUNGEN:
- Sprache: Deutsch (Schweiz)
- Single HTML-File, kein externes CSS/JS ausser Google Fonts
- Mobile-first, vollständig responsive mit Hamburger-Menü
- Smooth-Scroll-Navigation (fixed, scroll-responsiv)
- Scroll-Reveal-Animationen für alle Sections

DESIGN-TOKENS (Brand-spezifisch anpassen):
- Primärfarbe: [MARKENFARBE — z.B. tiefes Waldgrün #2d5016]
- Akzentfarbe: [KONTRAST-AKZENT — z.B. warmes Gold #c9a84c]
- Hintergrund: [WARM/KALT/NEUTRAL]
- Typografie-Hauptfont: [CHARAKTER-FONT — KEIN Inter/Roboto/Arial]
- Typografie-Headline: [SERIF-FONT für H1-H3]

TYPOGRAFIE-REGELN:
- Headlines (H1-H3): Charakterstarker Serif — z.B. Cormorant Garamond, DM Serif Display,
  Libre Baskerville, Lora, Playfair Display, Fraunces, Young Serif
- Body-Text: Moderner Sans — z.B. DM Sans, Plus Jakarta Sans, Outfit, Syne, Space Grotesk
  (KEIN Inter, Roboto, Arial, system-ui)
- Headline-Grösse: clamp(2.5rem, 6vw, 4.5rem) für H1, clamp(2rem, 4vw, 3rem) für H2
- Zeilenhöhe: 1.1 für Headlines, 1.7–1.8 für Fliesstext

LAYOUT-REGELN:
- Hero: Vollbild (100vh), Unsplash-Bild passend zum Business, Parallax-Overlay
- About: Alternating Grid (Bild links + Text rechts ODER umgekehrt) — KEIN 3-Spalten-Grid
- Services: Kreatives Layout — z.B. horizontale Karten, gestaffelte Reihen, Akkordeon
  (KEIN Standard-3-Spalten-Feature-Grid)
- Testimonials: Horizontaler Scroll oder Mosaic-Layout
- Kontakt: Map-Embed + Kontaktinfo nebeneinander
- Container-Verschachtelung: maximal 2 Ebenen

ANTI-SLOP CHECKLIST (diese Elemente VERBOTEN):
❌ Fonts: Inter, Roboto, Arial, system-ui als einzige Schrift
❌ Farben: Violett-Farbverläufe als primäre Palette (nur falls Markenfarbe)
❌ Farben: Teal/Türkis als Standard-Akzent
❌ Layouts: Standard 3-Spalten-Feature-Grid mit Icon oben
❌ Ornamente: Linker vertikaler Akzentbalken (border-left) als Dekoration
❌ Animationen: Blinkende Status-Dots oder Pulse-Effekte
❌ Navigation: Generische "Home / About / Services / Contact" ohne Branding
❌ Helden: Stock-Hero ohne Overlay oder Gradient-Bezug zu Markenfarben

SECTIONS (in dieser Reihenfolge):
1. Navigation (Logo + Links + Mobile Hamburger)
2. Hero (Vollbild, Marken-Badge mit Sternebewertung, 2 CTA-Buttons)
3. Über uns / Story (Grid: Bild + Text, 2-3 Statistiken)
4. Leistungen / Angebot (kreatives Layout, 4-6 Karten)
5. Warum wir? / USPs (alternierend oder Feature-Reihe)
6. Testimonials / Kundenstimmen (3 Reviews mit Avataren)
7. Galerie (Masonry oder asymmetrisches Grid, 6 Bilder)
8. Kontakt + Google Maps (2-spaltig)
9. Footer (Logo, Links, Copyright)

UNSPLASH-BILDER:
- Hero: business-spezifisches Suchterm, ?w=1400&q=80
- About: authentisches Bild, ?w=800&q=80
- Galerie: 6 passende Bilder, ?w=600&q=75
- Avatare: portrait photos, ?w=100&q=80

CSS-BEST-PRACTICES:
- CSS Custom Properties für alle Design-Tokens in :root
- clamp() für responsive Schriftgrössen
- CSS Grid + Flexbox (kein Float)
- Transition: all 0.4s ease auf interaktiven Elementen
- backdrop-filter: blur() für Glas-Effekte
- will-change: transform nur für animierte Elemente
- :hover mit transform: translateY(-2px–5px) für Karten

JS-BEST-PRACTICES:
- IntersectionObserver für Scroll-Reveal
- Hamburger-Menü mit transform statt display:none
- Smooth-Scroll via CSS (scroll-behavior:smooth)
- Kein jQuery, kein externes Framework
```

---

## Qualitäts-Checkliste vor Fertigstellung

Nach jeder Seite diese Punkte prüfen:

### Design
- [ ] Primärfarbe ist business-spezifisch und konsistent
- [ ] Font ist charakterstark und NICHT Inter/Roboto/Arial
- [ ] Kein generisches 3-Spalten-Grid als einziges Layout
- [ ] Jede Section hat eigene visuelle Identität
- [ ] Hover-States auf allen interaktiven Elementen

### Performance
- [ ] Bilder mit ?w= und ?q= optimiert (Unsplash)
- [ ] will-change sparsam eingesetzt
- [ ] Kein render-blocking JS in <head>
- [ ] Google Fonts: nur benötigte Weights geladen

### Responsive
- [ ] Hamburger-Menü funktioniert auf Mobile
- [ ] Hero-Headline lesbar auf 375px
- [ ] Alle Grids brechen sauber auf 1-Spalte zusammen
- [ ] Touch-Targets mind. 44px

### Accessibility
- [ ] alt-Attribute auf allen Bildern
- [ ] Kontrastrating mind. 4.5:1 für Body-Text
- [ ] lang="de" auf <html>
- [ ] Semantische HTML-Elemente (nav, main, section, footer)

---

## Business-Typ → Design-Empfehlungen

### Coiffeur / Beauty / Nails
- **Fonts**: Cormorant Garamond (Headlines) + DM Sans (Body)
- **Farben**: Warme Nude-Töne, Rosé-Gold, Tief-Bordeaux
- **Layout**: Elegantes Magazin-Layout, grosse Bilder
- **Feeling**: Luxus, Pflege, Wohlfühlen

### Restaurant / Café / Pizzeria
- **Fonts**: Fraunces (Headlines) + Plus Jakarta Sans (Body)
- **Farben**: Tiefes Rot/Braun, Goldgelb, Cremeweiß
- **Layout**: Menükarten-Style, Food-Fotografie prominent
- **Feeling**: Authentisch, einladend, lecker

### Reinigung / Handwerk / Service
- **Fonts**: Syne (Headlines) + Outfit (Body)
- **Farben**: Vertrauenswürdiges Blau, Frisches Grün, Sauberes Weiß
- **Layout**: Professionell, klar strukturiert, Trust-Signale
- **Feeling**: Zuverlässig, kompetent, transparent

### Zahnarzt / Kosmetik / Gesundheit
- **Fonts**: Libre Baskerville (Headlines) + Space Grotesk (Body)
- **Farben**: Kühles Minzgrün, Weißtöne, Zartes Blau
- **Layout**: Clean Medical, Trust-Badges prominent
- **Feeling**: Professionell, sauber, vertrauenswürdig

### Blumenladen / Garten
- **Fonts**: Young Serif (Headlines) + DM Sans (Body)
- **Farben**: Sattes Grün, Blütenfarben, Erdtöne
- **Layout**: Organisch, asymmetrisch, naturnahe Formen
- **Feeling**: Frisch, lebendig, handgemacht

---

## Verbesserungs-Prompts für bestehende Seiten

### Anti-Slop Audit
```
Analysiere diese HTML-Seite auf typische KI-Design-Fingerabdrücke:
1. Werden überbenutzte Fonts (Inter, Roboto, Arial) verwendet?
2. Gibt es generische 3-Spalten-Grids ohne Variation?
3. Sind Farben wirklich brand-spezifisch oder generisch?
4. Gibt es blinkende Animationen oder überbenutzte Effekte?
Erstelle eine Punch-List mit konkreten Verbesserungen.
```

### Typography Upgrade
```
Verbessere die Typografie dieser Seite:
- Ersetze [aktueller Font] durch einen charakterstarken Alternative
- Füge font-feature-settings: "liga" 1, "kern" 1 hinzu
- Verbessere Letter-Spacing bei Headlines
- Optimiere Zeilenhöhen für bessere Lesbarkeit
```

### Layout Diversification
```
Diese Seite hat zu viele ähnliche Grid-Layouts. 
Überarbeite die Services-Section mit einem alternativen Layout:
[Wähle: horizontale Scroll-Karten / gestaffelte Reihen / Akkordeon / Mosaic-Grid]
Stelle sicher dass jede Section eine eigene visuelle Sprache hat.
```

### Mobile UX Fix
```
Optimiere diese Seite für Mobile (375px–428px):
- Prüfe alle Schriftgrössen (min. 16px für Body)
- Stelle sicher dass Touch-Targets mind. 44px sind
- Überprüfe dass kein horizontales Scrolling entsteht
- Teste alle Hover-States (müssen auch ohne Hover funktionieren)
```

---

## Projekt-Konventionen

- **Dateiname**: `demo/[business-slug].html` (kebab-case)
- **Encoding**: UTF-8
- **Sprache**: `lang="de"` 
- **Bilder**: Nur Unsplash (unsplash.com/photos/...) mit ?w= und ?q= Params
- **Icons**: Nur Unicode-Emoji oder SVG inline (kein Font Awesome, kein Lucide)
- **Karten**: Nur embed.maps.google.com iFrame oder OpenStreetMap

---

## Commit-Konvention

```
feat: add [business-name] homepage
fix: [business-name] mobile layout
improve: [business-name] typography and colors
```
