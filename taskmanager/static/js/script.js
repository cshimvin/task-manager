document.addEventListener('DOMContentLoaded', function () {
    // sidenav initialisation
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    var modals = document.querySelectorAll(".modal");
    console.log(modals);
    M.Modal.init(modals);
});

// Or with jQuery

$(document).ready(function () {
    $('.sidenav').sidenav();
});