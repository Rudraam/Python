const form = document.getElementById("promptForm");
const container = document.getElementById("generated-images");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  container.innerHTML = ""; // clear previous images

  const promptValue = document.getElementById("prompt").value;

  // Add loading spinner
  container.innerHTML = `
    <div class="text-center">
      <div class="spinner-border text-primary" role="status"></div>
      <p class="mt-2">Generating your images...</p>
    </div>
  `;

  try {
    const res = await fetch(`/generateimages?prompt=${encodeURIComponent(promptValue)}&n=3`);
    const data = await res.json();

    container.innerHTML = ""; // clear spinner

    data.images.forEach(image => {
      const col = document.createElement("div");
      col.className = "col-md-4 text-center";

      if (image.startsWith("iVBOR")) {
        const img = document.createElement("img");
        img.src = "data:image/png;base64," + image;
        img.className = "img-fluid";
        col.appendChild(img);
      } else {
        const p = document.createElement("p");
        p.textContent = image;
        col.appendChild(p);
      }

      container.appendChild(col);
    });

  } catch (err) {
    console.error(err);
    container.innerHTML = `<p class="text-danger text-center">❌ Error generating images. Please try again.</p>`;
  }
});