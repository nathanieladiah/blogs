document.addEventListener('DOMContentLoaded', () => {
	add_image();
})

const add_image = () => {
	const headerPic = document.getElementById('header-image')
	headerPic.style.backgroundImage = "url('/static/assets/img/contact-bg.jpg')"
}