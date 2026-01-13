
import os

# --- TEMPLATE PARTS ---

CSS = """
    * { margin: 0; padding: 0; box-sizing: border-box; }

    :root {
      /* Colors */
      --color-bg-paper: #ffffff;
      --color-bg-tool: #fcfcfc;
      --color-text-main: #111111;
      --color-text-muted: #666666;
      --color-border: #e0e0e0;
      --color-border-strong: #000000;
      --color-accent: #000000;
      --color-highlight: #fff000;

      /* Source Colors (Repurposed for Project Themes) */
      --color-padayon: #4285f4;    /* Blue */
      --color-robosoccer: #d97706; /* Orange */
      --color-segue: #10a37f;      /* Green */
      --color-simala: #8b5cf6;     /* Purple */
      --color-connect4: #06b6d4;   /* Cyan */
      --color-yc: #f26522;         /* YC Orange */

      /* Spacing */
      --space-xs: 4px;
      --space-s: 8px;
      --space-m: 16px;
      --space-l: 24px;
      --space-xl: 40px;

      /* Typography */
      --font-main: -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
    }

    body {
      font-family: var(--font-main);
      font-size: 13px;
      background: var(--color-bg-paper);
      color: var(--color-text-main);
      height: 100vh;
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    .split-container {
      display: flex;
      height: 100vh;
    }

    /* LEFT: Narrative Side (Paper) */
    .paper-side {
      width: 60vw;
      height: 100vh;
      overflow-y: auto;
      padding: var(--space-xl);
      border-right: 2px solid var(--color-border-strong);
      background: var(--color-bg-paper);
    }

    .paper-header {
      margin-bottom: var(--space-l);
      padding-bottom: var(--space-m);
      border-bottom: 2px solid var(--color-border-strong);
    }

    .paper-title {
      font-size: 24px;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: -0.5px;
    }

    .paper-meta {
      font-size: 11px;
      color: var(--color-text-muted);
      text-transform: uppercase;
      letter-spacing: 1px;
      font-family: var(--font-mono);
      margin-top: 8px;
    }

    .section {
      margin-bottom: 40px;
    }

    .section-title {
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      border-bottom: 2px solid var(--color-border-strong);
      padding-bottom: var(--space-s);
      margin-bottom: var(--space-m);
    }

    .section p {
      line-height: 1.8;
      margin-bottom: 16px;
      font-size: 14px;
      text-align: left;
      color: #333;
    }

    .section ul {
      margin-left: 20px;
      margin-bottom: 16px;
    }

    .section li {
      margin-bottom: 8px;
      line-height: 1.6;
    }

    strong {
        font-weight: 700;
        color: #000;
    }

    /* RIGHT: Meta Side (Tool) */
    .tool-side {
      position: fixed;
      right: 0;
      top: 0;
      width: 40vw;
      height: 100vh;
      background: var(--color-bg-tool);
      display: flex;
      flex-direction: column;
      border-left: 2px solid var(--color-border-strong); /* Ensure border if overlapping */
    }

    .tool-header {
      background: var(--color-bg-paper);
      border-bottom: 2px solid var(--color-border-strong);
      padding: 16px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .tool-title {
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 1px;
      font-size: 12px;
    }

    .tool-content {
      flex: 1;
      padding: 32px;
      overflow-y: auto;
    }

    .project-thumbnail {
      width: 100%;
      height: auto;
      aspect-ratio: 16/9;
      object-fit: cover;
      border: 2px solid var(--color-border-strong);
      margin-bottom: 24px;
      background: #eee;
      display: block;
    }

    .meta-block {
      margin-bottom: 32px;
    }

    .meta-label {
      font-family: var(--font-mono);
      font-size: 10px;
      text-transform: uppercase;
      color: var(--color-text-muted);
      margin-bottom: 12px;
      letter-spacing: 1px;
      display: block;
    }

    .tech-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .tech-tag {
      font-family: var(--font-mono);
      font-size: 10px;
      padding: 6px 10px;
      border: 1px solid var(--color-border-strong);
      background: #fff;
      text-transform: uppercase;
    }

    .action-btn {
      display: block;
      width: 100%;
      padding: 14px;
      text-align: center;
      background: var(--color-view-project, #000);
      color: #fff;
      text-decoration: none;
      text-transform: uppercase;
      font-weight: 700;
      font-size: 12px;
      letter-spacing: 1px;
      border: none; /* 2px solid #000; */
      margin-bottom: 12px;
      transition: all 0.2s;
    }

    .action-btn:hover {
      opacity: 0.8;
      transform: translateY(-2px);
    }

    .action-btn.secondary {
        background: transparent;
        color: #000;
        border: 2px solid var(--color-border-strong);
    }

    .action-btn.secondary:hover {
        background: #000;
        color: #fff;
    }

    .stat-row {
      display: flex;
      justify-content: space-between;
      border-bottom: 1px solid var(--color-border);
      padding: 8px 0;
      font-family: var(--font-mono);
      font-size: 11px;
    }

    .stat-value {
      font-weight: 700;
    }

    /* Panel Toggle Controls */
    .panel-toggle-bar {
      position: fixed;
      top: 50%;
      left: 60%; /* Matches paper-side width */
      transform: translate(-50%, -50%);
      z-index: 1000;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0;
      background: var(--color-accent);
      border-radius: 20px;
      width: 16px;
      height: 16px;
      overflow: hidden;
      transition: all 1s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
      box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }

    .panel-toggle-bar:hover {
      width: 120px;
      height: 36px;
      gap: 4px;
      padding: 0 8px;
    }

    .panel-toggle-btn {
      width: 0;
      height: 24px;
      background: transparent;
      border: none;
      color: #fff;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 4px;
      opacity: 0;
      transition: all 1s cubic-bezier(0.16, 1, 0.3, 1);
      overflow: hidden;
      padding: 0;
      font-size: 14px;
    }

    .panel-toggle-bar:hover .panel-toggle-btn {
      width: 32px;
      opacity: 1;
    }

    .panel-toggle-btn svg { width: 16px; height: 16px; flex-shrink: 0; }

    /* Panel States */
    .split-container.left-expanded .paper-side { width: 90vw; }
    .split-container.left-expanded .tool-side { width: 10vw; }
    .split-container.right-expanded .tool-side { width: 90vw; }
    .split-container.right-expanded .paper-side { width: 10vw; }

    .paper-side, .tool-side { transition: width 1s cubic-bezier(0.16, 1, 0.3, 1); }

    .split-container.left-expanded .panel-toggle-bar { left: 90vw; }
    .split-container.right-expanded .panel-toggle-bar { left: 10vw; }

    /* Mobile */
    @media (max-width: 900px) {
      .split-container { flex-direction: column; }
      .paper-side { width: 100% !important; height: auto; padding: 20px; overflow: visible; }
      .tool-side { width: 100% !important; height: auto; position: relative; }
      .panel-toggle-bar { display: none; }
    }
"""

TEMPLATE_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    {css}
    :root {{ --color-view-project: var(--color-{theme_key}); }}
  </style>
</head>
<body>
  <div class="split-container" id="splitContainer">
    <!-- Panel Toggle Bar -->
    <div class="panel-toggle-bar" id="panelToggleBar">
      <button class="panel-toggle-btn" id="expandLeftBtn" title="Expand Narrative">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
      </button>
      <button class="panel-toggle-btn" id="resetBtn" title="Reset View">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
      </button>
      <button class="panel-toggle-btn" id="expandRightBtn" title="Expand Details">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
      </button>
    </div>

    <!-- LEFT: Narrative -->
    <div class="paper-side">
      <div class="paper-header">
        <div style="font-family: var(--font-mono); font-size: 10px; color: var(--color-text-muted); margin-bottom: 8px;">PROJECT / {type}</div>
        <h1 class="paper-title">{title}</h1>
        <div class="paper-meta">{date} • {role}</div>
      </div>

      {content}

    </div>

    <!-- RIGHT: Meta -->
    <div class="tool-side">
      <div class="tool-header">
        <span class="tool-title">Project Details</span>
        <a href="../portfolio.html" style="text-decoration: none; color: #000; font-weight: 700; font-size: 10px; text-transform: uppercase;">✕ Close</a>
      </div>

      <div class="tool-content">
        <img src="{image_path}" class="project-thumbnail" alt="Project Thumbnail" onerror="this.style.display='none'">

        <div class="meta-block">
            <a href="{link_url}" target="_blank" class="action-btn">Visit Project ↗</a>
            {extra_buttons}
        </div>

        <div class="meta-block">
          <span class="meta-label">At a Glance</span>
          <div class="stat-row">
            <span>Role</span>
            <span class="stat-value">{role}</span>
          </div>
          <div class="stat-row">
            <span>Timeline</span>
            <span class="stat-value">{timeline}</span>
          </div>
          <div class="stat-row">
            <span>Team</span>
            <span class="stat-value">{team_size}</span>
          </div>
           <div class="stat-row">
            <span>Key Metric</span>
            <span class="stat-value">{metric}</span>
          </div>
        </div>

        <div class="meta-block">
          <span class="meta-label">Technology Stack</span>
          <div class="tech-tags">
            {tech_tags}
          </div>
        </div>

        <div class="meta-block">
          <span class="meta-label">Awards & Recognition</span>
          <ul style="list-style: none; padding: 0; font-size: 11px; line-height: 1.6;">
            {awards_list}
          </ul>
        </div>

      </div>
    </div>
  </div>

  <script>
    // Panel Toggle Functionality
    (function() {{
      const container = document.getElementById('splitContainer');
      const expandLeftBtn = document.getElementById('expandLeftBtn');
      const expandRightBtn = document.getElementById('expandRightBtn');
      const resetBtn = document.getElementById('resetBtn');

      expandLeftBtn.addEventListener('click', function(e) {{
        e.stopPropagation();
        container.classList.remove('right-expanded');
        container.classList.toggle('left-expanded');
      }});

      expandRightBtn.addEventListener('click', function(e) {{
        e.stopPropagation();
        container.classList.remove('left-expanded');
        container.classList.toggle('right-expanded');
      }});

      resetBtn.addEventListener('click', function(e) {{
        e.stopPropagation();
        container.classList.remove('left-expanded', 'right-expanded');
      }});
    }})();
  </script>
</body>
</html>
"""

# --- PROJECT DATA ---

projects = {
    "padayon-ko": {
        "title": "Padayon Ko: AI-Powered Scholarship Platform",
        "type": "SOCIAL IMPACT / AI",
        "date": "2021-2025",
        "role": "Founder & Lead Engineer",
        "timeline": "4 Years (2021-2025)",
        "team_size": "Solo Founder",
        "metric": "500+ Students Helped",
        "image_path": "../padayon_preview.webp",
        "link_url": "#", # Placeholder as per instructions mostly
        "theme_key": "padayon",
        "tech": ["Python", "Google Cloud Run", "Vector Embeddings", "Gemini API", "Notion API", "Webflow"],
        "awards": [
            "🏆 Google AI for Impact Hackathon Winner ($8K Prize)",
            "🌟 Times Square Billboard Feature by Webflow",
            "🚀 Kaggle 'Tech for Better Education' Top 10",
            "🏫 Officially Adopted by STEC Student Gov"
        ],
        "content": """
        <div class="section">
            <h2 class="section-title">Overview</h2>
            <p><strong>"Padayon Ko"</strong> (Cebuano for "I will continue") is the Philippines' premier AI-powered scholarship matching platform. Born from my own struggle to fund my education—eventually securing $95,050 in personal scholarships—it evolved from a simple Notion tracker into a sophisticated AI system that has now helped over 500 students secure 200+ scholarships.</p>
            <p>The platform democratizes access to educational funding by using semantic vector search to match students with opportunities based on their unique stories, not just their grades.</p>
        </div>
        <div class="section">
            <h2 class="section-title">Key Innovation</h2>
            <p>Unlike traditional keyword-based scholarship finders, Padayon Ko uses <strong>vector embeddings (Sentence Transformers)</strong> to understand the semantic context of a student's profile. It analyzes qualitative data—essays, life experiences, and aspirations—to find hidden opportunities that a keyword search would miss.</p>
            <p>The system also integrates <strong>Multimodal AI</strong> (Google Chirp & Whisper) to support voice interaction in English, Tagalog, and Cebuano, breaking language barriers for students in rural provinces.</p>
        </div>
        <div class="section">
            <h2 class="section-title">Technical Architecture</h2>
            <p>The platform is a production-grade system built on <strong>Google Cloud Run</strong> using <strong>FastAPI</strong>. It leverages Notion as a headless CMS, allowing for a "no-code" admin interface that non-technical volunteers can manage, while the Python backend handles the heavy lifting of vector similarity search and real-time scraping.</p>
        </div>
        <div class="section">
            <h2 class="section-title">Impact</h2>
            <ul>
                <li><strong>Systemic Change:</strong> Transformed from a personal tool to an institutional program adopted by the STEC Senior High School Student Government.</li>
                <li><strong>Financial Impact:</strong> Facilitated hundreds of thousands of dollars in educational funding for underserved students.</li>
                <li><strong>Global Validation:</strong> Recognized by Webflow (Times Square Feature) and Google (Hackathon Winner) as a model for AI in social impact.</li>
            </ul>
        </div>
        """
    },
    "robosoccer": {
        "title": "WRO RoboSoccer: Autonomous PID Control System",
        "type": "ROBOTICS / ENGINEERING",
        "date": "2016-2019",
        "role": "Team Captain & Algorithm Engineer",
        "timeline": "4 Years",
        "team_size": "3 Members",
        "metric": "World Rank #6 (Bracket)",
        "image_path": "../robosoccer_preview.png",
        "link_url": "https://www.youtube.com/watch?v=bjiHhMB94G4",
        "theme_key": "robosoccer",
        "tech": ["LEGO EV3", "PID Control Theory", "C++ (RobotC)", "Sensor Fusion", "Algorithm Design"],
        "awards": [
            "🌎 6th Place - WRO World Finals 2019 (Hungary)",
            "🇵🇭 3rd Place - Philippine Robotics Olympiad",
            "🥇 1st Place - Lapu-Lapu City Division",
            "🏅 Philippine National Team Representative"
        ],
        "content": """
        <div class="section">
            <h2 class="section-title">The Challenge</h2>
            <p>World Robotics Olympiad (WRO) Football involves two fully autonomous robots per team playing soccer against an opponent. Once the match starts, human intervention is forbidden. The robots must detect an IR-emitting ball, navigate a field, avoid opponents, and score goals entirely on their own.</p>
        </div>
        <div class="section">
            <h2 class="section-title">Engineering Solution</h2>
            <p>As team captain and lead programmer, I self-taught university-level <strong>Control Theory</strong> to implement a custom <strong>PID (Proportional-Integral-Derivative) Controller</strong>. This algorithm allowed our robots to:</p>
            <ul>
                <li><strong>Track the ball</strong> with 360-degree IR sensor arrays while smoothing out noise.</li>
                <li><strong>Correct trajectory</strong> in real-time (20Hz loop) to account for wheel slippage and motor variance.</li>
                <li><strong>Coordinate strategy</strong> between "Striker" and "Goalie" roles.</li>
            </ul>
        </div>
        <div class="section">
            <h2 class="section-title">Journey to World Finals</h2>
            <p>Our custom algorithm propelled us from local underdogs to the global stage. After securing the Division Championship (1st Place) and the National Bronze Medal (3rd Place), we represented the Philippines at the <strong>WRO 2019 World Finals in Gyor, Hungary</strong>.</p>
            <p>Competing against 40+ countries, our team placed <strong>6th in our bracket</strong>, proving that high-level engineering could bloom from self-directed learning.</p>
        </div>
        """
    },
    "segue": {
        "title": "Segue MediRecords: Decentralized EMR System",
        "type": "HEALTHCARE / PRODUCT",
        "date": "2021-2023",
        "role": "Product Creator",
        "timeline": "2 Years",
        "team_size": "Lead + 3 Researchers",
        "metric": "1,300+ Research Reads",
        "image_path": "../segue_preview.png",
        "link_url": "https://notion.so/segue",
        "theme_key": "segue",
        "tech": ["Notion System", "Automation", "Healthcare UX", "Data Privacy (SOC 2)", "Product Management"],
        "awards": [
            "📄 Published Research (DOI: 10.13140/RG.2.2.15577.80481)",
            "🩺 Endorsed by Practicing Physicians",
            "🚀 ProductHunt Launch (Nov 2021)",
            "🎤 Presented at UP Cebu Congress"
        ],
        "content": """
        <div class="section">
            <h2 class="section-title">The Problem</h2>
            <p>In the Philippines, 67% of solo practice physicians still use paper records because EMR (Electronic Medical Record) systems are prohibitively expensive and complex. This disjointed data leads to medical errors and inefficient care.</p>
        </div>
        <div class="section">
            <h2 class="section-title">The Solution</h2>
            <p><strong>Segue MediRecords</strong> is a "freemium" decentralized EMR built entirely on Notion. It provides enterprise-grade structure—patient databases, consultation logs, lab results—without the enterprise price tag.</p>
            <p>By leveraging Notion's SOC 2 Type 2 compliant infrastructure, Segue offers a secure, HIPAA-aligned environment for doctors to digitize their practice in minutes, not months.</p>
        </div>
        <div class="section">
            <h2 class="section-title">Clinical Validation</h2>
            <p>The system was rigorously tested with practicing OB-GYNs and Pediatricians, achieving high usability scores. The project was published as a research paper ("Segue MediRecords") reaching <strong>1,300+ reads on ResearchGate</strong>, validating the model of low-code tools as viable healthcare infrastructure.</p>
        </div>
        """
    },
    "simala": {
        "title": "Overwatch Map Concept: Simala Sanctuary",
        "type": "CREATIVE / GAME DESIGN",
        "date": "2020",
        "role": "Concept Artist & Composer",
        "timeline": "3 Months",
        "team_size": "Solo",
        "metric": "National TV Feature",
        "image_path": "../simala_preview.webp",
        "link_url": "#",
        "theme_key": "simala",
        "tech": ["Photoshop", "After Effects", "Music Composition (DAW)", "Digital Matte Painting", "Worldbuilding"],
        "awards": [
            "🏆 Finalist - Blizzard Overwatch SEA Map Contest",
            "📺 Featured on ABS-CBN 'Maayong Buntag Kapamilya'",
            "🎨 'Youth Pride of Cebu' Award",
            "🎮 High-Fidelity AAA Concept Art"
        ],
        "content": """
        <div class="section">
            <h2 class="section-title">Concept</h2>
            <p>A reimagining of Cebu's iconic <strong>Simala Shrine</strong> as a futuristic map for the AAA game <em>Overwatch</em>. This project fused Filipino cultural heritage with high-tech sci-fi aesthetics, placing the gothic church high in the clouds as a sanctuary of the future.</p>
        </div>
        <div class="section">
            <h2 class="section-title">Execution</h2>
            <p>I created a complete multimedia package mimicking a real game expansion launch:</p>
            <ul>
                <li><strong>Visuals:</strong> Professional digital matte painting using Photoshop and After Effects to create an animated "Loading Screen".</li>
                <li><strong>Audio:</strong> Composed an original orchestral soundtrack in the style of Blizzard's music team, blending epic horns with choral elements fitting the sanctuary theme.</li>
                <li><strong>Lore:</strong> Wrote backstory integrating the shrine into the Overwatch universe's "Omnic Crisis".</li>
            </ul>
        </div>
        <div class="section">
            <h2 class="section-title">Recognition</h2>
            <p>The project was selected as a finalist in <strong>Blizzard's SEA Map Design Contest</strong>. Its cultural resonance led to a feature on national television (ABS-CBN), where I was interviewed as a representative of Cebuano creative talent.</p>
        </div>
        """
    },
    "connect4": {
        "title": "Connect 4 GPT: Productive Waiting",
        "type": "UX / SOFTWARE",
        "date": "2024",
        "role": "Developer",
        "timeline": "2 Weeks",
        "team_size": "Solo",
        "metric": "60% Win Rate Tuning",
        "image_path": "../connect4.png", # Placeholder
        "link_url": "#",
        "theme_key": "connect4",
        "tech": ["JavaScript", "MinMax Algorithm", "Chrome Extension API", "DOM MutationObserver", "Game AI"],
        "awards": [
            "🚀 Product Hunt Launch",
            "💡 Innovative UX Concept",
            "🧠 Custom MinMax AI Implementation"
        ],
        "content": """
        <div class="section">
            <h2 class="section-title">The Insight</h2>
            <p>AI models like ChatGPT often have "Research Mode" latency of 30-60 seconds. This dead time causes users to tab-switch and lose context. I asked: <em>What if waiting was the fun part?</em></p>
        </div>
        <div class="section">
            <h2 class="section-title">The Build</h2>
            <p>I built a Chrome Extension that uses <strong>MutationObservers</strong> to detect when ChatGPT enters "Thinking" state. It instantly overlays a <strong>Connect 4</strong> game board.</p>
            <p>The opponent is a custom <strong>MinMax AI</strong> algorithm I wrote from scratch. I tuned the difficulty (search depth of 6-7 plies) to achieve a 60% human win rate—challenging enough to engage, but easy enough to win within the 45-second waiting window.</p>
        </div>
        <div class="section">
            <h2 class="section-title">Impact</h2>
            <p>This project reimagines "latency" as an opportunity for delight. It transforms a friction point into a micro-engagement loop, keeping users in the flow of their work.</p>
        </div>
        """
    },
    "yc-startup": {
        "title": "YC AI Startup School: Founder Selection",
        "type": "ENTREPRENEURSHIP",
        "date": "Summer 2025",
        "role": "Founder Participant",
        "timeline": "Summer 2025",
        "team_size": "Cohort Member",
        "metric": "Elite Selection",
        "image_path": "../yc.png", # Placeholder
        "link_url": "#",
        "theme_key": "yc",
        "tech": ["Lean Startup", "Product-Market Fit", "AI Strategy", "Growth Metrics", "Venture Capital"],
        "awards": [
            "🎓 Selected for YC AI Startup School 2025",
            "🤝 Access to Y Combinator Network",
            "🚀 Validation of AI Startup Trajectory"
        ],
        "content": """
        <div class="section">
            <h2 class="section-title">The Program</h2>
            <p>I was selected to participate in <strong>Y Combinator's AI Startup School</strong> (Summer 2025), an exclusive program for top aspiring AI founders. This selection validates my track record in building AI products that solve real human problems.</p>
        </div>
        <div class="section">
            <h2 class="section-title">The Focus</h2>
            <p>The curriculum focuses on the unique challenges of the AI era: finding genuine product-market fit amidst hype, managing inference costs, and building defensible moats beyond just "wrapping an API".</p>
        </div>
        <div class="section">
            <h2 class="section-title">The Goal</h2>
            <p>This experience is the accelerator for my transition from "Engineer" to "Founder". It connects me with the world's best builders and investors, setting the stage for my next venture in the Neural Engineering space.</p>
        </div>
        """
    }
}

def generate_html(key, data):
    awards_html = "".join([f"<li>{award}</li>" for award in data['awards']])
    tech_html = "".join([f"<span class='tech-tag'>{t}</span>" for t in data['tech']])

    extra_btns = ""
    if key == "padayon-ko":
        extra_btns = "<a href='#' class='action-btn secondary'>View Case Study</a>"

    return TEMPLATE_HEAD.format(
        title=data['title'],
        css=CSS.replace("var(--color-view-project)", f"var(--color-{data['theme_key']})"),
        theme_key=data['theme_key'],
        type=data['type'],
        date=data['date'],
        role=data['role'],
        content=data['content'],
        image_path=data['image_path'],
        link_url=data['link_url'],
        extra_buttons=extra_btns,
        timeline=data['timeline'],
        team_size=data['team_size'],
        metric=data['metric'],
        tech_tags=tech_html,
        awards_list=awards_html
    )

if __name__ == "__main__":
    output_dir = "/Users/cvk/Downloads/carl/Typographic-Watermarking_25TPE/projects"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for key, data in projects.items():
        filename = f"{key}.html"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w") as f:
            f.write(generate_html(key, data))
        print(f"Generated {filepath}")
