document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('sentiment-form');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = new FormData(form);
        const text = formData.get('text');
        
        // You can perform additional tasks here, such as sending the form data to the server using fetch() or XMLHttpRequest.
        // After receiving a response from the server, you can update the DOM accordingly.
        console.log('Submitted text:', text);
    });
});
