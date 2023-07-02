addToFavoritesBtn = document.querySelector("#add_to_favorites");
addToFavoritesBtnLabels = document.querySelectorAll(".add_to_favorites_label");
addToFavoritesBtnLabels.forEach(label => {
    label.addEventListener("click", (event) => {
        event.target.classList.toggle("label_checked");
    })
})