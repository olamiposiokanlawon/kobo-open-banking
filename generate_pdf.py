from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

OUTPUT = r"C:\Users\USER\OneDrive\Documents\bank base\Kobo_Code_Explained.pdf"

INK        = colors.HexColor("#0A1628")
GREEN      = colors.HexColor("#16A34A")
GREEN_PALE = colors.HexColor("#ECFDF5")
CANVAS_BG  = colors.HexColor("#F8F6F1")
BORDER     = colors.HexColor("#E8E4DC")
MUTED      = colors.HexColor("#64748B")
CODE_BG    = colors.HexColor("#F1EFE8")
RED        = colors.HexColor("#F43F5E")
BLUE       = colors.HexColor("#0EA5E9")
WHITE      = colors.white

W, H     = A4
PAGE_W   = W - 4.8*cm

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    rightMargin=2.4*cm, leftMargin=2.4*cm,
    topMargin=2.4*cm,   bottomMargin=2.4*cm,
    title="Kobo Dashboard — Full Code Explanation",
)

def ps(name, **kw):
    return ParagraphStyle(name, **kw)

H1_S  = ps("H1",  fontName="Helvetica-Bold",   fontSize=20, leading=26, textColor=INK,   spaceBefore=24, spaceAfter=6)
H2_S  = ps("H2",  fontName="Helvetica-Bold",   fontSize=14, leading=19, textColor=INK,   spaceBefore=18, spaceAfter=5)
H3_S  = ps("H3",  fontName="Helvetica-Bold",   fontSize=11, leading=15, textColor=GREEN, spaceBefore=12, spaceAfter=3)
BODY  = ps("Body",fontName="Helvetica",         fontSize=10.5, leading=16, textColor=INK, spaceAfter=8, alignment=TA_JUSTIFY)
SMALL = ps("Sm",  fontName="Helvetica",         fontSize=9.5,  leading=14, textColor=MUTED, spaceAfter=5)
CODE  = ps("Code",fontName="Courier",           fontSize=8.8,  leading=13, textColor=colors.HexColor("#1E293B"),
           backColor=CODE_BG, spaceAfter=8, leftIndent=10, rightIndent=10, borderPadding=(7,10,7,10))
NOTE  = ps("Note",fontName="Helvetica-Oblique", fontSize=9.5,  leading=14, textColor=colors.HexColor("#1A4030"),
           backColor=GREEN_PALE, spaceAfter=8, leftIndent=10, rightIndent=10, borderPadding=(7,10,7,10))
BULL  = ps("Bull",fontName="Helvetica",         fontSize=10.5, leading=16, textColor=INK, leftIndent=14, spaceAfter=3)

def sp(h=0.3): return Spacer(1, h*cm)
def hr(): return HRFlowable(width="100%", thickness=1, color=BORDER, spaceAfter=6, spaceBefore=2)
def ghr(): return HRFlowable(width=48, thickness=3, color=GREEN, spaceAfter=12, spaceBefore=0)

def h1(t): return [Paragraph(t, H1_S), ghr()]
def h2(t): return Paragraph(t, H2_S)
def h3(t): return Paragraph(t, H3_S)
def body(t): return Paragraph(t, BODY)
def small(t): return Paragraph(t, SMALL)
def note(t): return Paragraph(f"<b>Note:</b> {t}", NOTE)
def bull(t): return Paragraph(f"&bull; &nbsp;{t}", BULL)

def code(t):
    t = t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return Paragraph(t, CODE)

def file_banner(path, description):
    tbl = Table([[path, description]], colWidths=[PAGE_W*0.44, PAGE_W*0.56])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(0,0), INK),
        ("BACKGROUND",(1,0),(1,0), colors.HexColor("#1A2A3A")),
        ("TEXTCOLOR", (0,0),(-1,-1), WHITE),
        ("FONTNAME",  (0,0),(0,0), "Courier-Bold"),
        ("FONTNAME",  (1,0),(1,0), "Helvetica-Oblique"),
        ("FONTSIZE",  (0,0),(-1,-1), 9),
        ("PADDING",   (0,0),(-1,-1), 8),
        ("VALIGN",    (0,0),(-1,-1), "MIDDLE"),
    ]))
    return [tbl, sp(0.2)]

def kv_table(rows, col1=4.0):
    result = []
    for k, v in rows:
        tbl = Table([[
            Paragraph(k, ps("K", fontName="Courier-Bold", fontSize=9, textColor=GREEN)),
            Paragraph(v, SMALL),
        ]], colWidths=[col1*cm, PAGE_W - col1*cm])
        tbl.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(0,0), CODE_BG),
            ("LINEBELOW",(0,0),(-1,-1), 0.5, BORDER),
            ("PADDING",(0,0),(-1,-1), 7),
            ("VALIGN",(0,0),(-1,-1), "TOP"),
        ]))
        result.append(tbl)
    return result

# ─── COVER ───────────────────────────────────────────────────────────────────
def cover():
    banner = Table([[
        Paragraph("Kɔbo Dashboard", ps("CT", fontName="Helvetica-Bold", fontSize=34,
                   textColor=WHITE, alignment=TA_CENTER)),
        Paragraph("Complete Code Reference", ps("CS", fontName="Helvetica", fontSize=15,
                   textColor=colors.HexColor("#9DB0C8"), alignment=TA_CENTER)),
        Paragraph("Every file · Every line · Every decision explained in plain English",
                   ps("CI", fontName="Helvetica-Oblique", fontSize=11,
                   textColor=colors.HexColor("#7A8BA0"), alignment=TA_CENTER)),
    ]], colWidths=[PAGE_W])
    banner.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), INK),
        ("PADDING",(0,0),(-1,-1), 28),
    ]))
    items = [banner, sp(0.5)]

    meta = [
        ("Project",    "Kɔbo — Open Banking Dashboard (Dashboard view)"),
        ("Stack",      "React 18 · Vite · Framer Motion · Lucide React"),
        ("Files",      "11 source files — data, utils, hooks, styles, components, page"),
        ("This PDF",   "Covers every single line of code currently in the bank-base folder"),
    ]
    for k, v in meta:
        row = Table([[
            Paragraph(k, ps("MK", fontName="Helvetica-Bold", fontSize=9.5, textColor=MUTED)),
            Paragraph(v, ps("MV", fontName="Helvetica", fontSize=10, textColor=INK)),
        ]], colWidths=[2.8*cm, PAGE_W-2.8*cm])
        row.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,-1), CANVAS_BG),
            ("PADDING",(0,0),(-1,-1), 9),
            ("LINEBELOW",(0,0),(-1,-1), 0.5, BORDER),
            ("VALIGN",(0,0),(-1,-1), "MIDDLE"),
        ]))
        items.append(row)

    items += [sp(0.8), body(
        "This document explains every file in the Kɔbo dashboard codebase. "
        "You will understand what every import does, what every function does, "
        "what every style property does, and why every design decision was made. "
        "Read it once and you will be able to explain any line of this code to anyone."
    ), PageBreak()]
    return items

# ─── TABLE OF CONTENTS ───────────────────────────────────────────────────────
def toc():
    sections = [
        ("1",  "How the project is structured",          "3"),
        ("2",  "index.html — the single HTML file",      "3"),
        ("3",  "src/main.jsx — JavaScript entry point",  "4"),
        ("4",  "src/index.css — global styles & animations","5"),
        ("5",  "src/data/mockData.js — all raw data",    "7"),
        ("6",  "src/utils/helpers.js — utility functions","9"),
        ("7",  "src/hooks/useCountUp.js — animation hook","10"),
        ("8",  "src/styles/theme.js — the design system","11"),
        ("9",  "src/components/Sidebar.jsx",             "15"),
        ("10", "src/components/TopBar.jsx",              "17"),
        ("11", "src/components/Pill.jsx",                "18"),
        ("12", "src/components/SectionHeader.jsx",       "19"),
        ("13", "src/components/TransactionRow.jsx",      "20"),
        ("14", "src/pages/OverviewPage.jsx",             "22"),
        ("15", "src/App.jsx — root component",           "26"),
        ("16", "Framer Motion animations — full guide",  "28"),
        ("17", "Design decisions explained",             "30"),
    ]
    items = h1("Table of Contents")
    for num, title, pg in sections:
        row = Table([[
            Paragraph(num+".", ps("TN", fontName="Helvetica-Bold", fontSize=10, textColor=GREEN)),
            Paragraph(title,   ps("TT", fontName="Helvetica", fontSize=10.5, textColor=INK)),
            Paragraph(pg,      ps("TP", fontName="Helvetica", fontSize=10, textColor=MUTED)),
        ]], colWidths=[0.8*cm, PAGE_W-2.2*cm, 1.4*cm])
        row.setStyle(TableStyle([
            ("LINEBELOW",(0,0),(-1,-1), 0.5, BORDER),
            ("PADDING",(0,0),(-1,-1), 6),
            ("VALIGN",(0,0),(-1,-1), "MIDDLE"),
        ]))
        items.append(row)
    items.append(PageBreak())
    return items

# ─── SECTION 1: Project structure ───────────────────────────────────────────
def s1_structure():
    items = h1("1. How the Project is Structured")
    items.append(body(
        "The project is split into folders by <b>purpose</b>. Each folder has one job and "
        "one job only. This makes it easy to find things and easy to change things."
    ))
    rows = [
        ("src/data/",       "Holds all the raw information the app displays — bank names, transactions, navigation labels."),
        ("src/utils/",      "Holds helper functions that transform data — formatting money, finding a bank by its ID."),
        ("src/hooks/",      "Holds custom React hooks — reusable logic that can be shared across components."),
        ("src/styles/",     "Holds the design system — every colour, font, shadow, and layout style in one place."),
        ("src/components/", "Holds small reusable UI pieces — a sidebar, a topbar, a pill, a card row."),
        ("src/pages/",      "Holds the full dashboard page assembled from components."),
        ("App.jsx",         "The root: wires everything together and renders the shell."),
    ]
    items += kv_table(rows, col1=3.8)
    items.append(note(
        "The open-banking-app folder holds the other pages (Transactions, Insights, Banks) "
        "that are not shown in this demo. They are safely stored there and can be moved back later."
    ))
    items.append(PageBreak())
    return items

# ─── SECTION 2: index.html ───────────────────────────────────────────────────
def s2_html():
    items = h1("2. index.html — The Single HTML File")
    items += file_banner("index.html", "The only HTML file. The browser loads this first.")
    items.append(code(
        '&lt;!DOCTYPE html&gt;\n'
        '&lt;html lang="en"&gt;\n'
        '  &lt;head&gt;\n'
        '    &lt;meta charset="UTF-8" /&gt;\n'
        '    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0" /&gt;\n'
        '    &lt;title&gt;Kɔbo — open banking&lt;/title&gt;\n'
        '    &lt;link rel="preconnect" href="https://fonts.googleapis.com" /&gt;\n'
        '    &lt;link rel="preconnect" href="https://fonts.gstatic.com" crossorigin /&gt;\n'
        '    &lt;link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque...\n'
        '  &lt;/head&gt;\n'
        '  &lt;body&gt;\n'
        '    &lt;div id="root"&gt;&lt;/div&gt;\n'
        '    &lt;script type="module" src="/src/main.jsx"&gt;&lt;/script&gt;\n'
        '  &lt;/body&gt;\n'
        '&lt;/html&gt;'
    ))
    rows = [
        ('&lt;!DOCTYPE html&gt;',         'Tells the browser this is a modern HTML5 document, not old HTML from the 1990s.'),
        ('lang="en"',                     'Tells screen readers and search engines this page is in English.'),
        ('charset="UTF-8"',               'UTF-8 is a character encoding that supports every character in the world — including the ɔ in Kɔbo and the ₦ Naira symbol.'),
        ('name="viewport"',               'Makes the page scale correctly on mobile phones. Without this, phones zoom out to show a tiny desktop-sized page.'),
        ('rel="preconnect"',              'Tells the browser to open a connection to Google Fonts early, before the font CSS is even requested. Saves time.'),
        ('crossorigin',                   'Required for font files loaded from a different domain (fonts.gstatic.com). Tells the browser to allow the cross-origin resource.'),
        ('family=Bricolage+Grotesque',    'The display font — used for headings and the big balance number. The + is a URL space character.'),
        ('family=Inter',                  'The body font — used for all regular text, labels, and UI copy.'),
        ('&lt;div id="root"&gt;',         'An empty box. React will fill this with the entire application. It starts completely empty.'),
        ('type="module"',                 'Tells the browser this script uses modern ES Module syntax (import/export). Vite intercepts this and serves the transformed code.'),
        ('src="/src/main.jsx"',           'The path to the JavaScript entry point. Vite processes this file and all its imports.'),
    ]
    items += kv_table(rows, col1=4.4)
    items.append(PageBreak())
    return items

# ─── SECTION 3: main.jsx ─────────────────────────────────────────────────────
def s3_main():
    items = h1("3. src/main.jsx — JavaScript Entry Point")
    items += file_banner("src/main.jsx", "First JavaScript file to run. Mounts React into the HTML page.")
    items.append(code(
        'import React from "react";\n'
        'import ReactDOM from "react-dom/client";\n'
        'import App from "./App.jsx";\n'
        'import "./index.css";\n\n'
        'ReactDOM.createRoot(document.getElementById("root")).render(\n'
        '  &lt;React.StrictMode&gt;\n'
        '    &lt;App /&gt;\n'
        '  &lt;/React.StrictMode&gt;\n'
        ');'
    ))
    rows = [
        ('import React',                  'Loads the React library. React is what lets us write JSX (the HTML-like syntax inside JavaScript).'),
        ('import ReactDOM',               'ReactDOM is the bridge between React and the real browser. React describes what the UI should look like; ReactDOM actually draws it.'),
        ('import App from "./App.jsx"',   'Loads our root component. The ./ means "same folder as this file".'),
        ('import "./index.css"',          'Loads the global CSS. Vite sees this import and bundles the CSS into the final build automatically.'),
        ('document.getElementById("root")', 'Finds the empty &lt;div id="root"&gt; from index.html in the live DOM.'),
        ('createRoot(...)',               'Tells React: "this div is where you will render everything". Creates an internal React root object.'),
        ('.render(&lt;App /&gt;)',         'Starts React rendering. It draws the App component inside the root div. From this point, React controls everything inside that div.'),
        ('React.StrictMode',             'A development-only wrapper that intentionally runs some things twice to catch bugs. Has zero effect in the production build.'),
    ]
    items += kv_table(rows, col1=4.8)
    items.append(note(
        "This file is almost never touched. It exists once, sets up React, and that is it. "
        "All real work happens in App.jsx and the components."
    ))
    items.append(PageBreak())
    return items

# ─── SECTION 4: index.css ────────────────────────────────────────────────────
def s4_css():
    items = h1("4. src/index.css — Global Styles & Animations")
    items += file_banner("src/index.css", "CSS that applies to the whole page. Also defines the keyframe animations.")
    items.append(h2("Reset rules"))
    items.append(code(
        'html, body, #root {\n'
        '  margin: 0;\n'
        '  height: 100%;\n'
        '  width: 100%;\n'
        '}'
    ))
    rows = [
        ('margin: 0',      'Browsers add a default margin around the &lt;body&gt; tag. This removes it. Without this, there would be a white gap around the entire app.'),
        ('height: 100%',   'Makes the html, body, and #root div all take up the full browser window height. Without this, the app would be 0px tall and invisible because its children have nothing to stretch into.'),
        ('width: 100%',    'Same principle for width — fills the full browser window width.'),
    ]
    items += kv_table(rows, col1=3.4)

    items.append(h2("Box sizing"))
    items.append(code('* { box-sizing: border-box; }'))
    items.append(body(
        "The * selector matches every single element on the page. "
        "border-box changes how width and height are calculated. "
        "By default (content-box), if you say an element is 200px wide and add 20px of padding, "
        "the element becomes 240px wide. With border-box, the padding is counted inside the 200px — "
        "the element stays 200px wide. This makes layout maths predictable."
    ))

    items.append(h2("Font smoothing"))
    items.append(code(
        '-webkit-font-smoothing: antialiased;\n'
        '-moz-osx-font-smoothing: grayscale;'
    ))
    items.append(body(
        "These two lines make text look sharper on Mac and iOS screens by smoothing the pixel edges "
        "of each letter. The -webkit- prefix applies to Chrome and Safari. The -moz- prefix applies to Firefox on Mac."
    ))

    items.append(h2(".tabular-nums — the money alignment class"))
    items.append(code('.tabular-nums { font-variant-numeric: tabular-nums; }'))
    items.append(body(
        "This is one of the most important professional details in the app. "
        "By default, fonts render digits at different widths — the digit '1' is narrower than '8'. "
        "This means a balance number like ₦1,290,340 would shift and wobble as it animates from 0 to "
        "its value, because each digit takes a different amount of space. "
        "tabular-nums forces every digit (0-9) to be exactly the same width, so numbers stay "
        "perfectly still as they change. Applied as a className on every financial figure."
    ))

    items.append(h2("Scrollbar styling"))
    items.append(code(
        '::-webkit-scrollbar { width: 8px; height: 8px; }\n'
        '::-webkit-scrollbar-track { background: transparent; }\n'
        '::-webkit-scrollbar-thumb { background: #d8d2c4; border-radius: 8px;\n'
        '                            border: 2px solid #F8F6F1; }\n'
        '::-webkit-scrollbar-thumb:hover { background: #c0bab0; }'
    ))
    rows = [
        ('::-webkit-scrollbar',        'Targets the scrollbar element itself. Sets its size to 8px (thin and unobtrusive).'),
        ('::-webkit-scrollbar-track',  'The background rail the thumb slides along. Transparent so the page shows through.'),
        ('::-webkit-scrollbar-thumb',  'The draggable scroll handle. Warm grey to match the page palette.'),
        ('border-radius: 8px',         'Rounds the thumb into a pill shape instead of a sharp rectangle.'),
        ('border: 2px solid #F8F6F1',  'Creates a gap between the thumb and track by applying the page background colour as a border. Makes it look "floating".'),
    ]
    items += kv_table(rows, col1=4.0)

    items.append(h2(".live-pulse-dot — the animated green dot"))
    items.append(code(
        '.live-pulse-dot {\n'
        '  width: 6px; height: 6px; border-radius: 6px;\n'
        '  background: #16A34A; display: inline-block;\n'
        '  animation: livePulse 1.8s ease-in-out infinite;\n'
        '}\n'
        '@keyframes livePulse {\n'
        '  0%, 100% { opacity: 1; transform: scale(1); }\n'
        '  50%       { opacity: 0.3; transform: scale(0.85); }\n'
        '}'
    ))
    rows = [
        ('border-radius: 6px',          'Equal to half the width/height, making the square div a perfect circle.'),
        ('display: inline-block',       'Allows a non-block element to have a set width and height.'),
        ('animation: livePulse 1.8s',   'Runs the livePulse keyframe animation over 1.8 seconds.'),
        ('ease-in-out',                 'The animation starts slow, speeds up in the middle, then slows again at the end. This makes the pulse feel organic, like breathing.'),
        ('infinite',                    'The animation loops forever until the element is removed from the page.'),
        ('@keyframes livePulse',        'Defines what happens at each point of the animation.'),
        ('0%, 100%',                    'At the start (0%) and end (100%) of each cycle, the dot is fully visible and full size.'),
        ('50%',                         'Halfway through, the dot fades to 30% opacity and shrinks to 85% size. Combined with the easing, this creates a gentle pulse.'),
    ]
    items += kv_table(rows, col1=3.8)

    items.append(h2(".bar-grow — the portfolio bar animation"))
    items.append(code(
        '.bar-grow {\n'
        '  animation: barGrow 0.9s cubic-bezier(0.2, 0.7, 0.2, 1) both;\n'
        '}\n'
        '@keyframes barGrow { from { width: 0 !important; } }'
    ))
    rows = [
        ('barGrow 0.9s',                       'Runs the barGrow animation over 0.9 seconds.'),
        ('cubic-bezier(0.2, 0.7, 0.2, 1)',     'A custom speed curve: starts very fast, decelerates smoothly. The bar shoots out and eases to a stop.'),
        ('both',                               'Applies the initial keyframe value (width:0) immediately, before the animation starts. Without this, the bar would flash at full width for one frame before animating.'),
        ('from { width: 0 !important; }',      'The starting state: zero width. !important overrides the inline style width that React sets, forcing the animation to always start from 0.'),
        ('(no "to" keyframe)',                 'When there is no "to" keyframe, the browser uses the element\'s natural width as the end state. The bar grows to whatever width the style prop sets.'),
    ]
    items += kv_table(rows, col1=4.4)
    items.append(PageBreak())
    return items

# ─── SECTION 5: mockData.js ──────────────────────────────────────────────────
def s5_mockdata():
    items = h1("5. src/data/mockData.js — All Raw Data")
    items += file_banner("src/data/mockData.js", "The single source of truth for all data displayed in the dashboard.")
    items.append(body(
        "Storing all data in one file means: when you connect a real API, you only change "
        "this one file. Nothing else needs to know where the data comes from."
    ))

    items.append(h2("CONNECTED_BANKS"))
    items.append(code(
        'export const CONNECTED_BANKS = [\n'
        '  {\n'
        '    id:            "access",\n'
        '    name:          "Access Bank",\n'
        '    shortName:     "Access",\n'
        '    brandColor:    "#E85C2B",\n'
        '    balance:       842500.75,\n'
        '    maskedAccount: "•••• 4471",\n'
        '    accountType:   "Savings",\n'
        '  },\n'
        '  // ... 4 more banks\n'
        '];'
    ))
    rows = [
        ('export const',    '"export" makes this variable available to other files. "const" means the array itself cannot be reassigned (though its contents can be read).'),
        ('id',              'A short unique string identifier for this bank. Used by transactions to say which bank they belong to (bankId: "access"). Must be unique across all banks.'),
        ('name',            'The full official bank name. Shown in the UI wherever there is enough space.'),
        ('shortName',       'The abbreviated name. Used on the mini cards in the hero section where there is very little space.'),
        ('brandColor',      'The bank\'s official hex colour code. Used as the background of the mini card, the initial badge, and the portfolio bar fill colour.'),
        ('balance',         'The account balance in Naira as a plain JavaScript number. Stored without formatting — the formatNaira() function handles display.'),
        ('maskedAccount',   'The partially hidden account number for privacy. The bullet characters (•) replace the first digits.'),
        ('accountType',     'Either "Savings" or "Current". Shown as a small label below the bank name on each card.'),
    ]
    items += kv_table(rows, col1=3.6)

    items.append(h2("TRANSACTIONS"))
    items.append(code(
        'export const TRANSACTIONS = [\n'
        '  {\n'
        '    id:          1,\n'
        '    bankId:      "stanbic",\n'
        '    description: "Salary — Andela",\n'
        '    category:    "Income",\n'
        '    amount:      1850000,\n'
        '    timestamp:   "Today, 09:12",\n'
        '    isOutgoing:  false,\n'
        '  },\n'
        '  // ... 9 more transactions\n'
        '];'
    ))
    rows = [
        ('id',           'A unique number for each transaction. React requires a unique "key" prop when rendering a list — this is what we use.'),
        ('bankId',       'The id of the bank this transaction belongs to. Matches one of the id values in CONNECTED_BANKS. The findBankById() helper uses this to look up the bank\'s name and colour.'),
        ('description',  'The human-readable transaction description shown in the UI (merchant name, transfer purpose, etc.).'),
        ('category',     'The spending category. Used in the full Transactions page to show a category column. Also used in Insights charts (stored in open-banking-app).'),
        ('amount',       'Always a positive number regardless of direction. The isOutgoing field determines whether money came in or went out.'),
        ('timestamp',    'A human-readable time string. In a real app, this would be an ISO 8601 date string that you format with a date library.'),
        ('isOutgoing',   'Boolean. true = money left the account (expense, shown in red). false = money came in (income, shown in green).'),
    ]
    items += kv_table(rows, col1=3.4)

    items.append(h2("NAV_ITEMS"))
    items.append(code(
        'export const NAV_ITEMS = [\n'
        '  { id: "overview",     label: "Overview"     },\n'
        '  { id: "transactions", label: "Transactions" },\n'
        '  { id: "insights",     label: "Insights"     },\n'
        '  { id: "banks",        label: "Banks"        },\n'
        '];'
    ))
    items.append(body(
        "The four navigation items shown in the sidebar. Each has an 'id' (used to identify "
        "which tab is active) and a 'label' (the text shown to the user). "
        "Icons are NOT stored here — they are in Sidebar.jsx where they are rendered, "
        "keeping data separate from UI. In the demo build only 'overview' is active."
    ))
    items.append(PageBreak())
    return items

# ─── SECTION 6: helpers.js ───────────────────────────────────────────────────
def s6_helpers():
    items = h1("6. src/utils/helpers.js — Utility Functions")
    items += file_banner("src/utils/helpers.js", "Pure functions that transform data. Reusable by any component.")
    items.append(body(
        "A pure function always returns the same result for the same input and has no side effects. "
        "These two functions are called throughout the app and are kept separate so any component "
        "can import them without importing the whole theme or data file."
    ))

    items.append(h2("formatNaira(amount, showDecimals = true)"))
    items.append(code(
        'import { CONNECTED_BANKS } from "../data/mockData";\n\n'
        'export function formatNaira(amount, showDecimals = true) {\n'
        '  const places = showDecimals ? 2 : 0;\n'
        '  return "\\u20A6" + amount.toLocaleString("en-NG", {\n'
        '    minimumFractionDigits: places,\n'
        '    maximumFractionDigits: places,\n'
        '  });\n'
        '}'
    ))
    rows = [
        ('export function',              'The "export" keyword makes this function importable by other files.'),
        ('amount',                       'The first parameter — the raw number to format (e.g. 842500.75).'),
        ('showDecimals = true',          'A default parameter. If the caller does not pass this second argument, it defaults to true. formatNaira(500) gives "₦500.00". formatNaira(500, false) gives "₦500".'),
        ('const places = showDecimals ? 2 : 0', 'A ternary expression — a compact if/else. If showDecimals is true, places = 2. If false, places = 0.'),
        ('toLocaleString("en-NG")',      'A built-in JavaScript method that formats a number according to the rules of a specific locale. "en-NG" is Nigerian English — it adds commas as thousand separators (1,000,000 not 1000000).'),
        ('minimumFractionDigits: places','At least this many decimal places. Ensures 500.50 never becomes 500.5.'),
        ('maximumFractionDigits: places','No more than this many decimal places. Ensures 500.999 becomes 501.00 not 500.999.'),
        ('"₦" +',                       'Prepends the Naira symbol. The + operator joins two strings together.'),
    ]
    items += kv_table(rows, col1=5.0)

    items.append(h2("findBankById(bankId)"))
    items.append(code(
        'export function findBankById(bankId) {\n'
        '  return (\n'
        '    CONNECTED_BANKS.find((bank) =&gt; bank.id === bankId) ||\n'
        '    { name: bankId, brandColor: "#64748B" }\n'
        '  );\n'
        '}'
    ))
    rows = [
        ('CONNECTED_BANKS.find()',      'The .find() method loops through the CONNECTED_BANKS array and returns the first item where the callback returns true.'),
        ('(bank) => bank.id === bankId','The callback function. For each bank object in the array, it checks if the bank\'s id property strictly equals the bankId argument.'),
        ('===',                         'Strict equality. Checks both value AND type. "access" === "access" is true. "access" === "Access" is false (case sensitive).'),
        ('||',                          'The OR operator. If .find() returns undefined (no match found), the expression after || is used instead.'),
        ('{ name: bankId, brandColor: "#64748B" }', 'A fallback object with a grey colour, returned if no bank is found. Prevents the app from crashing if a transaction references a bank that no longer exists.'),
    ]
    items += kv_table(rows, col1=4.8)
    items.append(PageBreak())
    return items

# ─── SECTION 7: useCountUp.js ────────────────────────────────────────────────
def s7_hook():
    items = h1("7. src/hooks/useCountUp.js — Animation Hook")
    items += file_banner("src/hooks/useCountUp.js", "Custom React hook. Animates a number from 0 to a target value.")
    items.append(body(
        "This hook is what makes the total balance '₦4,623,971.45' count up from zero when "
        "the dashboard loads. Custom hooks always start with 'use' — this is a React rule. "
        "They are functions that use React's built-in hooks (useState, useEffect) internally."
    ))
    items.append(code(
        'import { useState, useEffect } from "react";\n\n'
        'export function useCountUp(targetValue, durationMs = 1000) {\n'
        '  const [currentValue, setCurrentValue] = useState(0);\n\n'
        '  useEffect(() =&gt; {\n'
        '    let animationFrameId;\n'
        '    let startTimestamp;\n\n'
        '    function tick(timestamp) {\n'
        '      if (!startTimestamp) startTimestamp = timestamp;\n'
        '      const elapsed = timestamp - startTimestamp;\n'
        '      const rawProgress = Math.min(elapsed / durationMs, 1);\n'
        '      const easedProgress = 1 - Math.pow(1 - rawProgress, 3);\n'
        '      setCurrentValue(targetValue * easedProgress);\n'
        '      if (rawProgress &lt; 1) animationFrameId = requestAnimationFrame(tick);\n'
        '    }\n\n'
        '    animationFrameId = requestAnimationFrame(tick);\n'
        '    return () =&gt; cancelAnimationFrame(animationFrameId);\n'
        '  }, [targetValue, durationMs]);\n\n'
        '  return currentValue;\n'
        '}'
    ))
    rows = [
        ('useState(0)',                              'Creates a state variable called currentValue, starting at 0. Every time setCurrentValue is called with a new number, React re-renders the component showing the updated value.'),
        ('useEffect(() => { ... }, [...])',          'Runs the animation loop after every render where targetValue or durationMs changed. The function inside is the "effect".'),
        ('let animationFrameId',                    'Stores the ID of the pending animation frame so we can cancel it in the cleanup function.'),
        ('let startTimestamp',                      'Records the exact moment the animation began. Starts as undefined, gets set on the first tick.'),
        ('function tick(timestamp)',                'Called by the browser approximately 60 times per second. The browser passes the current time in milliseconds as "timestamp".'),
        ('if (!startTimestamp) startTimestamp = timestamp', 'On the very first call, timestamp is stored as the start time. After that, !startTimestamp is false so this line is skipped.'),
        ('elapsed = timestamp - startTimestamp',    'How many milliseconds have passed since the animation started.'),
        ('Math.min(elapsed / durationMs, 1)',       'Divides elapsed time by total duration to get progress (0.0 to 1.0). Math.min(..., 1) clamps it so progress never exceeds 1.0, even if the animation runs slightly over time.'),
        ('1 - Math.pow(1 - rawProgress, 3)',        'Cubic ease-out formula. When rawProgress is 0, result is 0. When rawProgress is 1, result is 1. But the curve is not straight — it accelerates quickly at the start and decelerates as it nears the end, like a ball rolling to a stop.'),
        ('setCurrentValue(targetValue * easedProgress)', 'Sets the displayed value to the target multiplied by how far through the eased curve we are.'),
        ('requestAnimationFrame(tick)',             'Schedules tick to be called again before the next screen repaint. This is what creates the smooth 60fps animation loop.'),
        ('return () => cancelAnimationFrame(...)',  'The cleanup function. When the component using this hook is removed from the page, this cancels any pending animation frame to prevent errors.'),
        ('[targetValue, durationMs]',               'The dependency array. useEffect re-runs when these values change. If the total balance changes (e.g. a bank is added), the animation restarts from the current value.'),
        ('return currentValue',                    'The hook returns the current animated value. The component using the hook receives this and displays it.'),
    ]
    items += kv_table(rows, col1=5.0)
    items.append(PageBreak())
    return items

# ─── SECTION 8: theme.js ─────────────────────────────────────────────────────
def s8_theme():
    items = h1("8. src/styles/theme.js — The Design System")
    items += file_banner("src/styles/theme.js", "Every colour, font, shadow, and layout style. One file controls all visuals.")
    items.append(body(
        "This file is imported by every component. Change one value here and it updates "
        "everywhere in the app instantly. This is called a 'single source of truth' for design."
    ))

    items.append(h2("COLORS"))
    color_rows = [
        ('ink: "#0A1628"',          'Deep navy. The darkest colour in the palette. Used for primary text, the sidebar background, and the hero card background.'),
        ('canvas: "#F8F6F1"',       'Warm off-white. The main page background. Slightly warm (not pure white) to reduce eye strain and feel premium.'),
        ('canvasDark: "#EFECE5"',   'A slightly darker warm white. Used for hover backgrounds and secondary surfaces.'),
        ('white: "#FFFFFF"',        'Pure white. Used for card backgrounds — creates contrast against the warm canvas.'),
        ('green: "#16A34A"',        'The brand green. Used for the logo, active navigation, CTA buttons, income indicators, and the live dot.'),
        ('greenPale: "#ECFDF5"',    'A very light green. Used as background tint behind green text — readable but not loud.'),
        ('red: "#F43F5E"',          'Alert red. Used only for outgoing transactions and the notification badge. Never used decoratively.'),
        ('redPale: "#FFF1F2"',      'Very light red. Used as the icon box background for outgoing transaction rows.'),
        ('blue: "#0EA5E9"',         'Sky blue. Reserved for the net cash flow stat card in the full Insights page.'),
        ('border: "#E8E4DC"',       'Warm grey border. Used on all cards. Slightly warm to match the canvas — pure grey would look out of place.'),
        ('borderLight: "#F2EFE8"',  'Even lighter border. Used for dividers inside cards (e.g. between transaction rows).'),
        ('mutedLight: "#94A3B8"',   'Slate grey. Used for meta text — timestamps, account numbers, section subtitles.'),
        ('muted: "#64748B"',        'Darker slate. Used for category labels and secondary information.'),
        ('sidebarText: "#C4CDD8"',  'Light blue-grey. The colour of text on the dark navy sidebar.'),
        ('sidebarMuted: "#7A8BA0"', 'Darker sidebar grey. Used for inactive navigation items.'),
    ]
    items += kv_table(color_rows, col1=4.0)

    items.append(h2("FONT"))
    items.append(code(
        'export const FONT = {\n'
        '  display: "\'Bricolage Grotesque\', system-ui, sans-serif",\n'
        '  body:    "\'Inter\', system-ui, sans-serif",\n'
        '};'
    ))
    items.append(body(
        "<b>FONT.display</b> (Bricolage Grotesque) is used for headings, the big balance number, section titles, "
        "and the brand name. It has personality and strong character weight contrast. "
        "<b>FONT.body</b> (Inter) is used for everything else — labels, body text, UI copy. "
        "It is neutral and highly legible at small sizes. "
        "<b>system-ui, sans-serif</b> are fallback fonts if Google Fonts fails to load — "
        "the OS system font is used instead."
    ))

    items.append(h2("SHADOW"))
    items.append(code(
        'export const SHADOW = {\n'
        '  card:      "0 1px 2px rgba(10,22,40,0.04), 0 4px 14px rgba(10,22,40,0.06)",\n'
        '  cardHover: "0 8px 32px rgba(10,22,40,0.14), 0 2px 6px rgba(10,22,40,0.06)",\n'
        '};'
    ))
    items.append(body(
        "Each shadow value follows the pattern: <b>x-offset y-offset blur-radius colour</b>. "
        "Two shadows are stacked with a comma — a close subtle shadow for definition, "
        "and a larger softer shadow for elevation. "
        "rgba(10,22,40,0.04) is the ink colour (10,22,40) at 4% opacity — the shadow is "
        "tinted to the brand colour rather than generic grey. "
        "On hover, the shadow intensifies and moves upward, giving the feeling that the card lifted."
    ))

    items.append(h2("S — the styles object (selected key styles explained)"))
    items.append(body(
        "S is a large JavaScript object. Each key holds an object of CSS properties "
        "in camelCase format. React converts camelCase to CSS kebab-case automatically: "
        "borderRadius becomes border-radius, backgroundColor becomes background-color."
    ))
    style_rows = [
        ('appShell: { display:"flex", height:"100vh", overflow:"hidden" }',
         'display:flex makes the sidebar and main column sit side by side horizontally. height:100vh fills the full browser window. overflow:hidden prevents double scrollbars.'),
        ('sidebar: { width:244, flexShrink:0 }',
         'Fixed 244px sidebar. flexShrink:0 prevents it from shrinking when the window gets smaller. Without this, the sidebar would compress.'),
        ('mainColumn: { flex:1, minWidth:0 }',
         'flex:1 tells this div to take all remaining horizontal space after the sidebar. minWidth:0 is a flex fix — without it, long text can overflow.'),
        ('pageScrollArea: { overflowY:"auto", flex:1 }',
         'overflowY:auto adds a scrollbar only when content is taller than the available space. flex:1 makes it fill all remaining vertical space below the topbar.'),
        ('heroCard: { borderRadius:24, padding:"40px 44px" }',
         '24px radius gives the hero card its rounded premium look. 40px top/bottom and 44px left/right padding gives generous breathing room around the content.'),
        ('heroGlowOrbGreen: { position:"absolute", pointerEvents:"none" }',
         'position:absolute takes the orb out of the layout flow — it overlays the hero card. pointerEvents:none means clicks pass through it to elements behind.'),
        ('bankCardFan: { display:"flex", flexShrink:0 }',
         'display:flex places the mini cards side by side. flexShrink:0 prevents the fan from being squished by the balance text on smaller screens.'),
        ('shareBarTrack: { height:5, overflow:"hidden" }',
         'A thin 5px track for the portfolio bar. overflow:hidden clips the bar fill to the track boundaries so the animated bar cannot overflow outside the track.'),
        ('shareBarFill: { transition:"width 1s cubic-bezier(.2,.7,.2,1)" }',
         'Smoothly animates the bar width when it first renders. The cubic-bezier curve makes it shoot out fast then ease to a stop.'),
        ('transactionListCard: { overflow:"hidden" }',
         'overflow:hidden on the card clips the hover background of each row to the card\'s rounded corners. Without this, the hover background would bleed outside the card corners.'),
    ]
    items += kv_table(style_rows, col1=5.4)
    items.append(PageBreak())
    return items

# ─── SECTION 9: Sidebar.jsx ──────────────────────────────────────────────────
def s9_sidebar():
    items = h1("9. src/components/Sidebar.jsx")
    items += file_banner("src/components/Sidebar.jsx", "The left navigation panel. Shows the brand, nav items, and security badge.")
    items.append(code(
        'import React from "react";\n'
        'import { motion } from "framer-motion";\n'
        'import { Wallet, LayoutDashboard, Receipt,\n'
        '         PieChart, Building2, ShieldCheck } from "lucide-react";\n'
        'import { S } from "../styles/theme";\n'
        'import { NAV_ITEMS } from "../data/mockData";'
    ))
    rows = [
        ('import React',            'Required for JSX to work. Every file that contains JSX must import React.'),
        ('import { motion }',       'Framer Motion\'s core. motion.div, motion.button etc. are animated versions of HTML elements.'),
        ('import { Wallet, ... }',  'Individual icon components from Lucide React. Each icon is a separate named export — we import only what we need.'),
        ('import { S }',            'The styles object from theme.js. Used as style={S.sidebar}, style={S.brandLogo} etc.'),
        ('import { NAV_ITEMS }',    'The array of navigation items from mockData.js. Looped over to render the nav buttons.'),
    ]
    items += kv_table(rows, col1=3.8)

    items.append(h2("NAV_ICONS lookup object"))
    items.append(code(
        'const NAV_ICONS = {\n'
        '  overview:     LayoutDashboard,\n'
        '  transactions: Receipt,\n'
        '  insights:     PieChart,\n'
        '  banks:        Building2,\n'
        '};'
    ))
    items.append(body(
        "This object maps tab ID strings to their corresponding Lucide icon components. "
        "Inside the nav loop, the icon is retrieved with NAV_ICONS[item.id]. "
        "Icons are stored here (not in mockData.js) because icon components are UI concerns, "
        "not data concerns. Keeping them separate prevents the data file from needing UI imports."
    ))

    items.append(h2("Props"))
    rows = [
        ('activeTab',   'A string — the ID of the currently active page ("overview"). Used to apply the active styles to the matching nav button.'),
        ('onNavigate',  'A function passed from App.jsx. Called with the tab ID when a nav button is clicked. In the demo build, this is a no-op function () => {}.'),
    ]
    items += kv_table(rows, col1=3.2)

    items.append(h2("The nav button render"))
    items.append(code(
        '{NAV_ITEMS.map((item) => {\n'
        '  const Icon = NAV_ICONS[item.id];\n'
        '  const isActive = activeTab === item.id;\n'
        '  return (\n'
        '    &lt;motion.button\n'
        '      key={item.id}\n'
        '      onClick={() =&gt; onNavigate(item.id)}\n'
        '      whileHover={{ x: 3 }}\n'
        '      whileTap={{ scale: 0.97 }}\n'
        '      transition={{ duration: 0.15 }}\n'
        '      style={{ ...S.navButton, ...(isActive ? S.navButtonActive : {}) }}\n'
        '    &gt;\n'
        '      &lt;Icon size={18} strokeWidth={isActive ? 2.4 : 2} /&gt;\n'
        '      &lt;span style={{ flex: 1 }}&gt;{item.label}&lt;/span&gt;\n'
        '      {isActive &amp;&amp; &lt;motion.span layoutId="navActiveIndicator" /&gt;}\n'
        '    &lt;/motion.button&gt;\n'
        '  );\n'
        '})}'
    ))
    rows = [
        ('.map((item) => ...)',          'Loops through the NAV_ITEMS array, returning a button element for each item.'),
        ('const Icon = NAV_ICONS[item.id]', 'Looks up the icon component. Stored in a variable starting with capital I so JSX renders it as a component (&lt;Icon /&gt;) not an HTML tag (&lt;icon /&gt;).'),
        ('const isActive = ...',         'True if the item\'s id matches the currently active tab.'),
        ('key={item.id}',                'React requires a unique key prop on every element in a list. It uses this to efficiently update only the changed items.'),
        ('whileHover={{ x: 3 }}',        'On hover, the button slides 3px to the right. Framer Motion automatically reverses this on mouse-out.'),
        ('whileTap={{ scale: 0.97 }}',   'On click, the button shrinks slightly to 97% size, giving tactile press feedback.'),
        ('{ ...S.navButton, ...(isActive ? S.navButtonActive : {}) }',
         'Spreads the base navButton styles, then spreads the active styles on top if isActive is true. The spread operator ... merges two objects, with later values overriding earlier ones.'),
        ('strokeWidth={isActive ? 2.4 : 2}', 'Active icons are slightly thicker (2.4 vs 2), making them visually heavier and more prominent.'),
        ('layoutId="navActiveIndicator"', 'Framer Motion magic. When the active tab changes, the green indicator dot slides from its old position to its new position rather than disappearing and reappearing. All elements with the same layoutId are connected.'),
    ]
    items += kv_table(rows, col1=4.8)
    items.append(PageBreak())
    return items

# ─── SECTION 10: TopBar.jsx ──────────────────────────────────────────────────
def s10_topbar():
    items = h1("10. src/components/TopBar.jsx")
    items += file_banner("src/components/TopBar.jsx", "The top header bar. Shows the page greeting, title, and action icons.")
    items.append(code(
        'export function TopBar() {\n'
        '  return (\n'
        '    &lt;header style={S.topBar}&gt;\n'
        '      &lt;div&gt;\n'
        '        &lt;div style={S.pageGreeting}&gt;Good morning, Tunde&lt;/div&gt;\n'
        '        &lt;h1 style={S.pageTitle}&gt;Your money, all banks&lt;/h1&gt;\n'
        '      &lt;/div&gt;\n'
        '      &lt;div style={S.topBarRight}&gt;\n'
        '        &lt;motion.button whileTap={{ scale: 0.93 }} style={S.iconButton}&gt;\n'
        '          &lt;Bell size={17} /&gt;\n'
        '          &lt;span style={S.notificationBadge} /&gt;\n'
        '        &lt;/motion.button&gt;\n'
        '        &lt;motion.button whileTap={{ scale: 0.93 }} style={S.iconButton}&gt;\n'
        '          &lt;Settings size={17} /&gt;\n'
        '        &lt;/motion.button&gt;\n'
        '        &lt;div style={S.avatarCircle}&gt;TA&lt;/div&gt;\n'
        '      &lt;/div&gt;\n'
        '    &lt;/header&gt;\n'
        '  );\n'
        '}'
    ))
    rows = [
        ('&lt;header&gt;',          'The semantic HTML element for the page header. Screen readers and search engines understand this is the page header.'),
        ('style={S.topBar}',        'Applies the topBar styles: flex layout, padding, bottom border, fixed background.'),
        ('style={S.pageGreeting}',  'Small green text above the title. Green colour matching the brand accent.'),
        ('&lt;h1&gt;',              'The most important heading on the page. There should be exactly one h1 per page — it tells search engines and screen readers the main topic.'),
        ('whileTap={{ scale: 0.93 }}', 'The bell and settings buttons shrink to 93% when clicked. This provides visual feedback that the button was pressed.'),
        ('size={17}',               'The icon size in pixels. 17px is the correct size for these utility icons — big enough to see, small enough not to dominate.'),
        ('&lt;span style={S.notificationBadge} /&gt;', 'A self-closing span with no content. It is just the red dot on the bell icon, positioned absolutely over the top-right corner.'),
        ('"TA"',                    'The initials of "Tunde Adeyemi" — the demo user. In a real app, this would be generated from the logged-in user\'s name.'),
        ('style={S.avatarCircle}',  'A square with border-radius:11 and the ink background. The initials are centred using display:grid and placeItems:center.'),
    ]
    items += kv_table(rows, col1=4.4)
    items.append(PageBreak())
    return items

# ─── SECTION 11: Pill.jsx ────────────────────────────────────────────────────
def s11_pill():
    items = h1("11. src/components/Pill.jsx")
    items += file_banner("src/components/Pill.jsx", "The small stat pill inside the hero card. Shows money in or money out.")
    items.append(code(
        'export function Pill({ icon: Icon, accentColor, label, value }) {\n'
        '  return (\n'
        '    &lt;div style={S.statPill}&gt;\n'
        '      &lt;span style={{ ...S.pillIconWrapper, background: accentColor + "22" }}&gt;\n'
        '        &lt;Icon size={15} color={accentColor} /&gt;\n'
        '      &lt;/span&gt;\n'
        '      &lt;div&gt;\n'
        '        &lt;div style={S.pillLabel}&gt;{label}&lt;/div&gt;\n'
        '        &lt;div style={S.pillValue} className="tabular-nums"&gt;{value}&lt;/div&gt;\n'
        '      &lt;/div&gt;\n'
        '    &lt;/div&gt;\n'
        '  );\n'
        '}'
    ))
    rows = [
        ('{ icon: Icon, accentColor, label, value }',
         'Destructuring the props object. "icon: Icon" renames the prop from "icon" to "Icon" (capital I) so JSX can render it as a component. The other props keep their original names.'),
        ('accentColor + "22"',
         'Appends "22" to a 6-digit hex colour, creating an 8-digit hex with an alpha channel. "22" in hex is approximately 13% opacity. This creates a lightly tinted icon background in the same colour as the icon itself.'),
        ('&lt;Icon size={15} color={accentColor} /&gt;',
         'Renders the icon component that was passed as a prop. size={15} sets it to 15px. The colour matches the accentColor prop.'),
        ('className="tabular-nums"',
         'Applies the .tabular-nums CSS class defined in index.css, ensuring the money value uses fixed-width digits so it does not wobble as numbers change.'),
    ]
    items += kv_table(rows, col1=5.0)
    items.append(body(
        "The Pill is used twice in OverviewPage: once for money in (green) and once for money out (pink). "
        "The same component handles both because it is parameterised — different accentColor and icon "
        "props produce visually distinct results."
    ))
    items.append(PageBreak())
    return items

# ─── SECTION 12: SectionHeader.jsx ──────────────────────────────────────────
def s12_sectionheader():
    items = h1("12. src/components/SectionHeader.jsx")
    items += file_banner("src/components/SectionHeader.jsx", "A reusable section title row with an optional action button.")
    items.append(code(
        'export function SectionHeader({ title, subtitle, actionLabel, onAction }) {\n'
        '  return (\n'
        '    &lt;div style={S.sectionHeaderRow}&gt;\n'
        '      &lt;div&gt;\n'
        '        &lt;h2 style={S.sectionTitle}&gt;{title}&lt;/h2&gt;\n'
        '        {subtitle &amp;&amp; &lt;div style={S.sectionSubtitle}&gt;{subtitle}&lt;/div&gt;}\n'
        '      &lt;/div&gt;\n'
        '      {actionLabel &amp;&amp; (\n'
        '        &lt;button style={S.sectionActionButton} onClick={onAction}&gt;\n'
        '          {actionLabel} &lt;ChevronRight size={14} /&gt;\n'
        '        &lt;/button&gt;\n'
        '      )}\n'
        '    &lt;/div&gt;\n'
        '  );\n'
        '}'
    ))
    rows = [
        ('{subtitle && ...}',   'Short-circuit evaluation. JavaScript evaluates left to right. If subtitle is falsy (undefined, null, empty string), the && stops and returns false — React renders nothing. If subtitle is truthy, the right side (the div) is rendered.'),
        ('{actionLabel && ...}','Same pattern for the action button. If no actionLabel is passed, no button renders. This makes the component flexible — some sections have actions, some do not.'),
        ('&lt;h2&gt;',          'The section heading level. h2 is second in importance after h1. Having correct heading hierarchy (h1 > h2 > h3) matters for accessibility.'),
        ('onClick={onAction}',  'Passes the onAction function to the button\'s click event. When clicked, onAction is called. In the dashboard-only build, this calls () => {} (does nothing).'),
        ('ChevronRight size={14}', 'A small right-pointing arrow icon next to the action label, indicating this is a navigation element.'),
    ]
    items += kv_table(rows, col1=3.8)
    items.append(PageBreak())
    return items

# ─── SECTION 13: TransactionRow.jsx ─────────────────────────────────────────
def s13_txnrow():
    items = h1("13. src/components/TransactionRow.jsx")
    items += file_banner("src/components/TransactionRow.jsx", "A single transaction row. Used in the Recent Activity list on the dashboard.")
    items.append(code(
        'export function TransactionRow({ transaction }) {\n'
        '  const bank = findBankById(transaction.bankId);\n'
        '  const isOutgoing = transaction.isOutgoing;\n\n'
        '  return (\n'
        '    &lt;motion.div\n'
        '      whileHover={{ background: "#FAFAF7" }}\n'
        '      transition={{ duration: 0.12 }}\n'
        '      style={S.transactionRow}\n'
        '    &gt;\n'
        '      &lt;span style={{\n'
        '        ...S.transactionIconBox,\n'
        '        background: isOutgoing ? COLORS.redPale : COLORS.greenPale,\n'
        '      }}&gt;\n'
        '        {isOutgoing\n'
        '          ? &lt;ArrowUpRight size={16} color={COLORS.red} /&gt;\n'
        '          : &lt;ArrowDownLeft size={16} color={COLORS.green} /&gt;\n'
        '        }\n'
        '      &lt;/span&gt;\n'
        '      &lt;div style={{ flex: 1, minWidth: 0 }}&gt;\n'
        '        &lt;div style={S.transactionName}&gt;{transaction.description}&lt;/div&gt;\n'
        '        &lt;div style={S.transactionMeta}&gt;\n'
        '          &lt;span style={{ ...S.colorDot, background: bank.brandColor }} /&gt;\n'
        '          {bank.name} · {transaction.timestamp}\n'
        '        &lt;/div&gt;\n'
        '      &lt;/div&gt;\n'
        '      &lt;div className="tabular-nums" style={{\n'
        '        ...S.transactionAmount,\n'
        '        color: isOutgoing ? COLORS.ink : "#15803D",\n'
        '      }}&gt;\n'
        '        {isOutgoing ? "\\u2212" : "+"}{formatNaira(transaction.amount)}\n'
        '      &lt;/div&gt;\n'
        '    &lt;/motion.div&gt;\n'
        '  );\n'
        '}'
    ))
    rows = [
        ('const bank = findBankById(transaction.bankId)',
         'Looks up the full bank object (name, colour) using the bankId string stored on the transaction. This is why we have the findBankById helper.'),
        ('const isOutgoing = transaction.isOutgoing',
         'Stored in a descriptive local variable to avoid repeating transaction.isOutgoing four times throughout the JSX.'),
        ('whileHover={{ background: "#FAFAF7" }}',
         'On hover the row gets a very slight warm background. The rest of the card is white — this subtle tint shows the row is interactive without being loud.'),
        ('transition={{ duration: 0.12 }}',
         '0.12 seconds is fast enough to feel instant but slow enough to notice. Background colour transitions that are too fast feel jarring.'),
        ('...S.transactionIconBox,',
         'Spreads all the base icon box styles (width, height, border-radius, display) then adds the background colour after, overriding it for each transaction.'),
        ('isOutgoing ? COLORS.redPale : COLORS.greenPale',
         'Ternary: if the transaction is outgoing, use the pale red background; otherwise use pale green. This applies to both the icon box and the icon colour.'),
        ('flex: 1, minWidth: 0',
         'flex:1 makes the description area take all available space between the icon and the amount. minWidth:0 is required for text-overflow:ellipsis to work inside a flex child.'),
        ('...S.colorDot, background: bank.brandColor',
         'A small coloured circle using the bank\'s brand colour. Placed before the bank name to make it visually scannable — the colour gives instant bank recognition.'),
        ('"−" : "+"',
         'Minus (−) for outgoing, plus (+) for incoming. The − is a proper minus sign (not a hyphen), which looks better typographically with numbers.'),
        ('color: isOutgoing ? COLORS.ink : "#15803D"',
         'Outgoing amounts are dark ink (neutral — you spent it). Incoming amounts are a deeper green than the brand green, making them feel like a positive financial event.'),
    ]
    items += kv_table(rows, col1=5.0)
    items.append(PageBreak())
    return items

# ─── SECTION 14: OverviewPage.jsx ────────────────────────────────────────────
def s14_overview():
    items = h1("14. src/pages/OverviewPage.jsx")
    items += file_banner("src/pages/OverviewPage.jsx", "The full dashboard page. Hero card, accounts grid, recent activity.")
    items.append(body(
        "This is the page your lecturer will see. It is assembled from smaller components "
        "and receives all its data as props from App.jsx."
    ))

    items.append(h2("Props received"))
    rows = [
        ('connectedBanks',        'The array of connected bank objects from App.jsx state.'),
        ('animatedTotalBalance',  'The animated (counting-up) version of the total balance, from the useCountUp hook.'),
        ('totalBalance',          'The actual total balance — used for percentage calculations (not shown directly).'),
        ('totalMoneyIn',          'The sum of all incoming transaction amounts for the month.'),
        ('totalMoneyOut',         'The sum of all outgoing transaction amounts for the month.'),
        ('onNavigate',            'A function to switch pages. In the demo build, this is () => {} and does nothing.'),
    ]
    items += kv_table(rows, col1=3.8)

    items.append(h2("cardVariants — named animation states"))
    items.append(code(
        'const cardVariants = {\n'
        '  hidden:  { opacity: 0, y: 16 },\n'
        '  visible: { opacity: 1, y: 0  },\n'
        '};'
    ))
    items.append(body(
        "Framer Motion variants define named animation states. Instead of writing "
        "initial={{ opacity:0, y:16 }} animate={{ opacity:1, y:0 }} on every card, "
        "we define the states once and pass them by name. Each bank card uses these "
        "variants and adds a staggered delay, creating a waterfall effect where cards "
        "appear one after another."
    ))

    items.append(h2("The hero card"))
    items.append(code(
        '&lt;motion.section\n'
        '  style={S.heroCard}\n'
        '  initial={{ opacity: 0, y: 20 }}\n'
        '  animate={{ opacity: 1, y: 0  }}\n'
        '  transition={{ duration: 0.35 }}\n'
        '&gt;\n'
        '  &lt;div style={S.heroGlowOrbGreen} /&gt;\n'
        '  &lt;div style={S.heroGlowOrbBlue} /&gt;\n'
        '  ...\n'
        '&lt;/motion.section&gt;'
    ))
    rows = [
        ('motion.section',                'A Framer Motion version of the semantic HTML &lt;section&gt; element.'),
        ('initial={{ opacity:0, y:20 }}', 'The card starts invisible and 20px below its final position.'),
        ('animate={{ opacity:1, y:0 }}',  'The card animates to full opacity and its natural position.'),
        ('transition={{ duration:0.35 }}','0.35 seconds — slow enough to be visible and satisfying, fast enough not to feel sluggish.'),
        ('heroGlowOrbGreen',              'An absolutely positioned div with a radial gradient. It creates the atmospheric green glow effect behind the balance number. It has no text or content — it is purely decorative.'),
        ('heroGlowOrbBlue',               'A second smaller blue glow orb in the bottom-left corner, adding depth and visual interest.'),
        ('position:"relative", zIndex:1', 'The text content (balance, pills, button) sits on a new stacking context above the glow orbs which have no z-index set.'),
    ]
    items += kv_table(rows, col1=4.2)

    items.append(h2("The balance number"))
    items.append(code(
        '&lt;div style={S.heroBalanceNumber} className="tabular-nums"&gt;\n'
        '  {formatNaira(animatedTotalBalance)}\n'
        '&lt;/div&gt;'
    ))
    items.append(body(
        "formatNaira(animatedTotalBalance) formats the current animation frame value. "
        "Because animatedTotalBalance changes ~60 times per second (from 0 to the real total), "
        "React re-renders this div on every frame, creating the counting effect. "
        "tabular-nums prevents the number from shifting sideways as digits change width."
    ))

    items.append(h2("The fanned bank cards"))
    items.append(code(
        '{connectedBanks.slice(0, 5).map((bank, index) => (\n'
        '  &lt;motion.div\n'
        '    key={bank.id}\n'
        '    whileHover={{ y: -12, zIndex: 10 }}\n'
        '    transition={{ duration: 0.22 }}\n'
        '    style={{\n'
        '      ...S.miniCard,\n'
        '      background: bank.brandColor,\n'
        '      marginLeft: index === 0 ? 0 : -38,\n'
        '      zIndex: index,\n'
        '      position: "relative",\n'
        '    }}\n'
        '  &gt;\n'
        '    ...\n'
        '  &lt;/motion.div&gt;\n'
        '))}'
    ))
    rows = [
        ('.slice(0, 5)',               'Takes the first 5 banks. slice(0, 5) returns elements at index 0, 1, 2, 3, 4. Even if there are 8 banks, only 5 fan cards show.'),
        ('index === 0 ? 0 : -38',     'The first card has no left margin. Every subsequent card overlaps the previous one by 38px (negative margin). This creates the stacked fan effect.'),
        ('zIndex: index',             'Later cards sit in front of earlier ones. index 0 is behind index 1, index 1 is behind index 2, etc. — correct visual stacking.'),
        ('whileHover={{ y:-12, zIndex:10 }}', 'On hover, the card rises 12px upward and jumps to the very front (zIndex 10). This lets users visually "pick up" each card to read it.'),
        ('position: "relative"',      'Required for zIndex to work on a flex item.'),
    ]
    items += kv_table(rows, col1=4.0)

    items.append(h2("The accounts grid"))
    items.append(code(
        '{connectedBanks.map((bank, index) => {\n'
        '  const portfolioPercentage = (bank.balance / totalBalance) * 100;\n'
        '  return (\n'
        '    &lt;motion.div\n'
        '      variants={cardVariants}\n'
        '      initial="hidden"\n'
        '      animate="visible"\n'
        '      transition={{ delay: index * 0.07, duration: 0.3 }}\n'
        '      whileHover={{ y: -4, boxShadow: SHADOW.cardHover }}\n'
        '      style={S.bankCard}\n'
        '    &gt;...'
    ))
    rows = [
        ('portfolioPercentage',       'The percentage of the total balance held in this bank. bank.balance / totalBalance gives a decimal (0.0 to 1.0), multiplied by 100 gives a percentage.'),
        ('variants={cardVariants}',   'Links this card to the cardVariants object defined at the top of the file.'),
        ('initial="hidden"',          'Starts in the "hidden" state: opacity 0, 16px below.'),
        ('animate="visible"',         'Animates to the "visible" state: opacity 1, natural position.'),
        ('delay: index * 0.07',       'Each card starts 70ms after the previous one. With 5 banks, the last card starts at 280ms. This creates a staggered cascade as the page loads.'),
        ('whileHover={{ y:-4, boxShadow:SHADOW.cardHover }}', 'The card lifts 4px and gets a deeper shadow on hover — communicating that it is interactive even without a click handler.'),
        ('portfolioPercentage.toFixed(1)', 'Formats the percentage to 1 decimal place. toFixed() returns a string, not a number.'),
    ]
    items += kv_table(rows, col1=4.0)

    items.append(h2("The recent activity list"))
    items.append(code(
        'const recentTransactions = TRANSACTIONS.slice(0, 5);\n\n'
        '{recentTransactions.map((transaction, index) => (\n'
        '  &lt;motion.div\n'
        '    key={transaction.id}\n'
        '    initial={{ opacity: 0, x: -10 }}\n'
        '    animate={{ opacity: 1, x: 0  }}\n'
        '    transition={{ delay: index * 0.06 }}\n'
        '  &gt;\n'
        '    &lt;TransactionRow transaction={transaction} /&gt;\n'
        '  &lt;/motion.div&gt;\n'
        '))}'
    ))
    items.append(body(
        "TRANSACTIONS.slice(0, 5) takes only the first 5 transactions — enough to show "
        "recent activity without making the page too long. Each row slides in from the left "
        "(x: -10 to x: 0) with a staggered delay of 60ms per row."
    ))
    items.append(PageBreak())
    return items

# ─── SECTION 15: App.jsx ─────────────────────────────────────────────────────
def s15_app():
    items = h1("15. src/App.jsx — Root Component")
    items += file_banner("src/App.jsx", "The root. Calculates derived data, renders the shell, passes props down.")
    items.append(body(
        "App.jsx is the top of the component tree. It is the only file that calculates "
        "the money totals and passes them down to the page. No state is managed here "
        "in the demo build — just derived values from the constant data."
    ))
    items.append(code(
        'import React, { useMemo } from "react";\n'
        'import { S } from "./styles/theme";\n'
        'import { CONNECTED_BANKS, TRANSACTIONS } from "./data/mockData";\n'
        'import { useCountUp } from "./hooks/useCountUp";\n'
        'import { Sidebar }      from "./components/Sidebar";\n'
        'import { TopBar }       from "./components/TopBar";\n'
        'import { OverviewPage } from "./pages/OverviewPage";\n\n'
        'export default function App() {\n'
        '  const totalBalance = useMemo(\n'
        '    () =&gt; CONNECTED_BANKS.reduce((sum, bank) =&gt; sum + bank.balance, 0),\n'
        '    []\n'
        '  );\n'
        '  const animatedTotalBalance = useCountUp(totalBalance);\n'
        '  const totalMoneyIn  = TRANSACTIONS.filter(t =&gt; !t.isOutgoing).reduce((s,t) =&gt; s+t.amount, 0);\n'
        '  const totalMoneyOut = TRANSACTIONS.filter(t =&gt;  t.isOutgoing).reduce((s,t) =&gt; s+t.amount, 0);\n\n'
        '  return (\n'
        '    &lt;div style={S.appShell}&gt;\n'
        '      &lt;Sidebar activeTab="overview" onNavigate={() =&gt; {}} /&gt;\n'
        '      &lt;div style={S.mainColumn}&gt;\n'
        '        &lt;TopBar /&gt;\n'
        '        &lt;div style={S.pageScrollArea}&gt;\n'
        '          &lt;OverviewPage\n'
        '            connectedBanks={CONNECTED_BANKS}\n'
        '            animatedTotalBalance={animatedTotalBalance}\n'
        '            totalBalance={totalBalance}\n'
        '            totalMoneyIn={totalMoneyIn}\n'
        '            totalMoneyOut={totalMoneyOut}\n'
        '            onNavigate={() =&gt; {}}\n'
        '          /&gt;\n'
        '        &lt;/div&gt;\n'
        '      &lt;/div&gt;\n'
        '    &lt;/div&gt;\n'
        '  );\n'
        '}'
    ))
    rows = [
        ('import { useMemo }',
         'useMemo is a React hook that caches a computed value and only recalculates it when its dependencies change.'),
        ('useMemo(() => CONNECTED_BANKS.reduce(...), [])',
         'Calculates totalBalance once and caches it. The empty array [] means "no dependencies" — recalculate never (only once on mount). .reduce() loops through all banks, adding each balance to the running sum starting at 0.'),
        ('useCountUp(totalBalance)',
         'Calls the custom hook. It returns a value that counts from 0 to totalBalance over 1 second. React re-renders the component on every animation frame, displaying the intermediate values.'),
        ('TRANSACTIONS.filter(t => !t.isOutgoing)',
         'Creates a new array containing only the non-outgoing (incoming) transactions. .filter() never modifies the original array.'),
        ('.reduce((sum, t) => sum + t.amount, 0)',
         'Sums up all the amounts in the filtered array. Starts from 0, adds each transaction\'s amount to the running total.'),
        ('activeTab="overview"',
         'Hardcoded string — tells the Sidebar to always highlight the Overview nav item. The app only shows the Overview page.'),
        ('onNavigate={() => {}}',
         'A no-op (does nothing) function. Passed where a navigation function is expected. Clicking nav items will call this and nothing will happen — appropriate for the demo.'),
        ('export default function App',
         '"export default" means this is the main export of the file. Other files import it without curly braces: import App from "./App.jsx".'),
    ]
    items += kv_table(rows, col1=5.0)
    items.append(PageBreak())
    return items

# ─── SECTION 16: Framer Motion guide ────────────────────────────────────────
def s16_framer():
    items = h1("16. Framer Motion Animations — Full Guide")
    items += file_banner("framer-motion", "The animation library. Installed with: npm install framer-motion")
    items.append(body(
        "Framer Motion is a production-ready animation library for React. "
        "It handles physics-based springs, enter/exit transitions, layout animations, "
        "and gesture interactions — all with a clean, declarative API."
    ))

    patterns = [
        ("motion.div / motion.button / motion.section",
         "Replace any HTML tag prefix with 'motion.' to make it animatable. "
         "motion.div is an animated div. motion.button is an animated button. All normal HTML attributes still work.",
         '&lt;motion.div style={myStyle} /&gt;  ← exactly like a div, but with animation props'),
        ("initial and animate",
         "initial = the state before the element appears on screen. "
         "animate = the state it transitions to. The difference between the two is what gets animated.",
         '&lt;motion.div initial={{ opacity:0, y:20 }} animate={{ opacity:1, y:0 }} /&gt;'),
        ("transition",
         "Controls the timing and physics of the animation. duration (seconds), ease (curve name or bezier array), "
         "delay (seconds before starting), type:'spring' for physics-based motion.",
         'transition={{ duration: 0.3, delay: 0.1, ease: "easeOut" }}'),
        ("type: 'spring'",
         "Uses a physics simulation instead of a timed curve. Feels natural and physical. "
         "stiffness controls how tight/fast the spring is. damping controls how quickly it stops bouncing.",
         'transition={{ type:"spring", stiffness:340, damping:28 }}'),
        ("whileHover",
         "Animation state applied while the mouse cursor is hovering over the element. "
         "Automatically reverses when the cursor leaves.",
         '&lt;motion.div whileHover={{ y:-4, boxShadow:"..." }} /&gt;'),
        ("whileTap",
         "Animation state applied while the element is being pressed/clicked. "
         "Automatically reverses on release.",
         '&lt;motion.button whileTap={{ scale:0.96 }} /&gt;'),
        ("variants",
         "Named animation states defined outside the JSX. Reference by name instead of inline objects. "
         "Enables parent-to-child orchestration.",
         'const v = { hidden:{opacity:0}, visible:{opacity:1} }\n'
         '&lt;motion.div variants={v} initial="hidden" animate="visible" /&gt;'),
        ("staggerChildren",
         "Used in a parent's transition variants. Delays each child's animation start by the given number of seconds. "
         "Creates a waterfall/cascade effect.",
         'variants={{ visible: { transition: { staggerChildren: 0.07 } } }}'),
        ("layoutId",
         "Connects elements that share the same layoutId across renders. "
         "When the active nav item changes, the green indicator dot slides from one position to another — "
         "Framer Motion handles the in-between animation automatically.",
         '&lt;motion.span layoutId="navActiveIndicator" /&gt;'),
    ]
    for name, explanation, example in patterns:
        items.append(KeepTogether([
            h3(name),
            body(explanation),
            code(example),
            sp(0.1),
        ]))
    items.append(PageBreak())
    return items

# ─── SECTION 17: Design decisions ───────────────────────────────────────────
def s17_design():
    items = h1("17. Design Decisions Explained")
    items.append(body(
        "Every visual choice is intentional. Here is the thinking behind each decision."
    ))
    decisions = [
        ("Warm canvas background (#F8F6F1)",
         "Pure white (#FFFFFF) is harsh under fluorescent office lights and causes eye fatigue. "
         "A warm off-white feels premium — used by Apple, Notion, Linear, and high-end finance apps. "
         "The slight warmth (yellow tint) also complements the green brand accent."),
        ("Two fonts only — Bricolage Grotesque + Inter",
         "More than two fonts creates visual chaos. Bricolage Grotesque has personality and contrast — "
         "it creates drama at large sizes (the balance number). Inter is neutral and legible at small sizes. "
         "The tension between the expressive display font and the neutral body font creates hierarchy."),
        ("24px border radius on cards, 18px on transaction card",
         "Larger rounded corners feel modern and approachable. Banks are traditionally cold and rectangular — "
         "the generous radius makes Kobo feel like a fintech app, not a bank. "
         "All card corners use the same radius for visual consistency."),
        ("Green as the only accent colour",
         "One accent colour creates visual clarity. Green is universally associated with money, growth, and health. "
         "Red appears only for outgoing transactions and the notification badge — it is never decorative. "
         "Using red sparingly preserves its meaning as an alert."),
        ("Two-layer card shadows",
         "One shadow layer close to the card gives it definition (where the card ends). "
         "One shadow layer far from the card gives it elevation (how high it floats). "
         "Single-layer shadows look flat. Three-layer shadows look overdone. Two is the sweet spot."),
        ("accentColor + '22' for icon backgrounds",
         "The icon sits on a background of the same colour at 13% opacity. This creates visual harmony — "
         "the icon 'glows' in its own colour tint. Used in stat pills, insight cards, and the modal. "
         "This pattern is used by Linear, Notion, and Apple's system icons."),
        ("tabular-nums on all financial figures",
         "Without this, digits like '1' and '8' are different widths. A balance number wobbles sideways "
         "as it counts up because each new digit takes different space. tabular-nums forces all digits "
         "to the same width — professional and undistracting."),
        ("40px page padding (sides), 36px top, 56px bottom",
         "More white space equals more premium. The original code used 26px. 40px gives each element "
         "room to breathe. The extra bottom padding (56px) prevents content from feeling crammed "
         "against the bottom of the viewport when scrolled to the bottom."),
        ("Negative marginLeft on fanned mini cards",
         "The overlapping bank card fan is the signature element of the app. It communicates "
         "'multiple accounts, one view' instantly without any text. Good UI communicates with shape before words. "
         "The hover behaviour (rising 12px, moving to front) makes the fan feel interactive."),
        ("Staggered entrance animations for lists and cards",
         "When all items appear simultaneously, the eye has nowhere to focus. When items appear in sequence "
         "(70ms apart for cards, 60ms apart for transaction rows), the eye naturally follows the cascade "
         "downward. This makes the UI feel alive and purposeful."),
    ]
    for title, explanation in decisions:
        items.append(KeepTogether([
            h3(title),
            body(explanation),
            sp(0.05),
        ]))

    items.append(sp(0.6))
    tbl = Table([[
        Paragraph(
            "You now understand every single line of code in the Kɔbo dashboard. "
            "Every import, every prop, every style property, every animation. "
            "Run it with npm run dev.",
            ps("Final", fontName="Helvetica-BoldOblique", fontSize=13,
               textColor=WHITE, alignment=TA_CENTER, leading=20)
        )
    ]], colWidths=[PAGE_W])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), GREEN),
        ("PADDING",(0,0),(-1,-1), 24),
    ]))
    items.append(tbl)
    return items

# ─── PAGE FOOTER ─────────────────────────────────────────────────────────────
def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(2.4*cm, 1.3*cm, "Kɔbo Dashboard — Complete Code Reference")
    canvas.drawRightString(W - 2.4*cm, 1.3*cm, f"Page {doc.page}")
    canvas.restoreState()

# ─── BUILD ────────────────────────────────────────────────────────────────────
story = []
story += cover()
story += toc()
story += s1_structure()
story += s2_html()
story += s3_main()
story += s4_css()
story += s5_mockdata()
story += s6_helpers()
story += s7_hook()
story += s8_theme()
story += s9_sidebar()
story += s10_topbar()
story += s11_pill()
story += s12_sectionheader()
story += s13_txnrow()
story += s14_overview()
story += s15_app()
story += s16_framer()
story += s17_design()

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f"PDF saved: {OUTPUT}")
