document.addEventListener('DOMContentLoaded', function () {
    // sidenav initialisation
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    var modals = document.querySelectorAll(".modal");
    console.log(modals);
    M.Modal.init(modals);

    var datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmm, yyyy",
        i18n: { done: "Select" }
    });

    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
});
