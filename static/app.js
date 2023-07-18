let $btn = $('start_button');
$btn.on("click", function() {
    $btn.addClass("hide")
});


let $yes = $('#yes_button');
let $no =  $('#no_button');

$yes.on('click', function(){
    $no.prop('checked', false)
})

$no.on('click', function(){
    $yes.prop('checked', false)
})