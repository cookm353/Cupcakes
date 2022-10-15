const $cupcakeDisplay = $('#cupcakeDisplay');
const $submitBttn = $('button');

cupcake = new Cupcake();

/* Show starting cupcakes on loading page */

async function showStartingCupcakes() {
    /**
     * Fetch starting cupcakes from API, generate HTML, and add to page
     */
    const cupcakeList = await cupcake.fetchAllCupcakes()

    for (let cupcake of cupcakeList) {
        $cupcakeDisplay.append(makeCupcakeHTML(cupcake))
    }
}

function makeCupcakeHTML(cupcake) {
    /**
     * Generate HTML for each cupcake
     */
    return `
    <div class="col-5 justify-content-center">
        <img src="${cupcake.image}">
        <ul>
            <h4>${titleCase(cupcake.flavor)}</h4>
            <li>${cupcake.rating}</li>
            <li>${titleCase(cupcake.size)}</li>
        </ul>
    </div>`
}

function titleCase(str) {
    // Convert A String To Title Case
    console.log(str)
    str = str.toLowerCase().split(' ');
    return str.map(word => word[0].toUpperCase() + word.slice(1)).join(' ');
}

$(window).on('load', showStartingCupcakes);

/* Handle form submission */

$submitBttn.click(async (evt) => {
    evt.preventDefault()
    let flavor = $('#flavor').val();
    let size = $('#size').val();
    let rating = $('#rating').val();
    let image = $('#image').val();

    const postResp = await axios.post(BASE_URL, {flavor, size, rating, image})

    const newCupcake = makeCupcakeHTML(postResp.data.cupcake)
    $cupcakeDisplay.append(newCupcake)
})