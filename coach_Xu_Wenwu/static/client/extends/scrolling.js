/*Auto-scroll down*/
document.querySelector(".scroll_down_button").addEventListener("click", function() {
  let target_down = document.querySelector(".scroll_target_down");
  target_down.scrollIntoView({ behavior: 'smooth' });
});

/*Auto-scroll top*/
document.querySelector(".scroll_top_button").addEventListener("click", function () {
  let target_top = document.querySelector(".scroll_target_top");
  target_top.scrollIntoView({behavior: 'smooth'});
});