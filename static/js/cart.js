function cartObjectLoader(pk){

    const url = /update_item/
    let data = pk

    let parameters = {

        method : "POST",
        headers : {
            'content-type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body : JSON.stringify({'productId':data})

    }

    fetch(url, parameters).then((response)=>{
        return response.json()
    }).then((data)=>{
        
        orderQuantity = Number(data);
        localStorage.setItem("myCartItems", orderQuantity);        
        cartValueNumber = localStorage.getItem("myCartItems");
        cartElement = document.getElementById("inCartNumber").innerHTML = cartValueNumber;

    })

}


let products = document.getElementsByClassName('bagButton')
let productKey

let cartValueNumber = localStorage.getItem("myCartItems");
document.getElementById("inCartNumber").innerHTML = cartValueNumber;

for (let i = 0; i < products.length; i++) {
    const element = products[i];
    element.addEventListener('click', () => {
        productKey = element.dataset.product
        // console.log(productKey)
        cartObjectLoader(productKey)
    })
}

document.getElementById("cartItemsTotal").innerHTML = `Items : ${cartValueNumber}`;

function innerBagProductButton(){

    let gottenElement = document.getElementsByClassName('productAddToCartButton');
    for (let i = 0; i < gottenElement.length; i++) {
        const element = gottenElement[i];
        let innerProductKey = element.dataset.product;
        // console.log(innerProductKey)
        cartObjectLoader(innerProductKey)
    }

}


