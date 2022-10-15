const BASE_URL = 'http://localhost:5000/api/cupcakes'

class Cupcake {
    async fetchAllCupcakes() {
        const cupcakes = await axios.get(BASE_URL);
        return cupcakes.data.cupcakes;
    }

    async createCupcake(formData) {
        return await axios.post(BASE_URL, formData)
    }

    async updateCupcake(id, formData) {
        return await axios.patch(`${BASE_URL}/${id}`, formData)
    }

    async deleteCupcake(id) {
        return await axios.delete(`${BASE_URL}/${id}`)
    }

    async findCupcake(id) {
        return await axios.get(`${BASE_URL}/${id}`)
    }
}
