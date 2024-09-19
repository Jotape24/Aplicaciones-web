document.addEventListener("DOMContentLoaded", () => {
    // Obtiene las imagenes
    var images = document.querySelectorAll(".grupo-span img");
    var modal = document.getElementById("imageModal");
    var modalImg = document.getElementById("modalImage");
    var closeModal = document.getElementById("closeModal");
  
    // Agrega evento a las imagenes
    images.forEach((image) => {
        image.addEventListener("click", () => {
          modal.style.display = "block";
          modalImg.src = image.src;
        });
    });
  
    // Para cerrar el modal 
    closeModal.addEventListener("click", () => {
      modal.style.display = "none";
    });
  
  });
  