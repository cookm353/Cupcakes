# Cupcakes

## Set Up

- [x] Make a venv and install dependencies
- [x] Make the project a Git repo

## Part One: Cupcake Model

- [ ] Create a Cupcake model in models.py
- Include the following columns
  - [ ] **id**: unique primary key that's an autoincrementing int
  - [ ] **flavor**: not nullable text column
  - [ ] **size**: not nullable text column
  - [ ] **rating**: not nullable float column
  - [ ] **image** non-nullable text column; default to https://tinyurl.com/demo-cupcake if no image is given
- [ ] Make a DB called `cupcakes`
- [ ] Add some cupcakes using seed.py