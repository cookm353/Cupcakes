# Cupcakes

## Set Up

- [x] Make a venv and install dependencies
- [x] Make the project a Git repo

## Part One: Cupcake Model

- [x] Create a Cupcake model in models.py
- Include the following columns
  - [x] **id**: unique primary key that's an autoincrementing int
  - [x] **flavor**: not nullable text column
  - [x] **size**: not nullable text column
  - [x] **rating**: not nullable float column
  - [x] **image** non-nullable text column; default to https://tinyurl.com/demo-cupcake if no image is given
- [x] Make a DB called `cupcakes`
- [x] Add some cupcakes using seed.py

## Part Two: Listing, Getting, and Creating Cupcakes

- Make the following routes:
- [x] **GET /api/cupcakes**
  - [x] Respond w/ JSON like `{cupcakes: [{id, flavor, size, rating, image), ...]}`
  - [x] Values should come from each cupcake instance
- [x] **GET /api/cupcakes/[cupcake-id]**
  - [x] Return data about a single cupcake
  - [x] Respond w/ JSON like `{cupcake: {id, flavor, size, rating, image}}`
  - [x] Should raise a 404 if cupcake can't be found
- [x] **POST /api/cupcakes**
  - [x] Create a cupcake with a flavor, size, rating, and image from the body of the request
  - [x] Respond w/ JSON like `{cupcake: {id, flavor, size, rating, image}}`
- [x] Test routes in Insomnia or some similar program
- [x] Use tests in tests.py

## Part Three: Update and Delete Cupcakes

- [x] Make the following routes:
- [x] **PATCH /api/cupcakes/[cupcake-id]**
  - [x] Update a cupcake w/ id passed from URL and use flavor, size, rating, and image data from body of request
  - [x] Raise a 404 if cupcake can't be found
  - [x] Respond with JSON of newly-updated cupcake like `{cupcake: {id, flavor, size, rating, image}}`
- [x] **DELETE /api/cupcakes/[cupcake-id]**
  - [x] Raise a 404 if the cupcake can't be found
  - [x] Delete cupcake with id passed in URL
  - [x] Respond with JSON like `{message: 'Deleted'}`
- [x] Test these routes in Insomnia

## Part Four: More Tests

- [x] Add tests for PATCH and DELETE routes

## Part Five: Start on the Front End

- [x] **GET /**
  - [x] Return an entirely static HTML page
  - [x] Should just have an empty list where cupcakes should appear and a form where new cupcakes can be added
- [x] Write a JS script w/ Axios and jQuery which...
  - [x] Queries the API to get cupcakes and add to the page
  - [x] Handles form submission to let the API know about new cupcake and update the list on the page to show it

## Further Study

- [x] Add test to ensure GET/PATCH/DELETE routes return a 404 when the cupcake can't be found
- [ ] Let users search for cupcakes by typing in a search term, submitting to the backend, and seeing a newly filtered list of cupcakes
  - [ ] Make sure the term is passed to the backend and you're using a LIKE or ILIKE SQL query
- [x] Refactor front-end to be object oriented
  - [x] Include `fetchAllCupcakes()` and `createCupcakes()` as class methods
  - [x] Include instance methods to update, delete, and search for cupcakes
- [x] Refactor HTML page to render a form made by WTForms
- [ ] Enhance search functionality so you don't have to wait to submit to filter by flavors
- [ ] Add functionality on front-end to update a cupcake
- [ ] Add another table for ingredients
  - [ ] When adding or editing a cupcake, identify the ingredients needed for that cupcake
  - [ ] Add a page for adding or editing ingredients
  - [ ] Will likely be many-to-many, so create a join table

## Takeaways

- Formatting data for Axios requests is a pain
- It's probably time to (re)learn Jasmine
- Never code in the main branch, only merge edits into it
- Bootstrap accordions are good in theory, but we'll leave that to the front-end devs
