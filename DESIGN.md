# DESIGN.md — [BUSINESS NAME]

_Fülle diese Datei aus BEVOR du eine neue Homepage erstellst.
Teile sie Claude als Kontext mit: "Hier ist mein DESIGN.md:"_

---

## 1. Business-Info

| Feld | Wert |
|------|------|
| Name | [z.B. Cabelo Vida] |
| Branche | [z.B. Coiffeur] |
| Ort | [z.B. Wallisellen, ZH] |
| USP | [z.B. Spezialisiert auf Balayage & Keratin] |
| Zielgruppe | [z.B. Frauen 25–50, gehobenes Segment] |
| Tonalität | [z.B. Warm, persönlich, professionell] |
| Kontakt | [Telefon, E-Mail, Adresse] |
| Google Maps ID | [ID aus Google Maps URL] |

---

## 2. Design-Tokens

```css
:root {
  /* Hauptfarben — brand-spezifisch wählen */
  --primary:        [HEX];   /* z.B. #2d5016 Waldgrün */
  --primary-light:  [HEX];   /* 15% heller als primary */
  --accent:         [HEX];   /* z.B. #c9a84c Warmgold */
  
  /* Hintergründe */
  --dark:           [HEX];   /* z.B. #0f1a0a Tiefes Dunkel */
  --light:          [HEX];   /* z.B. #f7f4ef Warmes Off-White */
  
  /* Text */
  --text:           [HEX];   /* z.B. #2c2c2c Fast-Schwarz */
  --text-light:     [HEX];   /* z.B. #6b6b6b Hellgrau */
  
  /* System */
  --radius:         [px];    /* z.B. 16px oder 4px (sharp) */
  --shadow: 0 8px 32px rgba(0,0,0,0.12);
}
```

---

## 3. Typografie

| Rolle | Font | Weights | Fallback |
|-------|------|---------|---------|
| Headlines (H1–H3) | [z.B. Cormorant Garamond] | 400, 700 | serif |
| Body / UI | [z.B. DM Sans] | 300, 400, 500, 600 | sans-serif |

**Google Fonts Import-URL:**
```
https://fonts.googleapis.com/css2?family=[HEADLINE-FONT]:wght@400;700&family=[BODY-FONT]:wght@300;400;500;600&display=swap
```

**Headline-Style:**
- [ ] Italic für emotionale Wirkung
- [ ] Letter-spacing: -0.02em (tight)
- [ ] oder Letter-spacing: 0.05em (weite, klassische Headlines)

---

## 4. Visuelle Persönlichkeit

**Ästhetik-Familie** (eine wählen):
- [ ] Warm Editorial — klassisch, wohnlich, handwerklich
- [ ] Modern Minimal — clean, viel Weissraum, präzise
- [ ] Luxus — dunkle Töne, Gold-Akzente, gross und kühn
- [ ] Frisch & Lebendig — Natur, Pflanzen, organische Formen
- [ ] Professionell — Trust-Signale, klar strukturiert

**Stimmungsbilder / Referenzen:**
- [URL oder Beschreibung]
- [URL oder Beschreibung]

---

## 5. Unsplash-Suchterms

| Section | Suchterm | Beispiel-URL |
|---------|---------|-------------|
| Hero | [z.B. hairdresser salon luxury] | https://unsplash.com/photos/... |
| About | [z.B. hairdresser woman smiling] | |
| Galerie 1 | [z.B. hair color balayage] | |
| Galerie 2 | | |
| Galerie 3 | | |
| Galerie 4 | | |
| Galerie 5 | | |
| Galerie 6 | | |
| Testimonial Avatar 1 | portrait woman | |
| Testimonial Avatar 2 | portrait woman | |
| Testimonial Avatar 3 | portrait woman | |

---

## 6. Content-Bausteine

### Hero
- **Haupttitel:** [z.B. "Schönheit, die bewegt."]
- **Untertitel:** [1–2 Sätze, 15–20 Wörter]
- **CTA primär:** [z.B. "Termin buchen"]
- **CTA sekundär:** [z.B. "Unsere Leistungen"]
- **Badge-Text:** [z.B. "⭐ 4.9 · 120+ Bewertungen · Wallisellen"]

### Über uns
- **Headline:** [z.B. "Leidenschaft für Ihr Haar"]
- **Text:** [3–4 Sätze, authentisch, persönlich]
- **Statistik 1:** [z.B. "15+" / "Jahre Erfahrung"]
- **Statistik 2:** [z.B. "2000+" / "Zufriedene Kunden"]
- **Statistik 3:** [z.B. "5★" / "Bewertungen"]

### Leistungen (4–6 Stück)
| Name | Beschreibung (1 Satz) | Emoji/Icon |
|------|-----------------------|------------|
| [Leistung 1] | | |
| [Leistung 2] | | |
| [Leistung 3] | | |
| [Leistung 4] | | |

### Testimonials (3 Stück)
| Name | Text (2–3 Sätze) | Sterne |
|------|-----------------|--------|
| [Name 1] | | ⭐⭐⭐⭐⭐ |
| [Name 2] | | ⭐⭐⭐⭐⭐ |
| [Name 3] | | ⭐⭐⭐⭐⭐ |

### Footer
- **Öffnungszeiten:** [z.B. Mo–Fr 09:00–18:30, Sa 09:00–16:00]
- **Adresse:** [Vollständige Adresse]
- **Telefon:** [+41 xx xxx xx xx]
- **E-Mail:** [info@...]

---

## 7. Layout-Entscheidungen

**Services-Layout** (eine wählen):
- [ ] Horizontale Karten mit Top-Border-Hover-Animation
- [ ] Gestaffelte Reihen (Bild abwechselnd links/rechts)
- [ ] Akkordeon mit expandierbaren Details
- [ ] Mosaic-Grid (unterschiedliche Kartengrößen)
- [ ] Horizontaler Scroll (Carousel ohne JS)

**Galerie-Layout** (eine wählen):
- [ ] CSS Masonry (columns: 3)
- [ ] Asymmetrisches Grid (2+1 oder 1+2 Reihen)
- [ ] Full-Bleed Horizontalreihe
- [ ] Overlapping Cards

---

## 8. Schnell-Prompt für Claude

Wenn das DESIGN.md ausgefüllt ist, nutze diesen Prompt:

```
Hier ist mein DESIGN.md für eine neue Homepage:

[DESIGN.md-Inhalt hier einfügen]

Erstelle eine vollständige, professionelle Single-Page-Website als einzelnes HTML-File.
Halte dich exakt an die Design-Tokens, Fonts und Content-Bausteine aus dem DESIGN.md.
Folge dem Anti-Slop-Regelwerk aus CLAUDE.md.
Verwende ausschliesslich die angegebenen Unsplash-Bilder.
```
