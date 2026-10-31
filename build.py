"""Generates the static pages of tapnrepeat.tecknologiks.com (EN at the root, FR in fr/)."""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1])
STORE = "https://apps.apple.com/app/id935631691"
MAIL = "support@tecknologiks.com"
UPDATED = {"en": "October 31, 2026", "fr": "31 octobre 2026"}

PAGES = {
    "en": {"home": "index.html", "privacy": "privacy.html", "support": "support.html", "legal": "legal.html"},
    "fr": {"home": "index.html", "privacy": "confidentialite.html", "support": "support.html", "legal": "mentions-legales.html"},
}
LABELS = {
    "en": {"home": "Home", "privacy": "Privacy", "support": "Support", "legal": "Legal notice", "privacy_long": "Privacy policy"},
    "fr": {"home": "Accueil", "privacy": "Confidentialité", "support": "Support", "legal": "Mentions légales", "privacy_long": "Politique de confidentialité"},
}


def href(lang, page, from_lang):
    """Link from a page in from_lang to page in lang."""
    if lang == from_lang:
        return PAGES[lang][page] if page != "home" else "./"
    if lang == "fr":
        return "fr/" + (PAGES["fr"][page] if page != "home" else "")
    return "../" + (PAGES["en"][page] if page != "home" else "")


def render(lang, page, title, description, body):
    pre = "" if lang == "en" else "../"
    other = "fr" if lang == "en" else "en"
    L = LABELS[lang]
    current = ' aria-current="page"'
    nav = "\n".join(
        f'        <a href="{href(lang, p, lang)}"{current if p == page else ""}>{L[p]}</a>'
        for p in ("support", "privacy"))
    foot = "\n".join(f'        <a href="{href(lang, p, lang)}">{L["privacy_long"] if p == "privacy" else L[p]}</a>'
                     for p in ("home", "support", "privacy", "legal"))
    alt_en = "https://tapnrepeat.tecknologiks.com/" + (PAGES["en"][page] if page != "home" else "")
    alt_fr = "https://tapnrepeat.tecknologiks.com/fr/" + (PAGES["fr"][page] if page != "home" else "")
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#fff6e5">
  <meta name="apple-itunes-app" content="app-id=935631691">
  <link rel="icon" href="{pre}assets/icon.png">
  <link rel="alternate" hreflang="en" href="{alt_en}">
  <link rel="alternate" hreflang="fr" href="{alt_fr}">
  <link rel="alternate" hreflang="x-default" href="{alt_en}">
  <link rel="stylesheet" href="{pre}assets/style.css">
</head>
<body>
  <div class="wrap">
    <header class="site">
      <a class="brand" href="./"><img src="{pre}assets/icon.png" width="36" height="36" alt="">Tap'n Repeat</a>
      <nav class="site" aria-label="Navigation">
{nav}
        <a href="{href(other, page, lang)}" hreflang="{other}" lang="{other}">{other.upper()}</a>
      </nav>
    </header>

{body}

    <footer class="site">
      <nav aria-label="{'Legal links' if lang == 'en' else 'Liens légaux'}">
{foot}
      </nav>
      <p>{'App Store and Game Center are trademarks of Apple Inc. Google AdMob is a trademark of Google LLC.' if lang == 'en' else 'App Store et Game Center sont des marques d’Apple Inc. Google AdMob est une marque de Google LLC.'}</p>
      <p>© 2026 <a href="https://tecknologiks.com/">TecKnologikS</a></p>
    </footer>
  </div>
</body>
</html>
"""


SHAPES = """        <div class="shapes" aria-hidden="true">
          <span class="shape rond"></span><span class="shape carre"></span><span class="shape etoile"></span><span class="shape coeur"></span>
        </div>"""

HOME = {
    "en": f"""    <main>
      <section class="hero">
        <img class="icon" src="assets/icon.png" width="120" height="120" alt="Tap'n Repeat icon">
        <h1>Watch. Remember.<br>Tap it back.</h1>
        <p class="lead">A memory game with toy shapes: watch the sequence light up, then repeat it. Six worlds, each with its own twist, and three stars to win on every level.</p>
{SHAPES}
        <a class="button" href="{STORE}">Download on the App Store</a>
      </section>

      <section class="features" aria-label="Features">
        <div class="feature"><h3>Six worlds</h3><p>Free order, in order, backwards, a sequence that keeps growing, shuffled pieces and a secret code.</p></div>
        <div class="feature"><h3>Stars and bonuses</h3><p>Win up to three stars per level. Coins buy bonuses like the 50/50 when a level gets tough.</p></div>
        <div class="feature"><h3>Free to play</h3><p>No purchase needed. Optional rewarded ads give you extra coins, up to five a day.</p></div>
        <div class="feature"><h3>Game Center</h3><p>Compare your star total and unlock an achievement for each world.</p></div>
      </section>
    </main>""",
    "fr": f"""    <main>
      <section class="hero">
        <img class="icon" src="../assets/icon.png" width="120" height="120" alt="Icône de Tap'n Repeat">
        <h1>Regarde. Retiens.<br>Reproduis.</h1>
        <p class="lead">Un jeu de mémoire avec des formes à encastrer : regarde la séquence s’allumer, puis reproduis-la. Six mondes, chacun avec sa règle, et trois étoiles à gagner à chaque niveau.</p>
{SHAPES}
        <a class="button" href="{STORE}">Télécharger sur l’App Store</a>
      </section>

      <section class="features" aria-label="Fonctionnalités">
        <div class="feature"><h3>Six mondes</h3><p>Dans le désordre, en ordre, à l’envers, une suite qui s’allonge, des pièces qui se mélangent et un code secret.</p></div>
        <div class="feature"><h3>Étoiles et bonus</h3><p>Jusqu’à trois étoiles par niveau. Les pièces achètent des bonus, comme le 50/50, quand un niveau résiste.</p></div>
        <div class="feature"><h3>Gratuit</h3><p>Aucun achat nécessaire. Des pubs facultatives donnent des pièces en plus, jusqu’à cinq par jour.</p></div>
        <div class="feature"><h3>Game Center</h3><p>Compare ton total d’étoiles et débloque un succès pour chaque monde.</p></div>
      </section>
    </main>""",
}

PRIVACY = {
    "en": f"""    <main class="doc">
      <h1>Privacy policy</h1>
      <p class="updated">Last updated: {UPDATED['en']}</p>
      <p class="summary"><strong>In short:</strong> Tap'n Repeat has no account and no server of its own. Your progress stays on your phone. The game shows optional rewarded ads through Google AdMob, which collects data to serve and measure ads, and personalises them only if you agree. If you use Game Center, Apple receives your star total and achievements.</p>

      <h2>1. Who is responsible</h2>
      <p>Tap'n Repeat and this website are published by TecKnologikS, data controller under the General Data Protection Regulation (GDPR). Contact for any question about your data: <a href="mailto:{MAIL}">{MAIL}</a>.</p>

      <h2>2. Data stored on your phone</h2>
      <p>Your progress (levels, stars, coins), your settings and the number of ads watched today are stored only on your phone. They are never sent to TecKnologikS. Deleting the app erases them.</p>

      <h2>3. Advertising (Google AdMob)</h2>
      <p>The game shows rewarded ads only when you choose to watch one, to earn extra coins (at most five a day). There are no banners. Ads are provided by Google AdMob. The Google Mobile Ads SDK collects the following data:</p>
      <div class="table-wrap"><table>
        <thead><tr><th>Data</th><th>Purpose</th></tr></thead>
        <tbody>
          <tr><td>Approximate location (from your IP address)</td><td>Third-party advertising, analytics</td></tr>
          <tr><td>Device identifiers (advertising identifier, if you allow it, or an app-scoped identifier)</td><td>Third-party advertising, analytics</td></tr>
          <tr><td>Product interactions (app launches, taps, video views)</td><td>Third-party advertising, analytics</td></tr>
          <tr><td>Advertising data (ads you have seen)</td><td>Third-party advertising, analytics</td></tr>
          <tr><td>Crash logs and performance data</td><td>Diagnostics, analytics</td></tr>
        </tbody>
      </table></div>
      <p>This data may be used to track you across apps and websites of other companies, only with your permission (see below). Learn more in <a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its services</a> and in <a href="https://policies.google.com/privacy">Google’s privacy policy</a>.</p>

      <h3>Your consent</h3>
      <ul>
        <li><strong>In the European Economic Area, the United Kingdom and Switzerland</strong>, a consent form from Google is shown at first launch. You can accept, refuse or choose by purpose. If you refuse, ads may still be shown, without personalisation.</li>
        <li><strong>On iOS</strong>, the system then asks whether the app may use your advertising identifier (App Tracking Transparency). If you refuse, the advertising identifier is not shared.</li>
      </ul>

      <h2>4. Game Center</h2>
      <p>If you are signed in to Game Center, the game sends Apple your star total (leaderboard) and the achievements you unlock. Game Center is run by Apple under <a href="https://www.apple.com/legal/privacy/">its own privacy policy</a>. You can play without Game Center.</p>

      <h2>5. Service providers</h2>
      <div class="table-wrap"><table>
        <thead><tr><th>Provider</th><th>Role</th></tr></thead>
        <tbody>
          <tr><td>Google LLC / Google Ireland Ltd</td><td>Ads (AdMob) and the consent form (User Messaging Platform)</td></tr>
          <tr><td>Apple Inc.</td><td>App Store, Game Center, App Tracking Transparency</td></tr>
          <tr><td>GitHub, Inc. (United States)</td><td>Hosting of this website (technical connection data such as your IP address)</td></tr>
        </tbody>
      </table></div>
      <p>Some providers are located outside the European Union. These transfers are covered by the safeguards provided by the GDPR (in particular the EU–US Data Privacy Framework or standard contractual clauses).</p>

      <h2>6. Legal bases</h2>
      <ul>
        <li>Your consent: personalised ads, the advertising identifier, and storing or reading information on your device for advertising.</li>
        <li>Our legitimate interest: showing non-personalised rewarded ads that keep the game free, and measuring and protecting them against fraud.</li>
      </ul>

      <h2>7. How long</h2>
      <ul>
        <li>Data on your phone: until you delete the app.</li>
        <li>Advertising data: kept by Google under its own retention rules.</li>
        <li>Game Center data: kept by Apple under its own rules.</li>
      </ul>

      <h2>8. Changing your choices and deleting your data</h2>
      <ul>
        <li><strong>Advertising identifier:</strong> iOS Settings → Privacy &amp; Security → Tracking, then turn off Tap'n Repeat.</li>
        <li><strong>Consent for ads (EEA, UK, Switzerland):</strong> on the home screen, tap the privacy button (raised hand, next to the trophy) to open the consent form again and change or withdraw your choice at any time.</li>
        <li><strong>Game Center:</strong> sign out in iOS Settings → Game Center.</li>
        <li><strong>Progress:</strong> deleting the app erases everything it stored on your phone.</li>
      </ul>
      <p>TecKnologikS has no account and no user database, so there is nothing else to delete on our side.</p>

      <h2>9. Your rights</h2>
      <p>You have the right to access, rectify, erase, object to, restrict and port your data, and to withdraw your consent. To exercise them, write to <a href="mailto:{MAIL}">{MAIL}</a>. For data held by Google or Apple, you can also contact them directly. You can lodge a complaint with your data protection authority (in France, the CNIL: <a href="https://www.cnil.fr">www.cnil.fr</a>).</p>

      <h2>10. Children</h2>
      <p>Tap'n Repeat can be played by the whole family. TecKnologikS does not knowingly collect personal data from children. Parents can turn off tracking in iOS Settings and refuse personalised ads in the consent form.</p>

      <h2>11. This website</h2>
      <p>This website sets no cookies and loads no third-party resources.</p>

      <h2>12. Changes</h2>
      <p>If this policy changes, the date at the top of the page will be updated.</p>
    </main>""",
    "fr": f"""    <main class="doc">
      <h1>Politique de confidentialité</h1>
      <p class="updated">Dernière mise à jour : {UPDATED['fr']}</p>
      <p class="summary"><strong>En bref :</strong> Tap'n Repeat n’a ni compte ni serveur à lui. Ta progression reste sur ton téléphone. Le jeu propose des pubs facultatives via Google AdMob, qui collecte des données pour diffuser et mesurer les annonces, et ne les personnalise que si tu es d’accord. Si tu utilises Game Center, Apple reçoit ton total d’étoiles et tes succès.</p>

      <h2>1. Responsable du traitement</h2>
      <p>Tap'n Repeat et ce site sont édités par TecKnologikS, responsable du traitement au sens du Règlement général sur la protection des données (RGPD). Contact pour toute question sur tes données : <a href="mailto:{MAIL}">{MAIL}</a>.</p>

      <h2>2. Données stockées sur ton téléphone</h2>
      <p>Ta progression (niveaux, étoiles, pièces), tes réglages et le nombre de pubs regardées dans la journée sont stockés uniquement sur ton téléphone. Ils ne sont jamais envoyés à TecKnologikS. Supprimer l’app les efface.</p>

      <h2>3. Publicité (Google AdMob)</h2>
      <p>Le jeu affiche des pubs « avec récompense » uniquement quand tu choisis d’en regarder une, pour gagner des pièces (cinq par jour au maximum). Il n’y a pas de bannières. Les annonces sont fournies par Google AdMob. Le SDK Google Mobile Ads collecte les données suivantes :</p>
      <div class="table-wrap"><table>
        <thead><tr><th>Donnée</th><th>Finalité</th></tr></thead>
        <tbody>
          <tr><td>Localisation approximative (à partir de l’adresse IP)</td><td>Publicité tierce, mesure d’audience</td></tr>
          <tr><td>Identifiants de l’appareil (identifiant publicitaire si tu l’autorises, ou un identifiant propre à l’app)</td><td>Publicité tierce, mesure d’audience</td></tr>
          <tr><td>Interactions (lancements de l’app, touches, vidéos vues)</td><td>Publicité tierce, mesure d’audience</td></tr>
          <tr><td>Données publicitaires (annonces vues)</td><td>Publicité tierce, mesure d’audience</td></tr>
          <tr><td>Rapports de plantage et données de performance</td><td>Diagnostic, mesure d’audience</td></tr>
        </tbody>
      </table></div>
      <p>Ces données peuvent servir à te suivre sur les apps et sites d’autres sociétés, uniquement avec ton accord (voir ci-dessous). Pour en savoir plus : <a href="https://policies.google.com/technologies/partner-sites?hl=fr">Comment Google utilise les informations des sites ou applications qui utilisent ses services</a> et <a href="https://policies.google.com/privacy?hl=fr">les règles de confidentialité de Google</a>.</p>

      <h3>Ton consentement</h3>
      <ul>
        <li><strong>Dans l’Espace économique européen, au Royaume-Uni et en Suisse</strong>, un formulaire de consentement de Google s’affiche au premier lancement. Tu peux accepter, refuser ou choisir finalité par finalité. Si tu refuses, des pubs peuvent quand même s’afficher, sans personnalisation.</li>
        <li><strong>Sur iOS</strong>, le système demande ensuite si l’app peut utiliser ton identifiant publicitaire (App Tracking Transparency). Si tu refuses, l’identifiant publicitaire n’est pas partagé.</li>
      </ul>

      <h2>4. Game Center</h2>
      <p>Si tu es connecté à Game Center, le jeu envoie à Apple ton total d’étoiles (classement) et les succès que tu débloques. Game Center est géré par Apple selon <a href="https://www.apple.com/fr/legal/privacy/">sa propre politique de confidentialité</a>. Tu peux jouer sans Game Center.</p>

      <h2>5. Prestataires</h2>
      <div class="table-wrap"><table>
        <thead><tr><th>Prestataire</th><th>Rôle</th></tr></thead>
        <tbody>
          <tr><td>Google LLC / Google Ireland Ltd</td><td>Publicité (AdMob) et formulaire de consentement (User Messaging Platform)</td></tr>
          <tr><td>Apple Inc.</td><td>App Store, Game Center, App Tracking Transparency</td></tr>
          <tr><td>GitHub, Inc. (États-Unis)</td><td>Hébergement de ce site (données techniques de connexion, comme l’adresse IP)</td></tr>
        </tbody>
      </table></div>
      <p>Certains prestataires sont situés hors de l’Union européenne. Ces transferts sont encadrés par les garanties prévues par le RGPD (notamment le Data Privacy Framework UE–États-Unis ou des clauses contractuelles types).</p>

      <h2>6. Bases légales</h2>
      <ul>
        <li>Ton consentement : publicité personnalisée, identifiant publicitaire, et stockage ou lecture d’informations sur ton appareil à des fins publicitaires.</li>
        <li>Notre intérêt légitime : afficher des pubs non personnalisées qui gardent le jeu gratuit, les mesurer et les protéger contre la fraude.</li>
      </ul>

      <h2>7. Durées de conservation</h2>
      <ul>
        <li>Données sur ton téléphone : jusqu’à la suppression de l’app.</li>
        <li>Données publicitaires : conservées par Google selon ses propres règles.</li>
        <li>Données Game Center : conservées par Apple selon ses propres règles.</li>
      </ul>

      <h2>8. Changer tes choix et supprimer tes données</h2>
      <ul>
        <li><strong>Identifiant publicitaire :</strong> Réglages iOS → Confidentialité et sécurité → Suivi, puis désactive Tap'n Repeat.</li>
        <li><strong>Consentement pour la publicité (EEE, Royaume-Uni, Suisse) :</strong> sur l’écran d’accueil, touche le bouton Confidentialité (la main levée, à côté du trophée) pour rouvrir le formulaire et modifier ou retirer ton choix à tout moment.</li>
        <li><strong>Game Center :</strong> déconnecte-toi dans Réglages iOS → Game Center.</li>
        <li><strong>Progression :</strong> supprimer l’app efface tout ce qu’elle a stocké sur ton téléphone.</li>
      </ul>
      <p>TecKnologikS n’a ni compte ni base d’utilisateurs : il n’y a rien d’autre à supprimer de notre côté.</p>

      <h2>9. Tes droits</h2>
      <p>Tu disposes d’un droit d’accès, de rectification, d’effacement, d’opposition, de limitation et de portabilité, ainsi que du droit de retirer ton consentement. Pour les exercer, écris à <a href="mailto:{MAIL}">{MAIL}</a>. Pour les données détenues par Google ou Apple, tu peux aussi les contacter directement. Tu peux introduire une réclamation auprès de la CNIL : <a href="https://www.cnil.fr">www.cnil.fr</a>.</p>

      <h2>10. Enfants</h2>
      <p>Tap'n Repeat se joue en famille. TecKnologikS ne collecte sciemment aucune donnée personnelle d’enfants. Les parents peuvent désactiver le suivi dans les Réglages iOS et refuser la publicité personnalisée dans le formulaire de consentement.</p>

      <h2>11. Ce site</h2>
      <p>Ce site ne dépose aucun cookie et ne charge aucune ressource tierce.</p>

      <h2>12. Modifications</h2>
      <p>Si cette politique change, la date en haut de la page sera mise à jour.</p>
    </main>""",
}

SUPPORT = {
    "en": f"""    <main class="doc">
      <h1>Support</h1>
      <p>A question, a bug, an idea? Write to <a href="mailto:{MAIL}">{MAIL}</a>. Tell us your iPhone model and iOS version if something goes wrong.</p>

      <h2>Frequently asked questions</h2>
      <h3>How do I earn coins?</h3>
      <p>By finishing levels, and by watching an optional rewarded ad (+30 coins, up to five a day).</p>
      <h3>No ad is available</h3>
      <p>Ads need an internet connection and may not always be available. You may also have reached today’s limit of five; it resets the next day.</p>
      <h3>How do I change my ad choices?</h3>
      <p>See <a href="privacy.html#8-changing">“Changing your choices” in the privacy policy</a>.</p>
      <h3>My stars don’t show in Game Center</h3>
      <p>Check that you are signed in to Game Center in iOS Settings. The total is sent after each finished level.</p>
      <h3>I changed phones</h3>
      <p>Progress is stored only on your phone and is not transferred to a new device.</p>
    </main>""",
    "fr": f"""    <main class="doc">
      <h1>Support</h1>
      <p>Une question, un bug, une idée ? Écris à <a href="mailto:{MAIL}">{MAIL}</a>. Si quelque chose ne marche pas, indique ton modèle d’iPhone et ta version d’iOS.</p>

      <h2>Questions fréquentes</h2>
      <h3>Comment gagner des pièces ?</h3>
      <p>En terminant des niveaux, et en regardant une pub facultative (+30 pièces, jusqu’à cinq par jour).</p>
      <h3>Aucune pub n’est disponible</h3>
      <p>Les pubs demandent une connexion internet et ne sont pas toujours disponibles. Tu as peut-être aussi atteint la limite de cinq pour aujourd’hui ; elle repart le lendemain.</p>
      <h3>Comment changer mes choix pour la publicité ?</h3>
      <p>Voir <a href="confidentialite.html#8-changer">« Changer tes choix » dans la politique de confidentialité</a>.</p>
      <h3>Mes étoiles n’apparaissent pas dans Game Center</h3>
      <p>Vérifie que tu es connecté à Game Center dans les Réglages iOS. Le total est envoyé après chaque niveau terminé.</p>
      <h3>J’ai changé de téléphone</h3>
      <p>La progression est stockée uniquement sur ton téléphone et n’est pas transférée sur un nouvel appareil.</p>
    </main>""",
}

LEGAL = {
    "en": f"""    <main class="doc">
      <h1>Legal notice</h1>
      <h2>Publisher</h2>
      <p>TecKnologikS<br>Contact: <a href="mailto:{MAIL}">{MAIL}</a></p>
      <p>Publication director: TecKnologikS</p>
      <h2>Website hosting</h2>
      <p>GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, United States — github.com.</p>
      <h2>Intellectual property</h2>
      <p>The texts, visuals and code of Tap'n Repeat are the property of the publisher. App Store and Game Center are trademarks of Apple Inc.; Google AdMob is a trademark of Google LLC.</p>
      <h2>Personal data</h2>
      <p>See the <a href="privacy.html">privacy policy</a>. This website sets no cookies.</p>
    </main>""",
    "fr": f"""    <main class="doc">
      <h1>Mentions légales</h1>
      <h2>Éditeur</h2>
      <p>TecKnologikS<br>Contact : <a href="mailto:{MAIL}">{MAIL}</a></p>
      <p>Directeur de la publication : TecKnologikS</p>
      <h2>Hébergement</h2>
      <p>GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis — github.com.</p>
      <h2>Propriété intellectuelle</h2>
      <p>Les textes, visuels et le code de Tap'n Repeat sont la propriété de l’éditeur. App Store et Game Center sont des marques d’Apple Inc. ; Google AdMob est une marque de Google LLC.</p>
      <h2>Données personnelles</h2>
      <p>Voir la <a href="confidentialite.html">politique de confidentialité</a>. Ce site ne dépose aucun cookie.</p>
    </main>""",
}

META = {
    "home": {"en": ("Tap'n Repeat — watch, remember, tap it back", "A memory game with toy shapes: watch the sequence, then repeat it. Free on iPhone."),
             "fr": ("Tap'n Repeat — regarde, retiens, reproduis", "Un jeu de mémoire avec des formes à encastrer : regarde la séquence, puis reproduis-la. Gratuit sur iPhone.")},
    "privacy": {"en": ("Privacy policy — Tap'n Repeat", "How Tap'n Repeat handles your data: local progress, Google AdMob ads, consent, Game Center."),
                "fr": ("Politique de confidentialité — Tap'n Repeat", "Comment Tap'n Repeat traite tes données : progression locale, pubs Google AdMob, consentement, Game Center.")},
    "support": {"en": ("Support — Tap'n Repeat", "Contact and frequently asked questions."),
                "fr": ("Support — Tap'n Repeat", "Contact et questions fréquentes.")},
    "legal": {"en": ("Legal notice — Tap'n Repeat", "Publisher and hosting of the Tap'n Repeat website."),
              "fr": ("Mentions légales — Tap'n Repeat", "Éditeur et hébergeur du site de Tap'n Repeat.")},
}

BODIES = {"home": HOME, "privacy": PRIVACY, "support": SUPPORT, "legal": LEGAL}

for lang in ("en", "fr"):
    for page, bodies in BODIES.items():
        title, desc = META[page][lang]
        body = bodies[lang]
        # Anchors for the "changing your choices" section, linked from the support page.
        body = body.replace("<h2>8. Changing", '<h2 id="8-changing">8. Changing').replace("<h2>8. Changer", '<h2 id="8-changer">8. Changer')
        path = OUT / PAGES[lang][page] if lang == "en" else OUT / "fr" / PAGES[lang][page]
        path.write_text(render(lang, page, title, desc, body), encoding="utf-8")
        print("wrote", path.relative_to(OUT))
