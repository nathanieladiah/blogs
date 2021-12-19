document.addEventListener('DOMContentLoaded', () => {
	document.querySelector('#add-new-comment').addEventListener('click', newComment);
})

function newComment() {
	const commentBody = document.querySelector('#new-comment-body')
	console.log(commentBody)
}
// TODO add a function for replying to comments using javascript