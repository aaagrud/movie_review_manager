# Movie Reviews Django App

## Name
Movie Reviews

## Description
Movie Reviews is a Django-based web application that allows users to create, view, edit, and delete movie reviews. Each review includes the movie's title, release year, and a brief summary. This application also includes a model for directors, although it's not fully integrated into the provided views.

## Features
- **Create Movie Reviews**: Users can fill out a form to add a new movie review to the database.
- **List Movie Reviews**: Users can see a list of all movie reviews stored in the database.
- **Edit Movie Reviews**: Users can update the details of an existing movie review.
- **Delete Movie Reviews**: Users can remove a movie review from the database.

## Tech Stack
- **Backend**: Django
- **Frontend**: HTML, CSS
- **Database**: SQLite (default for Django projects)
- **Forms**: Django Forms

## Views
- `create(request)`: Handles the creation of a new movie review.
- `list(request)`: Displays all movie reviews.
- `edit(request, pk)`: Handles the editing of an existing movie review.
- `delete(request, pk)`: Handles the deletion of a movie review.

## Models
- `MovieInfo`: Model to store movie details including title, year, and summary.
- `Director`: Model to store director details, currently not integrated with views.

## Forms
- `MovieForm`: Django ModelForm to create and update `MovieInfo` entries.

## Usage
1. **Creating a Review**: Navigate to the form to add a new movie review and submit it.
2. **Listing Reviews**: View all the movie reviews on the list page.
3. **Editing a Review**: Select a movie review to edit and update its details.
4. **Deleting a Review**: Select a movie review to delete from the database.

## Templates
- `create.html`: Form for creating and editing movie reviews.
- `list.html`: Displays the list of all movie reviews.

## CSS
- Custom CSS included for styling the templates.
