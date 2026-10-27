import os
import sys
import build_engine as be

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = "technical-trainee"
os.makedirs(OUT_DIR, exist_ok=True)

print(f"Generating human-friendly technical presentations in ./{OUT_DIR} ...")

# ==============================================================================
# 00: MASTER PRESENTATION (TECHNICAL TRACK - 3 SLIDES)
# ==============================================================================
tech_slide_1 = """
    <!-- SLIDE 1: 10-MINUTOWE WPROWADZENIE W PROSTYM JĘZYKU -->
    <div class="slide-container slide-dark" data-title="Praktyczny GitHub Copilot: Narzędzia w Rękach Dewelopera" data-type="Title">
      <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; max-width: 980px; z-index: 2;">
        <span class="slide-kicker" style="color: var(--accent); letter-spacing: 0.12em; margin-bottom: 14px;">TRANSITION TECHNOLOGIES PSC // WARSZTAT DLA PROGRAMISTÓW</span>
        <h1 style="font-size: 44px; font-weight: 800; line-height: 1.15; color: var(--text-light); margin-bottom: 18px;">Praktyczny GitHub Copilot: Narzędzia w Rękach Dewelopera</h1>
        <p style="font-size: 18px; line-height: 1.45; color: var(--text-light-muted); margin-bottom: 24px; max-width: 860px;">10-minutowe wprowadzenie do 4-godzinnego warsztatu praktycznego. Uczymy się pisać wartościowe testy, bezpiecznie badać błędy i zamykać zadania z konsoli bez zgadywania.</p>
        
        <!-- WAŻNA UWAGA O NDA I BEZPIECZEŃSTWIE -->
        <div style="background: rgba(225, 29, 72, 0.15); border-left: 4px solid var(--accent); border-radius: 0 8px 8px 0; padding: 12px 18px; margin-bottom: 24px; font-size: 13px; color: #FFFFFF; line-height: 1.4;">
          <strong>Ważna informacja organizacyjna:</strong> To szkolenie techniczne nie dotyczy umów NDA, audytów prawnych ani formalnych polityk bezpieczeństwa u konkretnych klientów. Wszelkie pytania i zasady dotyczące dopuszczenia narzędzi AI w Twoim projekcie omawiaj bezpośrednio ze swoim <strong>Managerem Projektu</strong>.
        </div>

        <div style="display: flex; gap: 32px; align-items: center; border-top: 1px solid var(--border-dark); padding-top: 18px;">
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Organizacja</span><strong style="font-size: 14px; color: var(--text-light);">Transition Technologies PSC</strong></div>
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Wstęp</span><strong style="font-size: 14px; color: var(--accent);">10 minut wprowadzenia</strong></div>
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Forma</span><strong style="font-size: 14px; color: var(--text-light);">4 godziny praktyki w IDE i konsoli</strong></div>
        </div>
      </div>
      <div class="slide-footer">
        <span style="color: var(--text-light-muted);">TTPSC TECHNICAL TRAINING // 2026</span>
        <span style="color: var(--text-light-muted);">Slajd 1</span>
      </div>
    </div>
"""

tech_slide_2 = """
    <!-- SLIDE 2: PEŁNE ODPOWIEDZI Z ANKIETY BEZ PRZYCINANIA (...) -->
    <div class="slide-container" data-title="Wyniki ankiety zespołu inżynierów (pełne odpowiedzi)" data-type="Ranking słupkowy">
      <header class="slide-header">
        <span class="slide-kicker">DIAGNOZA ZESPOŁU // ANKIETA PROGRAMISTÓW TTPSC (N=8)</span>
        <h2 class="slide-title">100% Używa Copilota, ale 38% Traci Czas na Poprawki Kodu AI</h2>
      </header>
      <div class="slide-body">
        <div style="display: grid; grid-template-columns: 1fr 280px; gap: 24px; align-items: center;">
          
          <!-- LISTA W PEŁNYM BRZMIENIU BEZ UCIĘĆ -->
          <div style="display: flex; flex-direction: column; gap: 10px;">
            
            <div style="display: grid; grid-template-columns: 1fr 100px; gap: 12px; align-items: center; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 14px;">
              <div style="font-size: 13px; font-weight: 700; color: var(--text-dark); line-height: 1.3;">Aktywne korzystanie z GitHub Copilot lub Copilot Chat w IDE</div>
              <div style="font-size: 14px; font-weight: 800; color: var(--primary); text-align: right;">100% (8/8)</div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 100px; gap: 12px; align-items: center; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 14px;">
              <div style="font-size: 13px; font-weight: 600; color: var(--text-dark); line-height: 1.3;">Przyspieszanie pisania kodu powtarzalnego (boilerplate) i uzupełnianie składni</div>
              <div style="font-size: 14px; font-weight: 800; color: var(--primary); text-align: right;">62.5% (5/8)</div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 100px; gap: 12px; align-items: center; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 14px;">
              <div style="font-size: 13px; font-weight: 600; color: var(--text-dark); line-height: 1.3;">Szukanie przyczyn błędów, analiza długich stack trace i debugowanie</div>
              <div style="font-size: 14px; font-weight: 800; color: var(--primary); text-align: right;">62.5% (5/8)</div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 100px; gap: 12px; align-items: center; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 14px;">
              <div style="font-size: 13px; font-weight: 600; color: var(--text-dark); line-height: 1.3;">Tworzenie dokumentacji technicznej, opisów Pull Requestów i dokumentów RFC</div>
              <div style="font-size: 14px; font-weight: 800; color: var(--primary); text-align: right;">50.0% (4/8)</div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 100px; gap: 12px; align-items: center; background: #FFF1F2; border: 1.5px solid var(--danger); border-radius: 6px; padding: 8px 14px;">
              <div style="font-size: 13px; font-weight: 700; color: var(--danger); line-height: 1.3;">Wpływ neutralny: czas poświęcony na review i poprawki kodu AI = czas pisania</div>
              <div style="font-size: 14px; font-weight: 800; color: var(--danger); text-align: right;">37.5% (3/8)</div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 100px; gap: 12px; align-items: center; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 14px;">
              <div style="font-size: 13px; font-weight: 600; color: var(--text-dark); line-height: 1.3;">Brak zespołowych reguł i instrukcji (.cursorrules, skille, prompt guidelines)</div>
              <div style="font-size: 14px; font-weight: 800; color: #64748B; text-align: right;">75.0% (6/8)</div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 100px; gap: 12px; align-items: center; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 14px;">
              <div style="font-size: 13px; font-weight: 600; color: var(--text-dark); line-height: 1.3;">Wykorzystywanie AI do pisania pełnych zestawów testów jednostkowych</div>
              <div style="font-size: 14px; font-weight: 800; color: #64748B; text-align: right;">12.5% (1/8)</div>
            </div>

          </div>

          <!-- KARTA WNIOSKU Z ANKIETY -->
          <div class="fragment" style="background: var(--bg-white); border: 2px solid var(--primary); border-radius: 12px; padding: 22px; text-align: center; box-shadow: 0 4px 16px rgba(123,45,133,0.08);">
            <span style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--primary); display: block; margin-bottom: 6px;">Kluczowy Wniosek z Ankiety</span>
            <div style="font-size: 44px; font-weight: 900; color: var(--primary); line-height: 1.1; margin-bottom: 8px;">38%</div>
            <p style="font-size: 13px; color: #475569; margin: 0 0 14px; line-height: 1.45;">Programistów nie zyskuje czasu, dopóki nie wprowadzi specyfikacji przed kodem i krytycznej weryfikacji asercji.</p>
            <div style="background: var(--primary-light); color: var(--primary); font-size: 12px; font-weight: 700; padding: 6px 10px; border-radius: 6px;">
              Cel: Przejście do kontrolowanej pętli inżynierskiej
            </div>
          </div>

        </div>
      </div>
      <div class="slide-footer">
        <span>DANE EMPIRYCZNE // PEŁNE WYNIKI ANKIETY</span>
        <span>Slajd 2</span>
      </div>
    </div>
"""

tech_slide_3 = """
    <!-- SLIDE 3: INTERAKTYWNA AGENDA Z BEZPOŚREDNIMI LINKAMI DO 9 ĆWICZEŃ -->
    <div class="slide-container" data-title="Plan warsztatu: Wybierz ćwiczenie (T1-T9)" data-type="Pipeline">
      <header class="slide-header">
        <span class="slide-kicker">PLAN WARSZTATU // KLIKNIJ ĆWICZENIE, ABY OTWORZYĆ PREZENTACJĘ</span>
        <h2 class="slide-title">Trzy Części Warsztatu i Bezpośredni Dostęp do 9 Zadań</h2>
      </header>
      <div class="slide-body" style="justify-content: center;">
        
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 14px;">
          
          <!-- BLOK 1 -->
          <div style="background: var(--bg-white); border: 1.5px solid var(--primary); border-radius: 10px; padding: 14px 14px 12px; display: flex; flex-direction: column;">
            <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--primary); margin-bottom: 4px;">Część 1 · 00:10–01:12</div>
            <h4 style="font-size: 16px; font-weight: 800; color: var(--text-dark); margin-bottom: 10px;">Diagnostyka & Testy w IDE</h4>
            
            <div style="display: flex; flex-direction: column; gap: 7px; flex: 1;">
              <a href="case-01-failing-test-debug.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#ECD3ED'; this.style.borderColor='#7B2D85'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: var(--primary);">T1 · Diagnostyka Testu ↗</div>
                <div style="font-size: 12px; color: #334155;">Izolacja błędu w stack trace bez zgadywania</div>
              </a>

              <a href="case-02-test-quality.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#ECD3ED'; this.style.borderColor='#7B2D85'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: var(--primary);">T2 · Jakość Testów ↗</div>
                <div style="font-size: 12px; color: #334155;">Wykrywanie pozornych testów i stanów brzegowych</div>
              </a>

              <a href="case-04-legacy-refactor.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#ECD3ED'; this.style.borderColor='#7B2D85'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: var(--primary);">T4 · Migracja Legacy ↗</div>
                <div style="font-size: 12px; color: #334155;">Wymiana wywołań w małych plastrach kodu</div>
              </a>
            </div>
          </div>

          <!-- BLOK 2 -->
          <div style="background: var(--bg-white); border: 1.5px solid var(--border-light); border-radius: 10px; padding: 14px 14px 12px; display: flex; flex-direction: column;">
            <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--primary); margin-bottom: 4px;">Część 2 · 01:22–02:24</div>
            <h4 style="font-size: 16px; font-weight: 800; color: var(--text-dark); margin-bottom: 10px;">Konsola CLI & Narzędzia</h4>
            
            <div style="display: flex; flex-direction: column; gap: 7px; flex: 1;">
              <a href="case-05-slow-sql-optimization.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#ECD3ED'; this.style.borderColor='#7B2D85'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: var(--primary);">T5 · Optymalizacja Oracle SQL ↗</div>
                <div style="font-size: 12px; color: #334155;">Analiza planu zapytania i test ekwiwalencji</div>
              </a>

              <a href="case-06-mockup-to-jira.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#ECD3ED'; this.style.borderColor='#7B2D85'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: var(--primary);">T6 · Makieta na Zadania Jira ↗</div>
                <div style="font-size: 12px; color: #334155;">Dekompozycja ekranu na zadania z kryteriami</div>
              </a>

              <a href="case-07-unfamiliar-repo.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#ECD3ED'; this.style.borderColor='#7B2D85'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: var(--primary);">T7 · Nowe Repozytorium ↗</div>
                <div style="font-size: 12px; color: #334155;">Nawigacja w kodzie z kontekstem @workspace</div>
              </a>
            </div>
          </div>

          <!-- BLOK 3 -->
          <div style="background: var(--bg-white); border: 1.5px solid var(--border-light); border-radius: 10px; padding: 14px 14px 12px; display: flex; flex-direction: column;">
            <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--primary); margin-bottom: 4px;">Część 3 · 02:34–04:00</div>
            <h4 style="font-size: 16px; font-weight: 800; color: var(--text-dark); margin-bottom: 10px;">Audyt Kodu & Komunikacja</h4>
            
            <div style="display: flex; flex-direction: column; gap: 7px; flex: 1;">
              <a href="case-03-code-review.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#ECD3ED'; this.style.borderColor='#7B2D85'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: var(--primary);">T3 · Sceptyczny Audyt PR ↗</div>
                <div style="font-size: 12px; color: #334155;">Sprawdzanie kodu AI jak sceptyk przed merge</div>
              </a>

              <a href="case-08-technical-to-business-update.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#ECD3ED'; this.style.borderColor='#7B2D85'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: var(--primary);">T8 · Notatka dla Biznesu ↗</div>
                <div style="font-size: 12px; color: #334155;">Tłumaczenie zmian technicznych na język PO</div>
              </a>

              <a href="case-09-client-restrictions-security.html" style="text-decoration: none; display: block; background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 6px; padding: 8px 10px; transition: all 0.2s;" onmouseover="this.style.background='#ECD3ED'; this.style.borderColor='#7B2D85'" onmouseout="this.style.background='#F8FAFC'; this.style.borderColor='#D9D9D9'">
                <div style="font-size: 11px; font-weight: 800; color: var(--primary);">T9 · Bezpieczny Sandbox ↗</div>
                <div style="font-size: 12px; color: #334155;">Praca na danych syntetycznych w izolacji</div>
              </a>
            </div>
          </div>

        </div>

        <div style="background: #F1F5F9; border-radius: 8px; padding: 10px 16px; font-size: 12px; color: #475569; display: flex; justify-content: space-between; align-items: center;">
          <span>💡 <strong>Nawigacja:</strong> Kliknij dowolne ćwiczenie powyżej, aby od razu otworzyć dedykowaną prezentację danego case'a.</span>
          <span style="font-weight: 700; color: var(--primary);">9 Gotowych Scenariuszy</span>
        </div>

      </div>
      <div class="slide-footer">
        <span>INTERAKTYWNY KATALOG // WYBIERZ CASE</span>
        <span>Slajd 3</span>
      </div>
    </div>
"""

tech_master_html = be.wrap_presentation(
    "GitHub Copilot · Wprowadzenie do Warsztatu (10 min)",
    f"{tech_slide_1}\n{tech_slide_2}\n{tech_slide_3}"
)
with open(os.path.join(OUT_DIR, "00-master-1h-training.html"), "w", encoding="utf-8") as f:
    f.write(tech_master_html)
print("  Generated: 00-master-1h-training.html (3 slides)")

# ==============================================================================
# HUMAN-FRIENDLY 4-SLIDE DECK BUILDER FOR TECHNICAL CASES
# ==============================================================================
def generate_human_tech_deck(filename, case_id, title, quote_heading, quote_body,
                             today_title, today_points, ai_title, ai_points,
                             step1, step2, step3, takeaway,
                             scenario, prompt, success, trap):
    
    # Slide 1: Hook & "Tak, to ja!"
    s1 = f"""
    <!-- SLIDE 1: ŻYCIOWY PUNKT WYJŚCIA -->
    <div class="slide-container slide-dark" data-title="{case_id}: {title}" data-type="Wprowadzenie">
      <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; max-width: 980px; z-index: 2;">
        <span class="slide-kicker" style="color: var(--accent); letter-spacing: 0.12em; margin-bottom: 12px;">{case_id} // GITHUB COPILOT W PRAKTYCE</span>
        <h1 style="font-size: 38px; font-weight: 800; line-height: 1.18; color: var(--text-light); margin-bottom: 20px;">{title}</h1>
        
        <div style="background: rgba(255, 255, 255, 0.08); border-left: 4px solid var(--accent); border-radius: 0 10px 10px 0; padding: 18px 24px; margin-bottom: 26px;">
          <div style="font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; color: var(--accent); margin-bottom: 6px;">
            💬 SYTUACJA Z ŻYCIA: "{quote_heading}"
          </div>
          <p style="font-size: 17px; line-height: 1.48; color: #F1F5F9; margin: 0;">
            {quote_body}
          </p>
        </div>

        <div style="display: flex; gap: 24px; align-items: center; border-top: 1px solid var(--border-dark); padding-top: 18px;">
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Format</span><strong style="font-size: 14px; color: var(--text-light);">12 minut ćwiczenia</strong></div>
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Złota Zasada</span><strong style="font-size: 14px; color: var(--accent);">Najpierw PLAN, potem KOD</strong></div>
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Cel</span><strong style="font-size: 14px; color: var(--text-light);">Czysty kod bez zgadywania</strong></div>
        </div>
      </div>
      <div class="slide-footer">
        <span style="color: var(--text-light-muted);">TTPSC TECHNICAL TRAINING // 2026</span>
        <span style="color: var(--text-light-muted);">Slajd 1 / 4</span>
      </div>
    </div>
    """

    # Slide 2: Contrast (Today vs AI)
    today_li = "".join([f"<li style='margin-bottom: 8px;'>{p}</li>" for p in today_points])
    ai_li = "".join([f"<li style='margin-bottom: 8px;'>{p}</li>" for p in ai_points])
    s2 = f"""
    <!-- SLIDE 2: ZDERZENIE RZECZYWISTOŚCI -->
    <div class="slide-container" data-title="Zderzenie rzeczywistości: Jak robisz to dziś vs z AI" data-type="Zderzenie">
      <header class="slide-header">
        <span class="slide-kicker">ZDERZENIE RZECZYWISTOŚCI // GDZIE TRACIMY CZAS?</span>
        <h2 class="slide-title">Jak Robisz To Dzisiaj vs. Jak Zrobisz To z Copilotem</h2>
      </header>
      <div class="slide-body" style="justify-content: center;">
        <div style="display: grid; grid-template-columns: 1fr 50px 1fr; gap: 16px; align-items: center; width: 100%;">
          
          <div class="fragment" style="background: #FFF5F5; border: 1.5px solid #FCA5A5; border-radius: 12px; padding: 22px; height: 100%; display: flex; flex-direction: column;">
            <div style="display: inline-block; padding: 4px 10px; background: #FEE2E2; color: #DC2626; font-size: 11px; font-weight: 800; border-radius: 4px; text-transform: uppercase; margin-bottom: 10px; width: fit-content;">
              ❌ DZIŚ: FRUSTRACJA I CHAOS
            </div>
            <h3 style="font-size: 18px; font-weight: 800; color: #991B1B; margin-bottom: 14px;">{today_title}</h3>
            <ul style="margin: 0; padding-left: 18px; font-size: 13.5px; color: #450A0A; line-height: 1.5; display: flex; flex-direction: column; gap: 8px;">
              {today_li}
            </ul>
          </div>

          <div style="display: flex; justify-content: center; align-items: center;">
            <svg viewBox="0 0 50 40" style="width: 44px; height: 34px;">
              <defs>
                <marker id="arrow_t_{case_id}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
                  <polygon points="0 1, 8 4, 0 7" fill="var(--primary)" />
                </marker>
              </defs>
              <line x1="4" y1="20" x2="40" y2="20" stroke="var(--primary)" stroke-width="3" stroke-linecap="round" marker-end="url(#arrow_t_{case_id})" />
            </svg>
          </div>

          <div class="fragment" style="background: #F0FDF4; border: 1.5px solid #86EFAC; border-radius: 12px; padding: 22px; height: 100%; display: flex; flex-direction: column;">
            <div style="display: inline-block; padding: 4px 10px; background: #DCFCE7; color: #16A34A; font-size: 11px; font-weight: 800; border-radius: 4px; text-transform: uppercase; margin-bottom: 10px; width: fit-content;">
              ✅ Z COPILOTEM: KONTROLA I SPOKÓJ
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

    # Slide 3: Golden Rule: Plan-First
    s3 = f"""
    <!-- SLIDE 3: ZŁOTA ZASADA: PLAN-FIRST -->
    <div class="slide-container" data-title="Złota zasada: Najpierw Plan, potem Implementacja" data-type="Złota Zasada">
      <header class="slide-header">
        <span class="slide-kicker">ZŁOTA ZASADA // WORKFLOW INŻYNIERSKI</span>
        <h2 class="slide-title">Nigdy Nie Proś o Kod w Ciemno: Najpierw PLAN, potem IMPLEMENTACJA</h2>
      </header>
      <div class="slide-body" style="justify-content: center;">
        
        <div style="display: grid; grid-template-columns: 1fr 30px 1fr 30px 1fr; align-items: center; width: 100%; margin-bottom: 20px;">
          
          <div class="fragment" style="background: #FFFFFF; border: 1.5px solid var(--border-light); border-top: 4px solid var(--primary); border-radius: 10px; padding: 18px; height: 100%;">
            <div style="font-size: 11px; font-weight: 800; color: var(--primary); text-transform: uppercase; margin-bottom: 6px;">KROK 1 · WYMUŚ PLAN</div>
            <h4 style="font-size: 16px; font-weight: 800; color: var(--text-dark); margin-bottom: 8px;">Zero Kodu w Pytaniu</h4>
            <p style="font-size: 13px; color: #475569; line-height: 1.45; margin: 0;">{step1}</p>
          </div>

          <div style="display: flex; justify-content: center;">
            <svg viewBox="0 0 30 20" style="width: 24px; height: 16px;">
              <defs><marker id="arr1_{case_id}" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0 1, 6 3, 0 5" fill="var(--primary)" /></marker></defs>
              <line x1="2" y1="10" x2="24" y2="10" stroke="var(--primary)" stroke-width="2.5" marker-end="url(#arr1_{case_id})" />
            </svg>
          </div>

          <div class="fragment" style="background: #FFFFFF; border: 1.5px solid var(--primary); border-top: 4px solid var(--accent); border-radius: 10px; padding: 18px; height: 100%; box-shadow: 0 4px 12px rgba(123,45,133,0.08);">
            <div style="font-size: 11px; font-weight: 800; color: var(--accent); text-transform: uppercase; margin-bottom: 6px;">KROK 2 · TWOJA DECYZJA</div>
            <h4 style="font-size: 16px; font-weight: 800; color: var(--text-dark); margin-bottom: 8px;">Przegląd w 30 Sekund</h4>
            <p style="font-size: 13px; color: #475569; line-height: 1.45; margin: 0;">{step2}</p>
          </div>

          <div style="display: flex; justify-content: center;">
            <svg viewBox="0 0 30 20" style="width: 24px; height: 16px;">
              <defs><marker id="arr2_{case_id}" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0 1, 6 3, 0 5" fill="var(--primary)" /></marker></defs>
              <line x1="2" y1="10" x2="24" y2="10" stroke="var(--primary)" stroke-width="2.5" marker-end="url(#arr2_{case_id})" />
            </svg>
          </div>

          <div class="fragment" style="background: #FFFFFF; border: 1.5px solid var(--border-light); border-top: 4px solid var(--success); border-radius: 10px; padding: 18px; height: 100%;">
            <div style="font-size: 11px; font-weight: 800; color: var(--success); text-transform: uppercase; margin-bottom: 6px;">KROK 3 · KOD PO KAWAŁKU</div>
            <h4 style="font-size: 16px; font-weight: 800; color: var(--text-dark); margin-bottom: 8px;">Tylko Wybrany Punkt</h4>
            <p style="font-size: 13px; color: #475569; line-height: 1.45; margin: 0;">{step3}</p>
          </div>

        </div>

        <div class="fragment" style="background: #FAF5FF; border-left: 4px solid var(--primary); border-radius: 0 8px 8px 0; padding: 12px 18px; font-size: 13px; color: #3B0764; line-height: 1.45;">
          💡 <strong>Dlaczego to działa w praktyce?</strong> {takeaway}
        </div>

      </div>
      <div class="slide-footer">
        <span>METODYKA // PLAN-FIRST</span>
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
        <h2 class="slide-title">Twoje Zadanie: Otwórz IDE i Zastosuj Regułę Plan-First</h2>
      </header>
      <div class="slide-body" style="justify-content: center;">
        
        <div style="background: #F8FAFC; border: 1px solid var(--border-light); border-radius: 8px; padding: 12px 18px; margin-bottom: 14px; font-size: 13.5px; color: #334155; line-height: 1.4;">
          <strong>Twoje zadanie:</strong> {scenario}
        </div>

        <div class="fragment" style="background: #0F172A; border-radius: 10px; padding: 16px 20px; margin-bottom: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-size: 11px; font-weight: 800; color: #38BDF8; letter-spacing: 0.08em; text-transform: uppercase;">
              👉 SKOPIUJ TEN PROMPT I WKLEJ DO COPILOT CHAT
            </span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">TRYB: PLAN-FIRST</span>
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
# 9 TECHNICAL CASE DECKS
# ==============================================================================

# T1
generate_human_tech_deck(
    filename="case-01-failing-test-debug.html",
    case_id="CASE T1",
    title="Czerwony Test na 15 Minut Przed Releasem",
    quote_heading="Piątek, 15:45 i czerwony pipeline",
    quote_body="Chcesz wdrożyć poprawkę i wyjść z pracy. Nagle test integracyjny wywala się z 80 liniami czerwonego błędu w terminalu. Wklejasz go w panice do Copilota z hasłem 'napraw to', a on podmienia pół klasy i psuje kolejne 3 moduły.",
    today_title="Dlaczego tracisz 40 minut na debugowanie?",
    today_points=[
        "Wklejasz cały 80-liniowy stack trace bez podania kontekstu i pliku",
        "Pytasz ogólnie 'gdzie jest błąd i napraw', więc AI strzela w ciemno",
        "Wciskasz Tab bez czytania i tracisz czas na odkręcanie zmian w gicie"
    ],
    ai_title="Opanowana diagnoza w 3 minuty",
    ai_points=[
        "Wskazujesz samą asercję i plik z błędem w edytorze (@workspace /explain)",
        "Zlecasz zbadanie 2-3 prawdopodobnych przyczyn BEZ pisania kodu",
        "Wybierasz właściwą hipotezę i dopiero wtedy generujesz 3 linijki poprawki"
    ],
    step1="Wpisz: 'Przeanalizuj ten stack trace. Nie generuj kodu. Wypisz w 3 punktach plan diagnozy i wskaż zmienną, która mogła mieć null'.",
    step2="Przeglądasz plan w 30 sekund: widzisz, że punkt 2 (brakujący nagłówek autoryzacji w requeście) to strzał w dziesiątkę.",
    step3="Dopiero teraz: 'Zaimplementuj Krok 2 z planu — dopisz sprawdzenie nagłówka w metodzie parseRequest() w minimalnej liczbie linii'.",
    takeaway="Copilot doskonale rozumie przyczynę błędu, ale jeśli od razu poprosisz o kod, zacznie zgadywać i zmieniać architekturę. Najpierw wymuś plan.",
    scenario="Otwórz plik z wywalającym się testem 'OrderProcessingTest'. Zamiast prosić o kod, przeprowadź kontrolowaną diagnozę.",
    prompt="""@workspace /explain Zbadaj powyższy błąd asercji w OrderProcessingTest.
NIE GENERUJ KODU IMPLEMENTACJI.
1. Wypisz 3 najbardziej prawdopodobne przyczyny asercji Expected: 200, Actual: 504.
2. Przygotuj 3-etapowy plan weryfikacji mocka i serwisu płatności.
3. Wskaż, którą linijkę musimy sprawdzić w debuggerze.""",
    success="Otrzymujesz 3 precyzyjne hipotezy i krótki plan weryfikacji mocka, bez ani jednej niepotrzebnej linijki wygenerowanego kodu.",
    trap="Pozwolenie Copilotowi na wygenerowanie nowego kodu w pierwszym kroku — to najczęstsza przyczyna regresji w projekcie."
)

# T2
generate_human_tech_deck(
    filename="case-02-test-quality.html",
    case_id="CASE T2",
    title="Copilot Napisał 10 Testów w 5 Sekund... ale One Nic Nie Testują",
    quote_heading="Zielony pasek, który kłamie",
    quote_body="Cieszysz się, bo Copilot wygenerował całą suitę testów i pokrycie skoczyło do 90%. Na code review kolega pyta: 'A co jeśli API zwróci pustą tablicę albo timeout?'. Sprawdzasz testy, a tam zamockowane wszystko na sztywno i asercja assertTrue(true).",
    today_title="Złudzenie bezpieczeństwa (testy-wydmuszki)",
    today_points=[
        "Prosisz ogólnie 'napisz unit testy do tej klasy' i akceptujesz wynik",
        "Copilot generuje testy tylko dla zadowolonej ścieżki (Happy Path)",
        "Asercje sprawdzają tylko czy funkcja się nie wywaliła, a nie logikę biznesową"
    ],
    ai_title="Twarde asercje i przypadki brzegowe",
    ai_points=[
        "Wymuszasz listę stanów brzegowych (Edge Cases) PRZED jakimkolwiek kodem",
        "Sam zatwierdzasz scenariusze: brak sieci, pusty string, ujemna kwota",
        "AI generuje testy z twardymi asercjami sprawdzającymi wyjątki i wartości"
    ],
    step1="Poproś o plan: 'Zbadaj metodę calculateDiscount(). Wypisz plan 5 testów brzegowych: wartości ujemne, zerowe, kwoty graniczne. Zero kodu'.",
    step2="Wybierasz 3 kluczowe scenariusze biznesowe, a 2 banalne odrzucasz.",
    step3="Generujesz kod testu tylko dla wybranego przypadku ujemnej kwoty, z asercją na wyjątek InvalidAmountException.",
    takeaway="Prawdziwą wartością testu nie jest zielony pasek, lecz to, czy test wywali się, gdy ktoś w przyszłości zepsuje logikę na produkcji.",
    scenario="Mamy klasę rabatów koszyka 'BasketDiscountService'. Chcemy przetestować zachowanie przy próbie naliczenia rabatu 110%.",
    prompt="""Przeanalizuj klasę BasketDiscountService.
NIE PISZ KODU TESTÓW.
1. Zaproponuj tabelę 4 przypadków brzegowych (dane wejściowe -> oczekiwany wynik).
2. Uwzględnij: pusty koszyk, rabat przekraczający 100%, kody rabatowe po terminie.
3. Wskaż, jakie konkretnie asercje i wyjątki musimy zweryfikować w każdym teście.""",
    success="Otrzymujesz kompletną matrycę scenariuszy brzegowych z konkretnymi wartościami wejściowymi i asercjami wyjątków.",
    trap="Akceptowanie testów, w których mock zwraca ten sam obiekt, który jest asertowany (test testuje sam siebie)."
)

# T3
generate_human_tech_deck(
    filename="case-03-code-review.html",
    case_id="CASE T3",
    title="Kolega Przysłał PR z Kodem z AI, a Ty Bezmyślnie Klikasz LGTM",
    quote_heading="Złudzenie idealnego kodu w PR",
    quote_body="Otwierasz Pull Request na 300 linii. Kod wygląda schludnie, ma ładne wcięcia i komentarze. Dajesz 'Approve'. Dwie godziny później na stagingu siada baza danych, bo kod generowany przez AI nie zamykał połączeń w bloku finally.",
    today_title="Pobieżne review i fałszywe zaufanie",
    today_points=[
        "Przeglądasz diff po łebkach, wierząc że 'skoro pisał z Copilotem, to działa'",
        "Przeoczasz brak obsługi timeoutów i brak indeksów przy zapytaniach SQL",
        "Wystawiasz formalny komentarz 'looks good to me' bez weryfikacji ryzyk"
    ],
    ai_title="Copilot jako adwokat diabła",
    ai_points=[
        "Używasz Copilota jako sceptycznego audytora bezpieczeństwa i wydajności",
        "Zlecasz mu wyszukanie 3 wektorów awarii i wycieków zasobów w diffie",
        "Sam sprawdzasz wskazane miejsca i zadajesz autorowi konkretne pytania"
    ],
    step1="Wklejasz diff PR-a. Prompt: 'Działaj jak bezlitosny audytor bezpieczeństwa. Wskaż w 3 punktach, gdzie ten kod wyłoży się pod obciążeniem'.",
    step2="Otrzymujesz plan ryzyk: brak limitu pobieranych wierszy, brak transakcyjności w zapisie.",
    step3="Formułujesz merytoryczne pytania do autora PR z odniesieniem do konkretnych linii diffa.",
    takeaway="Copilot doskonale znajduje luki we własnym i cudzym kodzie, o ile wyraźnie każesz mu szukać problemów, zamiast go chwalić.",
    scenario="Otwórz diff Pull Requesta z nowym endpointem pobierającym historię zamówień klienta.",
    prompt="""Przeanalizuj poniższy diff Pull Requesta jako sceptyczny Senior Architekt.
1. Wskaż 3 potencjalne problemy: wycieki pamięci, brak transakcji, zapytania N+1.
2. Przygotuj plan 2 pytań weryfikujących do autora PR.
3. Oceń, czy kod jest odporny na wstrzykiwanie parametrów (Parameter Tampering).""",
    success="Wykrycie braku stronicowania (pagination) w zapytaniu do bazy, zanim kod trafi na środowisko produkcyjne.",
    trap="Akceptowanie kodu z AI tylko dlatego, że wygląda elegancko i ma wygenerowane komentarze Javadoc."
)

# T4
generate_human_tech_deck(
    filename="case-04-legacy-refactor.html",
    case_id="CASE T4",
    title="Klasa na 600 Linii Napisana 7 Lat Temu i Strach Przed Zmianą",
    quote_heading="Kod, którego nikt nie rozumie",
    quote_body="Masz zmienić jeden warunek biznesowy w pliku 'PaymentManagerLegacy.java'. Ostatni commit był w 2019 roku, autor nie pracuje w firmie, a testów brak. Boisz się, że cokolwiek zmienisz — wywołasz lawinę błędów.",
    today_title="Ryzykowne przepisywanie od zera",
    today_points=[
        "Piszesz do Copilota: 'przepisz tę metodę na czysty kod'",
        "Copilot usuwa 'dziwne' warunki if, które były łatkami na błędy klienta",
        "Cały moduł przestaje działać w specyficznych przypadkach brzegowych"
    ],
    ai_title="Bezpieczne mikrokroki (Slicing)",
    ai_points=[
        "Najpierw tworzysz test utrwalający obecne zachowanie (Pinning Test)",
        "Zlecasz plan bezpiecznego rozbicia metody na małe, odizolowane plastry",
        "Wdrażasz refaktoryzację pojedynczymi krokami z natychmiastowym testem"
    ],
    step1="Poproś o plan: 'Zbadaj tę metodę. Nie refaktoryzuj. Zaproponuj plan wyodrębnienia pierwszej 10-linijkowej funkcji pomocniczej bez zmiany sygnatury'.",
    step2="Sprawdzasz czy plan nie modyfikuje ukrytego stanu obiektu.",
    step3="Generujesz kod tylko dla tej jednej małej funkcji i natychmiast odpalasz testy.",
    takeaway="W kodzie legacy największym wrogiem jest pośpiech. Bezpieczna zmiana to seria mikrokroków z zatwierdzonym planem.",
    scenario="Stara metoda obliczania podatku z 15 zagnieżdżonymi warunkami if/else bez żadnego testu jednostkowego.",
    prompt="""Przeanalizuj metodę calculateTaxLegacy().
NIE DOKONUJ REFAKTORYZACJI.
1. Przygotuj 3-etapowy plan wyciągania logiki: krok 1 (walidacja), krok 2 (stawki), krok 3 (zaokrąglenia).
2. Wskaż zmienne współdzielone (mutowalny stan), na które musimy uważać.
3. Zaproponuj minimalny test utrwalający obecne działanie (Pinning Test).""",
    success="Bezpieczny podział na małe, testowalne metody bez naruszenia dotychczasowego zachowania systemu.",
    trap="Zgoda na przepisanie całej klasy na nowy styl w jednym wielkim kroku bez testów utrwalających."
)

# T5
generate_human_tech_deck(
    filename="case-05-slow-sql-optimization.html",
    case_id="CASE T5",
    title="Na Twoim Laptopie Działało w 50 ms, u Klienta Muli przez 14 Sekund",
    quote_heading="Zderzenie z produkcyjną bazą danych",
    quote_body="Na lokalnej bazie z 50 rekordami wszystko śmigało. Klient odpala raport z 2 milionami wierszy i serwer staje dęba. Copilot podpowiada 'dodaj 4 indeksy', a baza klienta i tak ich nie użyje z powodu funkcji w klauzuli WHERE.",
    today_title="Optymalizacja w ciemno",
    today_points=[
        "Wklejasz samo zapytanie SQL i prosisz 'zoptymalizuj to zapytanie'",
        "Copilot przepisuje JOIN-y, gubiąc rekordy (zamienia LEFT JOIN na INNER JOIN)",
        "Wynik zapytania zmienia się po cichu, a raport pokazuje fałszywe sumy"
    ],
    ai_title="Analiza planu wykonania i ekwiwalencja",
    ai_points=[
        "Wklejasz plan wykonania (EXPLAIN PLAN) razem z zapytaniem SQL",
        "Wymuszasz plan sprawdzenia ekwiwalencji logicznej (identyczny zbiór wyników)",
        "Usuwasz operacje blokujące indeksy (np. funkcje na kolumnach indeksowanych)"
    ],
    step1="Oto zapytanie SQL i EXPLAIN PLAN. Wypisz plan: gdzie następuje Full Table Scan i dlaczego indeks nie jest używany.",
    step2="Weryfikujesz, czy proponowane przepisanie nie zgubi rekordów z wartościami NULL.",
    step3="Implementujesz zoptymalizowaną wersję i wykonujesz test porównawczy obu zapytań (MINUS / EXCEPT).",
    takeaway="Optymalizacja SQL to matematyka relacyjna. Każda zmiana zapytania musi zostać zweryfikowana testem ekwiwalencji zbiorów.",
    scenario="Wolne zapytanie filtrujące faktury po dacie i nazwie klienta z klauzulą WHERE UPPER(name) LIKE '%TECH%'.",
    prompt="""Przeanalizuj poniższe zapytanie SQL i plan wykonania EXPLAIN.
NIE PISZ NOWEGO QUERY WPROST.
1. Zidentyfikuj przyczynę pominięcia indeksu na kolumnie company_name.
2. Zaproponuj plan 2 wariantów optymalizacji: indeks funkcyjny vs przepisanie warunku.
3. Przygotuj zapytanie weryfikujące, czy oba warianty zwracają DOKŁADNIE tę samą liczbę wierszy (MINUS / EXCEPT).""",
    success="Skrócenie czasu zapytania z 14 sekund do 300 ms przy zerowym ryzyku przekłamania raportu finansowego.",
    trap="Zmiana struktury JOIN bez sprawdzenia przypadków brzegowych wartości NULL."
)

# T6
generate_human_tech_deck(
    filename="case-06-mockup-to-jira.html",
    case_id="CASE T6",
    title="Dostałeś Zrzut Ekranu od PO z Tekstem: 'Zróbcie to w Tym Sprincie'",
    quote_heading="Niejasne wymagania z Figmy",
    quote_body="Product Owner wrzuca na Slacka screen nowego formularza zamówienia i mówi: 'To tylko 3 pola, dacie radę do piątku'. Siadasz do kodu, a w czwartek okazuje się, że nikt nie opisał walidacji NIP, stanów ładowania ani co ma się stać przy braku połączenia.",
    today_title="Kodowanie bez dekompozycji",
    today_points=[
        "Zaczynasz od razu pisać komponenty bez rozpisania wymagań technicznych",
        "W połowie pracy pytasz PO o 10 szczegółów, blokując się nawzajem",
        "W piątek sprint kończy się niedokończonym kodem i nerwami na retro"
    ],
    ai_title="Precyzyjne tickety przed kodowaniem",
    ai_points=[
        "Wrzucasz opis makiety i prosisz o dekompozycję na konkretne zadania techniczne",
        "Copilot przygotowuje kryteria akceptacji w standardzie Given-When-Then",
        "Wklejasz gotowe tickety do Jiry przed napisaniem pierwszej linii kodu"
    ],
    step1="Zbadaj ten formularz. Rozpisz plan 3 niezależnych ticketów: 1. Model & Walidacja, 2. Integracja API, 3. Obsługa błędów UI.",
    step2="Dla każdego zadania wygeneruj 3 kryteria akceptacji (np. co się dzieje przy HTTP 422).",
    step3="Zatwierdzasz zakres z zespołem i dopiero wtedy implementujesz pierwszy ticket.",
    takeaway="Najtańszy błąd to ten, który wykryjesz przed napisaniem kodu. Dobry plan dekompozycji oszczędza dni pracy zespołu.",
    scenario="Makieta ekranu zmiany hasła z wymaganiami złożoności i potwierdzenia mailowego.",
    prompt="""Przeanalizuj ten komponent formularza zmiany hasła.
NIE GENERUJ KODU KOMPONENTU.
1. Rozbij zadanie na 3 tickety Jira (Front-end, Walidacja, Obsługa błędów API).
2. Dla każdego ticketu napisz kryteria akceptacji w formacie Given-When-Then.
3. Wypisz 3 stany brzegowe UI (brak sieci, wygaśnięcie tokenu sesji, podwójne kliknięcie).""",
    success="Kompletna, przejrzysta dekompozycja w Jirze z kryteriami akceptacji gotowa w 5 minut.",
    trap="Rozpoczynanie pisania stylów CSS przed ustaleniem kontraktu API i obsługi błędów."
)

# T7
generate_human_tech_deck(
    filename="case-07-unfamiliar-repo.html",
    case_id="CASE T7",
    title="Pierwszy Dzień w Projekcie: 40 Mikroserwisów i Zerowa Dokumentacja",
    quote_heading="Zgubiony w gąszczu obcego kodu",
    quote_body="Dołączasz do nowego zespołu u klienta. Repozytorium ma 400 tysięcy linii kodu, README ma 3 linijki z 2021 roku, a Ty masz naprawić błąd w fakturowaniu. Otwierasz IDE i nie wiesz nawet, która klasa startuje aplikację.",
    today_title="Szukanie po omacku",
    today_points=[
        "Klikasz po 40 folderach na oślep, szukając znajomo brzmiących słów",
        "Używasz globalnego wyszukiwania i dostajesz 800 wyników w 50 plikach",
        "Po 2 dniach nadal nie wiesz, jak dane wędrują od kontrolera do bazy"
    ],
    ai_title="Nawigacja z kontekstem @workspace",
    ai_points=[
        "Używasz kontekstu @workspace do zbudowania mapy przepływu żądania",
        "Pytasz o architekturę: 'Gdzie w tym projekcie walidujemy faktury?'",
        "Copilot wskazuje dokładny łańcuch wywołań klas w 10 sekund"
    ],
    step1="Użyj @workspace. Zbuduj plan ścieżki przepływu żądania dla operacji 'IssueInvoice': kontroler -> serwis -> repozytorium.",
    step2="Weryfikujesz 2 wskazane klasy i sprawdzasz wstrzykiwane zależności.",
    step3="Prosisz o zlokalizowanie miejsca, w którym rzucany jest badany wyjątek.",
    takeaway="@workspace w Copilocie to Twój prywatny przewodnik po obcym kodzie. Zamiast czytać tysiące linii, pytasz o relacje i przepływy.",
    scenario="Wejście do nieznanego repozytorium REST API opartego na Spring Boot / NestJS.",
    prompt="""@workspace Jak w tym repozytorium zorganizowana jest obsługa błędów?
1. Wskaż klasę obsługującą globalne wyjątki (np. @ControllerAdvice lub middleware).
2. Pokaż plan przepływu: co dzieje się, gdy serwis rzuca BusinessException.
3. Wskaż plik konfiguracyjny, w którym rejestrowane są filtry bezpieczeństwa.""",
    success="Błyskawiczna orientacja w strukturze projektu i odnalezienie właściwego modułu w 2 minuty.",
    trap="Pytanie o kod bez prefiksu @workspace — Copilot odpowie ogólnikami z internetu zamiast z Twojego projektu."
)

# T8
generate_human_tech_deck(
    filename="case-08-technical-to-business-update.html",
    case_id="CASE T8",
    title="Naprawiłeś Skomplikowany Bug, a PO Pyta: 'Co tam Właściwie Było?'",
    quote_heading="Klątwa wiedzy technicznej",
    quote_body="Spędziłeś 6 godzin na naprawieniu wyścigu wątków w transakcjach bazodanowych. Na standupie zaczynasz opowiadać o 'deadlockach na poziomie izolacji READ COMMITTED', a Product Owner patrzy na Ciebie pustym wzrokiem i pyta: 'Ale czy klient może już klikać?'.",
    today_title="Techniczny bełkot i nieporozumienia",
    today_points=[
        "Wklejasz na Slacka techniczny żargon albo git log z nazwami wewnętrznych metod",
        "Biznes nie rozumie ryzyka i nie wie, jak potwierdzić naprawę błędu",
        "Dochodzi do frustracji po obu stronach co do faktycznego postępu prac"
    ],
    ai_title="Tłumaczenie na język wartości biznesowej",
    ai_points=[
        "Wrzucasz diff commita do Copilota i prosisz o tłumaczenie na język korzyści",
        "Otrzymujesz 3 punkty: co było objawem, co naprawiono, jak to przetestować",
        "PO i klient dostają jasny, profesjonalny komunikat bez technicznego żargonu"
    ],
    step1="Oto diff commita. Przygotuj plan notatki w 3 punktach: 1. Co widział użytkownik, 2. Co naprawiono, 3. Co tester ma przeklikać.",
    step2="Sprawdzasz czy nie użyto hermetycznych nazw bibliotek i struktur bazodanowych.",
    step3="Kopiujesz zwięzłą notatkę do komentarza w Jirze lub maila do klienta.",
    takeaway="Najlepszy inżynier to taki, który potrafi wytłumaczyć wartość swojej pracy prostym językiem korzyści biznesowej.",
    scenario="Zamknięcie trudnego zadania z optymalizacji odświeżania tokenów uwierzytelniania.",
    prompt="""Przeanalizuj ten commit naprawiający wygasanie tokenów JWT.
Przetłumacz zmianę na notatkę dla Product Ownera i Testera:
1. Napisz w 2 zdaniach prostym językiem, co zyskuje użytkownik (zero żargonu).
2. Wypisz 3 proste kroki dla testera manualnego, jak potwierdzić naprawę.
3. Wskaż, czy zmiana wymagała migracji bazy lub restartu usług.""",
    success="Gotowy, elegancki update do ticketa w Jirze zrozumiały dla każdego członka zespołu.",
    trap="Używanie akronimów i nazw wewnętrznych tabel w oficjalnej komunikacji ze stroną biznesową."
)

# T9
generate_human_tech_deck(
    filename="case-09-client-restrictions-security.html",
    case_id="CASE T9",
    title="Klient Mówi: 'Zakaz AI i Chmury', a Ty Chcesz Pracować Wydajnie",
    quote_heading="Paraliż bezpieczeństwa vs wygoda",
    quote_body="Klient bankowy lub rządowy wpisał w umowie surowe kary za wysyłanie kodu do chmury. Część zespołu panikuje i wyłącza wszystkie narzędzia, a inni po cichu wklejają prawdziwe dane na czat ryzykując bezpieczeństwo firmy.",
    today_title="Skrajności: paraliż albo wyciek danych",
    today_points=[
        "Całkowita rezygnacja z asystenta AI i spadek produktywności zespołu o połowę",
        "Nieświadome wysyłanie wrażliwych danych (klucze API, PESEL, nazwy baz klienta)",
        "Strach przed audytem bezpieczeństwa i brak jasnych reguł w zespole"
    ],
    ai_title="Praca na syntetycznych abstrakcjach (Zero Risk)",
    ai_points=[
        "Wyodrębnienie czystego problemu algorytmicznego od poufnych danych klienta",
        "Generowanie struktur syntetycznych (Dummy Data / Generic Interfaces)",
        "100% zgodności z wymogami bezpieczeństwa i pełne wykorzystanie asystenta"
    ],
    step1="Zbadaj problem logiczny. Przygotuj plan sanityzacji: jak zastąpić dane klienta strukturą generyczną (ItemA, ItemB).",
    step2="Wysyłasz do Copilota wyłącznie czysty algorytm bez nazw domenowych klienta.",
    step3="Wygenerowane rozwiązanie wklejasz do zabezpieczonego środowiska klienta i wstrzykujesz właściwe typy.",
    takeaway="Ochrona własności intelektualnej klienta to priorytet inżyniera. Narzędzia AI wykorzystujemy do rozwiązywania łamigłówek logicznych na danych syntetycznych.",
    scenario="Złożony algorytm podziału budżetu i alokacji środków dla klienta korporacyjnego.",
    prompt="""Potrzebuję zoptymalizować algorytm alokacji zasobów.
Pracujemy w reżimie bezpieczeństwa (Zero Client Data).
1. Zaproponuj generyczny interfejs operujący na typach AllocationSource i AllocationTarget.
2. Przygotuj 3 syntetyczne przykłady danych testowych (zamaskowane ID, kwoty losowe).
3. Opracuj plan algorytmu dopasowania bez użycia zewnętrznych zależności.""",
    success="Rozwiązanie trudnego problemu logicznego przy zerowym ryzyku ujawnienia kodu i danych klienta.",
    trap="Wklejanie do czatu plików konfiguracyjnych .env, connection stringów lub prawdziwych nazw tabel klienta."
)

print("\nAll 9 technical case presentations successfully generated!")
