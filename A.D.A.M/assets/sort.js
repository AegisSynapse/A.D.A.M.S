// Get the table element

const table = document.querySelector("table");

// Get the header row

const headerRow = table.querySelector("thead tr");

// Attach a click listener to each header cell
headerRow.querySelectorAll("th").forEach((th, index)=> {
    th.addEventListener("click", () => {
        // Get the table body rows
        const rows = Array.from(table.querySelectorAll("tbody tr"));

        // Sort the rows based on the column clicked
        rows.sort((rowA, rowB) => {
            const cellA = rowA.querySelectorAll("td")[index];
            const cellB = rowA.querySelectorAll("td")[index];
            const valA = cellA.innerText;
            const valB = cellB.innerText;
            return valA.localeCompare(valB);

        });

        // Replace the old table body with the sorted rows
        const newTbody = document.createElement("tbody");
        rows.forEach((row) => {
            newTbody.appendChild(row);
        });
        table.replaceChild(newTbody, table.querySelector("tbody"));
    })
})
