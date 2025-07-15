document.addEventListener('DOMContentLoaded', function () {
  const divCharacter = document.getElementById('character');
  fetch('https://swapi-api.hbtn.io/api/people/10/?format=json')
    .then(response => {
      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      divCharacter.innerHTML = `${data.name}`;
    })
    .catch(error => {
      console.error('Error: ', error);
      divCharacter.innerHTML = 'error del pinchi servidor';
    });
});
