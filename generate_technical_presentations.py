import os
import sys
import build_engine as be

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = "technical-trainee"
os.makedirs(OUT_DIR, exist_ok=True)

print(f"Generating technical presentations in ./{OUT_DIR} ...")

# ==============================================================================
# 00: MASTER PRESENTATION (TECHNICAL TRACK - 4 SLIDES)
# ==============================================================================
master_slides = [
    be.slide_title(
        title="GitHub Copilot w Inżynierii Oprogramowania: Od Podpowiedzi do Samodzielnego Dewelopera w Pętli",
        kicker="TRANSITION TECHNOLOGIES PSC // TECHNICAL TRAINING TRACK",
        subtitle="1-godzinna prezentacja wprowadzająca do 4-godzinnego warsztatu praktycznego. Wyjaśnia zasady współpracy z asystentem AI w IDE i CLI, eliminację płytkich testów oraz reguły bezpieczeństwa w projektach komercyjnych.",
        meta="GitHub Copilot · CLI · Test-Driven · 2026"
    ),

    be.slide_ranking_bars(
        kicker="DIAGNOZA ZESPOŁU // ANKIETA TTPSC (N=8)",
        title="100% Używa Copilota, Lecz 38% Traci Tyle Samo Czasu na Poprawki Kodu",
        items=[
            ("Użycie GitHub Copilot / Chat w IDE", "100%", 100, True),
            ("Przyspieszenie: Boilerplate i szkielety", "62.5%", 62.5, True),
            ("Przyspieszenie: Debugowanie i stack trace", "62.5%", 62.5, True),
            ("Wpływ neutralny (review kodu AI = czas pisania)", "37.5%", 37.5, True),
            ("Restrykcje NDA klienta (blokada MCP / danych)", "75.0%", 75, False),
            ("Brak zespołowych reguł (.cursorrules / prompts)", "75.0%", 75, False),
            ("Generowanie wartościowych testów jednostkowych", "12.5%", 12.5, False)
        ],
        pareto_text={
            "big": "38%",
            "desc": "Inżynierów wskazuje brak oszczędności czasu bez jasnych kryteriów akceptacji i weryfikacji asercji."
        },
        slide_num=2
    ),

    be.slide_pipeline(
        kicker="HARMONOGRAM // 4-GODZINNY WARSZTAT HANDS-ON",
        title="Agenda Warsztatu: Trzy Pętle Praktyki i Weryfikacji (12 + 40 + 10 min)",
        steps=[
            {
                "phase": "00:00–00:10",
                "title": "Baza i Granice",
                "desc": "Zasady izolacji kodu, sanitacja danych klienta (NDA), kryteria akceptacji.",
                "active": False
            },
            {
                "phase": "00:10–01:12",
                "title": "Lab 1: Ticket → Testy",
                "desc": "Przekształcenie niejednoznacznego ticketu Jira w zbadany, bezpieczny wycinek kodu.",
                "active": True
            },
            {
                "phase": "01:22–02:24",
                "title": "Lab 2: CLI & Skille",
                "desc": "Zamykanie pętli zadania z konsoli z użyciem poleceń /goal i /loop.",
                "active": True
            },
            {
                "phase": "02:34–04:00",
                "title": "Lab 3: Sceptyczny PR",
                "desc": "Adversarial code review, porównanie modeli na jednym zadaniu i transfer do pracy.",
                "active": True
            }
        ],
        slide_num=3
    ),

    be.slide_cta_decision_rows(
        kicker="REZULTATY // CO ZABIERASZ Z WARSZTATU",
        title="Trzy Kluczowe Umiejętności po Zakończeniu Szkolenia",
        decisions=[
            {
                "num": "1",
                "title": "Spec-Driven Development",
                "desc": "Formułowanie kryteriów akceptacji przed poproszeniem o implementację w IDE.",
                "stat": "+60%",
                "stat_desc": "trafności kodu w pierwszym podejściu",
                "stat_color": "var(--success)"
            },
            {
                "num": "2",
                "title": "Sceptyczna Weryfikacja Asercji",
                "desc": "Wykrywanie fałszywych testów jednostkowych i sprawdzanie rzeczywistych brzegów.",
                "stat": "0%",
                "stat_desc": "ślepego zaufania do zielonego paska",
                "stat_color": "var(--danger)"
            },
            {
                "num": "3",
                "title": "Praca w Reżimie NDA Klienta",
                "desc": "Techniki pracy na danych syntetycznych w bezpiecznym sandboxie bez wycieku IP.",
                "stat": "100%",
                "stat_desc": "zgodności z politykami bezpieczeństwa",
                "stat_color": "var(--primary)"
            }
        ],
        slide_num=4
    )
]

html_00 = be.wrap_presentation("GitHub Copilot · 1h Master Keynote (Technical Track)", "\n".join(master_slides))
with open(os.path.join(OUT_DIR, "00-master-1h-training.html"), "w", encoding="utf-8") as f:
    f.write(html_00)
print("  Generated: 00-master-1h-training.html")

# ==============================================================================
# CASE STUDY GENERATOR HELPER
# ==============================================================================
def generate_case_deck(filename, case_id, title, situation, without_ai, with_ai, gain, good_result, guardrail, deep_diagram_type):
    slides = [
        be.slide_title(
            title=f"{case_id}: {title}",
            kicker="TECHNICAL CASE STUDY // GITHUB COPILOT",
            subtitle=f"Warsztatowe studium przypadku: od manualnego tarcia do zweryfikowanego rezultatu.",
            meta=f"Scenariusz {case_id} · TTPSC 2026"
        ),

        be.slide_split_screen(
            kicker="SYTUACJA I WYZWANIE // PROBLEM DEFINITION",
            title=f"Kontekst Operacyjny: {title}",
            left_badge="Wyzwanie w Projekcie",
            left_title="Stan Rzeczywisty",
            left_points=[
                f"<strong>Scena:</strong> {situation['scene']}",
                f"<strong>Presja:</strong> {situation['pressure']}",
                f"<strong>Ryzyko:</strong> {situation['risk']}"
            ],
            right_badge="Cel Warsztatu",
            right_title="Oczekiwana Transformacja",
            right_points=[
                f"<strong>Cel:</strong> {situation['goal']}",
                f"<strong>Narzędzie:</strong> {situation['tool']}",
                f"<strong>Standard:</strong> {situation['standard']}"
            ],
            slide_num=2
        ),

        be.slide_split_screen(
            kicker="PORÓWNANIE METODYK // WORKFLOW CONTRAST",
            title="Ścieżka Tradycyjna vs Praca z GitHub Copilot",
            left_badge="Bez Wsparcia AI",
            left_title="Przebieg Manualny",
            left_points=[
                f"<strong>Krok 1:</strong> {without_ai['step1']}",
                f"<strong>Krok 2:</strong> {without_ai['step2']}",
                f"<strong>Tarcie:</strong> {without_ai['friction']}"
            ],
            right_badge="Z GitHub Copilot",
            right_title="Pętla Wspomagana",
            right_points=[
                f"<strong>Krok 1:</strong> {with_ai['step1']}",
                f"<strong>Krok 2:</strong> {with_ai['step2']}",
                f"<strong>Dźwignia:</strong> {with_ai['gain']}"
            ],
            slide_num=3
        ),

        be.slide_pipeline(
            kicker="PRZEPŁYW LABORATORYJNY // 4 KROKI ĆWICZENIA",
            title="Krok po Kroku w Środowisku Sandbox",
            steps=[
                {"phase": "Krok 1 (10 min)", "title": "Przygotowanie", "desc": "Pobierz gałąź laboratoryjną i zanonimizuj wejściowe dane testowe.", "active": False},
                {"phase": "Krok 2 (15 min)", "title": "Interakcja AI", "desc": "Sformułuj precyzyjny prompt z kryteriami rozstrzygającymi.", "active": True},
                {"phase": "Krok 3 (10 min)", "title": "Weryfikacja", "desc": "Uruchom lokalny test suite i zbadaj wygenerowany diff.", "active": True},
                {"phase": "Krok 4 (5 min)", "title": "Decyzja Dewelopera", "desc": "Zaakceptuj, zmodyfikuj lub odrzuć propozycję asystenta.", "active": False}
            ],
            slide_num=4
        ),

        be.slide_hero_stat(
            kicker="REZULTAT JAKOŚCIOWY // MEASURABLE SUCCESS",
            title="Mierzalna Korzyść i Wartość dla Uczestnika",
            big_stat=gain['stat'],
            stat_sub=gain['stat_sub'],
            conclusion_bold=gain['title'],
            conclusion_text=gain['desc'],
            slide_num=5
        ),

        be.slide_cta_decision_rows(
            kicker="REKOMENDACJE & BARIERY // GUARDRAILS",
            title="Niezbędna Kontrola Człowieka i Kryteria Jakości",
            decisions=[
                {
                    "num": "1",
                    "title": "Definicja Sukcesu",
                    "desc": good_result,
                    "stat": "DONE",
                    "stat_desc": "Kryterium ukończenia",
                    "stat_color": "var(--success)"
                },
                {
                    "num": "2",
                    "title": "Punkt Kontroli Człowieka",
                    "desc": guardrail,
                    "stat": "HUMAN",
                    "stat_desc": "Wymóg zatwierdzenia",
                    "stat_color": "var(--danger)"
                }
            ],
            slide_num=6
        ),

        be.slide_closing(
            title=f"Gotowi do Zadania {case_id}?",
            subtitle="Otwórz IDE, pobierz przygotowany branch i rozpocznij ćwiczenie.",
            kicker=f"CASE STUDY {case_id} // HANDS-ON LAB",
            contact="support-lab@ttpsc.pl"
        )
    ]

    html_content = be.wrap_presentation(f"{case_id}: {title} · GitHub Copilot Case", "\n".join(slides))
    with open(os.path.join(OUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  Generated: {filename}")

# ==============================================================================
# TECHNICAL CASES DEFINITIONS (T1 - T9)
# ==============================================================================
cases = [
    {
        "filename": "case-01-failing-test-debug.html",
        "case_id": "T1",
        "title": "Diagnostyka Przyczyny Czerwonego Testu Jednostkowego",
        "situation": {
            "scene": "Wersja Release Candidate prawie gotowa, lecz pojedynczy test zaczął niespodziewanie failować.",
            "pressure": "Pull request czeka na merge przed zaplanowanym oknem wdrożeniowym.",
            "risk": "Zgadnięcie poprawki na ślepo lub wklejenie wrażliwych logów z produkcji do czatu.",
            "goal": "Znalezienie najmniejszego rozstrzygającego sprawdzenia bez zgadywania.",
            "tool": "Copilot Chat wewnątrz IDE ze zanonimizowanym stosem błędów.",
            "standard": "Zweryfikowana hipoteza i powtarzalny test odtwarzający defekt."
        },
        "without_ai": {
            "step1": "Odtworzenie błędu i ręczne przeglądanie 5 warstw stosu wywołań.",
            "step2": "Dodawanie printów i wielokrotne uruchamianie całego zestawu testów.",
            "friction": "Wiele rund prób i błędów przed odróżnieniem objawu od sedna awarii."
        },
        "with_ai": {
            "step1": "Udostępnienie testu, powiązanego kodu i zanonimizowanego fragmentu trace.",
            "step2": "Prośba o 2 konkurencyjne hipotezy i najtańszy test rozstrzygający.",
            "gain": "Zawężenie obszaru poszukiwań do 1 pliku w poniżej 3 minuty."
        },
        "gain": {
            "stat": "-70%",
            "stat_sub": "Czasu diagnozy",
            "title": "Błyskawiczna Izolacja Błędu",
            "desc": "Uczestnik uczy się formułować pytania o najmniejszy test rozstrzygający zamiast pytać o gotowy kod."
        },
        "good_result": "Zreprodukowany błąd, potwierdzona przyczyna źródłowa i ukierunkowany test asercji chroniący przed regresją.",
        "guardrail": "Potwierdź przyczynę bezpośrednio w kodzie; udostępniaj wyłącznie zanonimizowane logi bez danych klientów.",
        "deep_diagram_type": "ishikawa"
    },
    {
        "filename": "case-02-test-quality.html",
        "case_id": "T2",
        "title": "Podnoszenie Jakości i Pokrycia Generowanych Testów",
        "situation": {
            "scene": "Nowa funkcja jest gotowa, lecz zestaw testów pokrywa wyłącznie scenariusz pozytywny (happy path).",
            "pressure": "Wcześniej generowane testy AI przechodziły na zielono, ale pomijały kluczowe wyjątki.",
            "risk": "Fałszywe poczucie bezpieczeństwa i puchnący plik testowy o zerowej wartości weryfikacyjnej.",
            "goal": "Odkrycie nieoczywistych stanów brzegowych i asercji przed merge.",
            "tool": "Copilot Chat w połączeniu z lokalnym runnerem testów (pytest / jest / junit).",
            "standard": "Testy wykrywające rzeczywiste błędy biznesowe."
        },
        "without_ai": {
            "step1": "Ręczne wyobrażanie sobie nietypowych wejść (null, puste listy, timeouty).",
            "step2": "Pisanie powtarzalnego kodu mockującego w konwencji projektu.",
            "friction": "Zmęczenie dewelopera i przeoczenie nieoczywistych kombinacji parametrów."
        },
        "with_ai": {
            "step1": "Podanie funkcji i prośba: 'Zanim napiszesz test, wylistuj 5 brakujących przypadków brzegowych'.",
            "step2": "Krytyczna ocena listy, wybór 3 kluczowych i zlecenie wygenerowania precyzyjnych asercji.",
            "gain": "Wykrycie 2 krytycznych edge-case'ów przed audytem QA."
        },
        "gain": {
            "stat": "+85%",
            "stat_sub": "Wartości testów",
            "title": "Eliminacja Płytkich Testów",
            "desc": "Uczestnik zyskuje nawyk wymagania listy ryzyk przed pozwoleniem asystentowi na pisanie kodu testu."
        },
        "good_result": "Skupione testy sprawdzają rzeczywiste zachowanie, a mutacja warunku w kodzie natychmiast wywołuje czerwony pasek.",
        "guardrail": "Zielony pasek wygenerowanego testu niczego nie dowodzi; zbadaj każdą asercję pod kątem tautologii (np. assert res == res).",
        "deep_diagram_type": "double_diamond"
    },
    {
        "filename": "case-03-code-review.html",
        "case_id": "T3",
        "title": "Sceptyczny Audyt i Przegląd Kodu Wspomaganego AI",
        "situation": {
            "scene": "Pull Request oczekuje na akceptację; autor korzystał z AI i obawia się ukrytych założeń w kodzie.",
            "pressure": "Reviewer ma ograniczony czas i musi skupić się na architekturze i logice, nie formatowaniu.",
            "risk": "Bezrefleksyjne kliknięcie 'Approve' na 300 liniach wygenerowanego kodu.",
            "goal": "Ustrukturyzowany przegląd oparty na faktach i odrzucenie spekulacji.",
            "tool": "Copilot Chat z wczytanym diffem zmian oraz kryteriami z ticketa Jira.",
            "standard": "Znalezienie ukrytych luk bezpieczeństwa i niezgodności kontraktów."
        },
        "without_ai": {
            "step1": "Lektura całego diffa linia po linii z próbą odtworzenia kontekstu w pamięci.",
            "step2": "Zwracanie uwagi na drobne nity stylistyczne zamiast na błędy stanu.",
            "friction": "Wysoki koszt kognitywny i przepuszczanie cichych błędów logicznych."
        },
        "with_ai": {
            "step1": "Dostarczenie diffa i ticketa z poleceniem: 'Wskaż niezgodności z wymaganiami poparte dowodami w plikach'.",
            "step2": "Asystent priorytetyzuje znaleziska; deweloper weryfikuje tylko faktyczne luki.",
            "gain": "Wykrycie ukrytych założeń architektonicznych w 5 minut."
        },
        "gain": {
            "stat": "2.5x",
            "stat_sub": "Głębszy audyt",
            "title": "Skupienie na Sednie Kodu",
            "desc": "Zdolność zadawania pytań o dowody w kodzie zamiast przyjmowania sugestii za pewnik."
        },
        "good_result": "Przejrzana lista uwag o wysokim priorytecie i zweryfikowany diff pozbawiony nierozwiązanych wątpliwości.",
        "guardrail": "Sugestie AI to tropy śledcze, a nie pieczęć zatwierdzenia. Odpowiedzialność za merge zawsze spoczywa na deweloperze.",
        "deep_diagram_type": "vicious_cycle"
    },
    {
        "filename": "case-04-legacy-refactor.html",
        "case_id": "T4",
        "title": "Bezpieczna Migracja i Refaktoryzacja Kodu Legacy",
        "situation": {
            "scene": "Zespół zastępuje przestarzałą bibliotekę własnym wrapperem modułowym w dużej aplikacji.",
            "pressure": "Przeszukanie repozytorium znajduje dziesiątki wywołań o zróżnicowanych zestawach parametrów.",
            "risk": "Globalne 'Find & Replace' grozi regresją, która ujawni się dopiero pod obciążeniem.",
            "goal": "Zaplanowanie i wykonanie migracji w ograniczonych, bezpiecznych plastrach.",
            "tool": "Copilot Chat / Agent mode z precyzyjnymi granicami edycji w obszarze roboczym.",
            "standard": "Pełna kompatybilność wsteczna i 0 zmian w zachowaniu zewnętrznym."
        },
        "without_ai": {
            "step1": "Ręczne przeglądanie każdego wystąpienia i dokumentowanie wariantów w notatniku.",
            "step2": "Pojedyncza modyfikacja i lęk przed naruszeniem nieudokumentowanej logiki.",
            "friction": "Długotrwały, podatny na błędy proces blokujący rozwój nowych funkcji."
        },
        "with_ai": {
            "step1": "Polecenie znalezienia reprezentatywnych wariantów użycia w całym workspace.",
            "step2": "Przygotowanie planu etapowego: refaktor 1 ograniczonego plastra, test, rozszerzenie.",
            "gain": "Bezpieczna migracja 40 wywołań w kontrolowanych krokach."
        },
        "gain": {
            "stat": "-50%",
            "stat_sub": "Ryzyka regresji",
            "title": "Izolowane Plastry Zmian",
            "desc": "Uczestnik uczy się ograniczać zakres zmian asystenta do pojedynczego pliku i weryfikować diff przed kolejnym krokiem."
        },
        "good_result": "Czysty diff migracyjny bez starych wywołań, z zielonymi testami jednostkowymi i zachowanym kontraktem API.",
        "guardrail": "Zweryfikuj semantykę każdego wywołania; nie akceptuj hurtowych zmian w wielu plikach bez inspekcji diffa.",
        "deep_diagram_type": "transformation_bridge"
    },
    {
        "filename": "case-05-slow-sql-optimization.html",
        "case_id": "T5",
        "title": "Optymalizacja Wolnego Zapytania i Zadania Bazy Danych Oracle",
        "situation": {
            "scene": "Cykliczny job bazodanowy Oracle okresowo przekracza dopuszczalne okno czasowe.",
            "pressure": "Zespół posiada treść zapytania i plan wykonania (Explain Plan), lecz brakuje jasnej diagnozy spowolnienia.",
            "risk": "Modyfikacja zapytania bez gwarancji zwrócenia identycznego zbioru wynikowego.",
            "goal": "Przetestowanie hipotez optymalizacyjnych przy 100% zachowaniu ekwiwalencji danych.",
            "tool": "Copilot Chat analizujący zanonimizowany schemat tabel i drzewo planu zapytania.",
            "standard": "Skrócenie czasu wykonania potwierdzone w środowisku testowym."
        },
        "without_ai": {
            "step1": "Manualna analiza setek linii drzewa Explain Plan i próby wymuszenia hintów.",
            "step2": "Metoda prób i błędów na kopii bazy bez jasnej hierarchii podejrzeń.",
            "friction": "Wielogodzinne dochodzenie, dlaczego optymalizator wybrał Full Table Scan."
        },
        "with_ai": {
            "step1": "Wprowadzenie zanonimizowanego SQL i drzewa planu z prośbą o wskazanie wąskich gardeł.",
            "step2": "Otrzymanie 3 hipotez (np. brakujący indeks złożony, nieoptymalny join) wraz z testem ekwiwalencji.",
            "gain": "Sformułowanie zweryfikowanej hipotezy w 15 minut."
        },
        "gain": {
            "stat": "-80%",
            "stat_sub": "Czasu analizy planu",
            "title": "Precyzja Indeksowania",
            "desc": "Uczestnik uczy się dostarczać modelowi metadane i plany wykonania bez ujawniania danych biznesowych."
        },
        "good_result": "Zweryfikowany plan indeksacji lub przepisany SQL dający identyczny wynik przy drastycznie niższym koszcie I/O.",
        "guardrail": "Wykonuj testy wyłącznie na zanonimizowanych danych testowych; udowodnij identyczność wyników testem różnicowym.",
        "deep_diagram_type": "pipeline"
    },
    {
        "filename": "case-06-mockup-to-jira.html",
        "case_id": "T6",
        "title": "Transformacja Makiety UI w Gotowe Zadania Implementacyjne Jira",
        "situation": {
            "scene": "Lider projektu przekazuje makietę ekranu (np. Figma) z jednym ogólnikowym zdaniem opisu.",
            "pressure": "Młodszy programista musi rozpocząć pracę, lecz brakuje obsługi stanów błędów i walidacji pól.",
            "risk": "Ciche zamienienie domysłów dewelopera w nieuzgodnione wymagania biznesowe.",
            "goal": "Podział pracy na zadania UI, API i logikę z jawnym oznaczeniem pytań otwartych.",
            "tool": "GitHub Copilot analizujący zrzut makiety lub opis komponentów interfejsu.",
            "standard": "Kompletne kryteria akceptacji w formacie Given-When-Then."
        },
        "without_ai": {
            "step1": "Ręczne spisywanie kontrolek z makiety i wymyślanie scenariuszy brzegowych.",
            "step2": "Formatowanie opisów zgłoszeń w Jira od zera dla każdego komponentu.",
            "friction": "Pominięcie stanów ładowania, błędów sieciowych i walidacji formularza."
        },
        "with_ai": {
            "step1": "Wprowadzenie makiety z prośbą: 'Stwórz zadania z kryteriami akceptacji i sekcją pytań otwartych'.",
            "step2": "Wygenerowanie spójnego podziału na frontend, backend i stan pusty (empty state).",
            "gain": "Kompletny backlog zadania w 10 minut zamiast 2 godzin."
        },
        "gain": {
            "stat": "4x",
            "stat_sub": "Szybszy backlog",
            "title": "Eliminacja Niedomówień",
            "desc": "Zdolność natychmiastowego wyciągania pytań projektowych przed rozpoczęciem kodowania."
        },
        "good_result": "Przejrzany przez inżyniera zestaw zadań Jira z kryteriami akceptacji i wyeksponowanymi wątpliwościami.",
        "guardrail": "Człowiek rozstrzyga decyzje projektowe i zatwierdza treść w Jira. Copilot nie posiada bezpośredniego dostępu do tworzenia zgłoszeń bez autoryzacji.",
        "deep_diagram_type": "grid_matrix"
    },
    {
        "filename": "case-07-unfamiliar-repo.html",
        "case_id": "T7",
        "title": "Odnajdywanie Reguł Biznesowych w Nowym Repozytorium",
        "situation": {
            "scene": "Dołączasz do nowego projektu; zgłoszenie mówi o odrzucaniu błędnego wejścia, lecz nikt nie pamięta warstwy walidacji.",
            "pressure": "Repozytorium zawiera dziesiątki modułów, serwisów i podobnie nazwanych walidatorów.",
            "risk": "Wdrożenie duplikatu walidacji w złym miejscu architektury i naruszenie separacji warstw.",
            "goal": "Szybka orientacja w ścieżce wykonania przed zaproponowaniem jakiejkolwiek zmiany.",
            "tool": "Copilot Chat operujący na kontekście workspace (@workspace) w IDE.",
            "standard": "Zmapowany graf wywołań i wskazany właściwy punkt wejścia."
        },
        "without_ai": {
            "step1": "Globalne wyszukiwanie ciągów tekstowych i komunikatów o błędach w kodzie.",
            "step2": "Żmudne przechodzenie po referencjach (Go to Definition) w 15 plikach.",
            "friction": "Utrata orientacji w gąszczu abstrakcji i frameworków pośredniczących."
        },
        "with_ai": {
            "step1": "Zapytanie: '@workspace Gdzie w przepływie żądania sprawdzany jest warunek X i jakie testy go chronią?'.",
            "step2": "Asystent wskazuje 2 kluczowe klasy i powiązany plik testowy.",
            "gain": "Dotarcie do źródła reguły w 2 minuty bez pytania innych deweloperów."
        },
        "gain": {
            "stat": "-65%",
            "stat_sub": "Czasu onboardingu",
            "title": "Nawigacja w Repozytorium",
            "desc": "Uczestnik uczy się precyzyjnie odpytywać indeks @workspace o architekturę przepływu."
        },
        "good_result": "Zidentyfikowany punkt wejścia, zrozumiany kontrakt danych i przygotowany ukierunkowany test sprawdzający zachowanie.",
        "guardrail": "Zweryfikuj sugestię w drzewie kodu; indeks AI może pominąć dynamiczne ładowanie zależności lub konfigurację w runtime.",
        "deep_diagram_type": "pipeline"
    },
    {
        "filename": "case-08-technical-to-business-update.html",
        "case_id": "T8",
        "title": "Tłumaczenie Złożonych Zmian Technicznych na Język Biznesowy",
        "situation": {
            "scene": "Rozwiązałeś skomplikowaną awarię asynchronicznego worker'a; PM i Product Owner pytają o status i wpływ.",
            "pressure": "Notatki inżyniera zawierają nazwy wątków, deadlocki i pule połączeń bazy danych.",
            "risk": "Niezrozumienie przez biznes, eskalacja paniki lub zbagatelizowanie konieczności okna serwisowego.",
            "goal": "Przygotowanie zwięzłego podsumowania skupionego na ryzyku, korzyściach i kolejnych krokach.",
            "tool": "Copilot Chat przekształcający techniczny commit log w executive summary.",
            "standard": "Jasna komunikacja bez żargonu przy 100% zgodności merytorycznej."
        },
        "without_ai": {
            "step1": "Mozolne przepisywanie technicznych terminów na język ogólny.",
            "step2": "Dopisywanie wyjaśnień dlaczego naprawa trwała tyle czasu.",
            "friction": "Wyczerpujące redagowanie maila odciągające programistę od kolejnych zadań."
        },
        "with_ai": {
            "step1": "Wklejenie notatek technicznych z poleceniem: 'Przetłumacz na 3 punkty dla Product Ownera: Co się stało, wpływ na klienta, akcja'.",
            "step2": "Błyskawiczne wygenerowanie profesjonalnego, rzeczowego komunikatu.",
            "gain": "Gotowa notatka menedżerska w 3 minuty."
        },
        "gain": {
            "stat": "3x",
            "stat_sub": "Lepsza przejrzystość",
            "title": "Spójność z Biznesem",
            "desc": "Zdolność natychmiastowego generowania raportów biznesowych bezpośrednio ze zmian w kodzie."
        },
        "good_result": "Przejrzysta notatka biznesowa, w której liczby, terminy i ograniczenia są precyzyjnie zachowane i zrozumiałe dla interesariuszy.",
        "guardrail": "Sprawdź, czy asystent nie wygładził komunikatu do poziomu zatajenia realnego ryzyka lub nie obiecał nierealnego terminu.",
        "deep_diagram_type": "split_screen"
    },
    {
        "filename": "case-09-client-restrictions-security.html",
        "case_id": "T9",
        "title": "Praca w Reżimie Ograniczeń Klienta i Ochrona Danych (NDA / MCP)",
        "situation": {
            "scene": "Projekt komercyjny podlega rygorystycznemu NDA; klient blokuje zewnętrzne integracje MCP i przesyłanie kodu.",
            "pressure": "Deweloper chce korzystać z dobrodziejstw AI, lecz nie może naruszyć zasad bezpieczeństwa kontraktu.",
            "risk": "Wyciek własności intelektualnej klienta, incydent bezpieczeństwa lub zerwanie umowy.",
            "goal": "Opanowanie technik pracy w bezpiecznym sandboxie z użyciem danych syntetycznych.",
            "tool": "Lokalne szablony, zanonimizowane ekstrakty problemu i zatwierdzone instrukcje projektowe.",
            "standard": "Zero bajtów poufnych danych poza autoryzowaną granicą."
        },
        "without_ai": {
            "step1": "Całkowita rezygnacja z AI w obawie przed naruszeniem polityk bezpieczeństwa.",
            "step2": "Frustracja z powodu manualnej pracy w projektach objętych klauzulami.",
            "friction": "Brak wypracowanych bezpiecznych wzorców sanitacji i izolacji."
        },
        "with_ai": {
            "step1": "Wyodrębnienie abstrakcyjnego algorytmu na danych zastępczych (mock / dummy data).",
            "step2": "Rozwiązanie problemu w sandboxie i bezpieczne przeniesienie czystej logiki do repozytorium klienta.",
            "gain": "Pełne bezpieczeństwo prawne przy zachowaniu produktywności AI."
        },
        "gain": {
            "stat": "100%",
            "stat_sub": "Zgodności NDA",
            "title": "Bezpieczna Produktywność",
            "desc": "Uczestnik uczy się tworzyć zanonimizowane minimalne przykłady problemu (MRE) z zachowaniem pełnej poufności."
        },
        "good_result": "Zadanie rozwiązane z pomocą asystenta na danych syntetycznych bez wysłania ani jednego wrażliwego rekordu klienta.",
        "guardrail": "Przyjmij zasadę zerowego zaufania: jeśli masz wątpliwość co do klasyfikacji danych, skonsultuj się z Security Officerem projektu.",
        "deep_diagram_type": "grid_matrix"
    }
]

for c in cases:
    generate_case_deck(
        filename=c["filename"],
        case_id=c["case_id"],
        title=c["title"],
        situation=c["situation"],
        without_ai=c["without_ai"],
        with_ai=c["with_ai"],
        gain=c["gain"],
        good_result=c["good_result"],
        guardrail=c["guardrail"],
        deep_diagram_type=c["deep_diagram_type"]
    )

# ==============================================================================
# INDEX.HTML PORTAL FOR TECHNICAL TRAINEE
# ==============================================================================
index_cards_html = """
<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; margin-top: 30px;">
  <a href="00-master-1h-training.html" style="text-decoration: none; color: inherit; grid-column: 1 / -1;">
    <div style="background: linear-gradient(135deg, #2B0D30 0%, #4A1A52 100%); color: #FFFFFF; border-radius: 12px; padding: 28px 32px; box-shadow: 0 6px 20px rgba(43,13,48,0.2); border: 2px solid #D03A8C; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-3px)'" onmouseout="this.style.transform='translateY(0)'">
      <div style="font-size: 11px; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase; color: #D03A8C; margin-bottom: 8px;">★ PREZENTACJA GŁÓWNA // 1-GODZINNY PRZEGLĄD (4 SLAJDY)</div>
      <h2 style="font-size: 26px; font-weight: 800; margin: 0 0 10px; color: #FFFFFF;">00. GitHub Copilot w Inżynierii Oprogramowania: Sesja Wprowadzająca</h2>
      <p style="font-size: 15px; color: #D9D9D9; margin: 0; line-height: 1.45;">Zwięzły 4-slajdowy konspekt wprowadzający do 4-godzinnego warsztatu. Zawiera wyjaśnienie celu szkolenia, zebrane wnioski z ankiety zespołu inżynierów TTPSC, pełną agendę 4-godzinnego warsztatu (3 pętle) oraz kluczowe rezultaty.</p>
    </div>
  </a>
"""

for c in cases:
    index_cards_html += f"""
    <a href="{c['filename']}" style="text-decoration: none; color: inherit;">
      <div style="background: #FFFFFF; border: 1px solid #D9D9D9; border-top: 3px solid #7B2D85; border-radius: 10px; padding: 22px; height: 100%; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 12px rgba(0,0,0,0.03); transition: transform 0.2s, box-shadow 0.2s;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 18px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.03)'">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-size: 12px; font-weight: 800; color: #7B2D85; background: #ECD3ED; padding: 3px 8px; border-radius: 4px;">CASE {c['case_id']}</span>
            <span style="font-size: 11px; font-weight: 700; color: #6B7280; text-transform: uppercase;">LAB DECK</span>
          </div>
          <h3 style="font-size: 17px; font-weight: 700; color: #1F1F1F; margin: 0 0 8px; line-height: 1.3;">{c['title']}</h3>
          <p style="font-size: 13px; color: #475569; margin: 0; line-height: 1.4;">{c['situation']['scene']}</p>
        </div>
        <div style="margin-top: 16px; pt: 12px; border-top: 1px solid #F1F5F9; display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 12px; font-weight: 800; color: #64B237;">{c['gain']['stat']} {c['gain']['stat_sub']}</span>
          <span style="font-size: 12px; font-weight: 700; color: #7B2D85;">Otwórz slajdy →</span>
        </div>
      </div>
    </a>
    """

index_cards_html += "</div>"

portal_html = f"""<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Portal Prezentacji Inżynierskich · GitHub Copilot Training</title>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    body {{
      font-family: 'Montserrat', Arial, sans-serif;
      margin: 0;
      padding: 40px 20px;
      background: #FBF7FB;
      color: #1F1F1F;
    }}
    .container {{
      max-width: 1200px;
      margin: 0 auto;
    }}
    .header {{
      margin-bottom: 24px;
      border-bottom: 1px solid #D9D9D9;
      padding-bottom: 24px;
    }}
    .back-nav {{
      margin-bottom: 16px;
    }}
    .back-nav a {{
      color: #7B2D85;
      text-decoration: none;
      font-size: 13px;
      font-weight: 700;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="back-nav">
      <a href="../index.html">← Powrót do Głównego Portalu Szkolenia</a>
    </div>
    <header class="header">
      <span style="font-size: 12px; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase; color: #7B2D85;">TRANSITION TECHNOLOGIES PSC // TECHNICAL TRACK</span>
      <h1 style="font-size: 36px; font-weight: 800; margin: 8px 0 10px; color: #2B0D30;">Katalog Prezentacji dla Zespołów Inżynieryjnych</h1>
      <p style="font-size: 16px; color: #6B7280; margin: 0; max-width: 800px;">Zestaw interaktywnych prezentacji HTML & SVG dedykowanych inżynierom oprogramowania. Zawiera 1-godzinną sesję wprowadzającą oraz 9 szczegółowych modułów warsztatowych (T1 – T9) zoptymalizowanych do 4-godzinnego szkolenia hands-on.</p>
    </header>

    <div style="background: #FFFFFF; border: 1px solid #D9D9D9; border-radius: 8px; padding: 14px 20px; margin-bottom: 24px; display: flex; flex-wrap: wrap; gap: 20px; font-size: 13px; color: #475569;">
      <div><strong>Skróty klawiszowe w prezentacji:</strong></div>
      <div><kbd style="background:#eee; padding:2px 6px; border-radius:3px;">Spacja / →</kbd> Następny krok/slajd</div>
      <div><kbd style="background:#eee; padding:2px 6px; border-radius:3px;">G / Esc</kbd> Przegląd slajdów (Grid)</div>
      <div><kbd style="background:#eee; padding:2px 6px; border-radius:3px;">Alt + A</kbd> Panel Administratora (Motywy)</div>
      <div><kbd style="background:#eee; padding:2px 6px; border-radius:3px;">H</kbd> Ukryj pasek kontrolek</div>
    </div>

    {index_cards_html}

    <footer style="margin-top: 50px; padding-top: 20px; border-top: 1px solid #D9D9D9; font-size: 12px; color: #6B7280; text-align: center;">
      Transition Technologies PSC · AI Software Engineering Training Suite · 2026
    </footer>
  </div>
</body>
</html>
"""

with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(portal_html)
print("  Generated: index.html (Technical Trainee Portal)")

print("Technical track generated successfully.")
