from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index() :
    return redirect(url_for('accueil'))

@app.route('/accueil')
def accueil() :
    return render_template("accueil.html")

# -------------------------
# CHAMPIONNAT U10# --------
# -------------------------

matches_U10 = [
    {"date": "samedi 8 Novembre 2025", "team1": "NANGIS ES 21", "score1": 5, "team2": "LESIGNY U.S.C. 21", "score2": 0, "status": "played"},
    {"date": "samedi 8 Novembre 2025", "team1": "ALLIANCE 77 21", "score1": 10, "team2": "FC GUIGNES 21", "score2": 1, "status": "played"},
    {"date": "samedi 8 Novembre 2025", "team1": "CHATELET EN BRIE US 21", "score1": 1, "team2": "BOMBONNAISE AS 21", "score2": 4, "status": "played"},
    {"date": "samedi 15 Novembre 2025", "team1": "LESIGNY U.S.C. 21", "score1": 6, "team2": "ALLIANCE 77 21", "score2": 3, "status": "played"},
    {"date": "samedi 15 Novembre 2025", "team1": "NANGIS ES 21", "score1": 2, "team2": "CHATELET EN BRIE US 21", "score2": 2, "status": "played"},
    {"date": "samedi 15 Novembre 2025", "team1": "FC GUIGNES 21", "score1": 5, "team2": "BOMBONNAISE AS 21", "score2": 2, "status": "played"},
    {"date": "samedi 06 Décembre 2025", "team1": "ALLIANCE 77 21", "score1": 3, "team2": "NANGIS ES 21", "score2": 2, "status": "played"},

    # Match reporté
    {"date": "samedi 06 Décembre 2025", "team1": "BOMBONNAISE AS 21", "score1": None, "team2": "LESIGNY U.S.C. 21", "score2": None, "status": "postponed"},

    {"date": "samedi 06 Décembre 2025", "team1": "CHATELET EN BRIE US 21", "score1": 5, "team2": "FC GUIGNES 21", "score2": 4, "status": "played"},
    {"date": "samedi 13 Décembre 2025", "team1": "LESIGNY U.S.C. 21", "score1": 6, "team2": "FC GUIGNES 21", "score2": 7, "status": "played"},
    {"date": "samedi 13 Décembre 2025", "team1": "NANGIS ES 21", "score1": 4, "team2": "BOMBONNAISE AS 21", "score2": 1, "status": "played"},
    {"date": "samedi 13 Décembre 2025", "team1": "ALLIANCE 77 21", "score1": 5, "team2": "CHATELET EN BRIE US 21", "score2": 0, "status": "played"},
    {"date": "samedi 17 Janvier 2026", "team1": "FC GUIGNES 21", "score1": None, "team2": "NANGIS ES 21", "score2": None, "status": "postponed"},
    {"date": "samedi 17 Janvier 2026", "team1": "LESIGNY U.S.C. 21", "score1": 0, "team2": "CHATELET EN BRIE US 21", "score2": 4, "status": "played"},
    {"date": "samedi 17 Janvier 2026", "team1": "BOMBONNAISE AS 21", "score1": 2, "team2": "ALLIANCE 77 21", "score2": 1, "status": "played"},
    {"date": "samedi 24 Janvier 2026", "team1": "BOMBONNAISE AS 21", "score1": 2, "team2": "FC GUIGNES 21", "score2": 1, "status": "played"},
    {"date": "samedi 24 Janvier 2026", "team1": "LESIGNY U.S.C. 21", "score1": 3, "team2": "ALLIANCE 77 21", "score2": 3,"status": "played"},
    {"date": "samedi 24 Janvier 2026", "team1": "CHATELET EN BRIE US 21", "score1": None, "team2": "NANGIS ES 21", "score2": None,"status": "postponed"},
    {"date": "samedi 14 Février 2026", "team1": "FC GUIGNES 21", "score1": None, "team2": "CHATELET EN BRIE US 21", "score2": None, "status": "postponed"},
    {"date": "samedi 14 Février 2026", "team1": "LESIGNY U.S.C. 21", "score1": None, "team2": "BOMBONNAISE AS 21", "score2": None,"status": "postponed"},
    {"date": "samedi 14 Février 2026", "team1": "NANGIS ES 21", "score1": None, "team2": "ALLIANCE 77 21", "score2": None,"status": "postponed"},
    {"date": "samedi 14 Mars 2026", "team1": "CHATELET EN BRIE US 21", "score1": None, "team2": "ALLIANCE 77 21","score2": None, "status": "scheduled"},
    {"date": "samedi 14 Mars 2026", "team1": "BOMBONNAISE AS 21", "score1": None, "team2": "NANGIS ES 21","score2": None, "status": "scheduled"},
    {"date": "samedi 14 Mars 2026", "team1": "FC GUIGNES 21", "score1": None, "team2": "LESIGNY U.S.C. 21","score2": None, "status": "scheduled"},
    {"date": "samedi 21 Mars 2026", "team1": "NANGIS ES 21", "score1": None, "team2": "FC GUIGNES 21","score2": None, "status": "scheduled"},
    {"date": "samedi 21 Mars 2026", "team1": "CHATELET EN BRIE US 21", "score1": None, "team2": "LESIGNY U.S.C. 21","score2": None, "status": "scheduled"},
    {"date": "samedi 21 Mars 2026", "team1": "ALLIANCE 77 21", "score1": None, "team2": "BOMBONNAISE AS 21","score2": None, "status": "scheduled"},
    {"date": "samedi 28 Mars 2026", "team1": "LESIGNY U.S.C. 21", "score1": None, "team2": "NANGIS ES 21","score2": None, "status": "scheduled"},
    {"date": "samedi 28 Mars 2026", "team1": "FC GUIGNES 21", "score1": None, "team2": "ALLIANCE 77 21","score2": None, "status": "scheduled"},
    {"date": "samedi 28 Mars 2026", "team1": "BOMBONNAISE AS 21", "score1": None, "team2": "CHATELET EN BRIE US 21","score2": None, "status": "scheduled"},

]

@app.route('/Résultats')
def Résultats() :
    standings = compute_standings(matches_U10)
    return render_template("Résultats.html",matches = matches_U10, standings= standings)

# -------------------------
# CHAMPIONNAT U11
# -------------------------

matches_U11 = [

{"date": "samedi 8 Novembre 2025", "team1": "COMBS LA VILLE C.A 2", "score1": None, "team2": "ALLIANCE 77", "score2": None, "status": "postponed"},
{"date": "samedi 8 Novembre 2025", "team1": "CHEVRY COSSIGNY FC 2", "score1": 16, "team2": "MARLES AC 2", "score2": 4, "status": "played"},
{"date": "samedi 8 Novembre 2025", "team1": "PRESLES EN BRIE RC 2", "score1":7, "team2": "SERVON FC 2", "score2":1 , "status": "played"},

{"date": "samedi 15 Novembre 2025", "team1": "PRESLES EN BRIE RC 2", "score1":5, "team2": "MARLES AC 2", "score2":0, "status": "played"},
{"date": "samedi 15 Novembre 2025", "team1": "ALLIANCE 77", "score1":1, "team2": "CHEVRY COSSIGNY FC 2", "score2":8, "status": "played"},
{"date": "samedi 15 Novembre 2025", "team1": "SERVON FC 2", "score1":1 , "team2": "COMBS LA VILLE C.A 2", "score2":4 , "status": "played"},

{"date": "samedi 6 Décembre 2025", "team1": "COMBS LA VILLE C.A 2", "score1":3, "team2": "PRESLES EN BRIE RC 2", "score2":4, "status": "played"},
{"date": "samedi 6 Décembre 2025", "team1": "ALLIANCE 77", "score1":5, "team2": "MARLES AC 2", "score2":6, "status": "played"},
{"date": "samedi 6 Décembre 2025", "team1": "SERVON FC 2", "score1":1 , "team2": "CHEVRY COSSIGNY FC 2", "score2":2 , "status": "played"},

{"date": "samedi 13 Décembre 2025", "team1": "PRESLES EN BRIE RC 2", "score1":9, "team2": "CHEVRY COSSIGNY FC 2", "score2":0, "status": "played"},
{"date": "samedi 13 Décembre 2025", "team1": "COMBS LA VILLE C.A 2", "score1":21, "team2": "MARLES AC 2", "score2":1, "status": "played"},
{"date": "samedi 13 Décembre 2025", "team1": "SERVON FC 2", "score1":2 , "team2": "ALLIANCE 77", "score2":4 , "status": "played"},

{"date": "samedi 17 Janvier 2026", "team1": "CHEVRY COSSIGNY FC 2", "score1":None, "team2": "COMBS LA VILLE C.A 2", "score2":None, "status": "postponed"},
{"date": "samedi 17 Janvier 2026", "team1": "SERVON FC 2", "score1":1, "team2": "MARLES AC 2", "score2":0, "status": "played"},

{"date": "samedi 24 Janvier 2026", "team1": "CHEVRY COSSIGNY FC 2", "score1":13, "team2": "ALLIANCE 77", "score2":1, "status": "played"},
{"date": "samedi 24 Janvier 2026", "team1": "COMBS LA VILLE C.A 2", "score1":None, "team2": "SERVON FC 2", "score2":None, "status": "postponed"},
{"date": "samedi 24 Janvier 2026", "team1": "PRESLES EN BRIE RC 2", "score1":7, "team2": "MARLES AC 2", "score2":0, "status": "played"},

{"date": "samedi 14 Février 2026", "team1": "MARLES AC 2", "score1":None, "team2": "ALLIANCE 77", "score2":None, "status": "postponed"},
{"date": "samedi 14 Février 2026", "team1": "PRESLES EN BRIE RC 2", "score1":2, "team2": "COMBS LA VILLE C.A 2", "score2":6, "status": "played"},
{"date": "samedi 14 Février 2026", "team1": "SERVON FC 2", "score1":None, "team2": "CHEVRY COSSIGNY FC 2", "score2":None, "status": "postponed"},

{"date": "samedi 14 Mars 2026", "team1": "CHEVRY COSSIGNY FC 2", "score1":None, "team2": "PRESLES EN BRIE RC 2", "score2":None, "status": "scheduled"},
{"date": "samedi 14 Mars 2026", "team1": "MARLES AC 2", "score1":None, "team2": "COMBS LA VILLE C.A 2", "score2":None, "status": "scheduled"},
{"date": "samedi 14 Mars 2026", "team1": "ALLIANCE 77", "score1":None, "team2": "SERVON FC 2", "score2":None, "status": "scheduled"},

{"date": "samedi 21 Mars 2026", "team1": "COMBS LA VILLE C.A 2", "score1":None, "team2": "CHEVRY COSSIGNY FC 2", "score2":None, "status": "scheduled"},
{"date": "samedi 21 Mars 2026", "team1": "ALLIANCE 77", "score1":None, "team2": "PRESLES EN BRIE RC 2", "score2":None, "status": "scheduled"},
{"date": "samedi 21 Mars 2026", "team1": "MARLES AC 2", "score1":None, "team2": "SERVON FC 2", "score2":None, "status": "scheduled"},

{"date": "samedi 28 Mars 2026", "team1": "SERVON FC 2", "score1":None, "team2": "PRESLES EN BRIE RC 2", "score2":None, "status": "scheduled"},
{"date": "samedi 28 Mars 2026", "team1": "MARLES AC 2", "score1":None, "team2": "CHEVRY COSSIGNY FC 2", "score2":None, "status": "scheduled"},
{"date": "samedi 28 Mars 2026", "team1": "ALLIANCE 77", "score1":None, "team2": "COMBS LA VILLE C.A 2", "score2":None, "status": "scheduled"},

{"date": "samedi 04 Mars 2026", "team1": "PRESLES EN BRIE RC 2", "score1":None, "team2": "ALLIANCE 77", "score2":None, "status": "scheduled"},

]

@app.route('/Résultats_U11')
def Résultats_U11() :
    standings = compute_standings(matches_U11)
    return render_template("Résultats_U11.html",matches = matches_U11, standings= standings)

def compute_standings(matches):
    standings = {}

    for m in matches:

        # On ignore les matchs non joués
        if m.get("status") != "played":
            continue

        t1, t2 = m["team1"], m["team2"]
        s1, s2 = m["score1"], m["score2"]

        # Initialisation
        for team in (t1, t2):
            if team not in standings:
                standings[team] = {
                    "points": 0,
                    "played": 0,
                    "wins": 0,
                    "draws": 0,
                    "losses": 0,
                    "goals_for": 0,
                    "goals_against": 0
                }

        # Match joué
        standings[t1]["played"] += 1
        standings[t2]["played"] += 1

        # Buts
        standings[t1]["goals_for"] += s1
        standings[t1]["goals_against"] += s2
        standings[t2]["goals_for"] += s2
        standings[t2]["goals_against"] += s1

        # Résultat
        if s1 > s2:
            standings[t1]["points"] += 3
            standings[t1]["wins"] += 1
            standings[t2]["losses"] += 1
        elif s2 > s1:
            standings[t2]["points"] += 3
            standings[t2]["wins"] += 1
            standings[t1]["losses"] += 1
        else:
            standings[t1]["points"] += 1
            standings[t2]["points"] += 1
            standings[t1]["draws"] += 1
            standings[t2]["draws"] += 1

    # Différence de buts
    for team, data in standings.items():
        data["goal_diff"] = data["goals_for"] - data["goals_against"]

    # Tri officiel
    sorted_standings = sorted(
        standings.items(),
        key=lambda x: (x[1]["points"], x[1]["goal_diff"], x[1]["goals_for"]),
        reverse=True
    )

    return sorted_standings
print(compute_standings(matches_U10))
print(compute_standings(matches_U11))


if __name__ == '__main__': app.run(debug=True)


