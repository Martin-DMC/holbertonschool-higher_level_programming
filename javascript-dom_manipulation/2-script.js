document.addEventListener('DOMContentLoaded', function () {
  const header = this.querySelector('header');
  const activador = this.getElementById('red_header');

  activador.onclick = () => {
    header.classList.add('red');
  };
});
