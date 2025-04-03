console.log('hello world')

const helloWolrdBox = document.getElementById('hello-world')


$.ajax({
    type: 'GET',
    url: '/hello-world/',
    success: function(response){
        console.log('success', response.text)
        helloWolrdBox.textContent = response.text
    },
    error: function(error){
        confirm.log('error', error)
    }
})