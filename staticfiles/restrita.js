$(document).ready(function(){
    $('.sidenav').sidenav();
});


if ( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    $('.dropdown-trigger').dropdown({constrainWidth: false});
} else {
    $('.dropdown-trigger').dropdown({ hover: true, constrainWidth: false });
}
