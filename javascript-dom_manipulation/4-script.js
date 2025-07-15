document.addEventListener('DOMContentLoaded', function () {
  const uLista = document.querySelector('.my_list');
  const activador = document.getElementById('add_item');

  activador.onclick = () => {
    const li = document.createElement('li');
    li.innerHTML = 'Item';
    uLista.appendChild(li);
  };
});
