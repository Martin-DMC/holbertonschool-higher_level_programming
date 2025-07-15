document.addEventListener('DOMContentLoaded', function () {
  const uList = document.getElementById('list_movies');
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      data.results.forEach(movie => {
        const li = document.createElement('li');
        li.innerHTML = movie.title;
        uList.appendChild(li);
      });
    })
    .catch(error => {
      console.error('Error: ', error);
      uList.innerHTML = 'error del pinchi servidor';
    });
});
