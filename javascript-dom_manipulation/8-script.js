document.addEventListener('DOMContentLoaded', function () {
  const container = document.getElementById('hello');
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      container.innerHTML = `${data.hello}`;
    })
    .catch(error => {
      console.error('Error: ', error);
      container.innerHTML = 'error del pinchi servidor';
    });
});
