/*=========================  header slider  ================================================*/

let header_slider = new Swiper('.header_slider', {
	wrapperClass: "header_slider_wrap",
	slideClass: "page",
	slidesPerView: 4,
	spaceBetween: 20,
	loop: true,
})

/*=========================  popular excursions slider  ================================================*/

let popular_excursions_slider = new Swiper('.popular_excursions_slider', {
	wrapperClass: "popular_excursions_slider_wrap",
	slideClass: "page",
	slidesPerView: 5.1,
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
		pop_up_img.setAttribute("src", `/static/${src_for_popup.slice(src_for_popup.indexOf("img"), -2)}`);
	}
})

/*=========================  reviews  ================================================*/

let reviews_slider = new Swiper('.reviews_slider', {
	wrapperClass: "reviews_slider_wrap",
	slideClass: "page",
	slidesPerView: 2.3,
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

// /*=========================  Адаптив  ================================================*/

let width = window.innerWidth;
adaptive(width);


function adaptive(width) {
	if (width > 1920) {
		header_slider.params.slidesPerView = 5.2;
		reviews_slider.params.slidesPerView = 3.1;

	}

	if (width > 1600 && width <= 1920) {
		header_slider.params.slidesPerView = 4;
		popular_excursions_slider.params.slidesPerView = 5.1;
		popular_excursions_slider.params.spaceBetween = 20;
		reviews_slider.params.slidesPerView = 2.3;

	}

	if (width >= 1280 && width <= 1600) {
		header_slider.params.slidesPerView = 4;
		popular_excursions_slider.params.slidesPerView = 4;
		popular_excursions_slider.params.spaceBetween = 20;
		reviews_slider.params.slidesPerView = 2;
	}

	if (width >= 1024 && width < 1280) {
		header_slider.params.slidesPerView = 3;
		popular_excursions_slider.params.slidesPerView = 3.5;
		popular_excursions_slider.params.spaceBetween = 20;
		reviews_slider.params.slidesPerView = 1.5;

	}

	if (width >= 768 && width < 1024) {
		header_slider.params.slidesPerView = 3;
		popular_excursions_slider.params.slidesPerView = 2.8;
		popular_excursions_slider.params.spaceBetween = 10;
		reviews_slider.params.slidesPerView = 1.2;
	}

	if (width >= 480 && width < 768) {
		header_slider.params.slidesPerView = 1.5;
		popular_excursions_slider.params.slidesPerView = 2.1;
		popular_excursions_slider.params.spaceBetween = 10;
		if (width < 550) {
			popular_excursions_slider.params.slidesPerView = 1.5;

		}
		reviews_slider.params.slidesPerView = 1;

	}
	if (width >= 320 && width < 480) {
		header_slider.params.slidesPerView = 1.5;
		popular_excursions_slider.params.slidesPerView = 1.3;
		popular_excursions_slider.params.spaceBetween = 10;
		if (width < 350) {
			popular_excursions_slider.params.slidesPerView = 1.2;

		}
		reviews_slider.params.slidesPerView = 1.3;
	}
	if (width < 320) {
		header_slider.params.slidesPerView = 1.1;
		popular_excursions_slider.params.slidesPerView = 1.1;
		popular_excursions_slider.params.spaceBetween = 10;
	}
};
window.addEventListener("resize", event => {
	width = window.innerWidth;
	adaptive(width);
});





