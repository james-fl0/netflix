document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('dropdownMenuButton').addEventListener('click', function() {
        var dropdownContent = document.getElementById('dropdownMenu');
        if(dropdownContent.classList.contains('hidden')){
            dropdownContent.classList.remove('hidden');
        }else{
            dropdownContent.classList.add('hidden');
        }
    });
});
