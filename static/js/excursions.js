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



addToFavoritesBtn = document.querySelector("#add_to_favorites");
addToFavoritesBtnLabels = document.querySelectorAll(".add_to_favorites_label");
addToFavoritesBtnLabels.forEach(label => {
    label.addEventListener("click", (event) => {
        event.target.classList.toggle("label_checked");
    })
})




