function redirectToHomeCommunity() {
    window.location.href = "{{ url_for('homecommunity') }}";
}

function redirectToProfilePage() {
    window.location.href = "{{ url_for('profile') }}";
}

function toggleDropdown(event) {
    event.stopPropagation(); 
    var dropdownContent = document.querySelector('.dropdown-content');
    dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
}

document.addEventListener('click', function(event) {
    var dropdownContent = document.querySelector('.dropdown-content');
    if (event.target.closest('.dropdown') === null) {
        dropdownContent.style.display = 'none';
    }
});

function editProfile() {
    
}

function logout() {
    
}

var modal = document.getElementById("deleteAccountModal");

var deleteAccountBtn = document.getElementById("deleteAccountBtn");

var closeModalBtn = document.getElementsByClassName("close")[0];

deleteAccountBtn.onclick = function() {
    modal.style.display = "block";
}

closeModalBtn.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

var confirmDeleteBtn = document.getElementById("confirmDeleteBtn");
confirmDeleteBtn.onclick = function() {
    alert("Account deleted successfully!");
    modal.style.display = "none";
}