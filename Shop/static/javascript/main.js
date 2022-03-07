

function AddToCart(product_id, quantity, url, is_authenticated){    
    $.ajax({
        url: url,
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
                    $('#cart-sectio1n').empty()
                    $('#cart-section').append(res)
                }
            })
            
        }
    })    

}
