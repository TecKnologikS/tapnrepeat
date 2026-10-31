# tapnrepeat

Site de Tap'n Repeat (tapnrepeat.tecknologiks.com) : présentation, politique de confidentialité, support et mentions légales, en anglais (racine) et en français (`fr/`).

Site statique publié avec GitHub Pages (workflow `.github/workflows/pages.yml`, à chaque push sur `main`). Réglage à faire une fois sur GitHub : Settings → Pages → Source : « GitHub Actions ». Le domaine est donné par `CNAME`.

Les pages sont générées par `build.py` (textes et gabarit communs) : modifier `build.py`, puis lancer `python3 build.py .` et committer les HTML.

| Page | Rôle | URL à déclarer |
| --- | --- | --- |
| `index.html`, `fr/index.html` | Présentation, lien App Store | App Store Connect → URL de confidentialité (racine actuelle) / marketing |
| `privacy.html`, `fr/confidentialite.html` | Politique de confidentialité (AdMob, UMP, ATT, Game Center) | App Store Connect → *Privacy Policy URL* ; AdMob → message RGPD |
| `support.html`, `fr/support.html` | Contact et FAQ | App Store Connect → *Support URL* |
| `legal.html`, `fr/mentions-legales.html` | Mentions légales | — |

## À garder à jour

La politique de confidentialité décrit le fonctionnement réel de l'app. Toute évolution qui touche aux données (nouveau SDK, analytics, compte, achats intégrés…) doit être reportée ici avant sa mise en ligne, ainsi que dans la fiche « Confidentialité » d'App Store Connect.

Le site ne charge aucune ressource externe et ne dépose aucun cookie. Ces textes ne remplacent pas un avis juridique.
