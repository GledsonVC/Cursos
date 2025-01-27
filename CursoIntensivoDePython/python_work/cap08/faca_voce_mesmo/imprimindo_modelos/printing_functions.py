import printing_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# chamando função de print_models de printing_models
printing_models.print_models(unprinted_designs[:], completed_models)
# chamando função show_completed_models de printing_models
printing_models.show_completed_models(completed_models)
