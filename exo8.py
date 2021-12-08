dico = {
      'name': "nom-de-famille",
      'firstname': "prenom",
      'promo': 2021,
      'group': 111
}

print(f"votre nom est {dico['name']}, prénom est {dico['firstname']}, "
      f"vous faites partie de la promo {dico['promo']} et votre groupe est {dico['group']}")

rt111 = {
      '10': dico.items()
}
print(rt111['10'])