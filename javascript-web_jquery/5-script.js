// Script that adds a <li> element to a list when the user clicks on the tag

$(function () {
    $('DIV#add_item').click(function () {
        $('UL.my_list').append('<li>Item</li>');
    });
});
