function size(){
    let a = window.innerWidth;
    let b = document.getElementById('demo');
    b.innerHTML = a;
}



$(document).ready(function(){
    $("#toogle-button").click(
        function(){
            var div = $("#toogle-button-img");
            div.animate({height: "36px"}, 100);
            div.animate({height: "35px"}, 100);
            $("#primary-menu").fadeToggle();
            $("#primary-menu").css("display" ,"flex");
        })
})

$(document).ready(function(){
    $("#women-primary-menu").mouseenter(function(){
        $("#women-dropdown-container").slideDown();

    });

    $(".hide-panel").click(function(){
            var div = $(".hide-panel");
            div.animate({height: "25px"}, 100);
            div.animate({height: "18px"}, 100);
        $("#women-dropdown-container").slideUp();
    });

})




$(document).ready(function(){
    $("#men-primary-menu").mouseenter(function(){
        $("#men-dropdown-container").slideDown();
    });

    $(".hide-panel").click(function(){
        $("#men-dropdown-container").slideUp();
    });

})



$(document).ready(function(){
    $("#children-primary-menu").mouseenter(function(){
        $("#children-dropdown-container").slideDown();
    });

    $(".hide-panel").click(function(){
        $("#children-dropdown-container").slideUp();
    });


})


$(document).ready(function(){
    $("#accessories-primary-menu").mouseenter(function(){
        $("#accessories-dropdown-container").slideDown();
    });

    $(".hide-panel").click(function(){
        $("#accessories-dropdown-container").slideUp();
    });


})

