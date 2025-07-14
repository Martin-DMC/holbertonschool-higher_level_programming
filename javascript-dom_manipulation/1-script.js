document.addEventListener('DOMContentLoaded', function () {
  const activador = this.getElementById('red_header');
  const header = this.querySelector('header');
  activador.onclick = () => {
    header.style.color = '#ff0000';
  };
});
