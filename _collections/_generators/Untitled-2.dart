<script>
  function sortdocuments(criteria) {
    const documentList = document.getElementById('document-list');
    const docs = Array.from(documentList.getElementsByClassName('document-item'));
    const titleButton = document.getElementById('sort-title');
    const dateButton = document.getElementById('sort-date');
    let sorteddocuments;

    // Remove active class from both buttons
    titleButton.classList.remove('active');
    dateButton.classList.remove('active');

    // Set active class based on the criteria
    if (criteria === 'title') {
      titleButton.classList.add('active');
      sorteddocuments = docs.sort((a, b) => 
        a.dataset.title.localeCompare(b.dataset.title)
      );
    } else if (criteria === 'date') {
      dateButton.classList.add('active');
      sorteddocuments = docs.sort((a, b) => 
        new Date(a.dataset.date) - new Date(b.dataset.date)
      );
    }

    documentList.innerHTML = ''; // Clear the current list

    let currentDivider = '';

    // Render sorted documents and add appropriate dividers
    sorteddocuments.forEach(docs => {
      if (criteria === 'title') {
        const firstLetter = docs.dataset.title.charAt(0).toUpperCase();

        // Add alphabetic divider if the first letter changes
        if (firstLetter !== currentDivider) {
          currentDivider = firstLetter;

          const alphaDivider = document.createElement('h2');
          alphaDivider.textContent = currentDivider;
          alphaDivider.className = 'alpha-divider font-weight_bold p_0 col_all m_0 p-b_2 lh_0 br_solid br-b_2 br_primary';
          documentList.appendChild(alphaDivider);
        }
      } else if (criteria === 'date') {
        const documentDate = docs.dataset.year;

        // Add year divider if the year changes
        if (documentDate !== currentDivider) {
          currentDivider = documentDate;

          const yearDivider = document.createElement('h2');
          yearDivider.textContent = currentDivider;
          yearDivider.className = 'year-divider font-weight_bold p_0 col_all m_0 p-b_2 lh_0 br_solid br-b_2 br_primary';
          documentList.appendChild(yearDivider);
        }
      }

      documentList.appendChild(docs);
    });
  }

  // Initial sort by title on page load without adding year dividers
  document.addEventListener('DOMContentLoaded', () => sortdocuments('title'));
</script>