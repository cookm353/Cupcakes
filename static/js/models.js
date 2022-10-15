const BASE_URL = 'http://localhost:5000/api/cupcakes'

class Cupcake {
    constructor() {
        this.image
        this.flavor
        this.rating
        this.size
    }

    async fetchAllCupcakes() {
        const cupcakes = await axios.get(BASE_URL);
        // console.log(cupcakes.data.cupcakes);
        return cupcakes.data.cupcakes;
    }

    async createCupcake(formJSON) {
        return await axios.post(BASE_URL, formData)
    }

    async updateCupcake(id) {

    }

    async deleteCupcake(id) {
        await axios.delete(`url/${id}`)
    }

    async findCupcake(id) {
        return await axios.get(`url/${id}`)
    }

    parseCupcakeData(cupcake) {
        return {
            "image": cupcake.image,
            "flavor": cupcake.flavor,
            "rating": cupcake.rating,
            "size": cupcake.size
        }
    }
}
