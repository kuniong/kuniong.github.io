from __future__ import annotations

from hashlib import sha256
from pathlib import Path
from markupsafe import Markup
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
ENV = Environment(
    loader=FileSystemLoader(ROOT / "templates"),
    autoescape=select_autoescape(["html", "xml"]),
)
BASE = ENV.get_template("base.html")


def asset_version() -> str:
    digest = sha256()
    for asset in (ROOT / "assets/css/main.css", ROOT / "assets/js/main.js"):
        digest.update(asset.read_bytes())
    return digest.hexdigest()[:10]

SOCIAL = {
    "github": "https://github.com/kuniong",
    "orcid": "https://orcid.org/0000-0001-8934-0113",
    "email": "mailto:nguyen.quoc.hung.xu@alumni.tsukuba.ac.jp",
}

PUBLICATIONS = [
    {
        "year": "2026",
        "category": "journal selected",
        "title": "Minimax Access Regulation under Strategic Adversarial Arrivals",
        "authors": "Hung Q. Nguyen",
        "venue": "International Transactions in Operational Research, 2026 (in press)",
        "note": "A new strategic access-regulation model studying adversarial arrivals under minimax objectives.",
        "doi": "https://doi.org/10.1111/itor.70255",
    },
    {
        "year": "2026",
        "category": "journal selected",
        "title": "Learning to allocate automated speed enforcement: An observational policy optimization framework with reinforcement learning",
        "authors": "Hung Q. Nguyen",
        "venue": "Case Studies on Transport Policy, 25, 101855",
        "note": "Combines observational evidence with reinforcement learning to study where limited automated enforcement resources should be allocated.",
        "doi": "https://doi.org/10.1016/j.cstp.2026.101855",
        "detail": "/work/speed-enforcement/",
    },
    {
        "year": "2025",
        "category": "journal selected",
        "title": "Subgame perfect Nash equilibrium analysis in a two-population strategic matching queue with nonzero matching times",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "Operations Research Letters, 63, 107362",
        "note": "Shows how a high-dimensional matching queue can be reduced in equilibrium, yielding threshold behavior and pricing insights.",
        "doi": "https://doi.org/10.1016/j.orl.2025.107362",
        "detail": "/work/matching-queue/",
    },
    {
        "year": "2023",
        "category": "journal",
        "title": "Performance Analysis and Nash Equilibria in a Taxi-Passenger System with Two Types of Passenger",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "SN Computer Science, 4, Article 73",
        "note": "Analyzes system performance and strategic joining behavior when passenger classes differ.",
        "doi": "https://doi.org/10.1007/s42979-022-01479-1",
    },
    {
        "year": "2022",
        "category": "journal selected",
        "title": "Strategic customer behavior and optimal policies in a passenger–taxi double-ended queueing system with multiple access points and nonzero matching times",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "Queueing Systems, 102, 481–508",
        "note": "Studies strategic joining and system design when two populations match across multiple access points and matching takes time.",
        "doi": "https://doi.org/10.1007/s11134-022-09786-3",
        "detail": "/work/passenger-taxi/",
    },
    {
        "year": "2022",
        "category": "journal",
        "title": "To wait or not to wait: Strategic behaviors in an observable batch-service queueing system",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "Operations Research Letters, 50(3), 343–346",
        "note": "Characterizes decisions to join, balk, or wait to form a batch in an observable service system.",
        "doi": "https://doi.org/10.1016/j.orl.2022.04.003",
    },
    {
        "year": "2022",
        "category": "journal",
        "title": "Modified Erlang Loss System for Cognitive Wireless Networks",
        "authors": "Evsey Morozov, Sergey Rogozin, Hung Q. Nguyen, and Tuan Phung-Duc",
        "venue": "Mathematics, 10(12), 2101",
        "note": "Develops a stochastic performance model for a loss system motivated by cognitive wireless networks.",
        "doi": "https://doi.org/10.3390/math10122101",
    },
    {
        "year": "2022",
        "category": "journal selected",
        "title": "Supply–demand equilibria and multivariate optimization of social welfare in double-ended queueing systems",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "Computers & Industrial Engineering, 170, 108306",
        "note": "Connects strategic supply and demand behavior with multivariate welfare optimization in matching systems.",
        "doi": "https://doi.org/10.1016/j.cie.2022.108306",
        "detail": "/work/supply-demand/",
    },
    {
        "year": "2022",
        "category": "journal",
        "title": "A two-population game in observable double-ended queueing systems",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "Operations Research Letters, 50(4), 407–414",
        "note": "Analyzes equilibrium interaction between two strategic populations in an observable matching queue.",
        "doi": "https://doi.org/10.1016/j.orl.2022.05.004",
    },
    {
        "year": "2026",
        "category": "conference",
        "title": "Facial Recognition Ticket Gates in Railway Stations: A Queueing Model for Exceptions and Passenger Congestion",
        "authors": "Huy Q. Nguyen, Hung Q. Nguyen, and Tuan Phung-Duc",
        "venue": "Proceedings of the Conference on Optimization, Modeling, Simulation, and Analytics (COMOSA 2026), Hanoi, Vietnam, August 7–8, 2026",
        "note": "Shows how failed authentications can turn near-frictionless biometric gates into a congestion bottleneck—and how thresholds, retries, capacity, adoption, and fairness should be planned together.",
        "detail": "/work/facial-recognition-ticket-gates/",
    },
    {
        "year": "2025",
        "category": "conference selected",
        "title": "Safety Stock Model Selection Optimization for Budget-Constrained Multi-Item Inventory Management: A Scalable Framework",
        "authors": "Hung Q. Nguyen, Issei Suemitsu, Itoe Akutsu, Daisuke Aimi, and Tsuyoshi Oka",
        "venue": "IEEE CASE 2025",
        "note": "A scalable framework for selecting safety-stock models across many items under an aggregate budget constraint.",
        "doi": "https://doi.org/10.1109/CASE58245.2025.11163776",
        "detail": "/work/inventory-optimization/",
    },
    {
        "year": "2023",
        "category": "conference",
        "title": "M/M/c/Setup Queues: Conditional Mean Waiting Times and a Loop Algorithm to Derive Customer Equilibrium Threshold Strategy",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "EPEW 2022, Lecture Notes in Computer Science 13659",
        "note": "Derives conditional waiting-time measures and a computational loop for equilibrium threshold strategies.",
        "doi": "https://doi.org/10.1007/978-3-031-25049-1_6",
    },
    {
        "year": "2022",
        "category": "conference",
        "title": "Queueing Analysis and Nash Equilibria in an Unobservable Taxi-passenger System with Two Types of Passenger",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "Proceedings of the 11th International Conference on Operations Research and Enterprise Systems, Volume 1: ICORES, 48–55, ISBN 978-989-758-548-7",
        "note": "Models an unobservable taxi–passenger system with two passenger types and derives performance measures and Nash equilibrium joining rates.",
        "doi": "https://doi.org/10.5220/0010825200003117",
        "pdf": "https://www.scitepress.org/Papers/2022/108252/108252.pdf",
    },
    {
        "year": "2021",
        "category": "conference",
        "title": "Mixture Density Networks as a General Framework for Estimation and Prediction of Waiting Time Distributions in Queueing Systems",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "EPEW/ASMTA 2021, Lecture Notes in Computer Science 13104",
        "note": "Uses mixture density networks to estimate full waiting-time distributions rather than only point forecasts.",
        "doi": "https://doi.org/10.1007/978-3-030-91825-5_9",
    },
    {
        "year": "2023",
        "category": "other international-conference",
        "title": "The rational outcome of queueing games: A fixed-point iteration based approach",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "10th International Congress on Industrial and Applied Mathematics (ICIAM), Tokyo, Japan, August 20–25, 2023",
        "note": "Unrefereed international conference paper.",
    },
    {
        "year": "2021",
        "category": "other international-conference",
        "title": "Equilibria of supply and demand in double-ended queueing systems",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "31st European Conference on Operational Research, Athens, Greece, July 11–14, 2021",
        "note": "Unrefereed international conference paper.",
    },
    {
        "year": "2022",
        "category": "other domestic-conference",
        "title": "Nash equilibria in two-population queueing game",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "日本オペレーションズ・リサーチ学会2022年秋季研究発表会アブストラクト集",
        "note": "Unrefereed domestic conference paper.",
    },
    {
        "year": "2022",
        "category": "other domestic-conference",
        "title": "The rational outcome of a two-population game in a matching queue",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "第39回（2022年度）待ち行列シンポジウム「確率モデルとその応用」報文集",
        "note": "Unrefereed domestic conference paper.",
    },
    {
        "year": "2021",
        "category": "other domestic-conference",
        "title": "Equilibrium behavior in a double-ended queueing system with positive matching times",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "第38回（2021年度）待ち行列シンポジウム「確率モデルとその応用」(Online), 報文集",
        "note": "Unrefereed domestic conference paper.",
    },
    {
        "year": "2021",
        "category": "other domestic-conference",
        "title": "Customer joining behavior and performance analysis of the airport taxi-passenger queue with two types of customers",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "第37回（2020年度）待ち行列シンポジウム「確率モデルとその応用」(Online), 報文集",
        "note": "Unrefereed domestic conference paper.",
    },
    {
        "year": "2021",
        "category": "other domestic-conference",
        "title": "Mixture density networks (MDNs) as a general framework for estimation of waiting time distributions in queueing systems: Two case studies",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "第37回（2020年度）待ち行列シンポジウム「確率モデルとその応用」(Online), 報文集",
        "note": "Unrefereed domestic conference paper.",
    },
    {
        "year": "2023",
        "category": "other invited-article",
        "title": "両サイド型待ち行列における戦略的な挙動 ―多集団ゲーム理論的な解析―",
        "authors": "Hung Q. Nguyen and Tuan Phung-Duc",
        "venue": "オペレーションズ・リサーチ：経営の科学 68(10), 514–520",
        "note": "Invited domestic journal article (in Japanese).",
    },
    {
        "year": "2023",
        "category": "thesis",
        "title": "Agent behaviors and optimal designs in double-ended queueing systems",
        "authors": "Hung Q. Nguyen",
        "venue": "Doctoral dissertation, University of Tsukuba",
        "note": "Doctoral work on strategic behavior, equilibria, and system design in matching queues.",
        "pdf": "https://tsukuba.repo.nii.ac.jp/record/2008106/files/DA010775.pdf",
    },
]

PUBLICATION_SECTIONS = [
    ("journal", "Peer-reviewed journal articles"),
    ("conference", "Peer-reviewed conference papers"),
    ("international-conference", "International conference papers (unrefereed)"),
    ("domestic-conference", "Domestic conference papers (unrefereed)"),
    ("invited-article", "Invited journal article"),
    ("thesis", "Doctoral dissertation"),
]


def page_hero(eyebrow: str, title: str, lead: str, meta: str = "") -> str:
    meta_html = f'<div class="meta-line">{meta}</div>' if meta else ""
    return f"""
    <section class="page-hero">
      <div class="container">
        <h1>{title}</h1>
        <p class="lead">{lead}</p>
        {meta_html}
      </div>
    </section>
    """


def render(path: str, *, title: str, description: str, current: str, body: str, body_class: str = "") -> None:
    output = ROOT / path.lstrip("/")
    if output.suffix != ".html":
        output = output / "index.html"
    output.parent.mkdir(parents=True, exist_ok=True)
    html = BASE.render(
        title=title,
        description=description,
        current=current,
        body=Markup(body),
        body_class=body_class,
        path="/" if path in ("", "/", "index.html") else f"/{path.strip('/')}/",
        asset_version=asset_version(),
    )
    output.write_text(html, encoding="utf-8")


def build_home() -> None:
    body = """
    <section class="home-intro">
      <div class="container">
        <h1>Hung Q. Nguyen</h1>
        <p class="home-role">Researcher in Operations Research and Applied AI</p>
        <p class="home-affiliation">Advanced AI Innovation Center, Hitachi, Ltd.</p>
        <p class="home-summary">My research focuses on queueing theory, stochastic service systems, strategic behavior, and optimization. I am particularly interested in systems where users react to congestion and where mathematical models must ultimately support decisions under uncertainty and operational constraints.</p>
        <div class="profile-links">
          <a href="mailto:nguyen.quoc.hung.xu@alumni.tsukuba.ac.jp">Email</a>
          <a href="https://orcid.org/0000-0001-8934-0113">ORCID</a>
          <a href="https://scholar.google.com/citations?user=5o4yCtMAAAAJ&amp;hl=en">Google Scholar</a>
          <a href="https://github.com/kuniong">GitHub</a>
          <a href="/cv/">CV</a>
        </div>
        <div class="updated"><strong>Personal website notice:</strong> All statements and opinions expressed on this website are my own. They do not represent the official views of my employer or any affiliated organization.<br>Last updated: July 2026</div>
      </div>
    </section>

    <section class="academic-section">
      <div class="container">
        <h2>About</h2>
        <p>I received a Ph.D. in <a href="https://www.sk.tsukuba.ac.jp/PPS/en/">Policy and Planning Sciences</a> from the University of Tsukuba and an M.A. in Economics from Tohoku University. My academic work studies stochastic systems and strategic decision-making, especially queueing and matching systems. In industrial research, I work on optimization, forecasting, simulation, and data-driven decision support for operational problems.</p>
        <p>The common theme is simple: how should we understand and improve systems in which uncertainty, limited capacity, and human or organizational decisions interact?</p>
      </div>
    </section>

    <section class="academic-section">
      <div class="container">
        <h2>Research Interests</h2>
        <div class="interest-list">
          <div class="interest-item"><strong><a href="/research/#behavior">Queueing games and strategic behavior</a></strong><p>Equilibrium behavior, externalities, information, and system design when users react to congestion.</p></div>
          <div class="interest-item"><strong><a href="/research/#stochastic">Stochastic service systems</a></strong><p>Performance analysis of queues and matching systems, with emphasis on waiting, reliability, and uncertain system dynamics.</p></div>
          <div class="interest-item"><strong><a href="/research/#decisions">Optimization and decision support</a></strong><p>Mathematical optimization, simulation, forecasting, reinforcement learning, and other learning methods for operational decisions in real systems.</p></div>
        </div>
      </div>
    </section>

    <section class="academic-section">
      <div class="container">
        <h2>Selected Publications</h2>
        <ul class="selected-list">
          <li><div class="item-title"><a href="/work/speed-enforcement/">Learning to allocate automated speed enforcement: An observational policy optimization framework with reinforcement learning</a></div><div class="item-meta">Case Studies on Transport Policy, 2026 · <a href="/work/speed-enforcement/">Research story ↗</a></div></li>
          <li><div class="item-title"><a href="/work/matching-queue/">Subgame perfect Nash equilibrium analysis in a two-population strategic matching queue with nonzero matching times</a></div><div class="item-meta">Operations Research Letters, 2025 · <a href="/work/matching-queue/">Research story ↗</a></div></li>
          <li><div class="item-title"><a href="/work/passenger-taxi/">Strategic customer behavior and optimal policies in a passenger–taxi double-ended queueing system</a></div><div class="item-meta">Queueing Systems, 2022 · <a href="/work/passenger-taxi/">Research story ↗</a></div></li>
          <li><div class="item-title"><a href="/work/supply-demand/">Supply–demand equilibria and multivariate optimization of social welfare in double-ended queueing systems</a></div><div class="item-meta">Computers &amp; Industrial Engineering, 2022 · <a href="/work/supply-demand/">Research story ↗</a></div></li>
        </ul>
        <p><a href="/publications/">Complete publication list →</a></p>
      </div>
    </section>

    <section class="academic-section">
      <div class="container">
        <h2>Selected Applied Research</h2>
        <p class="section-note">Industrial work is described at a deliberately high level. Client identities, proprietary data, operational parameters, and non-public performance results are not disclosed.</p>
        <div class="two-column-list">
          <!-- Reservoir operations is hidden for now; retain the entry for possible future use.
          <div class="simple-entry"><h3><a href="/work/reservoir-operations/">Reservoir operations under uncertainty</a></h3><p>Forecasting, simulation, and optimization for multi-objective operational decision support.</p></div>
          -->
          <div class="simple-entry"><h3><a href="/work/inventory-optimization/">Inventory optimization at scale</a></h3><p>Scalable model selection and optimization for heterogeneous multi-item inventory systems.</p></div>
        </div>
        <p><a href="/projects/">More projects →</a></p>
      </div>
    </section>

    <section class="academic-section">
      <div class="container">
        <h2>News</h2>
        <ul class="news-list">
          <li><span class="news-date">2026.09</span><span>Granted the 16th Research Encourage Award for Young Researchers of the Operations Research Society of Japan.</span></li>
          <li><span class="news-date">2026.08</span><span>New paper titled "Minimax Access Regulation under Strategic Adversarial Arrivals" accepted in <em>International Transactions in Operational Research (ITOR)</em>.</span></li>
          <li><span class="news-date">2026.07</span><span>Our paper “Facial Recognition Ticket Gates in Railway Stations: A Queueing Model for Exceptions and Passenger Congestion” was accepted for COMOSA 2026 in Hanoi, Vietnam; proceedings publication forthcoming.</span></li>
          <li><span class="news-date">2026.05</span><span>New paper titled "
Learning to allocate automated speed enforcement: An observational policy optimization framework with reinforcement learning" published in <em>Case Studies on Transport Policy</em>.</span></li>
          <li><span class="news-date">2025.12</span><span>New paper titled "Subgame perfect Nash equilibrium analysis in a two-population strategic matching queue with nonzero matching times" published in <em>Operations Research Letters</em>.</span></li>
        </ul>
      </div>
    </section>

    <section class="academic-section">
      <div class="container">
        <h2>Contact</h2>
        <p>Email: nguyen.quoc.hung.xu [at] alumni.tsukuba.ac.jp</p>
      </div>
    </section>
    """
    render("index.html", title="Hung Q. Nguyen — Operations Research", description="Research in queueing theory, stochastic systems, strategic behavior, optimization, and decision support.", current="home", body=body)

def build_research() -> None:
    body = page_hero(
        "Research",
        "Research",
        "I study stochastic systems in which congestion, strategic behavior, uncertainty, and operational decisions interact. My work combines queueing theory and game theory with optimization, simulation, and data-driven methods.",
        "Core methods: queueing theory · stochastic processes · game theory · optimization · simulation · machine learning",
    )
    body += """
    <section class="methods-band"><div class="container methods-row"><span class="method">Queueing theory</span><span class="method">Game theory</span><span class="method">Stochastic processes</span><span class="method">Optimization</span><span class="method">Simulation</span><span class="method">Machine learning</span></div></section>
    <section class="section compact"><div class="container">
      <article class="research-block" id="behavior">
        <div class="research-index">01 / Behavior</div>
        <div class="research-content">
          <h2>Congestion, behavior &amp; incentives</h2>
          <p class="research-question">When users observe congestion and choose whether to join, wait, retry, switch, or leave, the system becomes a game—not only a queue.</p>
          <div class="research-columns">
            <div><h3>What I study</h3><p>I analyze how individual decisions respond to queue length, waiting costs, matching conditions, information, prices, and future utility. I am particularly interested in two-sided and matching systems where one population's behavior changes the incentives of the other.</p></div>
            <div><h3>Why it matters</h3><p>Policies that look efficient under fixed demand may fail once users react. Equilibrium analysis helps identify when information, pricing, access rules, or capacity changes improve performance—and when they create new externalities.</p></div>
          </div>
          <div class="related-links"><a class="related-link" href="/work/passenger-taxi/">Passenger–taxi matching queues</a><a class="related-link" href="/work/supply-demand/">Supply–demand equilibria</a><a class="related-link" href="/work/matching-queue/">Subgame-perfect equilibrium</a></div>
        </div>
      </article>
      <article class="research-block" id="stochastic">
        <div class="research-index">02 / Performance</div>
        <div class="research-content">
          <h2>Stochastic service systems</h2>
          <p class="research-question">How can we quantify delay, reliability, congestion, and failure when performance changes randomly over time?</p>
          <div class="research-columns">
            <div><h3>What I study</h3><p>My work uses continuous-time Markov chains, queueing models, conditional waiting-time analysis, distributional prediction, and stochastic simulation. The aim is not only to estimate an average, but to understand the mechanism that generates system-level performance.</p></div>
            <div><h3>Current direction</h3><p>I am extending this line toward data-driven stochastic OR: combining structural models with real observations, testing policies under demand surges and prediction errors, and studying systems with exceptions, retries, and endogenous routing.</p></div>
          </div>
          <div class="related-links"><a class="related-link" href="/publications/">Waiting-time prediction</a><a class="related-link" href="/publications/">Setup queues</a><a class="related-link" href="/projects/">Public and infrastructure systems</a></div>
        </div>
      </article>
      <article class="research-block" id="decisions">
        <div class="research-index">03 / Decisions</div>
        <div class="research-content">
          <h2>Decision support for complex operations</h2>
          <p class="research-question">A mathematically attractive policy is useful only when it survives data limitations, operational constraints, uncertainty, and stakeholder interpretation.</p>
          <div class="research-columns">
            <div><h3>What I build</h3><p>I translate operational questions into computational frameworks using mathematical optimization, scenario analysis, forecasting, simulation, and reinforcement learning. Applications include inventory, infrastructure operations, traffic safety, manufacturing, and digital services.</p></div>
            <div><h3>Research principle</h3><p>Prediction is an input to decision-making, not the endpoint. I focus on how forecasts enter policies, how errors propagate, which constraints are truly binding, and whether the result remains explainable enough to support action.</p></div>
          </div>
          <div class="related-links"><a class="related-link" href="/work/inventory-optimization/">Inventory optimization</a><!-- Reservoir operations link is hidden for now; retain it for possible future use.
            <a class="related-link" href="/work/reservoir-operations/">Reservoir operations</a>
            --><a class="related-link" href="/work/speed-enforcement/">Traffic safety allocation</a></div>
        </div>
      </article>
    </div></section>
    <section class="section compact"><div class="narrow callout"><strong>Research agenda.</strong> A central direction of my current work is data-driven stochastic operations research for service systems: integrating operating rules, user behavior, stochastic performance, and data so that policies can be evaluated under both normal and stress conditions.</div></section>
    """
    render("research", title="Research — Hung Q. Nguyen", description="Research themes in queueing games, stochastic service systems, optimization, and data-driven decision support.", current="research", body=body)


def build_publications() -> None:
    publication_sections = []
    for section_key, section_title in PUBLICATION_SECTIONS:
        papers = [
            publication
            for publication in PUBLICATIONS
            if section_key in publication["category"].split()
        ]
        papers.sort(key=lambda publication: int(publication["year"]), reverse=True)

        cards = []
        for index, p in enumerate(papers):
            links = []
            if p.get("detail"):
                links.append(f'<a href="{p["detail"]}">Research story ↗</a>')
            if p.get("doi"):
                links.append(f'<a href="{p["doi"]}" target="_blank" rel="noopener">DOI ↗</a>')
            if p.get("pdf"):
                links.append(f'<a href="{p["pdf"]}" target="_blank" rel="noopener">PDF ↗</a>')
            links_html = f'              <div class="pub-links">{"".join(links)}</div>' if links else ""
            publication_number = len(papers) - index
            year_html = f'<time class="pub-year" datetime="{p["year"]}">{p["year"]}</time>'
            if p["year"] in p["venue"]:
                venue_html = p["venue"].replace(p["year"], year_html)
            else:
                venue_html = f'{p["venue"]} <time class="pub-year" datetime="{p["year"]}">({p["year"]})</time>'
            authors_html = p["authors"].replace(
                "Hung Q. Nguyen",
                '<strong class="pub-author-me">Hung Q. Nguyen</strong>',
            )
            cards.append(f"""
          <li class="pub-card" data-category="{p['category']}" data-year="{p['year']}">
            <div class="pub-number" aria-label="Publication {publication_number}">{publication_number}.</div>
            <article class="pub-citation">
              <div class="pub-authors">{authors_html}</div>
              <h3>{p['title']}</h3>
              <div class="pub-venue">{venue_html}</div>
              <div class="pub-note">{p['note']}</div>
{links_html}
            </article>
          </li>
            """.rstrip())

        publication_sections.append(f"""
        <section class="publication-group" data-publication-group>
          <div class="publication-group-heading">
            <h2>{section_title}</h2>
            <span class="publication-count">{len(papers)}</span>
          </div>
          <ol class="publication-list" aria-label="{section_title}">{''.join(cards)}</ol>
        </section>
        """.rstrip())
    body = page_hero(
        "Publications",
        "Publications",
        "Peer-reviewed journal articles, conference papers, additional scholarly work, and doctoral research.",
        "8 peer-reviewed journal articles · conference papers · additional scholarly work · doctoral dissertation",
    )
    body += f"""
    <section class="section compact"><div class="container">
      <div class="filter-bar" role="group" aria-label="Filter publications">
        <button class="filter-button active" type="button" data-filter="all" aria-pressed="true">All</button>
        <!-- The Selected filter is hidden for now; retain it for possible future use.
        <button class="filter-button" type="button" data-filter="selected" aria-pressed="false">Selected</button>
        -->
        <button class="filter-button" type="button" data-filter="journal" aria-pressed="false">Journal articles</button>
        <button class="filter-button" type="button" data-filter="conference" aria-pressed="false">Conference papers</button>
        <button class="filter-button" type="button" data-filter="other" aria-pressed="false">Additional scholarly work</button>
        <button class="filter-button" type="button" data-filter="thesis" aria-pressed="false">Thesis</button>
      </div>
      <div class="publication-groups">{''.join(publication_sections)}</div>
    </div></section>
    """
    render("publications", title="Publications — Hung Q. Nguyen", description="Journal articles and conference papers in queueing theory, strategic behavior, stochastic systems, inventory, and applied AI.", current="publications", body=body)


def build_projects() -> None:
    body = page_hero(
        "Projects",
        "Projects",
        "Project descriptions are currently hidden.",
    )
    body += """
    <!-- Project content is hidden for now; retain it for possible future use.
    <section class="section compact"><div class="container">
      <div class="project-grid">
        <a class="project-card" href="/work/reservoir-operations/">
          <div class="work-type">Infrastructure · Optimization · Forecasting</div>
          <h2>Reservoir operations under uncertainty</h2>
          <p>Decision-support research for multi-objective water operations where present actions change future system states and outcomes depend on uncertain conditions.</p>
          <div class="tags"><span class="tag">Simulation</span><span class="tag">Optimization</span><span class="tag">Time series</span></div>
          <div class="project-footer"><span class="work-link">Read case study ↗</span><span class="confidential">Sanitized industrial project</span></div>
        </a>
        <a class="project-card" href="/work/inventory-optimization/">
          <div class="work-type">Manufacturing · Inventory · Scalable optimization</div>
          <h2>Inventory optimization at scale</h2>
          <p>A framework for selecting item-level safety-stock logic while respecting a shared budget across a large heterogeneous portfolio.</p>
          <div class="tags"><span class="tag">Inventory theory</span><span class="tag">Optimization</span><span class="tag">Scalability</span></div>
          <div class="project-footer"><span class="work-link">Read case study ↗</span><span class="confidential">Public method + sanitized context</span></div>
        </a>
        <a class="project-card" href="/work/ecommerce-decision-systems/">
          <div class="work-type">E-commerce · Reinforcement learning · Optimization</div>
          <h2>Decision systems for digital commerce</h2>
          <p>Research and prototyping across dynamic pricing, seller selection, advertising allocation, and logistics optimization.</p>
          <div class="tags"><span class="tag">Contextual bandits</span><span class="tag">Deep RL</span><span class="tag">Allocation</span></div>
          <div class="project-footer"><span class="work-link">Read case study ↗</span><span class="confidential">Prior research role</span></div>
        </a>
      </div>
    </div></section>
    <section class="section compact"><div class="container"><div class="disclosure-box"><h2>My disclosure rule</h2><p>A technically sophisticated reader should be able to understand why the work was difficult, what I contributed, and which capabilities it demonstrates—but not be able to reconstruct a client’s data, operating logic, proprietary implementation, or business performance. Where public papers or patents exist, the site links to those public artifacts instead of reproducing internal details.</p></div></div></section>
    -->
    """
    render("projects", title="Projects — Hung Q. Nguyen", description="Project descriptions are currently hidden.", current="projects", body=body)


def build_experience() -> None:
    body = page_hero(
        "Experience",
        "A path from economics and data science to <em>stochastic OR and industrial research.</em>",
        "My background combines formal training in economics, data science, and social engineering with research roles that require mathematical models to survive contact with real operations.",
    )
    body += """
    <section class="section compact"><div class="container">
      <div class="eyebrow">Professional experience</div>
      <div class="timeline" style="margin-top:24px">
        <article class="timeline-item"><div class="timeline-date">2023 — present</div><div><h3>Researcher</h3><div class="org">Hitachi, Ltd. · Advanced AI Innovation Center</div><p>Research and development in AI, operations research, mathematical optimization, and data analysis for operational problems in manufacturing, energy, infrastructure, and digital systems.</p><ul class="timeline-bullets"><li>Inventory optimization and scalable decision models</li><li>Reservoir-operation optimization and forecasting</li><li>Predictive models for operational processes and time series</li></ul></div></article>
        <article class="timeline-item"><div class="timeline-date">2022 — 2023</div><div><h3>Part-time Lecturer &amp; Researcher</h3><div class="org">VietDevelopers Technology, Ltd. · Remote</div><p>Worked on machine learning and optimization for e-commerce while teaching online courses in reinforcement learning, mathematical optimization, and mathematics for AI.</p></div></article>
      </div>
    </div></section>
    <section class="section compact"><div class="container">
      <div class="eyebrow">Education</div>
      <div class="timeline" style="margin-top:24px">
        <article class="timeline-item"><div class="timeline-date">2020 — 2023</div><div><h3>Ph.D. in Social Engineering</h3><div class="org">University of Tsukuba</div><p>Doctoral research on agent behavior and optimal design in double-ended queueing systems.</p></div></article>
        <article class="timeline-item"><div class="timeline-date">2017 — 2019</div><div><h3>M.A. in Economics</h3><div class="org">Tohoku University · Data Science Program</div><p>Graduate training connecting economics with quantitative and data-science methods.</p></div></article>
        <article class="timeline-item"><div class="timeline-date">2012 — 2017</div><div><h3>B.A. in Economics &amp; International Business</h3><div class="org">Foreign Trade University, Vietnam</div></div></article>
      </div>
    </div></section>
    <section class="section compact"><div class="container">
      <div class="section-head"><div><div class="eyebrow">Selected recognition</div><h2 class="section-title">Research recognized in both academic and industrial settings.</h2></div><p class="section-intro">I keep this list selective. The web CV contains the fuller chronology.</p></div>
      <div class="award-grid">
        <div class="award"><span class="award-year">2026</span><strong>16th Research Encourage Award for Young Researchers</strong><span>Operations Research Society of Japan · selected; ceremony scheduled September 2026</span></div>
        <div class="award"><span class="award-year">2025</span><strong>Digital Innovation R&amp;D Technology Award, 3rd place</strong><span>Hitachi internal recognition</span></div>
        <div class="award"><span class="award-year">2024</span><strong>Paper Award</strong><span>Queueing Research Group, Operations Research Society of Japan</span></div>
        <div class="award"><span class="award-year">2023</span><strong>President’s Award</strong><span>University of Tsukuba</span></div>
        <div class="award"><span class="award-year">2023</span><strong>Alumni Association Ezaki Award</strong><span>University of Tsukuba</span></div>
        <div class="award"><span class="award-year">2023</span><strong>Research Encouragement Award</strong><span>Queueing Research Group, Operations Research Society of Japan</span></div>
      </div>
    </div></section>
    <section class="section compact"><div class="narrow">
      <div class="eyebrow">Teaching</div><h2 class="section-title">Intuition first, then formalization and implementation.</h2><p class="hero-lead">I have taught online courses in Foundations of Reinforcement Learning, Mathematical Optimization, and Mathematics for AI. My teaching approach combines intuitive examples, visualization, hand calculations, and Python implementation so learners can move from a real decision problem to a mathematical representation and then back to interpretation.</p>
    </div></section>
    """
    render("experience", title="Experience — Hung Q. Nguyen", description="Professional experience, education, teaching, and selected awards in operations research and applied AI.", current="experience", body=body)


def build_teaching() -> None:
    body = page_hero(
        "Teaching",
        "Teaching",
        "My teaching approach starts from intuition and a concrete decision problem, then moves toward mathematical formulation, analysis, and implementation.",
    )
    body += """
    <section class="academic-section"><div class="container">
      <h2>Teaching Experience</h2>
      <div class="timeline">
        <article class="timeline-item"><div class="timeline-date">2022 — 2023</div><div><h3>Online Lecturer</h3><div class="org">VietDevelopers Technology, Ltd.</div><p>Developed and taught courses in Foundations of Reinforcement Learning, Mathematical Optimization, and Mathematics for AI, including lectures, code examples, exercises, and project materials.</p></div></article>
      </div>
    </div></section>
    <section class="academic-section"><div class="container">
      <h2>Teaching Approach</h2>
      <p>I prefer to begin with a system that students can reason about intuitively, such as waiting lines, inventory decisions, allocation problems, or sequential decisions under uncertainty. From there, I introduce the mathematical abstraction, work through the analysis, and return to interpretation and implementation.</p>
      <p>For students with different mathematical backgrounds, I use visual explanation, small hand-worked examples, and computational experiments before moving to more formal derivations. The goal is not only to apply a formula, but to understand what the model assumes, what its result means, and where it may fail.</p>
    </div></section>
    <section class="academic-section"><div class="container">
      <h2>Courses I Can Contribute To</h2>
      <div class="two-column-list">
        <div class="simple-entry"><h3>Probability and stochastic models</h3><p>Probability, stochastic processes, queueing models, and performance evaluation.</p></div>
        <div class="simple-entry"><h3>Operations research</h3><p>Mathematical modeling, optimization, simulation, and decision analysis.</p></div>
        <div class="simple-entry"><h3>Service systems</h3><p>Congestion, capacity, user behavior, and operational design.</p></div>
        <div class="simple-entry"><h3>Data-driven decision methods</h3><p>Forecasting, machine learning, reinforcement learning, and their role in operational decisions.</p></div>
      </div>
    </div></section>
    """
    render("teaching", title="Teaching — Hung Q. Nguyen", description="Teaching experience and approach in operations research, stochastic models, optimization, and data-driven decision methods.", current="teaching", body=body)


def build_cv() -> None:
    body = page_hero("Curriculum vitae", "Hung Q. Nguyen", "Operations research and applied AI researcher working across queueing theory, stochastic systems, optimization, and real-world decision support.")
    body += """
    <section class="section compact"><div class="container cv-shell">
      <aside class="cv-sidebar">
        <div class="cv-panel"><h2 class="cv-name">Hung Q. Nguyen</h2><div class="cv-role">Researcher · Operations Research &amp; Applied AI</div><div class="cv-links"><a href="mailto:nguyen.quoc.hung.xu@alumni.tsukuba.ac.jp">Email</a><a href="https://github.com/kuniong">GitHub</a><a href="https://orcid.org/0000-0001-8934-0113">ORCID 0000-0001-8934-0113</a></div></div>
        <div class="cv-panel"><button class="button primary print-button" data-print>Print / save as PDF</button></div>
        <div class="cv-panel"><strong>Research fields</strong><div class="tags" style="margin-top:12px"><span class="tag">Queueing theory</span><span class="tag">Game theory</span><span class="tag">Stochastic OR</span><span class="tag">Optimization</span><span class="tag">Applied AI</span></div></div>
      </aside>
      <div class="cv-main">
        <section class="cv-section"><h2>Appointments</h2>
          <div class="cv-entry"><div class="date">04/2023 — present</div><div><h3>Researcher, Hitachi, Ltd.</h3><div class="cv-affiliation">Advanced AI Innovation Center, Social Intelligence Research Department</div><p>Research and development in AI, operations research, mathematical optimization, forecasting, and data analysis.</p></div></div>
        </section>
        <section class="cv-section"><h2>Education</h2>
          <div class="cv-entry"><div class="date">04/2020 — 03/2023</div><div><h3>Ph.D. in <a href="https://www.sk.tsukuba.ac.jp/PPS/en/">Policy and Planning Sciences</a>, University of Tsukuba</h3><p><a href="http://sk.tsukuba.ac.jp/~tuan/lab/en/index.html">Applied Stochastic Systems Laboratory</a>, supervised by Professor <a href="http://sk.tsukuba.ac.jp/~tuan/">Tuan Phung-Duc</a>.<br>Dissertation: <em>Agent behaviors and optimal designs in double-ended queueing systems.</em></p></div></div>
          <div class="cv-entry"><div class="date">10/2017 — 09/2019</div><div><h3>M.A. in Economics, Tohoku University</h3><p>Graduate School of Economics and Management, Data Science Program.</p></div></div>
          <div class="cv-entry"><div class="date">08/2012 — 02/2017</div><div><h3>B.A. in Economics &amp; International Business, Foreign Trade University</h3><p>Graduated in the top 1% of the cohort.</p></div></div>
        </section>
        <section class="cv-section"><h2>Selected publications</h2>
          <ol class="cv-list">
            <li>Hung Q. Nguyen (2026). Learning to allocate automated speed enforcement: An observational policy optimization framework with reinforcement learning. <em>Case Studies on Transport Policy</em>, <strong>25</strong>, 101855. <a href="https://doi.org/10.1016/j.cstp.2026.101855">doi:10.1016/j.cstp.2026.101855</a>.</li>
            <li>Hung Q. Nguyen and Tuan Phung-Duc (2025). Subgame perfect Nash equilibrium analysis in a two-population strategic matching queue with nonzero matching times. <em>Operations Research Letters</em>, <strong>63</strong>, 107362. <a href="https://doi.org/10.1016/j.orl.2025.107362">doi:10.1016/j.orl.2025.107362</a>.</li>
            <li>Hung Q. Nguyen and Tuan Phung-Duc (2022). Strategic customer behavior and optimal policies in a passenger–taxi double-ended queueing system with multiple access points and nonzero matching times. <em>Queueing Systems</em>, <strong>102</strong>, 481–508. <a href="https://doi.org/10.1007/s11134-022-09786-3">doi:10.1007/s11134-022-09786-3</a>.</li>
            <li>Hung Q. Nguyen and Tuan Phung-Duc (2022). Supply–demand equilibria and multivariate optimization of social welfare in double-ended queueing systems. <em>Computers &amp; Industrial Engineering</em>, <strong>170</strong>, 108306. <a href="https://doi.org/10.1016/j.cie.2022.108306">doi:10.1016/j.cie.2022.108306</a>.</li>
            <li>Hung Q. Nguyen and Tuan Phung-Duc (2022). A two-population game in observable double-ended queueing systems. <em>Operations Research Letters</em>, <strong>50</strong>(4), 407–414. <a href="https://doi.org/10.1016/j.orl.2022.05.004">doi:10.1016/j.orl.2022.05.004</a>.</li>
          </ol>
          <div class="pub-links"><a href="/publications/">Complete publication list ↗</a></div>
        </section>
        <section class="cv-section"><h2>Awards</h2>
          <div class="cv-entry"><div class="date">09/2026</div><div><h3>16th Research Encourage Award for Young Researchers</h3><p>The Operations Research Society of Japan.</p></div></div>
          <div class="cv-entry"><div class="date">12/2025</div><div><h3>Digital Innovation R&amp;D Technology Award — 3rd Prize</h3><p>Hitachi, Ltd., Research &amp; Development Group.</p></div></div>
          <div class="cv-entry"><div class="date">12/2024</div><div><h3>Year-end Internal Award</h3><p>Hitachi, Ltd., Digital Systems &amp; Services Department.</p></div></div>
          <div class="cv-entry"><div class="date">05/2024</div><div><h3>Paper Award</h3><p>Special Interest Group of Queueing Theory, The Operations Research Society of Japan.</p></div></div>
          <div class="cv-entry"><div class="date">03/2023</div><div><h3>President’s Award</h3><p>University of Tsukuba.</p></div></div>
          <div class="cv-entry"><div class="date">03/2023</div><div><h3>Alumni Association Ezaki Award</h3><p>University of Tsukuba Alumni Association.</p></div></div>
          <div class="cv-entry"><div class="date">01/2023</div><div><h3>Research Encouragement Award</h3><p>Special Interest Group of Queueing Theory, The Operations Research Society of Japan.</p></div></div>
        </section>
        <section class="cv-section"><h2>Research funding</h2>
          <div class="cv-entry"><div class="date">2021 — 2023</div><div><h3>JST SPRING</h3><p>Japan Science and Technology Agency / University of Tsukuba.</p></div></div>
        </section>
        <section class="cv-section"><h2>Peer-review activities</h2>
          <div class="cv-entry"><div class="date">Journals</div><div><ul class="cv-list"><li><a href="https://link.springer.com/journal/10586">Cluster Computing</a></li><li><a href="https://link.springer.com/journal/10791">Discover Computing</a></li><li><a href="https://www.tandfonline.com/journals/tinf20">INFOR</a></li><li><a href="https://onlinelibrary.wiley.com/journal/14753995">International Transactions in Operational Research</a></li><li><a href="https://www.sciencedirect.com/journal/journal-of-mathematical-economics">Journal of Mathematical Economics</a></li><li><a href="https://www.sciencedirect.com/journal/mathematics-and-computers-in-simulation">Mathematics and Computers in Simulation</a></li><li><a href="https://link.springer.com/journal/11009">Methodology and Computing in Applied Probability</a></li><li><a href="https://www.sciencedirect.com/journal/omega">Omega</a></li><li><a href="https://www.sciencedirect.com/journal/performance-evaluation">Performance Evaluation</a></li><li><a href="http://qmsm.nchu.edu.tw/index.php/qmsm">Queueing Models and Service Management</a></li><li><a href="https://link.springer.com/journal/11134">Queueing Systems</a></li><li><a href="https://www.nature.com/srep/">Scientific Reports</a></li><li><a href="https://www.sciencedirect.com/journal/socio-economic-planning-sciences">Socio-Economic Planning Sciences</a></li><li><a href="https://www.tandfonline.com/journals/ytrl20">Transportation Letters</a></li></ul></div></div>
        </section>
        <!-- Languages section hidden for now; retain it for possible future use.
        <section class="cv-section"><h2>Languages</h2>
          <div class="language-grid"><div class="language-item"><strong>Vietnamese</strong><span>Native</span></div><div class="language-item"><strong>English</strong><span>Business level</span></div><div class="language-item"><strong>Japanese</strong><span>Nearly business level</span></div></div>
        </section>
        -->
      </div>
    </div></section>
    """
    render("cv", title="CV — Hung Q. Nguyen", description="Web curriculum vitae for Hung Q. Nguyen: research, education, appointments, publications, awards, funding, and peer-review activities.", current="cv", body=body, body_class="cv-page")


def case_page(slug: str, *, case_type: str, title: str, lead: str, meta: list[str], copy: str, aside: str, current: str) -> None:
    meta_html = "".join(f"<span>{m}</span>" for m in meta)
    body = f"""
    <section class="case-hero"><div class="container"><div class="case-type">{case_type}</div><h1>{title}</h1><p class="case-lead">{lead}</p><div class="case-meta">{meta_html}</div></div></section>
    <section><div class="container case-body"><article class="case-copy">{copy}</article><aside class="case-aside">{aside}</aside></div></section>
    """
    render(f"work/{slug}", title=f"{title} — Hung Q. Nguyen", description=lead, current=current, body=body)


def build_cases() -> None:
    case_page(
        "passenger-taxi",
        case_type="Research story · Queueing theory & game theory",
        title="Passenger–taxi matching with strategic arrivals",
        lead="What changes when both congestion and matching matter, agents choose whether to participate, and matching itself takes time?",
        meta=["Queueing Systems · 2022", "Double-ended queues", "Equilibrium & optimal policy"],
        current="research",
        copy="""
          <h2>The problem</h2><p>Passenger–taxi systems are not ordinary one-sided queues. Two populations arrive, their imbalance creates waiting on one side, and the system state affects whether a newly arriving agent finds participation worthwhile. Multiple access points and nonzero matching times make the state and decision structure richer.</p>
          <h2>Key idea</h2><p>The model treats participation as a strategic decision embedded in a stochastic matching system. Queueing analysis describes the evolving state; game-theoretic analysis characterizes how rational agents respond to what they observe.</p>
          <blockquote>A service system can change its own demand because users respond to the congestion it creates.</blockquote>
          <h2>Main contribution</h2><p>The paper characterizes strategic behavior and studies system-level policies in a passenger–taxi double-ended queue with multiple access points and nonzero matching times.</p>
          <h2>Why it matters</h2><p>The broader lesson applies to platforms and matching services: adding capacity or changing access conditions can alter behavior, so operational design should account for equilibrium response rather than treating arrivals as fixed.</p>
        """,
        aside="""
          <div class="aside-card"><h3>Methods</h3><ul><li>Double-ended queueing</li><li>Strategic joining</li><li>Equilibrium analysis</li><li>Policy optimization</li></ul></div>
          <div class="aside-card"><h3>Paper</h3><p><a href="https://doi.org/10.1007/s11134-022-09786-3" target="_blank" rel="noopener">Open DOI ↗</a></p></div>
          <div class="aside-card"><h3>Related</h3><p><a href="/work/supply-demand/">Supply–demand equilibria</a></p><p><a href="/work/matching-queue/">Subgame-perfect matching queue</a></p></div>
        """,
    )

    case_page(
        "supply-demand",
        case_type="Research story · Queueing games & optimization",
        title="Supply–demand equilibria in double-ended queues",
        lead="When both sides of a matching market react strategically, welfare optimization becomes a coupled problem in behavior and system design.",
        meta=["Computers & Industrial Engineering · 2022", "Two-population games", "Multivariate social optimization"],
        current="research",
        copy="""
          <h2>The question</h2><p>Many service systems need two populations at the same time: passengers and taxis, jobs and workers, buyers and sellers. Each side may decide whether entering the system is worthwhile based on current conditions.</p>
          <h2>Why the problem is difficult</h2><p>The participation decision of one population changes the waiting experience of the other. The resulting equilibrium is therefore coupled across supply and demand, while a system designer may have several policy variables available at once.</p>
          <h2>What the paper does</h2><p>The work analyzes equilibrium behavior in a double-ended queue and formulates multivariate optimization of social welfare. The combination makes it possible to compare decentralized behavior with coordinated system design.</p>
          <blockquote>The operational state changes incentives; incentives change arrivals; arrivals change the operational state.</blockquote>
          <h2>Broader relevance</h2><p>This feedback structure appears in labor platforms, transport matching, digital marketplaces, and any service where two strategic populations must meet.</p>
        """,
        aside="""
          <div class="aside-card"><h3>Methods</h3><ul><li>Queueing equilibrium</li><li>Two-sided systems</li><li>Social welfare</li><li>Multivariate optimization</li></ul></div>
          <div class="aside-card"><h3>Paper</h3><p><a href="https://doi.org/10.1016/j.cie.2022.108306" target="_blank" rel="noopener">Open DOI ↗</a></p></div>
          <div class="aside-card"><h3>Research theme</h3><p><a href="/research/#behavior">Congestion, behavior &amp; incentives</a></p></div>
        """,
    )

    case_page(
        "matching-queue",
        case_type="Research story · Strategic stochastic systems",
        title="Subgame-perfect behavior in a two-population matching queue",
        lead="A high-dimensional queueing game can sometimes hide a simpler equilibrium structure. The challenge is proving when the reduction is valid.",
        meta=["Operations Research Letters · 2025", "Subgame-perfect Nash equilibrium", "Pricing & welfare"],
        current="research",
        copy="""
          <h2>The problem</h2><p>In a two-population matching queue with nonzero matching times, agents observe the system and choose whether to join or balk. The natural state is multidimensional, which makes direct strategic analysis difficult.</p>
          <h2>The structural result</h2><p>The analysis shows that one dimension can be omitted when characterizing subgame-perfect Nash equilibrium. This reduction leads to threshold-based equilibrium strategies and makes the strategic system more tractable.</p>
          <h2>Design implication</h2><p>Numerical analysis studies pricing and social welfare. A targeted intervention on one side can outperform more diffuse policies under some system conditions.</p>
          <blockquote>The useful theorem is not only an equilibrium formula—it is the discovery of which part of the state actually matters strategically.</blockquote>
        """,
        aside="""
          <div class="aside-card"><h3>Methods</h3><ul><li>Matching queues</li><li>Dynamic games</li><li>Threshold strategies</li><li>Pricing</li></ul></div>
          <div class="aside-card"><h3>Paper</h3><p><a href="https://doi.org/10.1016/j.orl.2025.107362" target="_blank" rel="noopener">Open DOI ↗</a></p></div>
          <div class="aside-card"><h3>Related</h3><p><a href="/work/passenger-taxi/">Earlier matching-queue model</a></p></div>
        """,
    )

    case_page(
        "speed-enforcement",
        case_type="Public research project · Transport policy",
        title="Allocating automated speed enforcement",
        lead="How should limited enforcement resources be deployed when the evidence is observational and the policy must learn from heterogeneous locations?",
        meta=["Case Studies on Transport Policy · 2026", "Observational policy optimization", "Reinforcement learning"],
        current="projects",
        copy="""
          <h2>Context</h2><p>Automated enforcement programs operate under limited resources and heterogeneous road conditions. The decision is not simply whether enforcement works on average, but where deployment can create the most value.</p>
          <h2>Decision challenge</h2><p>Observed outcomes reflect the locations that were actually selected, so policy learning must be grounded in observational evidence rather than a clean randomized experiment. The allocation problem is also sequential: deployment choices affect which outcomes are observed next.</p>
          <h2>Approach</h2><p>The project develops an observational policy-optimization framework with reinforcement learning. The aim is to connect empirical evidence with an explicit resource-allocation decision.</p>
          <h2>Why it matters</h2><p>The project illustrates a broader research principle: predictive or causal evidence becomes operationally useful only after it is connected to the policy that must be chosen.</p>
        """,
        aside="""
          <div class="aside-card"><h3>Methods</h3><ul><li>Observational data</li><li>Policy optimization</li><li>Reinforcement learning</li><li>Transport safety</li></ul></div>
          <div class="aside-card"><h3>Paper</h3><p><a href="https://doi.org/10.1016/j.cstp.2026.101855" target="_blank" rel="noopener">Open DOI ↗</a></p></div>
          <div class="aside-card"><h3>Disclosure</h3><p>This is published academic work; the technical paper is the authoritative source.</p></div>
        """,
    )

    case_page(
        "facial-recognition-ticket-gates",
        case_type="Research story · Queueing systems &amp; biometric operations",
        title="When frictionless ticket gates fail",
        lead="A successful facial-recognition passage may feel effortless. The operational challenge begins when recognition fails: retries occupy a gate, unresolved passengers need assistance, and a small exception flow can become a peak-hour queue.",
        meta=["COMOSA 2026", "Biometric gates · retries · exceptions", "Security · congestion · fairness"],
        current="research",
        copy="""
          <h2>The hidden bottleneck</h2><p>Walk-through facial recognition promises faster, hands-free station access. But nominal scan speed tells only half the story. A failed authentication takes longer than a successful passage, may trigger several immediate retries, and can end with a passenger being sent to staff. At high demand, those failures—not the routine successes—can generate most of the biometric workload.</p>
          <blockquote>The speed of a successful scan is only part of the capacity story. Failures determine how much recovery capacity the station needs.</blockquote>

          <h2>One policy, three coupled queues</h2><p>The paper models biometric gates, conventional gates, and an exception desk as one connected service system. Passenger groups may differ in biometric adoption, image-acquisition quality, and sensitivity to delay. The recognition threshold and retry limit therefore do more than change accuracy: they determine gate occupation, exception arrivals, waiting, and whether each part of the system remains stable.</p><p>This makes exception demand <em>endogenous</em>. Tightening the recognition threshold can reduce false accepts, but it can also create more false non-matches, retries, and staff interventions. Allowing more retries can keep passengers away from the exception desk, yet block biometric gates for longer.</p>

          <h2>Four decisions that must move together</h2><ul><li><strong>Recognition threshold:</strong> balance security risk against false non-matches, delay, and recovery workload.</li><li><strong>Retry rule:</strong> use a finite limit that reflects actual field reliability; retries move congestion between the gates and the exception desk.</li><li><strong>Capacity:</strong> add gates when ordinary throughput is the bottleneck, but strengthen exception service when authentication failures dominate.</li><li><strong>Adoption:</strong> stage biometric use with the infrastructure mix. Moving everyone to the biometric channel can increase delay if gate and recovery capacity do not grow with it.</li></ul>

          <h2>No universal retry count</h2><p>The numerical results make the need for calibration concrete. In the stylized peak-period experiment, an intermediate threshold and a three-attempt limit minimized the modeled cost. In the public-data-anchored counterfactual, low benchmark error rates made additional retries comparatively inexpensive and moved the preferred retry limit to the top of the tested range. The contrast is the practical result: retry policy should be set from observed acquisition quality and passenger experience, not copied as a universal number.</p>

          <h2>Fairness beyond average waiting time</h2><p>Average delay can hide an important disparity. In the paper's stress test, passengers with more difficult image acquisition were routed to exception handling more than five times as often as the regular class at the most severe tested setting, even though the difference in average delay looked comparatively modest. Monitoring who is repeatedly stopped or redirected is therefore as important as monitoring the mean queue.</p>

          <h2>From a model to station-specific decisions</h2><p>The study anchors its counterfactuals in 44,168 station-hour observations from New York's subway system and biometric operating points from NIST benchmarks. Under the stated baseline assumptions, extra biometric-gate capacity was valuable at the busiest hubs, including Grand Central–42 St and Times Square, but not at the lower-demand stations. The analytical approximation was also checked against discrete-event simulation: it reproduced the main utilization, delay, and stability patterns, while supporting a conservative safety margin near saturation.</p>

          <h2>Operational takeaway</h2><div class="callout"><strong>Design the recovery path at the same time as the fast path.</strong> Thresholds, retry rules, adoption, biometric and conventional gates, and exception staffing form one operating policy. A deployment can appear frictionless for most passengers while still being fragile at the moments—and for the people—when recognition fails.</div>

          <h2>Evidence boundary</h2><div class="disclosure-box"><p>This page independently summarizes the authors' COMOSA 2026 conference paper. Its stylized experiments and public-data-anchored counterfactual are not an empirical evaluation of a live biometric deployment. MTA ridership data are not biometric-gate logs, OMNY share is only a digital-payment adoption proxy, and the biometric operating points come from NIST benchmarks rather than measurements at the modeled stations.</p><p>The numerical findings are scenario-dependent, not universal deployment prescriptions. The study analyzes queueing and operational consequences; privacy, consent, security, accessibility, and governance require separate evaluation.</p></div>
        """,
        aside="""
          <div class="aside-card"><h3>Methods</h3><ul><li>Multiclass queueing</li><li>Finite same-gate retries</li><li>Constrained optimization</li><li>Discrete-event simulation</li></ul></div>
          <div class="aside-card"><h3>Decision levers</h3><ul><li>Recognition threshold</li><li>Retry limit</li><li>Biometric adoption</li><li>Gate and recovery capacity</li></ul></div>
          <div class="aside-card"><h3>Evidence</h3><p>Stylized experiments plus a public-data-anchored counterfactual using MTA demand and NIST benchmark operating points.</p></div>
          <div class="aside-card"><h3>Paper</h3><p>COMOSA 2026<br>Hanoi, Vietnam<br>August 7–8, 2026</p></div>
          <div class="aside-card"><h3>Research theme</h3><p><a href="/research/#stochastic">Stochastic service systems</a></p></div>
        """,
    )

    case_page(
        "reservoir-operations",
        case_type="Sanitized industrial case study · Infrastructure",
        title="Reservoir operations under uncertainty",
        lead="Decision-support research for a multi-objective water system where today’s action changes tomorrow’s feasible choices.",
        meta=["Industrial research", "Forecasting · simulation · optimization", "Selected details omitted"],
        current="projects",
        copy="""
          <h2>Context</h2><p>Reservoir operations require sequential decisions under uncertain future conditions. Releases made now affect the future state of the system, while operational objectives and constraints may compete with one another.</p>
          <h2>Decision challenge</h2><p>The difficulty is not only finding a mathematical optimum. Operational rules, uncertain inputs, multiple performance criteria, and domain interpretation all affect whether a policy is useful.</p>
          <h2>My contribution</h2><p>My work focused on translating operational requirements into a mathematical and computational framework, developing evaluation and optimization methodology, and connecting model outputs with domain interpretation.</p>
          <h2>Approach</h2><ul><li>Formulate operational objectives and constraints at a decision-relevant level.</li><li>Evaluate alternatives under multiple future scenarios.</li><li>Use forecasting and simulation as inputs to decision analysis.</li><li>Optimize candidate decisions or operating policies and compare them using operational performance criteria.</li></ul>
          <h2>Outcome</h2><p>The framework supports systematic comparison of operational alternatives across scenarios and objectives. Detailed client information, parameters, architecture, algorithms, and quantitative results are omitted.</p>
          <blockquote>In applied OR, the hardest part is often deciding what the optimization problem should be—not solving the final mathematical program.</blockquote>
        """,
        aside="""
          <div class="aside-card"><h3>My role</h3><ul><li>Problem formulation</li><li>Computational methodology</li><li>Scenario-based evaluation</li><li>Translation of domain requirements</li></ul></div>
          <div class="aside-card"><h3>Methods</h3><ul><li>Time-series forecasting</li><li>Simulation</li><li>Optimization</li><li>Multi-objective analysis</li></ul></div>
          <div class="aside-card"><h3>Confidentiality</h3><p>Client identity, system topology, operational parameters, proprietary implementation, and non-public performance metrics are not disclosed.</p></div>
        """,
    )

    case_page(
        "inventory-optimization",
        case_type="Applied research · Manufacturing & inventory",
        title="Inventory optimization at scale",
        lead="Choose the right safety-stock model for each item without losing control of the portfolio budget. In a published evaluation on 2,500 items, the optimization completed in 2.32 seconds while enforcing a shared budget constraint.",
        meta=["Published 2,500-item benchmark", "Binary optimization · SOS1", "IEEE CASE 2025"],
        current="projects",
        copy="""
          <h2>Context</h2><p>Large inventory systems contain items with very different demand patterns, lead times, prices, and service requirements. Applying one safety-stock formula to every item is easy to operate but can be inaccurate: a conservative rule ties up working capital, while an aggressive rule creates shortages and urgent recovery work.</p>
          <h2>Decision challenge</h2><p>The item-level and portfolio-level decisions are coupled. Giving one item more safety stock consumes budget that could protect another, so the problem is not only how much stock to hold—it is also which inventory model should govern each item.</p>
          <h2>Why the approach is fast</h2><ul><li><strong>Precompute, then select.</strong> Each candidate model first produces an item-level safety-stock quantity and a historical performance score. The portfolio optimizer then chooses among these fixed alternatives instead of repeatedly simulating the entire inventory system.</li><li><strong>Use a linear binary formulation.</strong> The selection and budget constraints form a binary integer linear program with special ordered set constraints. This lets mature solvers use specialized branching and cutting methods.</li><li><strong>Avoid nonlinear search at scale.</strong> The benchmark nonlinear approaches repeatedly approximate gradients and evaluate objectives and constraints; their runtime grows rapidly and convergence can become difficult as the item count reaches the thousands.</li></ul>

          <h2>Why decision quality improves</h2><p>The method does not claim to improve demand-forecast accuracy. It improves the safety-stock decision by allowing different items to use different models and by evaluating whether historical protection has enough margin to remain useful when demand changes.</p><ul><li><strong>Model diversity:</strong> the public evaluation combines five candidates, including an MRP-based rule, normal-demand formulas, and empirical distribution-free formulas.</li><li><strong>Margin-aware scoring:</strong> models that merely tie at a 100% historical win rate are separated by how much additional demand they could absorb before a shortage.</li><li><strong>Diminishing returns:</strong> a root-margin score rewards useful protection but discounts excessive stock, leaving budget available for items where it reduces shortage risk more effectively.</li></ul>

          <h2>Published practical results</h2><div class="callout"><strong>2,500 items optimized in 2.32 seconds.</strong> One nonlinear comparison method did not converge, while another was still running when the 12-hour test limit was reached.</div><p>The paper reports a three-month retrospective evaluation using an industrial inventory dataset, five candidate models, and a 12-month historical window. Compared with the tailored MRP-based benchmark, the root-margin version of SSMSO achieved:</p><ul><li><strong>50–60% fewer shortage-affected items per month.</strong></li><li><strong>51–64% lower adjusted shortage rates</strong> across the three monthly evaluation periods.</li><li><strong>Budget-feasible portfolio selection</strong>, keeping the combined safety-stock recommendation within the shared cap while several single-model alternatives exceeded it.</li><li><strong>About 800× faster optimization at 1,000 items</strong>: 1.72 seconds versus 23 minutes for one nonlinear benchmark.</li></ul>

          <h2>Disclosure note</h2><div class="disclosure-box"><p>This page is an independent summary of results reported in the IEEE CASE 2025 paper and is not an official statement by my employer. Only information disclosed in the published paper is summarized; confidential data, client information, internal system details, proprietary implementation, and non-public operational results are omitted.</p><p>Reported improvements are from the paper’s retrospective evaluation and should not be interpreted as verified production-deployment outcomes. The adjusted shortage rate is a proxy for inventory performance.</p><p>This page uses independently written summaries and does not reproduce IEEE text, tables, figures, or the version-of-record article.</p></div>
          <h2>Public artifact</h2><p>The method and evaluation appear in “Safety Stock Model Selection Optimization for Budget-Constrained Multi-Item Inventory Management: A Scalable Framework,” presented at IEEE CASE 2025. <a href="https://doi.org/10.1109/CASE58245.2025.11163776">DOI ↗</a></p>
        """,
        aside="""
          <div class="aside-card"><h3>Evaluation at a glance</h3><ul><li>2,500-item published benchmark</li><li>5 candidate models</li><li>3 monthly evaluation periods</li><li>Shared portfolio budget</li><li>2.32-second solve time</li></ul></div>
          <div class="aside-card"><h3>Versus MRP benchmark</h3><ul><li>50–60% fewer shortage items</li><li>51–64% lower adjusted shortage rate</li><li>Budget-feasible selection</li></ul></div>
          <div class="aside-card"><h3>Methods</h3><ul><li>Inventory modeling</li><li>Model selection</li><li>Binary linear optimization</li><li>SOS1 constraints</li><li>Root-margin win rate</li></ul></div>
          <div class="aside-card"><h3>Evidence scope</h3><p>Published retrospective evaluation, not an official employer statement or a production-deployment claim.</p></div>
        """,
    )

    case_page(
        "ecommerce-decision-systems",
        case_type="Prior applied research · Digital commerce",
        title="Decision systems for e-commerce",
        lead="Research and prototyping at the intersection of learning, allocation, and optimization for digital marketplace decisions.",
        meta=["2022–2023", "Contextual bandits · deep RL", "Pricing · selection · logistics"],
        current="projects",
        copy="""
          <h2>Scope</h2><p>My work covered several decision problems in e-commerce where a platform must choose among actions, observe uncertain outcomes, and adapt over time.</p>
          <h2>Selected problem families</h2><ul><li>Dynamic pricing and seller selection.</li><li>Advertiser or winner selection in marketplace allocation.</li><li>Contextual bandit and reinforcement-learning formulations.</li><li>Delivery, supplier allocation, and routing optimization.</li></ul>
          <h2>What I learned</h2><p>These projects strengthened a principle that continues to shape my work: an ML model should be judged by the decision process it supports. Reward design, constraints, delayed feedback, and operational feasibility matter as much as predictive accuracy.</p>
          <h2>Teaching connection</h2><p>During the same period, I taught reinforcement learning, mathematical optimization, and mathematics for AI, using practical examples and Python implementation to connect formal methods with decisions.</p>
        """,
        aside="""
          <div class="aside-card"><h3>Methods</h3><ul><li>Contextual bandits</li><li>Deep reinforcement learning</li><li>Dynamic pricing</li><li>Allocation &amp; routing</li></ul></div>
          <div class="aside-card"><h3>Role</h3><p>Part-time researcher and online lecturer at VietDevelopers Technology, Ltd.</p></div>
          <div class="aside-card"><h3>Disclosure</h3><p>Only high-level problem families and methods are presented.</p></div>
        """,
    )


def build_404() -> None:
    body = """
    <section class="page-hero"><div class="narrow"><div class="eyebrow">404</div><h1>This state is outside the model.</h1><p class="lead">The page you requested does not exist. Return to the system boundary and choose another action.</p><div class="hero-actions"><a class="button primary" href="/">Back home</a><a class="button ghost" href="/research/">Research</a></div></div></section>
    """
    render("404.html", title="Page not found — Hung Q. Nguyen", description="Page not found.", current="", body=body)


def build_misc() -> None:
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://kuniong.github.io/sitemap.xml\n", encoding="utf-8")
    # The Reservoir operations page is retained but intentionally omitted from discovery and the sitemap.
    urls = ["", "research/", "publications/", "projects/", "teaching/", "experience/", "cv/", "work/passenger-taxi/", "work/supply-demand/", "work/speed-enforcement/", "work/facial-recognition-ticket-gates/", "work/matching-queue/", "work/inventory-optimization/", "work/ecommerce-decision-systems/"]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sitemap += [f"  <url><loc>https://kuniong.github.io/{u}</loc></url>" for u in urls]
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")


def main() -> None:
    build_home()
    build_research()
    build_publications()
    build_projects()
    build_experience()
    build_teaching()
    build_cv()
    build_cases()
    build_404()
    build_misc()
    print("Site built successfully.")


if __name__ == "__main__":
    main()
