const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_content");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");


const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment_id");
    console.log('commentId', commentId);
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute = `/blogs/%{slug}/edit_comment/${commentId}/`;
  });
}


for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let slug = window.location.href.split('/')
    slug = slug[slug.length - 2]
    deleteConfirm.href = `/blogs/%{slug}/delete_comment/${commentId}/`;
    deleteModal.show();
  });
}