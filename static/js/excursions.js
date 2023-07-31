// =============== types_of_excursions-tabs ===============

pathname = window.location.pathname;
let tabs_list = document.querySelector(".tabs_list");
for (let i = 0; i < tabs_list.children.length; i++) {
    if (tabs_list.children[i].children[0].getAttribute("href") == pathname) {
        tabs_list.children[i].classList.add("active");
    };
};

// =============== small_filter ===================================

let smallFilterDateInput = new AirDatepicker('.date-input', {
    multipleDates: true,
    buttons: ['clear']
});


if (window.innerWidth <= 768) {
    smallFilterDateInput.update(
        { isMobile: true }
    )
}


// =============== excursion_main =================================

let filter_elements = document.querySelectorAll(".big_filter .filter_element .element_header");
filter_elements.forEach(element => {
    element.addEventListener("click", () => {
        element.classList.toggle("hidden");
        if (element.classList.contains("hidden")) {
            element.nextElementSibling.style.cssText = "display: none;"
        }
        else {
            element.nextElementSibling.style.cssText = "display: block;"
        }

    })
})


bigFilterDataValue = new AirDatepicker('.big_filter_data_value', {
    buttons: ['clear']
});



// =============== кнопка добавления в избранное =================================
$(document).ready(function () {
    let = addToFavoritesBtnLabels = $('.add_to_favorites_label')
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






