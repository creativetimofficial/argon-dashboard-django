


// Obtiene una referencia a la barra lateral
const sidebar = document.getElementById('sidenav-main');

// Obtiene una referencia al botón de toggle
const sidebarToggleButton = document.querySelector('.navbar-toggler');

// Obtiene una referencia a todos los elementos de navegación en la barra lateral
const sidebarNavLinks = sidebar.querySelectorAll('.nav-link');

// Define los atributos data-placement para el estado contraído y expandido
const placementCollapsed = 'right';
const placementExpanded = 'bottom';

// Agrega un evento click al botón de toggle
sidebarToggleButton.addEventListener('click', toggleSidebar);

// Función para contraer o expandir la barra lateral
function toggleSidebar() {
  sidebar.classList.toggle('collapsed');

  // Obtiene el nuevo estado de la barra lateral
  const isCollapsed = sidebar.classList.contains('collapsed');

  // Actualiza los atributos data-placement de los elementos de navegación
  sidebarNavLinks.forEach(function(link) {
    const tooltip = bootstrap.Tooltip.getInstance(link);

    if (isCollapsed) {
      tooltip._config.placement = placementCollapsed;
    } else {
      tooltip._config.placement = placementExpanded;
    }

    tooltip.update();
  });
}


