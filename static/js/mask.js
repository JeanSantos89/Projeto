
document.addEventListener('DOMContentLoaded', function () {
    const telefoneInput = document.getElementById('telefoneContato');

    telefoneInput.addEventListener('input', function (event) {
        let value = event.target.value;
        
        // Remove qualquer caractere não numérico
        value = value.replace(/\D/g, '');

        // Aplica a máscara
        if (value.length > 10) {
            value = value.replace(/(\d{2})(\d{4})(\d{4})/, '($1) $2-$3');
        } else if (value.length > 5) {
            value = value.replace(/(\d{2})(\d{4})/, '($1) $2');
        } else if (value.length > 2) {
            value = value.replace(/(\d{2})/, '($1');
        }

        event.target.value = value;
    });
});