// =============== кнопка добавления в избранное =================================
$(document).ready(function () {
    let = addToFavoritesBtnLabels = $('.add_to_favorites_label')
    console.log(addToFavoritesBtnLabels);
    addToFavoritesBtnLabels.each(function () {
        let element = $(this);
        element.click(function () {

            if (element.hasClass('label_checked')) {
                ajax_url = `/tours/${element.data('tour_id')}/remove_from_favorites`
            }
            else {
                ajax_url = `/tours/${element.data('tour_id')}/add_to_favorites`
            }
            $.ajax({
                url: ajax_url,
                success: function (response) {
                    // Обработка успешного ответа
                    element.toggleClass("label_checked");
                    console.log(response);
                }
            });
        })
    });
});