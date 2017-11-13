/* like counting */
$(document).ready(function() {
    $('.post-likes').click(function() {
        var id;
        id = $(this).attr('data-testimonies-id');
        $.get('/like-testimonies/', {
            post_id: id
        }, function(data) {
            $('.like_count_testimonies').html(data);
        });
    });
});
