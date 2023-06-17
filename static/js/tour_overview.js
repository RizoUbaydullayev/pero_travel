// =============== header =================================
let addToFavoritesBtn = document.querySelectorAll(".add_to_favorites_input");
let addToFavoritesBtnLabels = document.querySelectorAll(".add_to_favorites_label");
addToFavoritesBtnLabels.forEach(label => {
	label.addEventListener("click", (event) => {
		addToFavoritesBtnLabels.forEach(el => {
			el.classList.toggle("label_checked");
		})
	})
})

// =============== travel_calendar =================================
let travelCalendar = new AirDatepicker('.travel_calendar-calendar', {
	classes: "air_datepicker-travel_calendar",

});

let calendarDays = document.querySelectorAll(".-day-");
let delimiter = (window.innerWidth <= 480) ? "" : "-";
calendarDays.forEach(el => {
	if (!el.classList.contains('-other-month-')) {
		let startTime = "6:00";
		let endTime = "20:00";
		el.innerHTML = `
        <div class="day_inner">
            <div>${el.textContent}</div>
            <div class="tour_time"><div>${startTime}</div>${delimiter}<div>${endTime}</div></div>
        </div>`
	}
})

// =============== route_description =================================
var routeDescriptionSlider = new Swiper('.route_description_slider', {
	wrapperClass: "route_description_slider-wrap",
	slideClass: "page",
	slidesPerView: 1.45,
	spaceBetween: 20,
	freeMode: {
		enabled: true,
		sticky: false,
	},
	pagination: {
		el: ".progress_line",
		type: "progressbar",
		progressbarOpposite: false,
	},
	navigation: {
		nextEl: ".swiper-button-next",
		prevEl: ".swiper-button-prev",
	},
})


/*=========================  galery  ================================================*/
let pop_up_for_gallery = document.querySelector(".pop_up_for_gallery");
let pop_up_img = pop_up_for_gallery.children[0].children[1];
let gallery_images = document.querySelector(".gallery > .gallery_images");
document.addEventListener("click", event => {
	if (event.target == pop_up_img ||
		event.target == pop_up_for_gallery.children[1]) {
		pop_up_for_gallery.style.cssText = "display: flex;";

	}
	else {
		gallery_images.style.cssText = "opacity: 1;";
		pop_up_for_gallery.style.cssText = "display: none;";
	}
})

document.addEventListener("click", event => {
	if (event.target.classList.contains("gallery_image")) {
		console.log(document.querySelector("body"));
		src_for_popup = window.getComputedStyle(event.target).backgroundImage;
		pop_up_for_gallery.style.cssText = "display: flex;";
		gallery_images.style.cssText = "opacity: 0.3;";
		pop_up_img.setAttribute("src", `./${src_for_popup.slice(src_for_popup.indexOf("img"), -2)}`);
	}
})

/*=========================  reviews  ================================================*/

let reviews_slider = new Swiper('.reviews_slider', {
	wrapperClass: "reviews_slider_wrap",
	slideClass: "page",
	slidesPerView: 2.3,
	spaceBetween: 20,
	freeMode: {
		enabled: false,
		sticky: true,
	},
	pagination: {
		el: ".progress_line",
		type: "progressbar",
		progressbarOpposite: false,
	},
	navigation: {
		nextEl: ".swiper-button-next",
		prevEl: ".swiper-button-prev",
	},
})

/*=========================  book_tour  ================================================*/

let bookTourDateInput = new AirDatepicker('.date-input', {
	classes: "book_tour-date_input",
});


// /*=========================  Адаптив  ================================================*/

adaptive(window.innerWidth);
window.addEventListener("resize", () => {
	width = window.innerWidth;
	adaptive(width);
});

function adaptive(width) {
	if (width > 1920) {
		reviews_slider.params.slidesPerView = 3.1;
	}

	if (width > 1600 && width <= 1920) {
		routeDescriptionSlider.params.slidesPerView = 1.5;
		reviews_slider.params.slidesPerView = 2.3;
	}


	if (width >= 1280 && width <= 1600) {
		routeDescriptionSlider.params.slidesPerView = 1.5;
		reviews_slider.params.slidesPerView = 2;
	}

	if (width >= 1024 && width < 1280) {
		routeDescriptionSlider.params.slidesPerView = 1.5;
		reviews_slider.params.slidesPerView = 1.5;
	}

	if (width >= 768 && width < 1024) {
		routeDescriptionSlider.params.slidesPerView = width / 413;
		reviews_slider.params.slidesPerView = 1.2;
	}

	if (width >= 480 && width < 768) {
		routeDescriptionSlider.params.slidesPerView = width / 413;
		reviews_slider.params.slidesPerView = 1;

	}

	if (width >= 320 && width < 480) {
		routeDescriptionSlider.params.slidesPerView = 1;
		reviews_slider.params.slidesPerView = 1.3;

	}

	if (width < 320) {
		routeDescriptionSlider.params.slidesPerView = 1;
	}

	// базовые действия
	routeDescriptionSlider.update();
};


