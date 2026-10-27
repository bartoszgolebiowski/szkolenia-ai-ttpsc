# Transition Technologies PSC · Akademia AI & Copilot

Kompletny zestaw interaktywnych prezentacji szkoleniowych w czystym HTML/CSS i Inline SVG (standard McKinsey, BCG, Google Keynote), opracowany na potrzeby 4-godzinnych warsztatów praktycznych z narzędzi Microsoft Copilot oraz GitHub Copilot.

---

## 🎯 Struktura Szkolenia (4-Godzinny Format Warsztatowy)

Każde szkolenie realizowane jest w rytmie **hands-on**:
- **00:00 – 00:10** · Otwarcie, zasady bezpieczeństwa (NDA, sanitacja) i definicja Done.
- **Trzy Pętle Laboratoryjne (12 + 40 + 10 min):**
  - **12 min** · Wprowadzenie do problemu operacyjnego i dźwignia AI.
  - **40 min** · Praktyka laboratoryjna na autoryzowanym zbiorze danych / repozytorium.
  - **10 min** · Inspekcja wyników, weryfikacja asercji i dyskusja.
- **Transfer Wiedzy (24 min)** · Wybór kolejnego procesu do optymalizacji w codziennej pracy.

---

## 📂 Zawartość Katalogów

### 1. `technical-trainee/` — Zespoły Inżynieryjne (GitHub Copilot)
Katalog dedykowany programistom, inżynierom oprogramowania i DevOps:
- [`00-master-1h-training.html`](./technical-trainee/00-master-1h-training.html) — **1-Godzinny Keynote Strategiczny**: ankieta TTPSC (N=8), architektura 4h, metoda "Zbierz → Strukturyzuj → Zbuduj → Przetestuj" (Double Diamond), błędne koło długu technicznego, diagram Ishikawy oraz reguły dewelopera.
- [`case-01-failing-test-debug.html`](./technical-trainee/case-01-failing-test-debug.html) — **T1**: Diagnostyka przyczyny czerwonego testu jednostkowego.
- [`case-02-test-quality.html`](./technical-trainee/case-02-test-quality.html) — **T2**: Podnoszenie jakości i pokrycia generowanych testów.
- [`case-03-code-review.html`](./technical-trainee/case-03-code-review.html) — **T3**: Sceptyczny audyt i przegląd kodu wspomaganego AI.
- [`case-04-legacy-refactor.html`](./technical-trainee/case-04-legacy-refactor.html) — **T4**: Bezpieczna migracja i refaktoryzacja kodu legacy.
- [`case-05-slow-sql-optimization.html`](./technical-trainee/case-05-slow-sql-optimization.html) — **T5**: Optymalizacja wolnego zapytania Oracle SQL.
- [`case-06-mockup-to-jira.html`](./technical-trainee/case-06-mockup-to-jira.html) — **T6**: Transformacja makiety UI w gotowe zadania Jira.
- [`case-07-unfamiliar-repo.html`](./technical-trainee/case-07-unfamiliar-repo.html) — **T7**: Odnajdywanie reguł biznesowych w nowym repozytorium.
- [`case-08-technical-to-business-update.html`](./technical-trainee/case-08-technical-to-business-update.html) — **T8**: Tłumaczenie zmian technicznych na język biznesu.
- [`case-09-client-restrictions-security.html`](./technical-trainee/case-09-client-restrictions-security.html) — **T9**: Praca w reżimie ograniczeń klienta i ochrona NDA.
- [`index.html`](./technical-trainee/index.html) — Portal nawigacyjny dla uczestników technicznych.

### 2. `non-technical-trainee/` — Zespoły Biznesowe (Microsoft Copilot)
Katalog dedykowany analitykom, kierownikom projektów i specjalistom operacyjnym:
- [`00-master-1h-training.html`](./non-technical-trainee/00-master-1h-training.html) — **1-Godzinny Keynote Strategiczny**: ankieta TTPSC (N=6), architektura 4h, uziemienie w plikach SharePoint, błędne koło braku źródeł, most dojrzałości oraz zasady weryfikacji.
- [`case-01-long-agreement-contract.html`](./non-technical-trainee/case-01-long-agreement-contract.html) — **N1**: Odnajdywanie kluczowych zapisów w długich umowach handlowych.
- [`case-02-correspondence-register.html`](./non-technical-trainee/case-02-correspondence-register.html) — **N2**: Budowa ustrukturyzowanego rejestru pism z plików SharePoint.
- [`case-03-source-access-sharepoint.html`](./non-technical-trainee/case-03-source-access-sharepoint.html) — **N3**: Weryfikacja uprawnień i źródeł (SharePoint vs Confluence).
- [`case-04-weekly-update-drafting.html`](./non-technical-trainee/case-04-weekly-update-drafting.html) — **N4**: Tworzenie cyklicznych raportów tygodniowych dla zarządu.
- [`case-05-spreadsheet-overdue-analysis.html`](./non-technical-trainee/case-05-spreadsheet-overdue-analysis.html) — **N5**: Identyfikacja zaległych działań i anomalii w Excelu.
- [`case-06-meeting-actions-follow-up.html`](./non-technical-trainee/case-06-meeting-actions-follow-up.html) — **N6**: Przekształcanie notatek ze spotkań Teams w rejestr zadań.
- [`case-07-report-to-presentation.html`](./non-technical-trainee/case-07-report-to-presentation.html) — **N7**: Skrót 40-stronicowego raportu do 5-slajdowej prezentacji.
- [`case-08-customer-meeting-prep.html`](./non-technical-trainee/case-08-customer-meeting-prep.html) — **N8**: Przygotowanie rozmowy z klientem B2B w trudnej sytuacji.
- [`case-09-estimating-implementation-work.html`](./non-technical-trainee/case-09-estimating-implementation-work.html) — **N9**: Szacowanie nakładu prac wdrożeniowych i struktura WBS.
- [`index.html`](./non-technical-trainee/index.html) — Portal nawigacyjny dla uczestników biznesowych.

---

## ⌨️ Skróty Klawiszowe Prezentera

Wszystkie prezentacje posiadają zintegrowany silnik sterowania:
- `Spacja` / `→` — Następny krok animowany (`.fragment`) lub następny slajd.
- `←` / `Backspace` — Poprzedni krok lub slajd.
- `G` / `Esc` — Włączenie / wyłączenie widoku siatki miniatur (**Grid View**).
- `Alt + A` — **Dyskretny Panel Administratora** (wybór motywu: TTPSC, PwC, CyberArk, Palo Alto, live color picker).
- `H` — Ukrycie dolnego paska nawigacji (tryb czystego ekranu przed widownią).
- `F` — Tryb pełnoekranowy (Fullscreen).
- `Ctrl + P` — Bezpośredni eksport do PDF z zachowaniem proporcji slajdów.

---

## 🎨 Zasady Wizualne
- **Czysta geometria SVG (Text-Free SVG):** Żadnych znaczników `<text>` w SVG – wszystkie etykiety umieszczone są w HTML/CSS.
- **Rygor redakcyjny:** Krótkie zdania, tytuły-wnioski, brak ścian tekstu, 20–35 słów na slajd.
- **Oficjalne motywy:** Domyślna paleta Transition Technologies PSC (`#2B0D30`, `#7B2D85`, `#D03A8C`, `#64B237`).
