function AddToCart(product_id, is_authenticated){
    var order_id = document.querySelector('#add-to-cart-button').dataset.order;
    var quantity = $(`#quantity-${product_id}`).val()
    var target_url = `http://127.0.0.1:8000/order/add_to_cart/${product_id}/${quantity}`
    if (is_authenticated == 'False'){
        $.ajax({
            url: target_url,
            type: 'POST',
            headers: {
                "X-CSRFToken": $.cookie("csrftoken")
            },
            success: (response) => {
                Swal.fire(
                    'Successful',
                    'Your product added to Cart.',
                    'success'
                )
                $("#cart-length").text(response.TotalItems)
                $.ajax({
                    url: response.url,
                    type: 'get',
                    success: (res) =>{
                        $('#shopping-cart').replaceWith(res)
                    }
                })
                
            }
        }) 
    }else{
        $.ajax({
            url: target_url,
            type: 'POST',
            headers: {
                "X-CSRFToken": $.cookie("csrftoken")
            },
            success: (response) => {
                Swal.fire(
                    'Successful',
                    'Your product added to Cart.',
                    'success'
                )
                $("#cart-length").text(response.TotalItems)
                $.ajax({
                    url: response.url,
                    type: 'get',
                    success: (res) =>{
                        $('#shopping-cart').replaceWith(res)
                    }
                })  
                              
            }
        }) // create cartitem in session cart
        $.ajax({
            url: 'http://127.0.0.1:8000/api/cartitem-list/',
            data: {'quantity':quantity, 'product':product_id, 'order':order_id},
            type: 'POST',
            success: (response)=>{
                console.log(response)
            }
        }) // create cartitem in db
    }

}


function deleteItem(product_id){
    target_url = `http://127.0.0.1:8000/order/delete_cart_item/${product_id}`
    console.log(product_id)
    $.ajax({
        url: target_url,
        type: 'delete',
        headers: {
            "X-CSRFToken": $.cookie("csrftoken")
        },

        success: (response) => {
            console.log(response.total_price)
            $("#cart-length").text(response.TotalItems)
                $.ajax({
                    url: response.url,
                    type: 'get',
                    success: (res) =>{
                        $('#shopping-cart').replaceWith(res)
                    }
                })
            $("#cart-total-price").text(response.total_price)
        }
    }) // delete cartitem in session cart
    $.ajax({
        url: `http://127.0.0.1:8000/api/cartitem-detail/${product_id}`,
        type: 'delete',
        headers: {
            "X-CSRFToken": $.cookie("csrftoken")
        },
        success: (response)=>{
            console.log(response)
        }
    }) // delete cartitem in database
}