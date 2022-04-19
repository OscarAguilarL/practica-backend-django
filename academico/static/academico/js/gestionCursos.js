window.addEventListener('DOMContentLoaded', () => {
  const btnEliminar = document.querySelectorAll('.btnEliminar')

  btnEliminar.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      const confirmacion = confirm('¿Estás seguro que deseas eliminar?')

      if (!confirmacion) {
        e.preventDefault()
      }
    })
  })
})
