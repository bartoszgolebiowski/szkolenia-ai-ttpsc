import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE_TEMPLATE_PATH = r"C:\Users\golebiowskib\.agents\skills\html-presentation\resources\base-template.html"

with open(BASE_TEMPLATE_PATH, "r", encoding="utf-8") as f:
    base_html = f.read()

deck_marker = '<div id="deck-wrapper">'
deck_pos = base_html.find(deck_marker)
prefix = base_html[:deck_pos + len(deck_marker) + 1]

closing_marker = "  </div>\n\n  <!-- WIDOK SIATKI MINIATUR -->"
closing_pos = base_html.find(closing_marker)
if closing_pos == -1:
    closing_marker = "</div>\n\n  <!-- WIDOK SIATKI MINIATUR -->"
    closing_pos = base_html.find(closing_marker)
suffix = base_html[closing_pos:]

def wrap_presentation(title, slides_html):
    res_prefix = prefix.replace("<title>Wzorzec Prezentacji Biznesowej HTML & Inline SVG</title>", f"<title>{title}</title>")
    return res_prefix + "\n" + slides_html + "\n" + suffix

# ==========================================================
# SLIDE TEMPLATE GENERATORS (TEXT-FREE SVG & MCKINSEY/BCG)
# ==========================================================

def slide_title(title, kicker="TRANSITION TECHNOLOGIES PSC // SZKOLENIE AI", subtitle="1-Godzinna Sesja Strategiczna w Ramach Warsztatu Hands-on", meta="Warsztaty AI Copilot · 2026"):
    return f"""
    <!-- SLIDE 1: TYTUŁOWY -->
    <div class="slide-container slide-dark" data-title="{title}" data-type="Title">
      <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; max-width: 960px; z-index: 2;">
        <span class="slide-kicker" style="color: var(--accent); letter-spacing: 0.12em; margin-bottom: 16px;">{kicker}</span>
        <h1 style="font-size: 46px; font-weight: 800; line-height: 1.15; color: var(--text-light); margin-bottom: 22px;">{title}</h1>
        <p style="font-size: 19px; line-height: 1.45; color: var(--text-light-muted); margin-bottom: 34px; max-width: 820px;">{subtitle}</p>
        <div style="display: flex; gap: 32px; align-items: center; border-top: 1px solid var(--border-dark); padding-top: 22px;">
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Organizacja</span><strong style="font-size: 14px; color: var(--text-light);">Transition Technologies PSC</strong></div>
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Format</span><strong style="font-size: 14px; color: var(--text-light);">1h Prezentacja / 4h Warsztat</strong></div>
          <div><span style="font-size: 11px; text-transform: uppercase; color: var(--text-light-muted); display: block;">Kontekst</span><strong style="font-size: 14px; color: var(--text-light);">{meta}</strong></div>
        </div>
      </div>
      <div class="slide-footer">
        <span style="color: var(--text-light-muted);">TTPSC AI TRAINING // 2026</span>
        <span style="color: var(--text-light-muted);">Slajd 1</span>
      </div>
    </div>
    """

def slide_split_screen(kicker, title, left_badge, left_title, left_points, right_badge, right_title, right_points, slide_num=2):
    left_li = "".join([f"<li style='margin-bottom: 8px;'>{pt}</li>" for pt in left_points])
    right_li = "".join([f"<li style='margin-bottom: 8px;'>{pt}</li>" for pt in right_points])
    return f"""
    <!-- SLIDE: SPLIT SCREEN -->
    <div class="slide-container" data-title="{title}" data-type="Split Screen">
      <header class="slide-header">
        <span class="slide-kicker">{kicker}</span>
        <h2 class="slide-title">{title}</h2>
      </header>
      <div class="slide-body" style="justify-content: center;">
        <div style="display: grid; grid-template-columns: 1fr 60px 1fr; gap: 20px; align-items: center; width: 100%;">
          
          <div class="fragment" style="background: var(--bg-white); border: 1px solid var(--border-light); border-radius: 12px; padding: 26px 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
            <div style="display: inline-block; padding: 4px 10px; background: var(--danger-light); color: var(--danger); font-size: 11px; font-weight: 800; border-radius: 4px; text-transform: uppercase; margin-bottom: 12px;">{left_badge}</div>
            <h3 style="font-size: 20px; font-weight: 700; color: var(--text-dark); margin-bottom: 16px;">{left_title}</h3>
            <ul class="bullet-list" style="margin: 0; padding-left: 20px; font-size: 14px; color: #334155;">
              {left_li}
            </ul>
          </div>

          <div style="display: flex; justify-content: center; align-items: center;">
            <svg viewBox="0 0 60 60" style="width: 50px; height: 50px;">
              <defs>
                <marker id="splitArrow_{slide_num}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
                  <polygon points="0 1, 8 4, 0 7" fill="var(--primary)" />
                </marker>
              </defs>
              <line x1="5" y1="30" x2="48" y2="30" stroke="var(--primary)" stroke-width="4" stroke-linecap="round" marker-end="url(#splitArrow_{slide_num})" />
            </svg>
          </div>

          <div class="fragment" style="background: var(--bg-white); border: 2px solid var(--primary); border-radius: 12px; padding: 26px 24px; box-shadow: 0 4px 16px rgba(123,45,133,0.08);">
            <div style="display: inline-block; padding: 4px 10px; background: var(--success-light); color: var(--success); font-size: 11px; font-weight: 800; border-radius: 4px; text-transform: uppercase; margin-bottom: 12px;">{right_badge}</div>
            <h3 style="font-size: 20px; font-weight: 700; color: var(--text-dark); margin-bottom: 16px;">{right_title}</h3>
            <ul class="bullet-list" style="margin: 0; padding-left: 20px; font-size: 14px; color: #334155;">
              {right_li}
            </ul>
          </div>

        </div>
      </div>
      <div class="slide-footer">
        <span>KONTRAST // METODYKA PRACY</span>
        <span>Slajd {slide_num}</span>
      </div>
    </div>
    """

def slide_cards_flow(kicker, title, cards, slide_num=3):
    # cards: list of 3 dicts: {num: '01', title: '...', desc: '...', featured: bool}
    c1, c2, c3 = cards[0], cards[1], cards[2]
    b1 = "2px solid var(--primary)" if c1.get('featured') else "1px solid var(--border-light)"
    b2 = "2px solid var(--primary)" if c2.get('featured') else "1px solid var(--border-light)"
    b3 = "2px solid var(--primary)" if c3.get('featured') else "1px solid var(--border-light)"

    return f"""
    <!-- SLIDE: CARDS FLOW (3 COLUMNS) -->
    <div class="slide-container" data-title="{title}" data-type="3 Kolumny">
      <header class="slide-header">
        <span class="slide-kicker">{kicker}</span>
        <h2 class="slide-title">{title}</h2>
      </header>
      <div class="slide-body">
        <div style="display: grid; grid-template-columns: 1fr 36px 1fr 36px 1fr; align-items: center; height: 100%;">
          
          <div class="fragment" style="background: var(--bg-white); border: {b1}; border-radius: 12px; padding: 26px 20px; height: 100%; display: flex; flex-direction: column;">
            <div style="font-size: 24px; font-weight: 900; color: var(--primary); margin-bottom: 10px;">{c1['num']}</div>
            <h3 style="font-size: 18px; font-weight: 700; color: var(--text-dark); margin-bottom: 10px;">{c1['title']}</h3>
            <p style="font-size: 13px; color: #475569; line-height: 1.45; margin: 0;">{c1['desc']}</p>
          </div>

          <div style="display: flex; justify-content: center;">
            <svg viewBox="0 0 36 24" style="width: 28px; height: 20px;">
              <defs>
                <marker id="cfArrow1_{slide_num}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
                  <polygon points="0 1, 8 4, 0 7" fill="var(--primary)" />
                </marker>
              </defs>
              <line x1="2" y1="12" x2="28" y2="12" stroke="var(--primary)" stroke-width="3" stroke-linecap="round" marker-end="url(#cfArrow1_{slide_num})" />
            </svg>
          </div>

          <div class="fragment" style="background: var(--bg-white); border: {b2}; border-radius: 12px; padding: 26px 20px; height: 100%; display: flex; flex-direction: column;">
            <div style="font-size: 24px; font-weight: 900; color: var(--primary); margin-bottom: 10px;">{c2['num']}</div>
            <h3 style="font-size: 18px; font-weight: 700; color: var(--text-dark); margin-bottom: 10px;">{c2['title']}</h3>
            <p style="font-size: 13px; color: #475569; line-height: 1.45; margin: 0;">{c2['desc']}</p>
          </div>

          <div style="display: flex; justify-content: center;">
            <svg viewBox="0 0 36 24" style="width: 28px; height: 20px;">
              <defs>
                <marker id="cfArrow2_{slide_num}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
                  <polygon points="0 1, 8 4, 0 7" fill="var(--primary)" />
                </marker>
              </defs>
              <line x1="2" y1="12" x2="28" y2="12" stroke="var(--primary)" stroke-width="3" stroke-linecap="round" marker-end="url(#cfArrow2_{slide_num})" />
            </svg>
          </div>

          <div class="fragment" style="background: var(--bg-white); border: {b3}; border-radius: 12px; padding: 26px 20px; height: 100%; display: flex; flex-direction: column;">
            <div style="font-size: 24px; font-weight: 900; color: var(--primary); margin-bottom: 10px;">{c3['num']}</div>
            <h3 style="font-size: 18px; font-weight: 700; color: var(--text-dark); margin-bottom: 10px;">{c3['title']}</h3>
            <p style="font-size: 13px; color: #475569; line-height: 1.45; margin: 0;">{c3['desc']}</p>
          </div>

        </div>
      </div>
      <div class="slide-footer">
        <span>PRZEPŁYW WARTOŚCI // STRUKTURA 3 KOLUMN</span>
        <span>Slajd {slide_num}</span>
      </div>
    </div>
    """

def slide_hero_stat(kicker, title, big_stat, stat_sub, conclusion_bold, conclusion_text, slide_num=4):
    return f"""
    <!-- SLIDE: HERO STAT / BIG NUMBER -->
    <div class="slide-container" data-title="{title}" data-type="Hero Stat">
      <header class="slide-header">
        <span class="slide-kicker">{kicker}</span>
        <h2 class="slide-title">{title}</h2>
      </header>
      <div class="slide-body" style="justify-content: center; align-items: center; text-align: center;">
        
        <div style="display: flex; align-items: center; justify-content: center; gap: 24px; margin-bottom: 24px;">
          <div style="font-size: 105px; font-weight: 900; line-height: 1; color: var(--primary); letter-spacing: -0.04em;">
            {big_stat}
          </div>
          <div style="display: flex; flex-direction: column; align-items: flex-start; text-align: left;">
            <svg viewBox="0 0 60 70" style="width: 44px; height: 52px;">
              <defs>
                <marker id="heroTrendArrow_{slide_num}" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
                  <polygon points="0 6, 4 0, 8 6" fill="var(--success)" />
                </marker>
              </defs>
              <path d="M 10 55 Q 15 18 42 14" fill="none" stroke="var(--success)" stroke-width="5" stroke-linecap="round" marker-end="url(#heroTrendArrow_{slide_num})" />
            </svg>
            <span style="font-size: 15px; font-weight: 800; color: var(--success); margin-top: 4px;">{stat_sub}</span>
          </div>
        </div>

        <p class="fragment" style="font-size: 22px; color: var(--text-dark); max-width: 780px; line-height: 1.45; margin: 0 auto;">
          <strong>{conclusion_bold}:</strong> {conclusion_text}
        </p>

      </div>
      <div class="slide-footer">
        <span>METRYKA KLUCZOWA // IMPACT</span>
        <span>Slajd {slide_num}</span>
      </div>
    </div>
    """

def slide_chart_columns(kicker, title, kpi_val, kpi_label, delta_val, delta_label, col_items, slide_num=5):
    # col_items: list of (label, val_str, height_px, is_primary)
    cols_html = ""
    for c in col_items:
        color = "var(--primary)" if c[3] else "#CBD5E1"
        weight = "800" if c[3] else "600"
        cols_html += f"""
        <div style="display: flex; flex-direction: column; justify-content: flex-end; align-items: center;">
          <div style="font-size: 20px; font-weight: {weight}; font-variant-numeric: tabular-nums; margin-bottom: 4px;">{c[1]}</div>
          <div style="width: 90px; height: {c[2]}px; background: {color}; border-radius: 4px 4px 0 0;"></div>
          <div style="width: 100%; border-top: 2px solid #CBD5E1; padding-top: 8px; height: 32px; text-align: center; font-size: 14px; font-weight: 600; color: var(--text-muted);">{c[0]}</div>
        </div>
        """

    return f"""
    <!-- SLIDE: CHART COLUMNS + KPI -->
    <div class="slide-container" data-title="{title}" data-type="Wykres kolumnowy">
      <header class="slide-header">
        <span class="slide-kicker">{kicker}</span>
        <h2 class="slide-title">{title}</h2>
      </header>
      <div class="slide-body" style="flex-direction: row; gap: 48px; align-items: stretch;">
        
        <div style="width: 300px; display: flex; flex-direction: column; justify-content: center; gap: 10px;">
          <div style="font-size: 54px; font-weight: 800; line-height: 1; color: var(--text-dark); letter-spacing: -0.03em; font-variant-numeric: tabular-nums;">{kpi_val}</div>
          <div style="font-size: 16px; color: var(--text-muted);">{kpi_label}</div>
          <div style="display: flex; align-items: center; gap: 12px; margin-top: 16px;">
            <svg viewBox="0 0 60 70" style="width: 36px; height: 44px;">
              <defs>
                <marker id="chartTrendArrow_{slide_num}" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
                  <polygon points="0 6, 4 0, 8 6" fill="var(--success)" />
                </marker>
              </defs>
              <path d="M 10 55 Q 15 18 42 14" fill="none" stroke="var(--success)" stroke-width="5" stroke-linecap="round" marker-end="url(#chartTrendArrow_{slide_num})" />
            </svg>
            <div>
              <div style="font-size: 32px; font-weight: 800; color: var(--success); line-height: 1;">{delta_val}</div>
              <div style="font-size: 13px; color: var(--text-muted); margin-top: 2px;">{delta_label}</div>
            </div>
          </div>
        </div>

        <div style="flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <div style="position: relative; display: grid; grid-template-columns: repeat({len(col_items)}, 1fr); height: 340px; align-items: end;">
            {cols_html}
          </div>
        </div>

      </div>
      <div class="slide-footer">
        <span>TREND DANYCH // ANKIETA TTPSC</span>
        <span>Slajd {slide_num}</span>
      </div>
    </div>
    """

def slide_pipeline(kicker, title, steps, slide_num=3):
    cards_html = ""
    for s in steps:
        border = "2px solid var(--primary)" if s.get('active') else "1px solid var(--border-light)"
        bg = "var(--bg-white)"
        cards_html += f"""
        <div class="fragment" style="background: {bg}; border: {border}; border-radius: 12px; padding: 20px 18px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
          <span style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--primary); display: block; margin-bottom: 6px;">{s['phase']}</span>
          <h4 style="font-size: 17px; font-weight: 700; color: var(--text-dark); margin-bottom: 10px;">{s['title']}</h4>
          <p style="font-size: 13px; color: #475569; margin: 0; line-height: 1.4;">{s['desc']}</p>
        </div>
        """

    return f"""
    <!-- SLIDE: PIPELINE PROCESS -->
    <div class="slide-container" data-title="{title}" data-type="Pipeline">
      <header class="slide-header">
        <span class="slide-kicker">{kicker}</span>
        <h2 class="slide-title">{title}</h2>
      </header>
      <div class="slide-body" style="justify-content: center;">
        
        <div style="position: relative; width: 100%; margin-bottom: 20px;">
          <svg viewBox="0 0 1152 40" style="width: 100%; height: 36px;">
            <defs>
              <marker id="pipeArrow_{slide_num}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
                <polygon points="0 1, 8 4, 0 7" fill="var(--primary)" />
              </marker>
            </defs>
            <line x1="20" y1="18" x2="1140" y2="18" stroke="#CBD5E1" stroke-width="4" stroke-linecap="round" />
            <line x1="20" y1="18" x2="880" y2="18" stroke="var(--primary)" stroke-width="4" stroke-linecap="round" marker-end="url(#pipeArrow_{slide_num})" />
            <circle cx="140" cy="18" r="9" fill="var(--primary)" />
            <circle cx="430" cy="18" r="9" fill="var(--primary)" />
            <circle cx="720" cy="18" r="9" fill="var(--primary)" />
            <circle cx="1010" cy="18" r="9" fill="#94A3B8" />
          </svg>
        </div>

        <div style="display: grid; grid-template-columns: repeat({len(steps)}, 1fr); gap: 16px;">
          {cards_html}
        </div>

      </div>
      <div class="slide-footer">
        <span>ARCHITEKTURA PRZEPŁYWU // PIPELINE</span>
        <span>Slajd {slide_num}</span>
      </div>
    </div>
    """

def slide_double_diamond(kicker, title, phases, slide_num=4):
    p_html = ""
    for i, p in enumerate(phases):
        p_html += f"""
        <div class="fragment" style="text-align: center; padding: 0 10px;">
          <div style="font-size: 16px; font-weight: 800; color: var(--primary);">{i+1}. {p['name']}</div>
          <div style="font-size: 13px; color: #334155; margin-top: 6px; line-height: 1.35;">{p['desc']}</div>
        </div>
        """
    return f"""
    <!-- SLIDE: DOUBLE DIAMOND -->
    <div class="slide-container" data-title="{title}" data-type="Double Diamond">
      <header class="slide-header">
        <span class="slide-kicker">{kicker}</span>
        <h2 class="slide-title">{title}</h2>
      </header>
      <div class="slide-body" style="justify-content: center; align-items: center;">
        <div style="width: 100%; max-width: 980px; display: flex; flex-direction: column; align-items: center;">
          
          <svg viewBox="0 0 900 220" style="width: 100%; height: 210px;">
            <defs>
              <marker id="ddArrowB_{slide_num}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
                <polygon points="0 1, 8 4, 0 7" fill="var(--primary)" />
              </marker>
              <marker id="ddArrowG_{slide_num}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
                <polygon points="0 1, 8 4, 0 7" fill="var(--success)" />
              </marker>
            </defs>

            <polygon points="50,110 250,15 450,110 250,205" fill="var(--primary-light)" stroke="var(--primary)" stroke-width="3" />
            <line x1="250" y1="15" x2="250" y2="205" stroke="var(--primary)" stroke-width="2" stroke-dasharray="4 4" />
            <line x1="25" y1="110" x2="48" y2="110" stroke="var(--primary)" stroke-width="3" marker-end="url(#ddArrowB_{slide_num})" />

            <polygon points="450,110 650,15 850,110 650,205" fill="var(--success-light)" stroke="var(--success)" stroke-width="3" />
            <line x1="650" y1="15" x2="650" y2="205" stroke="var(--success)" stroke-width="2" stroke-dasharray="4 4" />
            <line x1="845" y1="110" x2="875" y2="110" stroke="var(--success)" stroke-width="3" marker-end="url(#ddArrowG_{slide_num})" />
          </svg>

          <div style="display: grid; grid-template-columns: repeat(4, 1fr); width: 100%; margin-top: 16px;">
            {p_html}
          </div>

        </div>
      </div>
      <div class="slide-footer">
        <span>RAMA METODYCZNA // PODWÓJNY DIAMENT</span>
        <span>Slajd {slide_num}</span>
      </div>
    </div>
    """

def slide_vicious_cycle(kicker, title, nodes, slide_num=5):
    return f"""
    <!-- SLIDE: VICIOUS CYCLE -->
    <div class="slide-container" data-title="{title}" data-type="Błędne Koło">
      <header class="slide-header">
        <span class="slide-kicker">{kicker}</span>
        <h2 class="slide-title">{title}</h2>
      </header>
      <div class="slide-body" style="justify-content: center; align-items: center;">
        <div style="position: relative; width: 620px; height: 420px;">
          
          <svg viewBox="0 0 520 400" style="position: absolute; inset: 0; width: 100%; height: 100%; z-index: 1;">
            <defs>
              <marker id="cycleRedArrow_{slide_num}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
                <polygon points="0 1, 8 4, 0 7" fill="var(--danger)" />
              </marker>
            </defs>
            <path d="M 290 50 A 145 145 0 0 1 435 170" fill="none" stroke="var(--danger)" stroke-width="3.5" marker-end="url(#cycleRedArrow_{slide_num})" />
            <path d="M 435 230 A 145 145 0 0 1 290 350" fill="none" stroke="var(--danger)" stroke-width="3.5" marker-end="url(#cycleRedArrow_{slide_num})" />
            <path d="M 230 350 A 145 145 0 0 1 85 230" fill="none" stroke="var(--danger)" stroke-width="3.5" marker-end="url(#cycleRedArrow_{slide_num})" />
            <path d="M 85 170 A 145 145 0 0 1 230 50" fill="none" stroke="var(--danger)" stroke-width="3.5" marker-end="url(#cycleRedArrow_{slide_num})" />
          </svg>

          <div class="fragment" style="position: absolute; top: 5px; left: 205px; width: 210px; z-index: 2; background: #FFFFFF; border: 1.5px solid var(--border-light); border-radius: 8px; padding: 10px 14px; text-align: center; font-size: 13px; box-shadow: 0 4px 10px rgba(0,0,0,0.04);">
            <strong style="color: var(--danger);">{nodes[0]['num']}. {nodes[0]['title']}</strong><br>{nodes[0]['desc']}
          </div>

          <div class="fragment" style="position: absolute; top: 165px; right: 0px; width: 200px; z-index: 2; background: #FFFFFF; border: 1.5px solid var(--border-light); border-radius: 8px; padding: 10px 14px; text-align: center; font-size: 13px; box-shadow: 0 4px 10px rgba(0,0,0,0.04);">
            <strong style="color: var(--danger);">{nodes[1]['num']}. {nodes[1]['title']}</strong><br>{nodes[1]['desc']}
          </div>

          <div class="fragment" style="position: absolute; bottom: 5px; left: 205px; width: 210px; z-index: 2; background: #FFFFFF; border: 1.5px solid var(--border-light); border-radius: 8px; padding: 10px 14px; text-align: center; font-size: 13px; box-shadow: 0 4px 10px rgba(0,0,0,0.04);">
            <strong style="color: var(--danger);">{nodes[2]['num']}. {nodes[2]['title']}</strong><br>{nodes[2]['desc']}
          </div>

          <div class="fragment" style="position: absolute; top: 165px; left: 0px; width: 200px; z-index: 2; background: #FFFFFF; border: 1.5px solid var(--border-light); border-radius: 8px; padding: 10px 14px; text-align: center; font-size: 13px; box-shadow: 0 4px 10px rgba(0,0,0,0.04);">
            <strong style="color: var(--danger);">{nodes[3]['num']}. {nodes[3]['title']}</strong><br>{nodes[3]['desc']}
          </div>

        </div>
      </div>
      <div class="slide-footer">
        <span>DYNAMIKA SYSTEMOWA // BŁĘDNE KOŁO</span>
        <span>Slajd {slide_num}</span>
      </div>
    </div>
    """

def slide_ishikawa(kicker, title, head_text, cat1, cat2, cat3, cat4, slide_num=6):
    return f"""
    <!-- SLIDE: ISHIKAWA FISHBONE -->
    <div class="slide-container" data-title="{title}" data-type="Ishikawa">
      <header class="slide-header">
        <span class="slide-kicker">{kicker}</span>
        <h2 class="slide-title">{title}</h2>
      </header>
      <div class="slide-body">
        <div style="position: relative; width: 100%; height: 420px; display: flex; align-items: center;">
          
          <svg viewBox="0 0 1120 380" preserveAspectRatio="xMidYMid meet" style="position: absolute; inset: 0; width: 100%; height: 100%; z-index: 1;">
            <defs>
              <marker id="fishMainArrow_{slide_num}" markerWidth="10" markerHeight="10" refX="7" refY="5" orient="auto">
                <polygon points="0 2, 8 5, 0 8" fill="var(--text-dark)" />
              </marker>
              <marker id="ribArrow_{slide_num}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
                <polygon points="0 1, 8 4, 0 7" fill="var(--primary)" />
              </marker>
            </defs>

            <line x1="60" y1="190" x2="870" y2="190" stroke="var(--text-dark)" stroke-width="4" marker-end="url(#fishMainArrow_{slide_num})" />

            <line x1="220" y1="50" x2="360" y2="190" stroke="var(--primary)" stroke-width="3" marker-end="url(#ribArrow_{slide_num})" />
            <line x1="540" y1="50" x2="680" y2="190" stroke="var(--primary)" stroke-width="3" marker-end="url(#ribArrow_{slide_num})" />

            <line x1="220" y1="330" x2="360" y2="190" stroke="var(--primary)" stroke-width="3" marker-end="url(#ribArrow_{slide_num})" />
            <line x1="540" y1="330" x2="680" y2="190" stroke="var(--primary)" stroke-width="3" marker-end="url(#ribArrow_{slide_num})" />
          </svg>

          <div style="position: absolute; inset: 0; z-index: 2; pointer-events: none;">
            
            <div class="fragment" style="position: absolute; top: 10px; left: 100px; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 8px; padding: 10px 14px; max-width: 230px; pointer-events: auto;">
              <strong style="color: var(--primary);">{cat1['title']}:</strong> {cat1['desc']}
            </div>

            <div class="fragment" style="position: absolute; top: 10px; left: 440px; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 8px; padding: 10px 14px; max-width: 230px; pointer-events: auto;">
              <strong style="color: var(--primary);">{cat2['title']}:</strong> {cat2['desc']}
            </div>

            <div class="fragment" style="position: absolute; bottom: 10px; left: 100px; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 8px; padding: 10px 14px; max-width: 230px; pointer-events: auto;">
              <strong style="color: var(--primary);">{cat3['title']}:</strong> {cat3['desc']}
            </div>

            <div class="fragment" style="position: absolute; bottom: 10px; left: 440px; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 8px; padding: 10px 14px; max-width: 230px; pointer-events: auto;">
              <strong style="color: var(--primary);">{cat4['title']}:</strong> {cat4['desc']}
            </div>

            <div style="position: absolute; top: 140px; right: 20px; background: var(--bg-dark); color: #FFFFFF; border-radius: 10px; padding: 20px 24px; max-width: 220px; text-align: center; pointer-events: auto;">
              <span style="font-size: 11px; text-transform: uppercase; color: var(--accent); font-weight: 800; display: block; margin-bottom: 4px;">Problem Główny</span>
              <h4 style="font-size: 16px; font-weight: 700; margin: 0; line-height: 1.3;">{head_text}</h4>
            </div>

          </div>

        </div>
      </div>
      <div class="slide-footer">
        <span>ROOT CAUSE // DIAGRAM ISHIKAWA</span>
        <span>Slajd {slide_num}</span>
      </div>
    </div>
    """

def slide_transformation_bridge(kicker, title, from_title, from_points, bridge_steps, to_title, to_points, slide_num=7):
    from_li = "".join([f"<li style='font-size: 13px; margin-bottom: 6px;'>{p}</li>" for p in from_points])
    to_li = "".join([f"<li style='font-size: 13px; margin-bottom: 6px;'>{p}</li>" for p in to_points])
    b_cards = ""
    for b in bridge_steps:
        b_cards += f"""
        <div class="fragment" style="flex: 1; background: #FFFFFF; border: 1.5px dashed var(--primary); border-radius: 8px; padding: 10px 12px; font-size: 12px; text-align: center;">
          <strong style="color: var(--primary);">{b['k']}:</strong><br>{b['v']}
        </div>
        """

    return f"""
    <!-- SLIDE: TRANSFORMATION BRIDGE -->
    <div class="slide-container" data-title="{title}" data-type="Most Transformacji">
      <header class="slide-header">
        <span class="slide-kicker">{kicker}</span>
        <h2 class="slide-title">{title}</h2>
      </header>
      <div class="slide-body">
        <div style="display: grid; grid-template-columns: 270px 1fr 270px; gap: 20px; align-items: center; height: 100%;">
          
          <div class="fragment" style="background: var(--bg-white); border: 1px solid var(--border-light); border-radius: 12px; padding: 22px; display: flex; flex-direction: column;">
            <span style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--danger); margin-bottom: 6px;">Stan Obecny</span>
            <h4 style="font-size: 18px; font-weight: 700; color: var(--text-dark); margin-bottom: 12px;">{from_title}</h4>
            <ul class="bullet-list" style="margin: 0; padding-left: 18px;">
              {from_li}
            </ul>
          </div>

          <div style="display: flex; flex-direction: column; align-items: center; position: relative;">
            <svg viewBox="0 0 520 130" style="width: 100%; height: 130px;">
              <defs>
                <marker id="bridgeHead_{slide_num}" markerWidth="10" markerHeight="10" refX="7" refY="5" orient="auto">
                  <polygon points="0 2, 8 5, 0 8" fill="var(--primary)" />
                </marker>
              </defs>
              <path d="M 20 105 Q 260 15 490 105" fill="none" stroke="var(--primary)" stroke-width="4" stroke-dasharray="6 6" marker-end="url(#bridgeHead_{slide_num})" />
              <rect x="195" y="20" width="130" height="28" rx="14" fill="var(--primary-light)" stroke="var(--primary)" stroke-width="1" />
            </svg>
            <div style="position: absolute; top: 25px; font-size: 12px; font-weight: 800; color: var(--primary); text-transform: uppercase; letter-spacing: 0.05em;">
              Most Zmiany
            </div>
            <div style="display: flex; gap: 10px; width: 100%; margin-top: 8px;">
              {b_cards}
            </div>
          </div>

          <div class="fragment" style="background: var(--bg-white); border: 2px solid var(--success); border-radius: 12px; padding: 22px; display: flex; flex-direction: column;">
            <span style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--success); margin-bottom: 6px;">Stan Docelowy</span>
            <h4 style="font-size: 18px; font-weight: 700; color: var(--text-dark); margin-bottom: 12px;">{to_title}</h4>
            <ul class="bullet-list" style="margin: 0; padding-left: 18px;">
              {to_li}
            </ul>
          </div>

        </div>
      </div>
      <div class="slide-footer">
        <span>GAP ANALYSIS // MOST TRANSFORMACJI</span>
        <span>Slajd {slide_num}</span>
      </div>
    </div>
    """

def slide_grid_matrix(kicker, title, label_top, label_bottom, label_left, label_right, q1, q2, q3, q4, slide_num=8):
    return f"""
    <!-- SLIDE: GRID MATRIX 2X2 -->
    <div class="slide-container" data-title="{title}" data-type="Siatka 2x2">
      <header class="slide-header">
        <span class="slide-kicker">{kicker}</span>
        <h2 class="slide-title">{title}</h2>
      </header>
      <div class="slide-body" style="justify-content: center; align-items: center;">
        <div style="position: relative; width: 840px; height: 420px;">
          
          <svg viewBox="0 0 840 420" style="position: absolute; inset: 0; width: 100%; height: 100%; z-index: 1;">
            <defs>
              <marker id="matrixArrow_{slide_num}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
                <polygon points="0 1, 8 4, 0 7" fill="#64748B" />
              </marker>
            </defs>
            <line x1="40" y1="210" x2="800" y2="210" stroke="#94A3B8" stroke-width="2.5" marker-end="url(#matrixArrow_{slide_num})" />
            <line x1="420" y1="380" x2="420" y2="30" stroke="#94A3B8" stroke-width="2.5" marker-end="url(#matrixArrow_{slide_num})" />
          </svg>

          <div style="position: absolute; top: 5px; left: 430px; font-size: 11px; font-weight: 800; color: #475569; text-transform: uppercase;">{label_top}</div>
          <div style="position: absolute; bottom: 5px; left: 430px; font-size: 11px; font-weight: 800; color: #475569; text-transform: uppercase;">{label_bottom}</div>
          <div style="position: absolute; top: 215px; left: 45px; font-size: 11px; font-weight: 800; color: #475569; text-transform: uppercase;">{label_left}</div>
          <div style="position: absolute; top: 215px; right: 45px; font-size: 11px; font-weight: 800; color: #475569; text-transform: uppercase;">{label_right}</div>

          <div class="fragment" style="position: absolute; top: 35px; left: 50px; width: 340px; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 8px; padding: 14px 16px; z-index: 2;">
            <strong style="color: var(--primary);">{q1['title']}</strong><br><span style="font-size: 12px; color: #475569;">{q1['desc']}</span>
          </div>

          <div class="fragment" style="position: absolute; top: 35px; right: 50px; width: 340px; background: #FFFFFF; border: 2px solid var(--primary); border-radius: 8px; padding: 14px 16px; z-index: 2; box-shadow: 0 4px 12px rgba(123,45,133,0.06);">
            <strong style="color: var(--accent);">{q2['title']}</strong><br><span style="font-size: 12px; color: #475569;">{q2['desc']}</span>
          </div>

          <div class="fragment" style="position: absolute; bottom: 35px; left: 50px; width: 340px; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 8px; padding: 14px 16px; z-index: 2;">
            <strong style="color: var(--text-dark);">{q3['title']}</strong><br><span style="font-size: 12px; color: #475569;">{q3['desc']}</span>
          </div>

          <div class="fragment" style="position: absolute; bottom: 35px; right: 50px; width: 340px; background: #FFFFFF; border: 1px solid var(--border-light); border-radius: 8px; padding: 14px 16px; z-index: 2;">
            <strong style="color: var(--text-dark);">{q4['title']}</strong><br><span style="font-size: 12px; color: #475569;">{q4['desc']}</span>
          </div>

        </div>
      </div>
      <div class="slide-footer">
        <span>DECYZJA STRATEGICZNA // MATRYCA 2X2</span>
        <span>Slajd {slide_num}</span>
      </div>
    </div>
    """

def slide_ranking_bars(kicker, title, items, pareto_text, slide_num=9):
    rows_html = ""
    for it in items:
        color = "var(--primary)" if it[3] else "#CBD5E1"
        weight = "800" if it[3] else "500"
        rows_html += f"""
        <div style="display: grid; grid-template-columns: 240px 1fr 90px; gap: 14px; align-items: center; height: 34px;">
          <div style="font-size: 14px; font-weight: {weight}; color: var(--text-dark); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{it[0]}</div>
          <div style="background: #F1F5F9; height: 18px; border-radius: 3px; overflow: hidden;">
            <div style="height: 100%; width: {it[2]}%; background: {color}; border-radius: 0 3px 3px 0;"></div>
          </div>
          <div style="font-size: 14px; font-weight: 800; font-variant-numeric: tabular-nums; color: var(--text-dark);">{it[1]}</div>
        </div>
        """

    return f"""
    <!-- SLIDE: RANKING BARS WITH PARETO -->
    <div class="slide-container" data-title="{title}" data-type="Ranking słupkowy">
      <header class="slide-header">
        <span class="slide-kicker">{kicker}</span>
        <h2 class="slide-title">{title}</h2>
      </header>
      <div class="slide-body">
        <div style="display: grid; grid-template-columns: 1fr 220px; gap: 24px; align-items: center;">
          
          <div style="display: flex; flex-direction: column; gap: 4px;">
            {rows_html}
          </div>

          <div class="fragment" style="background: var(--bg-white); border: 2px solid var(--primary); border-radius: 12px; padding: 22px; text-align: center; box-shadow: 0 4px 16px rgba(123,45,133,0.08);">
            <span style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--primary); display: block; margin-bottom: 6px;">Wniosek z Ankiety</span>
            <div style="font-size: 38px; font-weight: 900; color: var(--primary); line-height: 1.1; margin-bottom: 8px;">{pareto_text['big']}</div>
            <p style="font-size: 13px; color: #475569; margin: 0; line-height: 1.4;">{pareto_text['desc']}</p>
          </div>

        </div>
      </div>
      <div class="slide-footer">
        <span>DANE EMPIRYCZNE // ANKIETA TTPSC</span>
        <span>Slajd {slide_num}</span>
      </div>
    </div>
    """

def slide_cta_decision_rows(kicker, title, decisions, slide_num=10):
    rows_html = ""
    for d in decisions:
        rows_html += f"""
        <div class="fragment" style="flex: 1; display: grid; grid-template-columns: 60px 1fr 240px; align-items: center; gap: 20px; background: var(--bg-white); border: 1px solid var(--border-light); border-radius: 12px; padding: 0 28px;">
          <div style="font-size: 40px; font-weight: 900; color: var(--primary);">{d['num']}</div>
          <div>
            <div style="font-size: 20px; font-weight: 700; color: var(--text-dark);">{d['title']}</div>
            <div style="font-size: 14px; color: var(--text-muted); margin-top: 4px;">{d['desc']}</div>
          </div>
          <div style="border-left: 2px solid var(--border-light); padding-left: 24px;">
            <div style="font-size: 34px; font-weight: 800; color: {d['stat_color']}; line-height: 1;">{d['stat']}</div>
            <div style="font-size: 13px; color: var(--text-muted); margin-top: 4px;">{d['stat_desc']}</div>
          </div>
        </div>
        """

    return f"""
    <!-- SLIDE: CTA DECISION ROWS -->
    <div class="slide-container" data-title="{title}" data-type="CTA">
      <header class="slide-header">
        <span class="slide-kicker">{kicker}</span>
        <h2 class="slide-title">{title}</h2>
      </header>
      <div class="slide-body" style="gap: 14px; padding-bottom: 12px;">
        {rows_html}
      </div>
      <div class="slide-footer">
        <span>REKOMENDACJE STRATEGICZNE // NASTĘPNE KROKI</span>
        <span>Slajd {slide_num}</span>
      </div>
    </div>
    """

def slide_closing(title="Podsumowanie & Pytania", subtitle="Przejście do sesji laboratoryjnej hands-on", kicker="TRANSITION TECHNOLOGIES PSC // WARSZTAT AI", contact="zespol-ai@ttpsc.pl"):
    return f"""
    <!-- SLIDE FINAŁOWY: Q&A -->
    <div class="slide-container slide-dark" data-title="{title}" data-type="Finał">
      <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; z-index: 2;">
        <span class="slide-kicker" style="color: var(--accent); letter-spacing: 0.12em; margin-bottom: 14px;">{kicker}</span>
        <h2 style="font-size: 54px; font-weight: 800; color: var(--text-light); margin-bottom: 20px;">{title}</h2>
        <p style="font-size: 20px; color: var(--text-light-muted); max-width: 640px; margin-bottom: 36px; line-height: 1.4;">{subtitle}</p>
        <div style="display: flex; gap: 20px;">
          <div style="background: rgba(255,255,255,0.08); border: 1px solid var(--border-dark); border-radius: 8px; padding: 12px 24px; color: var(--text-light); font-size: 14px;">
            <strong>Kontakt z trenerem:</strong> {contact}
          </div>
          <div style="background: rgba(255,255,255,0.08); border: 1px solid var(--border-dark); border-radius: 8px; padding: 12px 24px; color: var(--text-light); font-size: 14px;">
            <strong>Materiały repo:</strong> Transition Technologies PSC
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span style="color: var(--text-light-muted);">TTPSC AI TRAINING // FIN</span>
        <span style="color: var(--text-light-muted);">Koniec</span>
      </div>
    </div>
    """
