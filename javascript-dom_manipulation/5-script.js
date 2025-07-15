document.addEventListener('DOMContentLoaded', function () {
  const header = this.querySelector('header');
  const activador = document.getElementById('update_header');
  activador.onclick = () => {
    header.innerHTML = '';
    header.innerHTML = 'New Header!!!';
  };
});
