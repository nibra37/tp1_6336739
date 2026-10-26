from app.core.storage import Storage, Entree

s = Storage("vault.json")
print(s.charger_donnees())
s.sauvegarder_donnees([Entree("a@b.com", "abc"), Entree("b@a.com", "xyz")])
for e in s.charger_donnees():
    print(e.email, e.mot_de_passe)