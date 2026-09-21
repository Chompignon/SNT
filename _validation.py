from capytale.autoeval import Validate, ValidateVariables, ValidateFunction, ValidateFunctionPretty


test_variables = ValidateVariables({"a":"Hello World!", "b" : "Bonjour", "c" : 63, "d" : 725, "e" : "Nombre" , "f" : "Je sais créer une variable.", "g" : 33.8})
test_exercice1 = ValidateVariables({"degre_H" : 3, "distance_H_F" : 4, "exc_A" : 5, "exc_B" : 4, "exc_C" : 4, "exc_D" : 4, "exc_E" : 3, "exc_F" : 5, "exc_G" : 3, "exc_H" : 4, "exc_I" : 3, "exc_J" : 4, "rayon" : 3, "diametre" : 5, "centre" : ("E", "G", "I")})
test_exercice2 = ValidateVariables({"rayon" : 5, "diametre" : 9, "centre" : ("E", "I"), "etapes_E" : 5, "etapes_P" : 9})
test_exercice3 = ValidateVariables({"compte_max_abonnes" : "T", "compte_max_abonnements" : "L", "N_publie" : "Oui", "I_publie" : "Non", "Etapes_N" : 3})