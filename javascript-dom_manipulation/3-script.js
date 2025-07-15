document.addEventListener('DOMContentLoaded', function () {
  const header = this.querySelector('header');
  const activador = this.getElementById('toggle_header');
  activador.onclick = () => {
    if (header.classList.contains('green')) {
      header.classList.add('red');
      header.classList.remove('green');
    } else {
      header.classList.add('green');
      header.classList.remove('red');
    }
  };
});
