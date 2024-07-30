// Script that fetches and lists the title for all movies by using the URL

$(document).ready(function () {
    $.ajax({
      type: 'GET',
      url: 'https://swapi-api.hbtn.io/api/films/?format=json',
      success: function (data) {
        const films = data.results;
        $.each(films, function (i, film) {
          const listItem = document.createElement('li');
          listItem.innerText = film.title;
          $('#list_movies').append(listItem);
        });
      }
    });
  });
