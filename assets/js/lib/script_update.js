// The debounce function receives our function as a parameter
const debounce = (fn) => {
	// This holds the requestAnimationFrame reference, so we can cancel it if we wish
	let frame;
	// The debounce function returns a new function that can receive a variable number of arguments
	return (...params) => {
		// If the frame variable has been defined, clear it now, and queue for next frame
		if (frame) {
			cancelAnimationFrame(frame);
		}
		// Queue our function call for the next frame
		frame = requestAnimationFrame(() => {
			// Call our function and pass any params we received
			fn(...params);
		});
	};
};
// Reads out the scroll position and stores it in the data attribute
// so we can use it in our stylesheets
const storeScroll = () => {
	document.documentElement.dataset.scroll = window.scrollY;
};
// Listen for new scroll events, here we debounce our `storeScroll` function
document.addEventListener("scroll", debounce(storeScroll), { passive: true });
// Update scroll position for first time
storeScroll();


// let nav = document.getElementById("navigation");
// navigation.addEventListener("mouseenter", openMainDesktopNav);
// navigation.addEventListener("mouseleave", closeMainDesktopNav);
let nav = document.getElementById("navigation");
let touchToggle = document.getElementById("mainDesktopNavTouchToggle");

touchToggle.addEventListener("click", toggleClickMainNav);

function toggleClickMainNav() {
  if (navigation.classList.contains("nav-maxed")) {
    closeMainDesktopNav();
  } else {
    openMainDesktopNav();
  }
}
//test document width is greater than 768px
var mainNavMin = true;
var mouseIsOver = false;
nav.onmouseover = function()   {
   this.mouseIsOver = true;
};
nav.onmouseout = function()   {
   this.mouseIsOver = false;
}

function toggleMainDesktopNav(){
if(this.mainNavMin && this.mouseIsOver ){
	console.log("openMainDesktopNav")
this.mainNavMin = false

}else{
	console.log("closeMainDesktopNav")
this.mainNavMin = true

}

}
function openMainDesktopNav() {
	setTimeout(function () {
		if (
			document.documentElement.clientWidth > 768
		) {
			navigation.classList.add("hover", "nav-maxed");
			navigation.classList.remove("nav-mined");
			let navItems = navigation.querySelectorAll(".nav-item");
      let icon = touchToggle.querySelector(".icon");
      icon.classList.toggle("rotate_180");
			navItems.forEach(function (navItem) {
				setTimeout(function () {
					navItem
						.querySelector(".label")
						.classList.add("inline-block", "opacity_none");
					navItem
						.querySelector(".label")
						.classList.remove("display_none:md", "opacity_0");
				}, 300);
			});
		}
	}, 500);
}
function closeMainDesktopNav() {
	setTimeout(function () {
		navigation.classList.remove("hover", "nav-maxed");
		navigation.classList.add("nav-mined");
		let navItems = navigation.querySelectorAll(".nav-item");
    let icon = touchToggle.querySelector(".icon");
    icon.classList.toggle("rotate_180");
		navItems.forEach(function (navItem) {
			navItem.querySelector(".label").classList.remove("inline-block");
			navItem.querySelector(".label").classList.add("display_none:md");
			//test document width is greater than 768px
			if (document.documentElement.clientWidth > 768) {
				navItem
					.querySelector(".label")
					.classList.remove("opacity_none");
				navItem.querySelector(".label").classList.add("opacity_0");
			}
		});
	}, 300);
}

			// let filterZone = document.getElementById("filterZone");
			// let filterZoneNav = filterZone.querySelector("nav");
			// let filterFacets = filterZone.querySelector("#filterFacets");
			// let filterZoneExpanded = true;
			// filterZoneNav.addEventListener("click", function () {
			// 	if (filterZoneExpanded) {
			// 		filterFacets.classList.toggle("opacity_0");
			// 		filterFacets.classList.toggle("opacity_none");
			// 		setTimeout(function () {
			// 			filterFacets.classList.toggle("{display_none}");
			// 			filterFacets.classList.toggle("display_none");
			// 			filterFacets.classList.toggle("min-h_0:md");
			// 			filterFacets.classList.toggle("min-h_30:md");
			// 			filterZone.classList.remove("{nav-mined}", "nav-maxed");
			// 			filterZone.classList.add("nav-mined", "{nav-maxed}");
			// 			filterZoneNav.querySelector("span.label").classList.toggle("{display_none:md}");
			// 			filterZoneNav.querySelector("span.label").classList.toggle("display_none:md");
			// 			filterZoneExpanded = false;
			// 		}, 300);
			// 		return;
			// 	} else {
			// 		filterZone.classList.add( "{nav-mined}", "nav-maxed");
			// 		filterZone.classList.remove( "nav-mined", "{nav-maxed}");
			// 		filterFacets.classList.toggle("min-h_0:md");
			// 		filterFacets.classList.toggle("min-h_30:md");
			// 		filterFacets.classList.toggle("{display_none}");
			// 		filterFacets.classList.toggle("display_none");
			// 		setTimeout(function () {
			// 			filterFacets.classList.toggle("opacity_0");
			// 			filterFacets.classList.toggle("opacity_none");
			// 			filterZoneNav.querySelector("span.label").classList.toggle("{display_none:md}");
			// 			filterZoneNav.querySelector("span.label").classList.toggle("display_none:md");
			// 			filterZoneExpanded = true;
			// 		}, 300);
			// 		return;
			// 	}
			// });