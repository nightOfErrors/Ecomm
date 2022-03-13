let products = document.getElementsByClassName('bagButton')

let productKey

// let cartObject = []

for (let i = 0; i < products.length; i++) {
    const element = products[i];
    element.addEventListener('click', () => {

        productKey = element.dataset.product

        // cartObject.push({ productKey })

        // console.log(productKey)

    })

}

// console.log(cartObject)


function cartObjectLoader() {

    let url = /updateItem/

    let body = productKey

    let parametes = {

        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body: JSON.stringify(body)

    }

    fetch(url, parametes).then((response) => {
        return response.json()
    }).then((data) => {
        console.log(data)
    })

}


