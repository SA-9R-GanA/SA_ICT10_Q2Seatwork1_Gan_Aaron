from pyscript import document


def fighters(e):
    fighters_list = ["KEN MASTERS", "CHUN LI", "CHARLIE NASH", "WILLIAM GUILE", "M. BISON", "VIKTOR SAGAT", "CAMMY WHITE", "E. HONDA", "FEI LONG", "KASANE TETO", ""
    ]

    f_name = document.getElementById("first_name")
    l_name = document.getElementById("last_name")
    Fighter = f_name + " " + l_name
    roster_checker = Fighter.upper() in fighters_list

    response = (f'Sorry {Fighter}, your name is not in the list. Better luck next time!' f'Congrats {Fighter}, your name is on the list of fighters! Goodluck in the tournament, fighter!')

    document.getElementById('res').innerHTML = response[roster_checker]
