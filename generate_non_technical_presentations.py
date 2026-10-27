import os
import sys
import build_engine as be

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = "non-technical-trainee"
os.makedirs(OUT_DIR, exist_ok=True)

print(f"Generating human-friendly non-technical presentations in ./{OUT_DIR} ...")

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
# HUMAN-FRIENDLY 4-SLIDE DECK BUILDER FOR NON-TECHNICAL CASES
# ==============================================================================
def generate_human_non_tech_deck(filename, case_id, title, quote_heading, quote_body,
                                 today_title, today_points, ai_title, ai_points,
                                 step1, step2, step3, takeaway,
                                 scenario, prompt, success, trap):
    
    # Slide 1: Hook & "Tak, to ja!"
    s1 = f"""
    <!-- SLIDE 1: ŻYCIOWY PUNKT WYJŚCIA -->
    <div class="slide-container slide-dark" data-title="{case_id}: {title}" data-type="Wprowadzenie">
      <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; max-width: 980px; z-index: 2;">
        <span class="slide-kicker" style="color: #64B237; letter-spacing: 0.12em; margin-bottom: 12px;">{case_id} // MICROSOFT COPILOT DLA BIZNESU</span>
        <h1 style="font-size: 38px; font-weight: 800; line-height: 1.18; color: var(--text-light); margin-bottom: 20px;">{title}</h1>
        
        <div style="background: rgba(255, 255, 255, 0.08); border-left: 4px solid #64B237; border-radius: 0 10px 10px 0; padding: 18px 24px; margin-bottom: 26px;">
          <div style="font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; color: #64B237; margin-bottom: 6px;">
            💬 SYTUACJA Z ŻYCIA: "{quote_heading}"
          </div>
          <p style="font-size: 17px; line-height: 1.48; color: #F1F5F9; margin: 0;">
            {quote_body}
          </p>
        </div>

        <div style="display: flex; gap: 24px; align-items: center; border-top: 1px solid var(--border-dark); padding-top: 18px;">
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Format</span><strong style="font-size: 14px; color: var(--text-light);">12 minut ćwiczenia</strong></div>
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Narzędzie</span><strong style="font-size: 14px; color: #64B237;">Custom Agent / Notebook</strong></div>
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Zasada</span><strong style="font-size: 14px; color: var(--text-light);">Uziemienie i weryfikacja [1]</strong></div>
        </div>
      </div>
      <div class="slide-footer">
        <span style="color: var(--text-light-muted);">TTPSC BUSINESS TRAINING // 2026</span>
        <span style="color: var(--text-light-muted);">Slajd 1 / 4</span>
      </div>
    </div>
    """

    # Slide 2: Contrast (Today vs AI)
    today_li = "".join([f"<li style='margin-bottom: 8px;'>{p}</li>" for p in today_points])
    ai_li = "".join([f"<li style='margin-bottom: 8px;'>{p}</li>" for p in ai_points])
    s2 = f"""
    <!-- SLIDE 2: ZDERZENIE RZECZYWISTOŚCI -->
    <div class="slide-container" data-title="Zderzenie rzeczywistości: Ręczne przeklejanie vs Praca z AI" data-type="Zderzenie">
      <header class="slide-header">
        <span class="slide-kicker">ZDERZENIE RZECZYWISTOŚCI // GDZIE TRACIMY CZAS?</span>
        <h2 class="slide-title">Jak Robisz To Dzisiaj vs. Jak Zrobisz To z Copilotem</h2>
      </header>
      <div class="slide-body" style="justify-content: center;">
        <div style="display: grid; grid-template-columns: 1fr 50px 1fr; gap: 16px; align-items: center; width: 100%;">
          
          <div class="fragment" style="background: #FFF5F5; border: 1.5px solid #FCA5A5; border-radius: 12px; padding: 22px; height: 100%; display: flex; flex-direction: column;">
            <div style="display: inline-block; padding: 4px 10px; background: #FEE2E2; color: #DC2626; font-size: 11px; font-weight: 800; border-radius: 4px; text-transform: uppercase; margin-bottom: 10px; width: fit-content;">
              ❌ DZIŚ: RĘCZNA KATORGA
            </div>
            <h3 style="font-size: 18px; font-weight: 800; color: #991B1B; margin-bottom: 14px;">{today_title}</h3>
            <ul style="margin: 0; padding-left: 18px; font-size: 13.5px; color: #450A0A; line-height: 1.5; display: flex; flex-direction: column; gap: 8px;">
              {today_li}
            </ul>
          </div>

          <div style="display: flex; justify-content: center; align-items: center;">
            <svg viewBox="0 0 50 40" style="width: 44px; height: 34px;">
              <defs>
                <marker id="arrow_n_{case_id}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
                  <polygon points="0 1, 8 4, 0 7" fill="#256654" />
                </marker>
              </defs>
              <line x1="4" y1="20" x2="40" y2="20" stroke="#256654" stroke-width="3" stroke-linecap="round" marker-end="url(#arrow_n_{case_id})" />
            </svg>
          </div>

          <div class="fragment" style="background: #F0FDF4; border: 1.5px solid #86EFAC; border-radius: 12px; padding: 22px; height: 100%; display: flex; flex-direction: column;">
            <div style="display: inline-block; padding: 4px 10px; background: #DCFCE7; color: #16A34A; font-size: 11px; font-weight: 800; border-radius: 4px; text-transform: uppercase; margin-bottom: 10px; width: fit-content;">
              ✅ Z COPILOTEM: SPOKÓJ I DOKŁADNOŚĆ
            </div>
            <h3 style="font-size: 18px; font-weight: 800; color: #14532D; margin-bottom: 14px;">{ai_title}</h3>
            <ul style="margin: 0; padding-left: 18px; font-size: 13.5px; color: #052E16; line-height: 1.5; display: flex; flex-direction: column; gap: 8px;">
              {ai_li}
            </ul>
          </div>

        </div>
      </div>
      <div class="slide-footer">
        <span>KONTRAST // CO ZMIENIAMY</span>
        <span>Slajd 2 / 4</span>
      </div>
    </div>
    """

    # Slide 3: Super-Tool: Custom Agent & Copilot Notebook
    s3 = f"""
    <!-- SLIDE 3: SPOSÓB PRACY: CUSTOM AGENT & COPILOT NOTEBOOK -->
    <div class="slide-container" data-title="Złota zasada: Custom Agent i Copilot Notebook" data-type="Złota Zasada">
      <header class="slide-header">
        <span class="slide-kicker">SPOSÓB PRACY // BEZPIECZEŃSTWO I DUŻY KONTEKST</span>
        <h2 class="slide-title">Koniec z Gubieniem Wątków: Użyj Copilot Notebooka lub Własnego Agenta</h2>
      </header>
      <div class="slide-body" style="justify-content: center;">
        
        <div style="display: grid; grid-template-columns: 1fr 30px 1fr 30px 1fr; align-items: center; width: 100%; margin-bottom: 20px;">
          
          <div class="fragment" style="background: #FFFFFF; border: 1.5px solid var(--border-light); border-top: 4px solid #256654; border-radius: 10px; padding: 18px; height: 100%;">
            <div style="font-size: 11px; font-weight: 800; color: #256654; text-transform: uppercase; margin-bottom: 6px;">KROK 1 · DUŻA PRZESTRZEŃ</div>
            <h4 style="font-size: 16px; font-weight: 800; color: var(--text-dark); margin-bottom: 8px;">Notebook / Własny Agent</h4>
            <p style="font-size: 13px; color: #475569; line-height: 1.45; margin: 0;">{step1}</p>
          </div>

          <div style="display: flex; justify-content: center;">
            <svg viewBox="0 0 30 20" style="width: 24px; height: 16px;">
              <defs><marker id="arr1_n_{case_id}" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0 1, 6 3, 0 5" fill="#256654" /></marker></defs>
              <line x1="2" y1="10" x2="24" y2="10" stroke="#256654" stroke-width="2.5" marker-end="url(#arr1_n_{case_id})" />
            </svg>
          </div>

          <div class="fragment" style="background: #FFFFFF; border: 1.5px solid #256654; border-top: 4px solid #64B237; border-radius: 10px; padding: 18px; height: 100%; box-shadow: 0 4px 12px rgba(37,102,84,0.08);">
            <div style="font-size: 11px; font-weight: 800; color: #256654; text-transform: uppercase; margin-bottom: 6px;">KROK 2 · KONKRETNA TABELA</div>
            <h4 style="font-size: 16px; font-weight: 800; color: var(--text-dark); margin-bottom: 8px;">Wskaż Plik i Kolumny</h4>
            <p style="font-size: 13px; color: #475569; line-height: 1.45; margin: 0;">{step2}</p>
          </div>

          <div style="display: flex; justify-content: center;">
            <svg viewBox="0 0 30 20" style="width: 24px; height: 16px;">
              <defs><marker id="arr2_n_{case_id}" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0 1, 6 3, 0 5" fill="#256654" /></marker></defs>
              <line x1="2" y1="10" x2="24" y2="10" stroke="#256654" stroke-width="2.5" marker-end="url(#arr2_n_{case_id})" />
            </svg>
          </div>

          <div class="fragment" style="background: #FFFFFF; border: 1.5px solid var(--border-light); border-top: 4px solid #0284C7; border-radius: 10px; padding: 18px; height: 100%;">
            <div style="font-size: 11px; font-weight: 800; color: #0284C7; text-transform: uppercase; margin-bottom: 6px;">KROK 3 · REGUŁA PRZYPISU [1]</div>
            <h4 style="font-size: 16px; font-weight: 800; color: var(--text-dark); margin-bottom: 8px;">Sprawdź 1 Liczbę u Źródła</h4>
            <p style="font-size: 13px; color: #475569; line-height: 1.45; margin: 0;">{step3}</p>
          </div>

        </div>

        <div class="fragment" style="background: #E3EFE9; border-left: 4px solid #256654; border-radius: 0 8px 8px 0; padding: 12px 18px; font-size: 13px; color: #1D2B29; line-height: 1.45;">
          💡 <strong>Dlaczego to działa w praktyce?</strong> {takeaway}
        </div>

      </div>
      <div class="slide-footer">
        <span>METODYKA // AGENT & NOTEBOOK</span>
        <span>Slajd 3 / 4</span>
      </div>
    </div>
    """

    # Slide 4: Workshop Exercise
    s4 = f"""
    <!-- SLIDE 4: ĆWICZENIE WARSZTATOWE -->
    <div class="slide-container" data-title="Zadanie warsztatowe: Przetestuj ten workflow" data-type="Warsztat">
      <header class="slide-header">
        <span class="slide-kicker">WARSZTAT HANDS-ON // CZAS NA PRAKTYKĘ (12 MIN)</span>
        <h2 class="slide-title">Twoje Zadanie: Zastosuj Copilota do Swojego Dokumentu</h2>
      </header>
      <div class="slide-body" style="justify-content: center;">
        
        <div style="background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 8px; padding: 12px 18px; margin-bottom: 14px; font-size: 13.5px; color: #334155; line-height: 1.4;">
          <strong>Twoje zadanie:</strong> {scenario}
        </div>

        <div class="fragment" style="background: #0F172A; border-radius: 10px; padding: 16px 20px; margin-bottom: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-size: 11px; font-weight: 800; color: #64B237; letter-spacing: 0.08em; text-transform: uppercase;">
              👉 SKOPIUJ TEN PROMPT I WKLEJ DO COPILOT / NOTEBOOK
            </span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">TRYB: DANE FIRMOWE</span>
          </div>
          <pre style="margin: 0; font-family: 'Consolas', 'Courier New', monospace; font-size: 13px; color: #E2E8F0; line-height: 1.45; white-space: pre-wrap; word-break: break-word;">{prompt}</pre>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
          
          <div class="fragment" style="background: #F0FDF4; border: 1.5px solid #86EFAC; border-radius: 8px; padding: 12px 16px;">
            <span style="font-size: 11px; font-weight: 800; color: #16A34A; text-transform: uppercase; display: block; margin-bottom: 4px;">🎯 Oczekiwany Wynik (Definicja Sukcesu)</span>
            <div style="font-size: 12.5px; color: #14532D; line-height: 1.4;">{success}</div>
          </div>

          <div class="fragment" style="background: #FFF1F2; border: 1.5px solid #FDA4AF; border-radius: 8px; padding: 12px 16px;">
            <span style="font-size: 11px; font-weight: 800; color: #E11D48; text-transform: uppercase; display: block; margin-bottom: 4px;">⚠️ Na Co Uważać (Częsty Błąd)</span>
            <div style="font-size: 12.5px; color: #881337; line-height: 1.4;">{trap}</div>
          </div>

        </div>

      </div>
      <div class="slide-footer">
        <span>PRAKTYKA // ĆWICZENIE WARSZTATOWE</span>
        <span>Slajd 4 / 4</span>
      </div>
    </div>
    """

    deck_html = be.wrap_presentation(f"{case_id}: {title}", f"{s1}\n{s2}\n{s3}\n{s4}")
    with open(os.path.join(OUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(deck_html)
    print(f"  Generated: {filename} (4 human-friendly slides)")

# ==============================================================================
# 9 NON-TECHNICAL CASE DECKS
# ==============================================================================

# N1
generate_human_non_tech_deck(
    filename="case-01-long-agreement-contract.html",
    case_id="CASE N1",
    title="Dostałeś 60 Stron Umowy i Musisz Znać Kary na Jutro Rano",
    quote_heading="Drobny druczek i nocne ślęczenie",
    quote_body="Dostawca przysłał zaktualizowaną umowę ramową na 60 stron. Jutro o 9:00 masz spotkanie z dyrektorem i musisz wiedzieć: kiedy mija termin wypowiedzenia, jakie są kary za opóźnienia i kto odpowiada za awarie. Przeczytanie tego słowo w słowo zajmie 4 godziny.",
    today_title="Przeszukiwanie na oślep (Ctrl+F)",
    today_points=[
        "Wciskasz Ctrl+F i szukasz słów 'kara', 'termin', 'odpowiedzialność'",
        "Przeoczasz kluczowy zapis ukryty w Załączniku nr 4 pod innym sformułowaniem",
        "Wchodzisz na spotkanie z niepewnością i stresem, że czegoś nie doczytałeś"
    ],
    ai_title="Ekstrakcja faktów z odnośnikami do stron",
    ai_points=[
        "Wrzucasz umowę do Copilot Notebook lub Agenta 'Audytor Umów'",
        "Prosisz o tabelę: Zdarzenie, Wartość kary/Termin, Dokładny paragraf i strona",
        "Klikasz przypis [1] i weryfikujesz w 30 sekund kluczowy zapis w tekście"
    ],
    step1="Otwórz Copilot Notebook. Wklej treść lub wskaż plik PDF z umowy z SharePointa — masz tu przestrzeń na długie dokumenty.",
    step2="Zadaj prompt o tabelę z 4 kolumnami: Zdarzenie | Kwota kary | Warunek naliczenia | Numer paragrafu i strony.",
    step3="Zasada Źródła: Kliknij odnośnik [1] przy najwyższej karze i sprawdź, czy w umowie nie ma wyłączenia odpowiedzialności.",
    takeaway="Copilot nie ma zastąpić radcy prawnego — ma oszczędzić Ci 3 godziny żmudnego szukania i wskazać palcem właściwy akapit.",
    scenario="Otwórz załączoną umowę SLA w PDF. Musisz wyciągnąć wszystkie kary umowne i terminy reakcji na zgłoszenia awarii.",
    prompt="""Przeanalizuj załączony dokument umowy SLA.
Zbuduj tabelę z 4 kolumnami:
1. Kategoria ryzyka (Kary umowne, Terminy zgłoszeń, Warunki odstąpienia).
2. Konkretny wymóg / wartość liczbowa.
3. Dokładny numer paragrafu i numer strony w pliku.
4. Potencjalne ryzyko dla naszej firmy w 1 zdaniu.
Nie dopowiadaj informacji spoza załączonego tekstu.""",
    success="Gotowa tabela podsumowująca 60 stron w 2 minuty z precyzyjnymi namiarami na paragrafy i strony.",
    trap="Zaufanie kwocie kary bez kliknięcia w odnośnik i sprawdzenia kontekstu zapisu w oryginalnym dokumencie."
)

# N2
generate_human_non_tech_deck(
    filename="case-02-correspondence-register.html",
    case_id="CASE N2",
    title="W Folderze Leży 30 Pism od Klientów, a Szef Chce Tabelę w Excelu",
    quote_heading="Ręczne przeklepywanie danych",
    quote_body="Co tydzień na SharePoint wpływa kilkadziesiąt pism, aneksów i protokołów. Twój poniedziałek to otwieranie każdego PDF-a po kolei, kopiowanie numeru pisma, daty wpływu, kwoty i wklejanie do tabeli w Excelu. Pół dnia monotonnej, nudnej pracy.",
    today_title="Kopiuj-wklej i literówki",
    today_points=[
        "Ręczne otwieranie każdego pliku, Ctrl+C i Ctrl+V do kolejnych komórek",
        "Literówki w numerach pism i pomyłki w formatach dat, które psują sortowanie",
        "Zmęczenie i frustracja z powodu powtarzalnej pracy mechanicznej"
    ],
    ai_title="Custom Agent skanujący folder SharePoint",
    ai_points=[
        "Podłączasz Custom Agenta w SharePoint bezpośrednio do folderu z pismami",
        "Agent automatycznie czyta zawartość i ekstrahuje metadane do tabeli",
        "Kopiujesz gotową tabelę do Excela w 3 minuty i masz wolny czas na ważne zadania"
    ],
    step1="W SharePoint utwórz prostego Agenta 'Rejestrator Pism' ze wskazanym folderem jako źródłem wiedzy.",
    step2="Zadaj prompt: 'Przejrzyj pliki i stwórz tabelę z kolumnami: Nr pisma, Data, Nadawca, Kwota, Czego dotyczy'.",
    step3="Skopiuj wygenerowaną tabelę do Excela i sprawdź wyrywkowo 2 pozycje u źródła.",
    takeaway="Od powtarzalnego wyciągania danych z dokumentów jest wyspecjalizowany Agent, nie człowiek.",
    scenario="Folder z 5 pismami urzędowymi i ofertami na OneDrive/SharePoint, z których trzeba złożyć rejestr korespondencji.",
    prompt="""Przejrzyj pliki w załączonym folderze.
Wygeneruj tabelę gotową do wklejenia do Excela z kolumnami:
| L.p. | Nazwa pliku | Nadawca | Data pisma | Znak sprawy / Nr | Czego dotyczy (max 10 słów) | Termin odpowiedzi |
Jeśli w dokumencie brak terminu, wpisz 'Brak terminu'.""",
    success="Kompletny rejestr korespondencji gotowy do wklejenia do Excela bez ani jednego ręcznego przepisywania.",
    trap="Wrzucanie do analizy plików z różnych lat bez ograniczenia zakresu dat w folderze."
)

# N3
generate_human_non_tech_deck(
    filename="case-03-source-access-sharepoint.html",
    case_id="CASE N3",
    title="Copilot Podał Ci Odpowiedź, ale Czy Możesz Jej Zaufać Przed Szefem?",
    quote_heading="Zagadka pochodzenia informacji",
    quote_body="Zapytałeś Copilota o firmowe zasady zwrotu kosztów delegacji. Odpowiedział pewnym tonem: 'Limit wynosi 150 zł na dobę'. Idziesz z tym do szefa, a on mówi: 'Skąd to wziąłeś? Te zasady zmieniliśmy 3 lata temu!'. Okazało się, że Copilot zindeksował starą roboczą prezentację ze śmietnika na SharePoincie.",
    today_title="Ślepe zaufanie do odpowiedzi",
    today_points=[
        "Ufasz odpowiedziom z czatu bez sprawdzania, z jakich plików pochodzą",
        "Nie wiesz, czy Copilot czyta aktualną procedurę, czy czyjąś prywatną notatkę",
        "Ryzykujesz wpadkę wizerunkową w rozmowie z zarządem lub klientem"
    ],
    ai_title="Uziemienie (Grounding) i sprawdzanie daty",
    ai_points=[
        "Zawsze sprawdzasz etykiety źródeł pod odpowiedzią (przypisy [1], [2])",
        "Wymuszasz w prompcie: 'Korzystaj wyłącznie z plików w folderze Oficjalne 2026'",
        "Tworzysz Custom Agenta z zawężoną bazą wiedzy, który nie widzi wersji roboczych"
    ],
    step1="Użyj Custom Agenta z przypisanym wyłącznie oficjalnym folderem procedur firmy.",
    step2="W prompcie dopisz: 'Podaj datę ostatniej modyfikacji dokumentu, na który się powołujesz'.",
    step3="Kliknij odnośnik [1] i upewnij się, że dokument nie ma w tytule słowa 'DRAFT' lub 'ARCHIWUM'.",
    takeaway="Copilot wie tylko tyle, do ilu plików masz dostęp. Jeśli na SharePoincie panuje bałagan, Copilot może zacytować starą wersję roboczą.",
    scenario="Pytanie o aktualną procedurę rozliczania delegacji zagranicznych w organizacji.",
    prompt="""Jakie są aktualne zasady rozliczania diet zagranicznych w naszej firmie?
WARUNKI ODPOWIEDZI:
1. Wskaż dokładną nazwę pliku źródłowego i folder, w którym się znajduje.
2. Podaj datę modyfikacji tego dokumentu.
3. Wypisz odpowiedź punktowo z odnośnikami do konkretnych sekcji.
Jeśli masz dostęp do kilku wersji tego samego pliku, użyj wyłącznie najnowszego.""",
    success="Pewność co do źródła i natychmiastowe wykrycie przestarzałych plików w organizacji.",
    trap="Brak weryfikacji daty pliku przy pytaniach o procedury finansowe i prawne."
)

# N4
generate_human_non_tech_deck(
    filename="case-04-weekly-update-drafting.html",
    case_id="CASE N4",
    title="Piątek 15:30, 10 Wątków na Mailu i Musisz Napisać Raport dla Szefa",
    quote_heading="Piątkowa panika raportowa",
    quote_body="Dyrektor oczekuje zwięzłego podsumowania tygodnia: co zrobiliśmy, gdzie stoimy, jakie są ryzyka. Ty masz w głowie chaos: 15 maili od klienta, 8 rozmów na Teamsie i notatki w 3 różnych miejscach. Spędzasz 2 godziny próbując sklecić z tego zgrabny tekst.",
    today_title="Pisanie od zera w stresie",
    today_points=[
        "Próbujesz odtworzyć z pamięci, co działo się we wtorek rano",
        "Piszesz zbyt długi, rozwlekły elaborat, którego nikt z zarządu nie przeczyta",
        "Wychodzisz z pracy po godzinach zmęczony pisaniem sprawozdań"
    ],
    ai_title="Copilot Notebook jako redaktor zarządczy",
    ai_points=[
        "Wklejasz luźne, chaotyczne notatki z całego tygodnia do Copilot Notebooka",
        "Zadajesz prompt o format zarządczy: Sukcesy, Wyzwania/Ryzyka, Decyzje",
        "W 3 minuty otrzymujesz profesjonalną, jednostronicową notatkę gotową do wysłania"
    ],
    step1="Otwórz Copilot Notebook i wklej surowe notatki, fragmenty maili i ustaleń ze spotkań.",
    step2="Zadaj prompt: 'Zamień ten chaos w format dla Dyrektora: 3 sukcesy, 1 główne ryzyko, 1 decyzja do podjęcia'.",
    step3="Przejrzyj szkic w 60 sekund, dopisz jedno kluczowe nazwisko i wyślij gotowy status.",
    takeaway="Notebook pozwala Ci zrzucić surowe myśli bez ładu, a Copilot zamienia je w elegancki format biznesowy.",
    scenario="Mamy 5 luźnych notatek ze spotkań projektowych z tego tygodnia. Trzeba złożyć z tego raport dla Dyrektora.",
    prompt="""Oto moje luźne notatki z minionego tygodnia w projekcie X:
[WKLEJ SWOJE PUNKTY / MAILE]

Zredaguj z tego oficjalny status tygodniowy dla Członka Zarządu:
- Styl: biznesowy, konkretny, bez lania wody.
- Układ: 
  1. Kluczowe Osiągnięcia (max 3 punkty z liczbami).
  2. Zidentyfikowane Ryzyka i Wpływ na Harmonogram.
  3. Decyzje Wymagane od Zarządu (jeśli brak, napisz 'Brak').
Maksymalnie 1 strona A4.""",
    success="Błyskawiczny, profesjonalny raport zarządczy w 4 minuty zamiast 2 godzin ślęczenia.",
    trap="Zostawienie w raporcie żargonu operacyjnego, którego zarząd nie potrzebuje."
)

# N5
generate_human_non_tech_deck(
    filename="case-05-spreadsheet-overdue-analysis.html",
    case_id="CASE N5",
    title="Arkusz na 2000 Wierszy i Strach Przed Formułą WYSZUKAJ.PIONOWO",
    quote_heading="Koszmar tabeli przestawnej",
    quote_body="Dział finansowy przesłał tabelę ze wszystkimi transakcjami z ostatniego kwartału. Musisz znaleźć klientów, którzy zalegają z płatnością powyżej 30 dni, policzyć ile łącznie są nam winni i pogrupować ich według handlowców. Zaczynasz szukać w Google formuł Excela i klniesz na błędy #N/D!.",
    today_title="Ręczne filtrowanie i błędy formuł",
    today_points=[
        "Ręczne filtrowanie i sortowanie kolumn, ryzyko pominięcia ukrytych wierszy",
        "Tracenie godziny na przypomnienie sobie składni skomplikowanych formuł",
        "Ręczne przepisywanie sum na kartkę z ryzykiem błędu rachunkowego"
    ],
    ai_title="Rozmowa z Excelem ludzkim językiem",
    ai_points=[
        "Formatujesz dane jako Tabelę Excel (Ctrl+T) i uruchamiasz Copilota w Excelu",
        "Pytasz po polsku: 'Pokaż sumę zaległości powyżej 30 dni w podziale na opiekuna'",
        "Copilot sam wstawia nową kolumnę z formułą i generuje gotowy wykres"
    ],
    step1="Warunek konieczny: zaznacz dane w Excelu i wciśnij Ctrl+T (Copilot działa tylko na Tabelach Excel).",
    step2="Wpisz polecenie: 'Dodaj kolumnę Dni Spóźnienia i podświetl na czerwono wartości powyżej 30'.",
    step3="Kliknij 'Wstaw tabelę przestawną' wygenerowaną przez Copilota i masz gotowy raport.",
    takeaway="W Excelu nie musisz być programistą formuł. Wystarczy, że wiesz, o jakie zjawisko biznesowe pytasz.",
    scenario="Arkusz z rejestrem faktur i terminami płatności. Chcemy znaleźć największe zaległości.",
    prompt="""W arkuszu faktur:
1. Dodaj nową kolumnę z obliczeniem liczby dni po terminie na dzień dzisiejszy.
2. Wskaż 3 klientów z najwyższą łączną kwotą przeterminowanych należności.
3. Przygotuj tabelę podsumowującą łączną wartość zadłużenia w podziale na kategorie: 
   0-30 dni, 31-60 dni, pow. 60 dni.""",
    success="Zaawansowana analiza finansowa wykonana w 60 sekund bez ręcznego wpisywania formuł.",
    trap="Próba uruchomienia Copilota na zwykłym zakresie komórek zamiast Tabeli Excela (Ctrl+T)."
)

# N6
generate_human_non_tech_deck(
    filename="case-06-meeting-actions-follow-up.html",
    case_id="CASE N6",
    title="Godzinne Spotkanie na Teamsach, 8 Osób i Nikt Nie Wie Co Ma Robić",
    quote_heading="Spotkanie, z którego nic nie wynika",
    quote_body="Właśnie skończył się długi call projektowy. Było dużo dyskusji, padły obietnice i pomysły. Po rozłączeniu każdy wraca do swoich spraw. Za tydzień na kolejnym spotkaniu okazuje się, że nikt niczego nie zrobił, bo 'myślałem, że to miał przygotować Tomek'.",
    today_title="Zgubione ustalenia i brak notatek",
    today_points=[
        "Brak notatek ze spotkania, bo każdy liczył, że ktoś inny zapisuje",
        "Przeglądanie godzinnego nagrania wideo z prędkością 1.5x (strata 40 minut)",
        "Niejasna odpowiedzialność i opóźnienia w realizacji projektu"
    ],
    ai_title="Transkrypcja Teams na listę zadań w 60 sekund",
    ai_points=[
        "Włączona transkrypcja na Teamsach podczas trwania spotkania",
        "Po spotkaniu pytasz Copilota: 'Wypisz listę zadań: Co, Kto i na Kiedy'",
        "Wklejasz tabelę na czat spotkania 60 sekund po zakończeniu rozmowy"
    ],
    step1="Upewnij się, że na początku calla włączono transkrypcję (Teams świetnie radzi sobie z językiem polskim).",
    step2="Po spotkaniu w panelu Copilota kliknij: 'Wygeneruj zadania do wykonania (Action Items)'.",
    step3="Skopiuj tabelę na czat spotkania z dopiskiem: 'Dajcie znać, czy Wasze terminy się zgadzają'.",
    takeaway="Najlepsze spotkanie to takie, które kończy się spisaną listą właścicieli zadań w 2 minuty po callu.",
    scenario="Właśnie zakończone spotkanie projektowe z transkrypcją. Trzeba sporządzić notatkę z decyzjami.",
    prompt="""Na podstawie transkrypcji zakończonego spotkania:
1. Przygotuj tabelę zadań (Action Items):
   | Zadanie | Osoba odpowiedzialna | Zadeklarowany termin |
2. Wypisz 2 najważniejsze decyzje, które zostały podjęte.
3. Wskaż tematy, które pozostały otwarte i wymagają kolejnego spotkania.
Format: krótki post gotowy do wklejenia na kanał Teams.""",
    success="Gotowy, precyzyjny follow-up wysłany do zespołu zanim zdążą zaparzyć kolejną kawę.",
    trap="Zapomnienie o włączeniu transkrypcji przed rozpoczęciem dyskusji."
)

# N7
generate_human_non_tech_deck(
    filename="case-07-report-to-presentation.html",
    case_id="CASE N7",
    title="Raport na 40 Stron, a Szef Mówi: 'Zrób mi z Tego 5 Slajdów na Jutro'",
    quote_heading="Przekształcenie encyklopedii w prezentację",
    quote_body="Dostałeś obszerną analizę rynkową lub raport z wdrożenia w Wordzie. Masz 40 stron gęstego tekstu. Dyrektor mówi: 'Jutro rano mam komitet sterujący, potrzebuję 5 slajdów: problem, liczby, opcje i Twoja rekomendacja'. Otwierasz pusty PowerPoint i ogarnia Cię niemoc.",
    today_title="Ściana tekstu na slajdach",
    today_points=[
        "Kopiujesz całe akapity z Worda i wklejasz je na slajdy małą czcionką",
        "Spędzasz 3 godziny na formatowaniu ramek i dobieraniu kolorów zamiast na treści",
        "Zarząd na spotkaniu czyta slajdy zamiast słuchać Twojej prezentacji"
    ],
    ai_title="Copilot w PowerPoint na podstawie pliku Word",
    ai_points=[
        "Używasz funkcji: 'Utwórz prezentację na podstawie pliku' wskazując plik Worda",
        "Określasz strukturę: dokładnie 5 slajdów według schematu zarządczego",
        "Copilot generuje zwięzłe punkty, a Ty dopracowujesz tylko liczby"
    ],
    step1="W pustym PowerPoint kliknij Copilot -> 'Utwórz prezentację na podstawie pliku' i wskaż raport z OneDrive.",
    step2="Zadaj prompt: 'Przygotuj dokładnie 5 slajdów: Wyzwanie, Dane, 2 Opcje, Rekomendacja, Następne kroki'.",
    step3="Usuń zbędne przymiotniki — zostaw same liczby, fakty i krótkie hasła.",
    takeaway="Slajdy mają być tłem dla Twojej wypowiedzi, a nie kopią dokumentu. Copilot zdejmuje z Ciebie ciężar wstępnego szkicu.",
    scenario="Mamy 40-stronicowy raport z badania satysfakcji klientów. Trzeba przygotować 5 slajdów dla Zarządu.",
    prompt="""Utwórz prezentację na podstawie załączonego pliku Raport_Satysfakcji.docx.
WYTYCZNE DLA COPILOTA:
1. Przygotuj dokładnie 5 slajdów według standardu zarządczego:
   Slajd 1: Tytuł i główny wniosek (Executive Summary)
   Slajd 2: Wyniki liczbowe (NPS, czas obsługi)
   Slajd 3: Główne wąskie gardła zgłaszane przez klientów
   Slajd 4: Dwa warianty usprawnień (Szybkie vs Długoterminowe)
   Slajd 5: Rekomendacja i plan wdrożenia na 30 dni
2. Maksymalnie 3-4 punkty na slajd. Zero ścian tekstu.""",
    success="Gotowy, elegancki szkiet prezentacji z notatkami w 2 minuty.",
    trap="Zostawienie na slajdach długich, wielokrotnie złożonych zdań zamiast zwięzłych haseł i liczb."
)

# N8
generate_human_non_tech_deck(
    filename="case-08-customer-meeting-prep.html",
    case_id="CASE N8",
    title="Za 10 Minut Dzwoni Wściekły Klient, a Ty Nie Pamiętasz Ustaleń",
    quote_heading="Kryzysowa rozmowa z klientem",
    quote_body="Dostajesz powiadomienie z kalendarza: za 10 minut call z kluczowym klientem, który jest niezadowolony z opóźnień. W projekcie wymieniłeś z nim 20 maili w ciągu 2 tygodni. Nie pamiętasz, co mu obiecał kolega, a co zablokował dział prawny. Czujesz, jak rośnie tętno.",
    today_title="Gorączkowe szukanie w Outlooku",
    today_points=[
        "Gorączkowe przeszukiwanie skrzynki Outlooka i otwieranie 15 wątków naraz",
        "Wchodzisz na rozmowę niepewny faktów i dajesz się zepchnąć do defensywy",
        "Obiecujesz coś nierealnego pod presją, bo nie znasz dokładnego stanu ustaleń"
    ],
    ai_title="Podsumowanie wątku w Outlooku w 3 minuty",
    ai_points=[
        "Klikasz 'Podsumowanie przez Copilot' nad długą konwersacją mailową w Outlooku",
        "Pytasz: 'Jakie były ostatnie 3 obietnice złożone klientowi i na co narzekał?'",
        "Wchodzisz na rozmowę opanowany, mając przed sobą chronologiczną ściągę"
    ],
    step1="W Outlooku kliknij 'Podsumowanie przez Copilot' nad wątkiem korespondencji z klientem.",
    step2="Zadaj pytanie: 'Wypisz tabelę: Data | Kto pisał | Co obiecano | Czego klient domaga się teraz'.",
    step3="Wydrukuj lub otwórz ściągę na drugim ekranie i prowadź rozmowę w oparciu o fakty.",
    takeaway="Klient docenia spokój i opanowanie faktów. Zamiast 'wydaje mi się', mówisz '14 października ustaliliśmy, że...'.",
    scenario="Za chwilę dzwoni klient w sprawie reklamacji opóźnionego etapu wdrożenia. Trzeba poznać historię.",
    prompt="""Przeanalizuj załączony wątek korespondencji z klientem Acme Corp.
Przygotuj dla mnie 1-stronicową ściągę przed rozmową:
1. Główny zarzut klienta (w czym tkwi sedno problemu?).
2. Co i kiedy zadeklarowaliśmy w poprzednich mailach (z datami).
3. Gdzie leży przyczyna opóźnienia według naszych ustaleń wewnętrznych.
4. Propozycja 2 bezpiecznych rozwiązań, które mogę zaoferować podczas rozmowy.""",
    success="Błyskawiczne opanowanie sytuacji kryzysowej i wejście na rozmowę z gotowymi opcjami.",
    trap="Przepraszanie klienta bez sprawdzenia, czy opóźnienie nie wynikało z braku decyzji po jego stronie."
)

# N9
generate_human_non_tech_deck(
    filename="case-09-estimating-implementation-work.html",
    case_id="CASE N9",
    title="Klient Napisał: 'Chcemy Prosty Portal, Ile to Potrwa?'",
    quote_heading="Wycena pisana na kolanie",
    quote_body="Dział sprzedaży przesyła maila od potencjalnego klienta: 'Potrzebujemy aplikacji do rezerwacji sal, nic wielkiego, wyceńcie to do jutra'. Wiesz, że 'prosty portal' w głowie klienta oznacza integrację z 3 systemami, płatności online i aplikację mobilną. Jeśli rzucisz liczbę z sufitu — polegniecie na wdrożeniu.",
    today_title="Strzelanie liczbami z sufitu",
    today_points=[
        "Strzelanie w ciemno: 'To zajmie jakieś 2 miesiące', a potem praca po nocach",
        "Pominięcie ukrytych prac: migracja danych, testy bezpieczeństwa, szkolenia",
        "Konflikt z klientem przy pierwszej dodatkowej fakturze za 'rzeczy oczywiste'"
    ],
    ai_title="Custom Agent 'Kalkulator Ofert' i dekompozycja WBS",
    ai_points=[
        "Wrzucasz zapytanie klienta do Copilot Notebook lub Agenta 'Kalkulator Ofert'",
        "Copilot generuje strukturę podziału prac (WBS) na 4 fazy z ukrytymi ryzykami",
        "Generujesz listę 5 kluczowych pytań doprecyzowujących, które chronią firmę"
    ],
    step1="Wklej maila klienta do Copilot Notebooka i poproś o dekompozycję WBS na 4 etapy.",
    step2="Zapytaj Agenta: 'Czego klient nie napisał w mailu, a co będzie konieczne do działania tego systemu?'.",
    step3="Wyślij klientowi wstępne widełki wraz z listą 5 założeń i pytań doprecyzowujących.",
    takeaway="Wycena to nie wróżenie, to zarządzanie ryzykiem. Zadanie dobrych pytań buduje Twój autorytet w oczach klienta.",
    scenario="Krótkie zapytanie ofertowe od klienta na wdrożenie panelu dla partnerów handlowych.",
    prompt="""Oto krótkie zapytanie od klienta:
'Chcemy panel dla naszych 500 dystrybutorów, gdzie będą pobierać faktury i składać zamówienia. Ile to zajmie?'

1. Przygotuj wstępną strukturę podziału prac (WBS) na 4 etapy.
2. Wypisz 4 krytyczne elementy niewspomniane przez klienta (integracja z ERP, RODO, autoryzacja 2FA).
3. Sformułuj 5 profesjonalnych pytań doprecyzowujących do wysłania klientowi przed podaniem ostatecznej kwoty.""",
    success="Profesjonalna, bezpieczna dekompozycja zakresu w 5 minut chroniąca budżet projektu.",
    trap="Podawanie sztywnej kwoty i terminu na podstawie 3 nieprecyzyjnych zdań od klienta."
)

print("\nAll 9 non-technical case presentations successfully generated!")
