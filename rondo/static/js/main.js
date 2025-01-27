const answerYes = document.getElementById("radio-yes");
const answerNo = document.getElementById("radio-no");
const itemRole = document.getElementById("item-role");
const permissionBox = document.getElementById("permission-box");
const box = document.getElementById("box");
const customPermissions = document.getElementById("custom-permissions");

let tags = [];

if (answerNo && answerYes) {
  answerNo.addEventListener("click", (e) => {
    permissionBox.style.display = "block";
  });
  answerYes.addEventListener("click", (e) => {
    permissionBox.style.display = "none";
    tags = [];
    box.innerHTML = "";
  });
}

function addItems() {
  // Empty the text and replace it with
  customPermissions.value = "";
  tags.forEach((tag) => {
    customPermissions.value += tag + " ";
  });
}

if (itemRole) {
  itemRole.addEventListener("change", (e) => {
    if (!tags.includes(e.target.value)) {
      tags.push(e.target.value);
      addItems();
      addTag(e);
    }
  });
}

function addTag(e) {
  // create a span element for the tag
  const spanTag = document.createElement("span");
  const anchorTag = document.createElement("a");

  // Add the required classes
  spanTag.classList.add("tag", "is-dark");
  anchorTag.classList.add("tag", "is-delete");

  // Create the text nodes required for the spanTag
  const content = document.createTextNode(e.target.value);

  // Add a click event to the close button to remove the elements
  anchorTag.addEventListener("click", (e) => {
    tags.pop(e.target.parentElement.textContent);
    addItems();
    e.target.parentElement.remove();
  });
  //Add the span tag to the box
  spanTag.appendChild(content);
  spanTag.appendChild(anchorTag);
  box.appendChild(spanTag);
}

document.addEventListener("DOMContentLoaded", () => {
  // Functions to open and close a modal
  function openModal($el) {
    $el.classList.add("is-active");
  }

  function closeModal($el) {
    $el.classList.remove("is-active");
  }

  function closeAllModals() {
    (document.querySelectorAll(".modal") || []).forEach(($modal) => {
      closeModal($modal);
    });
  }

  // Add a click event on buttons to open a specific modal
  (document.querySelectorAll(".js-modal-trigger") || []).forEach(($trigger) => {
    const modal = $trigger.dataset.target;
    const $target = document.getElementById(modal);

    $trigger.addEventListener("click", () => {
      openModal($target);
    });
  });

  // Add a click event on various child elements to close the parent modal
  (
    document.querySelectorAll(
      ".modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button",
    ) || []
  ).forEach(($close) => {
    const $target = $close.closest(".modal");

    $close.addEventListener("click", () => {
      closeModal($target);
    });
  });

  // Add a keyboard event to close all modals
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeAllModals();
    }
  });

  // For closing the notification windows
  (document.querySelectorAll(".notification .delete") || []).forEach(
    ($delete) => {
      const $notification = $delete.parentNode;

      $delete.addEventListener("click", () => {
        $notification.parentNode.removeChild($notification);
      });
    },
  );
});
