import os
import sys
import build_engine as be

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = "non-technical-trainee"
os.makedirs(OUT_DIR, exist_ok=True)

print(f"Generating non-technical presentations in ./{OUT_DIR} ...")

# ==============================================================================
# 00: MASTER PRESENTATION (NON-TECHNICAL TRACK - 3 SLIDES)
# ==============================================================================
non_tech_slide_1 = """
    <!-- SLIDE 1: 10-MINUTOWE WPROWADZENIE W PROSTYM JĘZYKU -->
    <div class="slide-container slide-dark" data-title="Praktyczny Microsoft Copilot: Jak Ułatwić Sobie Codzienną Pracę" data-type="Title">
      <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; max-width: 980px; z-index: 2;">
        <span class="slide-kicker" style="color: #64B237; letter-spacing: 0.12em; margin-bottom: 14px;">TRANSITION TECHNOLOGIES PSC // WARSZTAT DLA ZESPOŁÓW BIZNESOWYCH</span>
        <h1 style="font-size: 44px; font-weight: 800; line-height: 1.15; color: var(--text-light); margin-bottom: 18px;">Praktyczny Microsoft Copilot: Jak Ułatwić Sobie Codzienną Pracę</h1>
        <p style="font-size: 18px; line-height: 1.45; color: var(--text-light-muted); margin-bottom: 24px; max-width: 860px;">10-minutowe wprowadzenie do 4-godzinnego warsztatu. Uczymy się na Waszych codziennych dokumentach, mailach i arkuszach — prosto, bezpiecznie i bez technicznego żargonu.</p>
        
        <!-- WAŻNA UWAGA O NDA I BEZPIECZEŃSTWIE -->
        <div style="background: rgba(100, 178, 55, 0.15); border-left: 4px solid #64B237; border-radius: 0 8px 8px 0; padding: 12px 18px; margin-bottom: 24px; font-size: 13px; color: #FFFFFF; line-height: 1.4;">
          <strong>Ważna informacja organizacyjna:</strong> To szkolenie nie dotyczy umów NDA ani formalnych polityk bezpieczeństwa u konkretnych klientów. Wszelkie pytania i zasady dotyczące dopuszczalności przetwarzania danych w Twoim zespole omawiaj bezpośrednio ze swoim <strong>Managerem</strong>.
        </div>

        <div style="display: flex; gap: 32px; align-items: center; border-top: 1px solid var(--border-dark); padding-top: 18px;">
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Organizacja</span><strong style="font-size: 14px; color: var(--text-light);">Transition Technologies PSC</strong></div>
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Wstęp</span><strong style="font-size: 14px; color: #64B237;">10 minut wprowadzenia</strong></div>
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Forma</span><strong style="font-size: 14px; color: var(--text-light);">4 godziny praktyki na żywo</strong></div>
        </div>
      </div>
      <div class="slide-footer">
        <span style="color: var(--text-light-muted);">TTPSC BUSINESS TRAINING // 2026</span>
        <span style="color: var(--text-light-muted);">Slajd 1</span>
      </div>
    </div>
"""

non_tech_slide_2 = """
    <!-- SLIDE 2: WYNIKI ANKIETY BEZ PRZYCINANIA -->
    <div class="slide-container" data-title="Wyniki ankiety zespołu biznesowego (pełne odpowiedzi)" data-type="Wykres kolumnowy">
      <header class="slide-header">
        <span class="slide-kicker">WYNIKI ANKIETY // ZESPÓŁ BIZNESOWY TTPSC (N=6)</span>
        <h2 class="slide-title">Wszyscy Korzystamy z AI, ale wciąż Ręcznie Przetwarzamy Dane</h2>
      </header>
      <div class="slide-body" style="flex-direction: row; gap: 40px; align-items: center;">
        
        <div style="width: 290px; display: flex; flex-direction: column; justify-content: center; gap: 8px;">
          <div style="font-size: 52px; font-weight: 800; line-height: 1; color: var(--text-dark); letter-spacing: -0.03em;">83%</div>
          <div style="font-size: 15px; color: var(--text-muted);">Używa Copilota codziennie w pracy</div>
          
          <div style="margin-top: 18px; padding: 12px 14px; background: #E3EFE9; border-radius: 8px; border: 1px solid #C9DED1;">
            <div style="font-size: 12px; font-weight: 800; color: #256654; text-transform: uppercase; margin-bottom: 4px;">Główny Potencjał</div>
            <div style="font-size: 12px; color: #1D2B29; line-height: 1.35;">Przejście od prostego pisania maili do automatyzacji arkuszy i analizy umów.</div>
          </div>
        </div>

        <div style="flex: 1; display: flex; flex-direction: column; gap: 9px;">
          
          <div style="display: grid; grid-template-columns: 1fr 90px; gap: 12px; align-items: center; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 14px;">
            <div style="font-size: 13px; font-weight: 700; color: var(--text-dark);">Redagowanie, poprawianie maili i pism (Word / Outlook)</div>
            <div style="font-size: 14px; font-weight: 800; color: #256654; text-align: right;">100% (6/6)</div>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 90px; gap: 12px; align-items: center; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 14px;">
            <div style="font-size: 13px; font-weight: 700; color: var(--text-dark);">Wyszukiwanie informacji i research zamiast wyszukiwarki</div>
            <div style="font-size: 14px; font-weight: 800; color: #256654; text-align: right;">100% (6/6)</div>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 90px; gap: 12px; align-items: center; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 14px;">
            <div style="font-size: 13px; font-weight: 600; color: var(--text-dark);">Podsumowywanie spotkań, transkryptów i długich plików w Teams</div>
            <div style="font-size: 14px; font-weight: 800; color: #256654; text-align: right;">50.0% (3/6)</div>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 90px; gap: 12px; align-items: center; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 14px;">
            <div style="font-size: 13px; font-weight: 600; color: var(--text-dark);">Analiza danych i praca z arkuszami kalkulacyjnymi w Excelu</div>
            <div style="font-size: 14px; font-weight: 800; color: #256654; text-align: right;">50.0% (3/6)</div>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 90px; gap: 12px; align-items: center; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 14px;">
            <div style="font-size: 13px; font-weight: 600; color: var(--text-dark);">Tworzenie zarysów prezentacji i zawartości slajdów w PowerPoint</div>
            <div style="font-size: 14px; font-weight: 800; color: #64748B; text-align: right;">33.3% (2/6)</div>
          </div>

        </div>

      </div>
      <div class="slide-footer">
        <span>DANE EMPIRYCZNE // PEŁNE WYNIKI ANKIETY</span>
        <span>Slajd 2</span>
      </div>
    </div>
"""

non_tech_slide_3 = """
    <!-- SLIDE 3: INTERAKTYWNA ODPOWIEDŹ NA ANKIETĘ Z BEZPOŚREDNIMI LINKAMI DO 9 ĆWICZEŃ -->
    <div class="slide-container" data-title="Odpowiedź na ankietę: Wybierz ćwiczenie (N1-N9)" data-type="Pipeline">
      <header class="slide-header">
        <span class="slide-kicker">PLAN WARSZTATU // KLIKNIJ ĆWICZENIE, ABY OTWORZYĆ PREZENTACJĘ</span>
        <h2 class="slide-title">Trzy Części Warsztatu i Bezpośredni Dostęp do 9 Zadań</h2>
      </header>
      <div class="slide-body" style="justify-content: center;">
        
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 14px;">
          
          <!-- BLOK 1 -->
          <div style="background: var(--bg-white); border: 1.5px solid #256654; border-radius: 10px; padding: 14px 14px 12px; display: flex; flex-direction: column;">
            <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: #256654; margin-bottom: 4px;">Część 1 · Umowy i Pliki</div>
            <h4 style="font-size: 16px; font-weight: 800; color: var(--text-dark); margin-bottom: 10px;">Word & SharePoint</h4>
            
            <div style="display: flex; flex-direction: column; gap: 7px; flex: 1;">
              <a href="case-01-long-agreement-contract.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#E3EFE9'; this.style.borderColor='#256654'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: #256654;">N1 · Zapisy w Umowach ↗</div>
                <div style="font-size: 12px; color: #334155;">Wyciąganie terminów i kar z 60 stron umowy</div>
              </a>

              <a href="case-02-correspondence-register.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#E3EFE9'; this.style.borderColor='#256654'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: #256654;">N2 · Rejestr Pism z SharePoint ↗</div>
                <div style="font-size: 12px; color: #334155;">Automatyczna tabela w Excelu bez przepisywania</div>
              </a>

              <a href="case-03-source-access-sharepoint.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#E3EFE9'; this.style.borderColor='#256654'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: #256654;">N3 · Uprawnienia i Źródła ↗</div>
                <div style="font-size: 12px; color: #334155;">Sprawdzanie do czego Copilot ma faktyczny dostęp</div>
              </a>
            </div>
          </div>

          <!-- BLOK 2 -->
          <div style="background: var(--bg-white); border: 1.5px solid var(--border-light); border-radius: 10px; padding: 14px 14px 12px; display: flex; flex-direction: column;">
            <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: #256654; margin-bottom: 4px;">Część 2 · Raporty i Klienci</div>
            <h4 style="font-size: 16px; font-weight: 800; color: var(--text-dark); margin-bottom: 10px;">Word, PowerPoint, Outlook</h4>
            
            <div style="display: flex; flex-direction: column; gap: 7px; flex: 1;">
              <a href="case-04-weekly-update-drafting.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#E3EFE9'; this.style.borderColor='#256654'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: #256654;">N4 · Raport dla Zarządu ↗</div>
                <div style="font-size: 12px; color: #334155;">Złożenie luźnych notatek w zwięzły status</div>
              </a>

              <a href="case-07-report-to-presentation.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#E3EFE9'; this.style.borderColor='#256654'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: #256654;">N7 · Raport na 5 Slajdów ↗</div>
                <div style="font-size: 12px; color: #334155;">Przekształcenie 40 stron raportu w prezentację</div>
              </a>

              <a href="case-08-customer-meeting-prep.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#E3EFE9'; this.style.borderColor='#256654'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: #256654;">N8 · Rozmowa z Klientem ↗</div>
                <div style="font-size: 12px; color: #334155;">Przygotowanie rozmowy handlowej w 5 minut</div>
              </a>
            </div>
          </div>

          <!-- BLOK 3 -->
          <div style="background: var(--bg-white); border: 1.5px solid var(--border-light); border-radius: 10px; padding: 14px 14px 12px; display: flex; flex-direction: column;">
            <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: #256654; margin-bottom: 4px;">Część 3 · Dane i Zespół</div>
            <h4 style="font-size: 16px; font-weight: 800; color: var(--text-dark); margin-bottom: 10px;">Excel, Teams, Oferty</h4>
            
            <div style="display: flex; flex-direction: column; gap: 7px; flex: 1;">
              <a href="case-05-spreadsheet-overdue-analysis.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#E3EFE9'; this.style.borderColor='#256654'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: #256654;">N5 · Zaległości w Excelu ↗</div>
                <div style="font-size: 12px; color: #334155;">Formuły i wyłapywanie opóźnień w arkuszu</div>
              </a>

              <a href="case-06-meeting-actions-follow-up.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#E3EFE9'; this.style.borderColor='#256654'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: #256654;">N6 · Notatki Teams na Zadania ↗</div>
                <div style="font-size: 12px; color: #334155;">Zamiana nagrania w listę akcji z właścicielami</div>
              </a>

              <a href="case-09-estimating-implementation-work.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#E3EFE9'; this.style.borderColor='#256654'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: #256654;">N9 · Wycena Prac Wdrożeń ↗</div>
                <div style="font-size: 12px; color: #334155;">Wstępna struktura WBS i wyłapywanie ryzyk</div>
              </a>
            </div>
          </div>

        </div>

        <div style="background: #E3EFE9; border-radius: 8px; padding: 10px 16px; font-size: 12px; color: #1D2B29; display: flex; justify-content: space-between; align-items: center;">
          <span>💡 <strong>Nawigacja:</strong> Kliknij dowolne ćwiczenie powyżej, aby od razu otworzyć dedykowaną prezentację danego case'a.</span>
          <span style="font-weight: 700; color: #256654;">9 Gotowych Scenariuszy</span>
        </div>

      </div>
      <div class="slide-footer">
        <span>INTERAKTYWNY KATALOG // WYBIERZ CASE</span>
        <span>Slajd 3</span>
      </div>
    </div>
"""

non_tech_master_html = be.wrap_presentation(
    "Microsoft Copilot · Wprowadzenie do Warsztatu (10 min)",
    f"{non_tech_slide_1}\n{non_tech_slide_2}\n{non_tech_slide_3}"
)
with open(os.path.join(OUT_DIR, "00-master-1h-training.html"), "w", encoding="utf-8") as f:
    f.write(non_tech_master_html)
print("  Generated: 00-master-1h-training.html (3 slides)")

# ==============================================================================
# CASE STUDY GENERATOR HELPER
# ==============================================================================
def generate_case_deck(filename, case_id, title, situation, without_ai, with_ai, gain, good_result, guardrail, deep_diagram_type):
    slides = [
        be.slide_title(
            title=f"{case_id}: {title}",
            kicker="BUSINESS CASE STUDY // MICROSOFT COPILOT",
            subtitle=f"Warsztatowe studium przypadku: od manualnego tarcia do zweryfikowanego rezultatu w M365.",
            meta=f"Scenariusz {case_id} · TTPSC 2026"
        ),

        be.slide_split_screen(
            kicker="SYTUACJA I WYZWANIE // PROBLEM DEFINITION",
            title=f"Kontekst Operacyjny: {title}",
            left_badge="Wyzwanie w Pracy",
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
            title="Ścieżka Tradycyjna vs Praca z Microsoft Copilot",
            left_badge="Bez Wsparcia AI",
            left_title="Przebieg Manualny",
            left_points=[
                f"<strong>Krok 1:</strong> {without_ai['step1']}",
                f"<strong>Krok 2:</strong> {without_ai['step2']}",
                f"<strong>Tarcie:</strong> {without_ai['friction']}"
            ],
            right_badge="Z Microsoft Copilot",
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
            title="Krok po Kroku z Autoryzowanym Zbiorem Danych",
            steps=[
                {"phase": "Krok 1 (10 min)", "title": "Wybór Źródła", "desc": "Wskaż zatwierdzony plik w SharePoint lub załącz przygotowany dokument.", "active": False},
                {"phase": "Krok 2 (15 min)", "title": "Struktura Promptu", "desc": "Sformułuj zapytanie z wymogiem numerów stron i zakazem zmyślania.", "active": True},
                {"phase": "Krok 3 (10 min)", "title": "Weryfikacja Faktów", "desc": "Zweryfikuj każdą datę i kwotę bezpośrednio w pliku bazowym.", "active": True},
                {"phase": "Krok 4 (5 min)", "title": "Decyzja Biznesowa", "desc": "Zatwierdź wersję roboczą notatki, tabeli lub slajdu.", "active": False}
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
            subtitle="Uruchom aplikację M365, otwórz plik ćwiczeniowy i rozpocznij zadanie.",
            kicker=f"CASE STUDY {case_id} // HANDS-ON LAB",
            contact="support-biz@ttpsc.pl"
        )
    ]

    html_content = be.wrap_presentation(f"{case_id}: {title} · Microsoft Copilot Case", "\n".join(slides))
    with open(os.path.join(OUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  Generated: {filename}")

# ==============================================================================
# NON-TECHNICAL CASES DEFINITIONS (N1 - N9)
# ==============================================================================
cases_nt = [
    {
        "filename": "case-01-long-agreement-contract.html",
        "case_id": "N1",
        "title": "Odnajdywanie Kluczowych Zapisów w Długich Umowach Handlowych",
        "situation": {
            "scene": "Przed jutrzejszym spotkaniem z dostawcą musisz ustalić zasady odnowienia umowy, termin wypowiedzenia i wyjątki.",
            "pressure": "Umowa liczy 60 stron prawniczego języka, a kluczowy aneks ukryty jest na końcu dokumentu.",
            "risk": "Tradycyjne wyszukiwanie Ctrl+F może pominąć wyjątek zdefiniowany w innym paragrafie.",
            "goal": "Przygotowanie zestawienia warunków z numerami paragrafów i jawnym wskazaniem niepewności.",
            "tool": "Word Copilot lub Copilot Chat z załączonym autoryzowanym plikiem umowy.",
            "standard": "Zwięzły brief na spotkanie; każda data i warunek zweryfikowane w tekście źródłowym."
        },
        "without_ai": {
            "step1": "Wpisywanie haseł 'wypowiedzenie', 'okres' i czytanie dziesiątek trafień.",
            "step2": "Ręczne kopiowanie fragmentów zdań do roboczego dokumentu OneNote.",
            "friction": "Wieloetapowe kartkowanie i wysokie ryzyko przeoczenia warunku zawieszającego."
        },
        "with_ai": {
            "step1": "Załączenie pliku i precyzyjne pytanie o warunki odnowienia z podaniem numerów sekcji.",
            "step2": "Dopytanie o wyjątki i kary umowne, a następnie zestawienie wyników w 3-kolumnowej tabeli.",
            "gain": "Kompletna analiza warunków w 10 minut zamiast 2 godzin."
        },
        "gain": {
            "stat": "-75%",
            "stat_sub": "Czasu lektury umowy",
            "title": "Precyzja Paragrafowa",
            "desc": "Uczestnik uczy się zmuszać asystenta do podawania numerów stron i sekcji przy każdym wyciągniętym warunku."
        },
        "good_result": "Przejrzysta notatka z potwierdzonymi datami, numerami klauzul i listą pytań prawnych.",
        "guardrail": "Sprawdź dosłowne brzmienie klauzuli w dokumencie. Copilot wspiera lekturę, lecz nie zastępuje opinii działu prawnego.",
        "deep_diagram_type": "split_screen"
    },
    {
        "filename": "case-02-correspondence-register.html",
        "case_id": "N2",
        "title": "Budowa Ustrukturyzowanego Rejestru Pism z Plików SharePoint",
        "situation": {
            "scene": "Koniec miesiąca: zespół musi sporządzić zestawienie wysłanych i odebranych pism urzędowych.",
            "pressure": "Dokumenty znajdują się w folderze SharePoint, lecz brakuje spójnego rejestru w Excelu.",
            "risk": "Błędy w przepisywaniu sygnatur, pomyłki w datach doręczenia i strata całego popołudnia.",
            "goal": "Ekstrakcja kluczowych metadanych (nadawca, data, sygnatura, sprawa) do gotowej tabeli.",
            "tool": "Copilot Chat operujący na pakiecie dokumentów oraz MS Excel.",
            "standard": "Jeden wiersz na dokument, brak zmyślonych pól, jawne flagi 'BRAK DANYCH'."
        },
        "without_ai": {
            "step1": "Otwieranie każdego pliku PDF/Word z osobna i szukanie sygnatury w nagłówku.",
            "step2": "Ręczne wklejanie danych komórka po komórce do arkusza kalkulacyjnego.",
            "friction": "Monotonna, męcząca praca prowadząca do literówek w kluczowych numerach spraw."
        },
        "with_ai": {
            "step1": "Przekazanie partii pism i zlecenie wygenerowania tabeli ze zdefiniowanymi nagłówkami.",
            "step2": "Zastosowanie reguły: 'Jeśli brak sygnatury, wpisz BRAK, nie zgaduj'.",
            "gain": "Wygenerowanie tabeli dla 15 pism w 3 minuty."
        },
        "gain": {
            "stat": "5x",
            "stat_sub": "Szybsza rejestracja",
            "title": "Strukturyzacja Danych",
            "desc": "Zdolność automatycznego przetwarzania niestrukturyzowanych pism w ustandaryzowaną tabelę Excel."
        },
        "good_result": "Arkusz Excel z kompletem wierszy odpowiadających liczbie dokumentów źródłowych, bez zmyślonych wartości.",
        "guardrail": "Zweryfikuj losowo 30% wygenerowanych wierszy z oryginałem. Pamiętaj o używaniu wyłącznie autoryzowanych próbek pism.",
        "deep_diagram_type": "pipeline"
    },
    {
        "filename": "case-03-source-access-sharepoint.html",
        "case_id": "N3",
        "title": "Weryfikacja Uprawnień i Odnajdywanie Właściwego Źródła Wiedzy",
        "situation": {
            "scene": "Współpracownik pyta o aktualną procedurę onboardingu; pliki krążą w SharePoint, mailach i Confluence.",
            "pressure": "Nie wiesz, do których źródeł Copilot ma faktyczny dostęp i która wersja dokumentu jest obowiązująca.",
            "risk": "Podanie nieaktualnych wytycznych sprzed roku lub oparcie się na roboczym szkicu kolegi.",
            "goal": "Nauczenie się sprawdzania uprawnień, źródeł cytowań i ograniczeń integracji Confluence.",
            "tool": "Microsoft 365 Copilot z badaniem linków źródłowych i uprawnień.",
            "standard": "Pewna informacja z jednoznacznym adresem URL do autoryzowanego dokumentu polityki."
        },
        "without_ai": {
            "step1": "Przeszukiwanie każdego portalu osobno (SharePoint, Teams, maile).",
            "step2": "Pytanie na czacie ogólnym: 'Czy ktoś ma najnowszą wersję procedury?'.",
            "friction": "Wielogodzinne oczekiwanie na odpowiedź i chaos informacyjny."
        },
        "with_ai": {
            "step1": "Zapytanie Copilota z wymogiem wskazania daty modyfikacji i ścieżki w SharePoint.",
            "step2": "Weryfikacja zwróconego odnośnika: czy to oficjalna biblioteka HR, czy prywatny OneNote.",
            "gain": "Natychmiastowa identyfikacja oficjalnego źródła prawdy."
        },
        "gain": {
            "stat": "100%",
            "stat_sub": "Pewności źródła",
            "title": "Świadomość Uprawnień",
            "desc": "Uczestnik rozumie, że Copilot widzi wyłącznie pliki dostępne dla jego konta i nie zastępuje braku uprawnień."
        },
        "good_result": "Zweryfikowana aktualna procedura z autoryzowanego źródła lub jasny wniosek, że dany zasób wymaga integracji.",
        "guardrail": "Copilot nie nadaje uprawnień i nie omija zabezpieczeń; jeśli dokument jest poufny, asystent nie ujawni go nieuprawnionym.",
        "deep_diagram_type": "grid_matrix"
    },
    {
        "filename": "case-04-weekly-update-drafting.html",
        "case_id": "N4",
        "title": "Tworzenie Spójnych Raportów Tygodniowych dla Kierownictwa",
        "situation": {
            "scene": "Piątek po południu: Project Lead musi przygotować raport tygodniowy przed komitetem sterującym.",
            "pressure": "Fakty są rozproszone w krótkich notatkach, Jira i statusach Teams; szablon z zeszłego tygodnia jest wzorem.",
            "risk": "Długie formatowanie kradnie czas potrzebny na faktyczne rozwiązywanie problemów projektu.",
            "goal": "Przekształcenie punktowych notatek w profesjonalny, ustrukturyzowany status executive.",
            "tool": "Copilot w Word lub Copilot Chat z wykorzystaniem szablonu raportu.",
            "standard": "Raport gotowy do wysyłki w 10 minut, z widocznymi ryzykami i właścicielami."
        },
        "without_ai": {
            "step1": "Ręczne kopiowanie zdań z komunikatora i układanie ich w spójne akapity.",
            "step2": "Usuwanie powtórzeń, sprawdzanie stylistyki i formatowanie tabel.",
            "friction": "Zmęczenie końcem tygodnia i pominięcie kluczowej informacji o opóźnieniu."
        },
        "with_ai": {
            "step1": "Wklejenie surowych notatek i poprzedniego raportu jako wzorca struktury.",
            "step2": "Polecenie: 'Zachowaj układ, wyodrębnij 3 sukcesy, 2 blokery i oznacz brakujące terminy'.",
            "gain": "Gotowa wersja robocza w zaledwie 2 minuty."
        },
        "gain": {
            "stat": "-70%",
            "stat_sub": "Czasu redagowania",
            "title": "Strukturyzacja Raportu",
            "desc": "Nawyk reużywania promptu strukturalnego, który automatycznie wyłapuje brakujące daty i osoby odpowiedzialne."
        },
        "good_result": "Zwięzły raport odpowiadający standardom zarządu, z precyzyjnie wyeksponowanymi wąskimi gardłami.",
        "guardrail": "Sprawdź każde nazwisko, datę i status zadania. Tylko człowiek decyduje, czy dana informacja nadaje się do publikacji.",
        "deep_diagram_type": "split_screen"
    },
    {
        "filename": "case-05-spreadsheet-overdue-analysis.html",
        "case_id": "N5",
        "title": "Identyfikacja Zaległych Działań i Anomalii w Arkuszach Excel",
        "situation": {
            "scene": "Przed cotygodniowym spotkaniem menedżer pyta o zaległe zadania i osoby za nie odpowiedzialne.",
            "pressure": "Arkusz zawiera setki wierszy, niejednolite formaty dat i puste komórki w kolumnach statusu.",
            "risk": "Błędne filtrowanie ukryje krytyczne opóźnienie lub wygeneruje fałszywy wykres.",
            "goal": "Szybka analiza wyjątków, wygenerowanie formuł sprawdzających i zestawienie wyników.",
            "tool": "Copilot w MS Excel (lub asysta Copilot Chat przy tworzeniu zaawansowanych formuł).",
            "standard": "Zestawienie poparte sprawdzonymi formułami i weryfikacją losowych wierszy."
        },
        "without_ai": {
            "step1": "Próby ręcznego ustawiania skomplikowanych filtrów i tabel przestawnych.",
            "step2": "Pisanie z pamięci formuł WYSZUKAJ.PIONOWO lub ORAZ/JEŻELI z błędami składni.",
            "friction": "Niepewność, czy formuła poprawnie obsłużyła puste komórki i formaty tekstowe."
        },
        "with_ai": {
            "step1": "Polecenie dla Copilot w Excel: 'Zidentyfikuj wiersze przeterminowane i pogrupuj według właścicieli'.",
            "step2": "Alternatywnie w Chat: prośba o dokładną formułę Excel z wyjaśnieniem założeń.",
            "gain": "Bezpieczna analiza dużego zbioru w kilka minut."
        },
        "gain": {
            "stat": "3x",
            "stat_sub": "Szybsza analityka",
            "title": "Formuły Bez Frustracji",
            "desc": "Uczestnik zyskuje umiejętność przekładania pytań biznesowych na sprawdzalne formuły arkusza."
        },
        "good_result": "Podsumowanie zaległości zgodne z ręczną wyrywkową kontrolą, z ujawnionymi brakami w danych wejściowych.",
        "guardrail": "Zweryfikuj logikę dat, filtry i puste komórki. Wygenerowane obliczenia pozostają niepotwierdzone do momentu kontroli człowieka.",
        "deep_diagram_type": "transformation_bridge"
    },
    {
        "filename": "case-06-meeting-actions-follow-up.html",
        "case_id": "N6",
        "title": "Przekształcanie Notatek ze Spotkań Teams w Rejestr Zadań",
        "situation": {
            "scene": "Zakończyło się 90-minutowe spotkanie projektowe; ustalenia znikają w ferworze kolejnych zadań.",
            "pressure": "Uczestnicy wracają do bieżących obowiązków, a nikt nie spisał jednoznacznej listy odpowiedzialności.",
            "risk": "Rozmycie odpowiedzialności, zapomnienie o terminach i konieczność ponownego spotkania.",
            "goal": "Błyskawiczne wyciągnięcie decyzji, właścicieli, terminów i przygotowanie maila z podsumowaniem.",
            "tool": "Copilot w Teams (lub Copilot Chat z wklejonym zanonimizowanym transkryptem).",
            "standard": "Rejestr zadań z podziałem na osoby oraz wersja robocza wiadomości follow-up."
        },
        "without_ai": {
            "step1": "Odsłuchiwanie nagrania lub czytanie 15 stron surowego transkryptu.",
            "step2": "Ręczne wyłapywanie kto co obiecał i spisywanie listy zadań.",
            "friction": "Wyczerpujący proces zajmujący nawet godzinę po każdym ważnym zebraniu."
        },
        "with_ai": {
            "step1": "Polecenie: 'Wyodrębnij podjęte decyzje, przypisz zadania do osób i wskaż sprawy nierozstrzygnięte'.",
            "step2": "Przygotowanie zwięzłego maila podsumowującego w profesjonalnym tonie.",
            "gain": "Kompletne podsumowanie spotkania w 5 minut po zakończeniu."
        },
        "gain": {
            "stat": "-85%",
            "stat_sub": "Czasu na follow-up",
            "title": "Rozliczalność Zespołu",
            "desc": "Zdolność natychmiastowego zamykania spotkań ustrukturyzowanym rejestrem decyzji i terminów."
        },
        "good_result": "Przejrzysty rejestr akcji z przypisanymi właścicielami i terminami, zaakceptowany przez uczestników.",
        "guardrail": "Sprawdź, czy Copilot nie przypisał zadania niewłaściwej osobie na podstawie luźnej dyskusji. Użytkownik decyduje o wysyłce.",
        "deep_diagram_type": "pipeline"
    },
    {
        "filename": "case-07-report-to-presentation.html",
        "case_id": "N7",
        "title": "Skrót 40-Stronicowego Raportu do 5-Slajdowej Prezentacji",
        "situation": {
            "scene": "Jutro komitet sterujący; otrzymałeś 40-stronicowy raport z audytu i musisz zreferować wnioski w 5 slajdach.",
            "pressure": "Zarząd oczekuje wyłącznie kluczowych liczb, ryzyk i rekomendacji decyzyjnych.",
            "risk": "Przeładowanie slajdów ścianami tekstu lub pominięcie zastrzeżenia wpływającego na decyzję.",
            "goal": "Przekształcenie gęstego raportu w zwięzły konspekt narracyjny zgodny ze standardem McKinsey.",
            "tool": "Word / PowerPoint Copilot lub Copilot Chat z analizą dokumentu źródłowego.",
            "standard": "5 slajdów z nagłówkami-wnioskami, wykresem i jasnym wezwaniem do działania (CTA)."
        },
        "without_ai": {
            "step1": "Czytanie całego raportu z zakreślaczem i tworzenie konspektu na kartce.",
            "step2": "Manualne wklejanie fragmentów tekstu do pustych pól tekstowych w PowerPoint.",
            "friction": "Powstanie nudnej prezentacji pełnej bullet-pointów, której nikt nie przeczyta."
        },
        "with_ai": {
            "step1": "Zapytanie: 'Wyciągnij główną tezę, 3 dowody liczbowe, 2 ryzyka i ułóż w konspekt 5 slajdów'.",
            "step2": "Zastosowanie reguły nagłówków-wniosków zamiast tytułów kategorii.",
            "gain": "Gotowa struktura narracyjna prezentacji w 15 minut."
        },
        "gain": {
            "stat": "4x",
            "stat_sub": "Lepszy odbiór zarządu",
            "title": "Synteza Menadżerska",
            "desc": "Uczestnik uczy się destylować obszerne opracowania do formatu decyzji biznesowej popartej danymi."
        },
        "good_result": "5-slajdowy zwięzły deck z jasną tezą, dowodami z raportu i konkretnymi decyzjami do podjęcia.",
        "guardrail": "Zweryfikuj każdą liczbę i wykres z raportem bazowym; usuń wszelkie niepoparte źródłem deklaracje asystenta.",
        "deep_diagram_type": "double_diamond"
    },
    {
        "filename": "case-08-customer-meeting-prep.html",
        "case_id": "N8",
        "title": "Przygotowanie Rzeczowej Rozmowy z Klientem w Trudnej Sytuacji",
        "situation": {
            "scene": "Za 20 minut rozpoczyna się call z kluczowym klientem; nastąpiło opóźnienie w dostawie modułu.",
            "pressure": "Notatki od deweloperów są hermetyczne, a Ty musisz wyjaśnić sytuację bez obiecywania nierealnych terminów.",
            "risk": "Złożenie pochopnej obietnicy pod presją klienta lub zabrzmienie zbyt szorstko i defensywnie.",
            "goal": "Opracowanie spokojnego otwarcia, 3 pytań odkrywających i bezpiecznych ram rozmowy.",
            "tool": "Copilot Chat / Word przekształcający techniczne fakty w dyplomatyczny talk-track.",
            "standard": "Przećwiczona agenda spotkania oparta wyłącznie na potwierdzonych faktach."
        },
        "without_ai": {
            "step1": "Gorączkowe przeglądanie maili i próby ułożenia w głowie planu wypowiedzi.",
            "step2": "Poczucie stresu i ryzyko wejścia w tłumaczenie technicznych szczegółów.",
            "friction": "Prowizoryczne przygotowanie zwiększające napięcie podczas rozmowy."
        },
        "with_ai": {
            "step1": "Wprowadzenie potwierdzonych faktów z poleceniem: 'Przygotuj otwarcie, pytania i listę tematów tabu'.",
            "step2": "Wygenerowanie profesjonalnego scenariusza skupionego na planie naprawczym.",
            "gain": "Spokój i pełna kontrola nad agendą spotkania w 5 minut."
        },
        "gain": {
            "stat": "100%",
            "stat_sub": "Pewności komunikacji",
            "title": "Kontrola Przebiegu",
            "desc": "Zdolność błyskawicznego przygotowania profesjonalnego talk-tracku na trudne rozmowy biznesowe."
        },
        "good_result": "Ustrukturyzowany konspekt rozmowy chroniący relację z klientem i nieujawniający nieautoryzowanych deklaracji.",
        "guardrail": "Nigdy nie pozwalaj modelowi wymyślać nowych dat dostawy. Trzymaj się wyłącznie faktów zatwierdzonych przez zespół.",
        "deep_diagram_type": "split_screen"
    },
    {
        "filename": "case-09-estimating-implementation-work.html",
        "case_id": "N9",
        "title": "Szacowanie Nakładu Prac Wdrożeniowych i Migracyjnych z AI",
        "situation": {
            "scene": "Klient pyta o wstępną wycenę migracji systemu; zakres obejmuje 4 moduły i integrację bazodanową.",
            "pressure": "Potrzebujesz wstępnego rozbicia struktury prac (WBS), aby przedyskutować estymacje z architektem.",
            "risk": "Pominięcie ukrytych prac (migracja danych, testy UAT, szkolenia) i niedoszacowanie budżetu.",
            "goal": "Błyskawiczne przygotowanie szablonu dekompozycji prac wraz z listą ryzyk projektowych.",
            "tool": "Copilot Chat / Excel generujący tabelę WBS na bazie zakresu oferty.",
            "standard": "Szkic struktury zadań z jawnymi założeniami wyceny i buforem niepewności."
        },
        "without_ai": {
            "step1": "Szukanie starych ofert w folderach i ręczne kopiowanie tabel kosztorysowych.",
            "step2": "Próby przypomnienia sobie wszystkich faz wdrożenia od zera.",
            "friction": "Długotrwały proces i ryzyko pominięcia fazy testów bezpieczeństwa."
        },
        "with_ai": {
            "step1": "Wklejenie opisu zakresu z poleceniem: 'Zbuduj strukturę WBS w 4 fazach, wskaż 5 ryzyk i założenia'.",
            "step2": "Otrzymanie kompletnej matrycy prac gotowej do weryfikacji przez Tech Leada.",
            "gain": "Wstępna struktura oferty w 10 minut zamiast 3 godzin."
        },
        "gain": {
            "stat": "-70%",
            "stat_sub": "Czasu tworzenia WBS",
            "title": "Kompletność Oferty",
            "desc": "Uczestnik uczy się wykorzystywać asystenta jako partnera do wyłapywania ukrytych faz wdrożenia."
        },
        "good_result": "Przejrzysta tabela dekompozycji zadań z wyodrębnionymi założeniami i buforami ryzyka.",
        "guardrail": "Ostateczne roboczogodziny i stawki zawsze ustala wykwalifikowany inżynier i kierownik projektu. AI przygotowuje jedynie strukturę.",
        "deep_diagram_type": "grid_matrix"
    }
]

for c in cases_nt:
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
# INDEX.HTML PORTAL FOR NON-TECHNICAL TRAINEE
# ==============================================================================
index_cards_html = """
<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; margin-top: 30px;">
  <a href="00-master-1h-training.html" style="text-decoration: none; color: inherit; grid-column: 1 / -1;">
    <div style="background: linear-gradient(135deg, #2B0D30 0%, #4A1A52 100%); color: #FFFFFF; border-radius: 12px; padding: 28px 32px; box-shadow: 0 6px 20px rgba(43,13,48,0.2); border: 2px solid #D03A8C; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-3px)'" onmouseout="this.style.transform='translateY(0)'">
      <div style="font-size: 11px; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase; color: #D03A8C; margin-bottom: 8px;">★ WPROWADZENIE // 10 MINUT (3 SLAJDY W PROSTYM JĘZYKU)</div>
      <h2 style="font-size: 26px; font-weight: 800; margin: 0 0 10px; color: #FFFFFF;">00. Microsoft Copilot w Pracy Biznesowej: Jak Ułatwić Sobie Codzienną Pracę</h2>
      <p style="font-size: 15px; color: #D9D9D9; margin: 0; line-height: 1.45;">Krótkie 10-minutowe otwarcie warsztatu w prostym języku. Wyjaśnia cel szkolenia, pokazuje wyniki ankiety zespołu biznesowego TTPSC oraz przedstawia 3 praktyczne zadania warsztatowe odpowiadające bezpośrednio na Wasze potrzeby.</p>
    </div>
  </a>
"""

for c in cases_nt:
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
  <title>Portal Prezentacji Biznesowych · Microsoft Copilot Training</title>
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
      <span style="font-size: 12px; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase; color: #7B2D85;">TRANSITION TECHNOLOGIES PSC // BUSINESS TRACK</span>
      <h1 style="font-size: 36px; font-weight: 800; margin: 8px 0 10px; color: #2B0D30;">Katalog Prezentacji dla Zespołów Biznesowych</h1>
      <p style="font-size: 16px; color: #6B7280; margin: 0; max-width: 800px;">Zestaw interaktywnych prezentacji HTML & SVG dedykowanych specjalistom biznesowym, PM, analitykom i liderom. Zawiera 1-godzinną sesję wprowadzającą oraz 9 praktycznych modułów warsztatowych (N1 – N9) zoptymalizowanych do 4-godzinnego szkolenia w ekosystemie Microsoft 365.</p>
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
      Transition Technologies PSC · Microsoft 365 Copilot Training Suite · 2026
    </footer>
  </div>
</body>
</html>
"""

with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(portal_html)
print("  Generated: index.html (Non-Technical Trainee Portal)")

print("Non-technical track generated successfully.")
