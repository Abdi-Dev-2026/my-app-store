// Marka uu bogga dhameystirmo (Load)
document.addEventListener('DOMContentLoaded', function() {
    console.log("Dukaanka App-ka waa diyaar! 🚀");

    // Tusaale: Haddii qofku gujiyo badanka soo dejinta
    const downloadBtns = document.querySelectorAll('.btn-download');
    
    downloadBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            alert("Dalabkaaga waa la farsameynayaa...");
        });
    });
});